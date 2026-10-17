#!/usr/bin/env python3
"""Local native capture records. Integrity/coverage checks, never visual QA.

Python 3.10+, standard library. Captures require existing authorized native tools.
Build, runtime, state and reviewer declarations are NOT independently attested.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import struct
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from typing import Any
import uuid
import zlib

SCHEMA = 1
SLUG = re.compile(r"^[a-z0-9][a-z0-9_-]{0,79}$")
HASH = re.compile(r"^[0-9a-f]{64}$")
PNG = b"\x89PNG\r\n\x1a\n"
VERDICTS = {"acceptable", "needs-repair", "indeterminate"}
DISCLAIMER = (
    "File/hash/coverage validation only. Runtime, build, screen, data and reviews "
    "are operator-declared, not independently attested. No visual or behavior pass."
)


class EvidenceError(ValueError):
    """Invalid input, unsafe path, incomplete native tooling, or corrupt record."""


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise EvidenceError(f"Cannot read JSON {path}: {exc}") from exc


def save_json(path: Path, value: Any) -> None:
    """Atomic metadata replacement; image attempts are never overwritten."""
    text = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix=".metadata-", delete=False) as handle:
        tmp = Path(handle.name)
        handle.write(text)
    try:
        os.replace(tmp, path)
    finally:
        tmp.unlink(missing_ok=True)


def obj(value: Any, where: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise EvidenceError(f"{where} must be an object")
    return value


def text(value: Any, where: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EvidenceError(f"{where} must be nonempty text")
    if re.search(r"\bREPLACE(?:_[A-Z0-9]+)*\b", value):
        raise EvidenceError(f"{where} is still a template placeholder")
    return value


def slug(value: Any, where: str) -> str:
    value = text(value, where)
    if not SLUG.fullmatch(value):
        raise EvidenceError(f"{where} must be a lowercase safe identifier")
    return value


def items(value: Any, where: str, nonempty: bool = True) -> list[Any]:
    if not isinstance(value, list) or (nonempty and not value):
        raise EvidenceError(f"{where} must be {'a nonempty' if nonempty else 'a'} list")
    return value


def positive(value: Any, where: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
        raise EvidenceError(f"{where} must be a finite positive number")
    return float(value)


def validate_plan(plan: Any) -> dict[str, Any]:
    plan = obj(plan, "plan")
    if type(plan.get("schema_version")) is not int or plan["schema_version"] != SCHEMA:
        raise EvidenceError("Unsupported plan schema_version")
    for name in ("app_id", "data_id"):
        text(plan.get(name), name)
    for ref in items(plan.get("reference_ids"), "reference_ids", nonempty=False):
        text(ref, "reference identifier")
    variants: dict[str, Any] = {}
    for raw in items(plan.get("variants"), "variants"):
        v = obj(raw, "variant")
        ident = slug(v.get("id"), "variant.id")
        if ident in variants:
            raise EvidenceError(f"Duplicate variant {ident}")
        allowed = {"android": {"emulator", "physical-device"},
                   "ios": {"simulator", "physical-device"}}
        if v.get("platform") not in allowed or v.get("runtime") not in allowed[v["platform"]]:
            raise EvidenceError(f"Not a supported native platform/runtime for {ident}")
        for name in ("device_id", "os_version", "locale", "text_setting", "appearance", "orientation"):
            text(v.get(name), f"{ident}.{name}")
        # Prevent an accidental option or a control character being used as a device ID.
        device = v["device_id"]
        if device.startswith("-") or any(c.isspace() for c in device):
            raise EvidenceError(f"Unsafe device_id for {ident}")
        size = items(v.get("logical_size"), f"{ident}.logical_size")
        if len(size) != 2:
            raise EvidenceError("logical_size needs width and height")
        for number in size:
            positive(number, "logical size")
        positive(v.get("density"), f"{ident}.density")
        variants[ident] = v
    case_ids: set[str] = set()
    for raw in items(plan.get("cases"), "cases"):
        case = obj(raw, "case")
        ident = slug(case.get("id"), "case.id")
        if ident in case_ids:
            raise EvidenceError(f"Duplicate case {ident}")
        case_ids.add(ident)
        if case.get("variant_id") not in variants:
            raise EvidenceError(f"Unknown variant for case {ident}")
        for name in ("screen", "state"):
            text(case.get(name), f"{ident}.{name}")
        for step in items(case.get("setup"), f"{ident}.setup"):
            text(step, "setup step")
    return plan


def inside(root: Path, relative: Any) -> Path:
    name = text(relative, "relative artifact path")
    p = Path(name)
    if p.is_absolute() or ".." in p.parts:
        raise EvidenceError(f"Artifact path escapes run: {name}")
    resolved = (root / p).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise EvidenceError(f"Artifact symlink escapes run: {name}")
    return resolved


def png_size(data: bytes) -> tuple[int, int]:
    """Check PNG chunk structure and CRC, not pixels/appearance or authenticity."""
    if len(data) > 100 * 1024 * 1024:
        raise EvidenceError("PNG exceeds the 100 MiB safety limit")
    if not data.startswith(PNG):
        raise EvidenceError("Capture is not a PNG")
    pos, size, seen_idat = 8, None, False
    while pos + 12 <= len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        tag = data[pos + 4:pos + 8]
        end = pos + 12 + length
        if end > len(data):
            raise EvidenceError("Truncated PNG chunk")
        payload = data[pos + 8:pos + 8 + length]
        crc = struct.unpack(">I", data[pos + 8 + length:end])[0]
        if zlib.crc32(tag + payload) & 0xFFFFFFFF != crc:
            raise EvidenceError("PNG chunk CRC mismatch")
        if size is None:
            if tag != b"IHDR" or length != 13:
                raise EvidenceError("PNG missing initial IHDR")
            size = struct.unpack(">II", payload[:8])
            if not all(0 < x <= 40000 for x in size):
                raise EvidenceError("Invalid or excessive PNG dimensions")
        elif tag == b"IHDR":
            raise EvidenceError("Duplicate PNG IHDR")
        if tag == b"IDAT":
            seen_idat = True
        if tag == b"IEND":
            if length != 0 or not seen_idat or end != len(data):
                raise EvidenceError("Invalid PNG ending")
            return size
        pos = end
    raise EvidenceError("PNG has no valid IEND")


def initialize(plan_path: Path, out: Path, build_id: str) -> dict[str, Any]:
    text(build_id, "build_id")
    validate_plan(load_json(plan_path))
    raw = plan_path.read_bytes()
    if out.exists():
        raise EvidenceError("Run folder already exists; choose a new one (no overwrite)")
    out.mkdir(parents=True)
    (out / "captures").mkdir()
    (out / "plan.json").write_bytes(raw)
    manifest = {"schema_version": SCHEMA, "created_at": now(), "build_id": build_id,
                "plan_sha256": digest(raw), "attempts": [], "disclaimer": DISCLAIMER}
    save_json(out / "manifest.json", manifest)
    return {"run": str(out.resolve()), "status": "initialized_not_captured", "disclaimer": DISCLAIMER}


def read_run(root: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    root = root.resolve()
    m = obj(load_json(root / "manifest.json"), "manifest")
    if type(m.get("schema_version")) is not int or m["schema_version"] != SCHEMA:
        raise EvidenceError("Unsupported manifest schema_version")
    text(m.get("build_id"), "manifest.build_id")
    sha = text(m.get("plan_sha256"), "plan_sha256")
    if not HASH.fullmatch(sha):
        raise EvidenceError("Invalid plan hash")
    try:
        raw = (root / "plan.json").read_bytes()
    except OSError as exc:
        raise EvidenceError(f"Cannot read frozen plan: {exc}") from exc
    if digest(raw) != sha:
        raise EvidenceError("Frozen plan changed; create a new run, do not rewrite coverage")
    p = validate_plan(load_json(root / "plan.json"))
    valid_cases = {c["id"]: c for c in p["cases"]}
    seen: set[str] = set()
    for raw_attempt in items(m.get("attempts"), "attempts", nonempty=False):
        a = obj(raw_attempt, "attempt")
        ident = slug(a.get("id"), "attempt.id")
        if ident in seen:
            raise EvidenceError("Duplicate attempt ID")
        seen.add(ident)
        if a.get("case_id") not in valid_cases or a.get("build_id") != m["build_id"]:
            raise EvidenceError("Attempt case/build mismatch")
        if a.get("status") not in {"captured", "capture_failed"}:
            raise EvidenceError("Invalid attempt status")
        text(a.get("created_at"), "attempt timestamp")
        if a["status"] == "capture_failed":
            text(a.get("error"), "failed-attempt error")
            continue
        if a.get("source") not in {"native-tool", "operator-import"}:
            raise EvidenceError("Invalid capture source")
        text(a.get("provenance"), "capture provenance")
        path = inside(root, a.get("file"))
        try:
            data = path.read_bytes()
        except OSError as exc:
            raise EvidenceError(f"Capture missing/unreadable: {path.name}") from exc
        if digest(data) != a.get("sha256"):
            raise EvidenceError(f"Capture changed: {path.name}")
        if list(png_size(data)) != a.get("pixel_size"):
            raise EvidenceError("Recorded image size mismatch")
        reviews = items(a.get("reviews"), "reviews", nonempty=False)
        for r_raw in reviews:
            r = obj(r_raw, "review")
            if r.get("verdict") not in VERDICTS or r.get("image_sha256") != a["sha256"]:
                raise EvidenceError("Invalid/stale review")
            for field in ("reviewer", "notes", "created_at"):
                text(r.get(field), f"review.{field}")
    return m, p


def get_case(plan: dict[str, Any], case_id: str) -> tuple[dict[str, Any], dict[str, Any]]:
    case = next((c for c in plan["cases"] if c["id"] == case_id), None)
    if case is None:
        raise EvidenceError(f"Unknown case: {case_id}")
    variant = next(v for v in plan["variants"] if v["id"] == case["variant_id"])
    return case, variant


def run_command(args: list[str]) -> subprocess.CompletedProcess[bytes]:
    try:
        result = subprocess.run(args, capture_output=True, check=False, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise EvidenceError(f"Native tool failed: {exc}") from exc
    if result.returncode:
        message = result.stderr.decode("utf-8", "replace").strip()[:1200]
        raise EvidenceError(f"Native tool exit {result.returncode}: {message}")
    return result


def native_capture(variant: dict[str, Any], output: Path) -> list[str]:
    if variant["platform"] == "android":
        if not shutil.which("adb"):
            raise EvidenceError("adb is not installed/on PATH; no native capture performed")
        command = ["adb", "-s", variant["device_id"], "exec-out", "screencap", "-p"]
        data = run_command(command).stdout
        with output.open("xb") as handle:
            handle.write(data)
        return command
    if variant["runtime"] != "simulator":
        raise EvidenceError("iOS direct capture supports Simulator only; attach real device evidence from your runner")
    if not shutil.which("xcrun"):
        raise EvidenceError("xcrun is not installed/on PATH; no native capture performed")
    command = ["xcrun", "simctl", "io", variant["device_id"], "screenshot", "--type=png", str(output)]
    run_command(command)
    return command


def capture(root: Path, case_id: str, observed_build_id: str, *,
            confirmed: bool = False, imported: Path | None = None,
            provenance: str | None = None) -> dict[str, Any]:
    root = root.resolve()
    m, p = read_run(root)
    case, variant = get_case(p, case_id)
    if text(observed_build_id, "observed_build_id") != m["build_id"]:
        raise EvidenceError("Observed build ID differs; start a new run for the new build")
    if imported is None and not confirmed:
        raise EvidenceError("Navigate/verify app-state-build readiness first, then pass --confirm-ready")
    if imported is not None:
        text(provenance, "native screenshot provenance")
    attempt_id = "a-" + uuid.uuid4().hex
    relative = f"captures/{case_id}-{attempt_id}.png"
    target = inside(root, relative)
    attempt: dict[str, Any] = {"id": attempt_id, "case_id": case_id, "build_id": m["build_id"],
                               "created_at": now(), "status": "capture_failed", "reviews": []}
    try:
        if imported is None:
            command = native_capture(variant, target)
            attempt.update(source="native-tool", command=command,
                           provenance="Operator declared correct native app/build/device/state; not independently attested")
        else:
            with target.open("xb") as handle:
                handle.write(imported.read_bytes())
            attempt.update(source="operator-import", provenance=provenance)
        raw = target.read_bytes()
        size = png_size(raw)
        attempt.update(status="captured", file=relative, sha256=digest(raw), pixel_size=list(size))
    except (OSError, EvidenceError) as exc:
        # Failed attempts remain in the manifest; partial corrupt image files are not counted as evidence.
        attempt["error"] = str(exc)
        m["attempts"].append(attempt)
        save_json(root / "manifest.json", m)
        raise EvidenceError(f"Capture failed and was recorded ({attempt_id}): {exc}") from exc
    m["attempts"].append(attempt)
    save_json(root / "manifest.json", m)
    return {"attempt": attempt_id, "file": str(target), "status": "captured_unreviewed", "disclaimer": DISCLAIMER}


def latest_attempt(m: dict[str, Any], case_id: str) -> dict[str, Any] | None:
    return next((a for a in reversed(m["attempts"]) if a["case_id"] == case_id), None)


def record_review(root: Path, case_id: str, reviewer: str, verdict: str, notes: str) -> dict[str, Any]:
    m, p = read_run(root)
    get_case(p, case_id)
    text(reviewer, "reviewer")
    text(notes, "notes")
    if verdict not in VERDICTS:
        raise EvidenceError("Unknown verdict")
    a = latest_attempt(m, case_id)
    if a is None or a["status"] != "captured":
        raise EvidenceError("Latest attempt has no valid capture; do not review an older passing image instead")
    a["reviews"].append({"reviewer": reviewer, "verdict": verdict, "notes": notes,
                         "image_sha256": a["sha256"], "created_at": now()})
    save_json(root / "manifest.json", m)
    return {"status": "review_recorded_not_independently_verified", "disclaimer": DISCLAIMER}


def check(root: Path, require_reviewed: bool = False) -> tuple[dict[str, Any], int]:
    m, p = read_run(root)
    missing, unreviewed, unresolved = [], [], []
    for case in p["cases"]:
        a = latest_attempt(m, case["id"])
        if a is None or a["status"] != "captured":
            missing.append(case["id"])
        elif not a["reviews"]:
            unreviewed.append(case["id"])
        elif a["reviews"][-1]["verdict"] != "acceptable":
            unresolved.append(case["id"])
    incomplete = bool(missing or unresolved or (require_reviewed and unreviewed))
    return {"evidence_integrity": "valid", "capture_coverage": "incomplete" if missing else "complete",
            "missing_latest_captures": missing, "unreviewed_cases": unreviewed,
            "latest_review_not_acceptable": unresolved, "visual_quality": "not_assessed_by_checker",
            "native_behavior": "not_assessed_by_checker", "review_required": require_reviewed,
            "disclaimer": DISCLAIMER}, 2 if incomplete else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    subs.add_parser("preflight")
    init = subs.add_parser("init")
    init.add_argument("--plan", type=Path, required=True)
    init.add_argument("--out", type=Path, required=True)
    init.add_argument("--build-id", required=True)
    for name in ("capture", "attach"):
        command = subs.add_parser(name)
        command.add_argument("--run", type=Path, required=True)
        command.add_argument("--case", required=True)
        command.add_argument("--observed-build-id", required=True)
        if name == "capture":
            command.add_argument("--confirm-ready", action="store_true")
        else:
            command.add_argument("--file", type=Path, required=True)
            command.add_argument("--provenance", required=True)
    review = subs.add_parser("review")
    review.add_argument("--run", type=Path, required=True)
    review.add_argument("--case", required=True)
    review.add_argument("--reviewer", required=True)
    review.add_argument("--verdict", choices=sorted(VERDICTS), required=True)
    review.add_argument("--notes", required=True)
    verify = subs.add_parser("check")
    verify.add_argument("--run", type=Path, required=True)
    verify.add_argument("--require-reviewed", action="store_true")
    args = parser.parse_args()
    code = 0
    try:
        if args.command == "preflight":
            result = {"host": platform.system(), "python": platform.python_version(),
                      "tool_paths": {name: shutil.which(name) for name in ("adb", "xcrun", "flutter", "codex")},
                      "native_tool_invocations": 0, "disclaimer": DISCLAIMER}
        elif args.command == "init":
            result = initialize(args.plan, args.out, args.build_id)
        elif args.command == "capture":
            result = capture(args.run, args.case, args.observed_build_id, confirmed=args.confirm_ready)
        elif args.command == "attach":
            result = capture(args.run, args.case, args.observed_build_id, imported=args.file, provenance=args.provenance)
        elif args.command == "review":
            result = record_review(args.run, args.case, args.reviewer, args.verdict, args.notes)
        else:
            result, code = check(args.run, args.require_reviewed)
    except (EvidenceError, OSError) as exc:
        result, code = {"error": str(exc), "disclaimer": DISCLAIMER}, 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
