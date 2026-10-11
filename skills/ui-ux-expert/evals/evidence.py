"""Check evidence integrity/coverage, never pixels, taste or reviewer honesty.

The matrix is an independently chosen acceptance contract. Keep it fixed before
capture; weakening it after a failure invalidates a comparison.
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inside(root, name):
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError("file path must be relative")
    root = root.resolve()
    path = (root / name).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError(f"missing or escaping file: {name}")
    return path


def validate(matrix, manifest, source_root, evidence_root):
    errors = []
    try:
        if not isinstance(matrix, dict) or not isinstance(manifest, dict):
            raise ValueError("matrix and manifest must be objects")
        for obj in (matrix, manifest):
            if type(obj.get("schema_version")) is not int or obj["schema_version"] != 1:
                raise ValueError("schema_version must be 1")
        files = matrix.get("source_files")
        required = matrix.get("required")
        captures = manifest.get("captures")
        if not isinstance(files, list) or not files or any(not isinstance(p, str) for p in files):
            raise ValueError("source_files must be a nonempty path list")
        if len(set(files)) != len(files):
            raise ValueError("duplicate source files")
        hashes = {p: digest(inside(source_root, p)) for p in files}
        if not isinstance(required, list) or not required or not isinstance(captures, list):
            raise ValueError("required states and captures must be lists; requirements cannot be empty")
        by_id = {}
        for capture in captures:
            if not isinstance(capture, dict) or not isinstance(capture.get("id"), str):
                raise ValueError("capture needs a string id")
            if capture["id"] in by_id:
                raise ValueError("duplicate capture id")
            by_id[capture["id"]] = capture
        seen = set()
        for requirement in required:
            if not isinstance(requirement, dict):
                raise ValueError("requirement must be an object")
            key = requirement.get("id")
            if not isinstance(key, str) or not key.strip() or key in seen:
                raise ValueError("required ids must be unique nonempty strings")
            seen.add(key)
            for field in ("route", "state"):
                if not isinstance(requirement.get(field), str) or not requirement[field].strip():
                    raise ValueError(f"{key}: missing {field}")
            vp = requirement.get("viewport")
            if not isinstance(vp, list) or len(vp) != 2 or any(type(n) is not int or n <= 0 for n in vp):
                raise ValueError(f"{key}: invalid viewport")
            checks = requirement.get("checks")
            if not isinstance(checks, list) or not checks or any(not isinstance(c, str) or not c for c in checks):
                raise ValueError(f"{key}: checks must be nonempty names")
            capture = by_id.get(key)
            if capture is None:
                errors.append(f"{key}: missing capture")
                continue
            for field in ("route", "state", "viewport"):
                if capture.get(field) != requirement[field]:
                    errors.append(f"{key}: wrong {field}")
            if capture.get("source_hashes") != hashes:
                errors.append(f"{key}: stale or incomplete source hashes")
            try:
                img = inside(evidence_root, capture.get("file"))
                if img.suffix.lower() != ".png" or not img.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
                    errors.append(f"{key}: not a PNG capture")
                if digest(img) != capture.get("sha256"):
                    errors.append(f"{key}: image hash mismatch")
            except (OSError, ValueError) as exc:
                errors.append(f"{key}: {exc}")
            review = capture.get("review")
            if not isinstance(review, dict) or any(not isinstance(review.get(f), str) or not review[f].strip() for f in ("reviewer", "note")):
                errors.append(f"{key}: no recorded visual review")
            results = capture.get("checks")
            if not isinstance(results, dict):
                errors.append(f"{key}: no check results")
            else:
                for check in checks:
                    if results.get(check) != "passed":
                        errors.append(f"{key}: required check {check} did not pass")
        extras = set(by_id) - seen
        if extras:
            errors.append(f"captures outside matrix: {sorted(extras)}")
    except (OSError, ValueError, TypeError) as exc:
        errors.append(str(exc))
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matrix", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--evidence-root", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        matrix = json.loads(args.matrix.read_text(encoding="utf-8"))
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        errors = validate(matrix, manifest, args.source_root, args.evidence_root)
    except (OSError, UnicodeError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        print("EVIDENCE NOT VERIFIED\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print("EVIDENCE INTEGRITY OK: declared coverage/hashes/review/checks only; not a design verdict.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
