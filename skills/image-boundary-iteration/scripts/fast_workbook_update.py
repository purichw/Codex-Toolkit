#!/usr/bin/env python3
"""Run the image-boundary workbook packet workflow with one command.

This wrapper keeps the existing safe packet updater as the source of truth. It
adds the repetitive glue around it: runtime setup, dry-run/apply invocation,
compact summaries, and post-apply compiled JSON ID checks.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path("/Users/point/outputs/nudity_reference_prompting")
REFERENCES_DIR = PROJECT_ROOT / "References for Codex"
PROJECT_SCRIPTS_DIR = PROJECT_ROOT / "scripts"
WORKBOOK_UPDATER = PROJECT_SCRIPTS_DIR / "workbook_update_from_packet.mjs"
DEFAULT_WORKBOOK = REFERENCES_DIR / "sensitive_figure_reference_prompting_glossary.verification-2026-06-24.xlsx"
COMPILED_JSON = REFERENCES_DIR / "sensitive_figure_reference_prompting_glossary.compiled.json"
NODE_BIN = Path("/Users/point/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node")
NODE_MODULES = Path("/Users/point/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules")
PROJECT_NODE_MODULES = PROJECT_SCRIPTS_DIR / "node_modules"


SECTION_ID_FIELDS = {
    "retestResultsLog": ("retest_results_log", "test_id", "testId"),
    "passedVisuals": ("passed_visuals", "image_id", "imageId"),
    "promptTemplates": ("prompt_templates", "template_name", "templateName"),
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def ensure_node_modules() -> None:
    PROJECT_SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    if PROJECT_NODE_MODULES.is_symlink() or PROJECT_NODE_MODULES.exists():
        if PROJECT_NODE_MODULES.resolve() == NODE_MODULES:
            return
        raise SystemExit(f"Refusing to replace existing node_modules: {PROJECT_NODE_MODULES}")
    os.symlink(NODE_MODULES, PROJECT_NODE_MODULES)


def run_updater(args: argparse.Namespace) -> dict[str, Any]:
    ensure_node_modules()
    cmd = [
        str(NODE_BIN),
        str(WORKBOOK_UPDATER),
        "--packet",
        str(args.packet),
        "--workbook",
        str(args.workbook),
        "--render",
        args.render,
    ]
    if args.apply:
        cmd.append("--apply")
    if args.no_compile:
        cmd.append("--no-compile")

    run = subprocess.run(
        cmd,
        cwd=str(PROJECT_SCRIPTS_DIR),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if run.returncode != 0:
        sys.stderr.write(run.stdout)
        sys.stderr.write(run.stderr)
        raise SystemExit(run.returncode)
    try:
        return json.loads(run.stdout)
    except json.JSONDecodeError as exc:
        sys.stderr.write(run.stdout)
        sys.stderr.write(run.stderr)
        raise SystemExit(f"Updater succeeded but stdout was not JSON: {exc}") from exc


def packet_expected_ids(packet: dict[str, Any]) -> dict[str, list[str]]:
    updates = packet.get("updates", {})
    expected: dict[str, list[str]] = {}
    for packet_key, (_compiled_key, _compiled_id, packet_id) in SECTION_ID_FIELDS.items():
        ids = [
            str(row.get(packet_id, "")).strip()
            for row in updates.get(packet_key, [])
            if str(row.get(packet_id, "")).strip()
        ]
        if ids:
            expected[packet_key] = ids
    return expected


def compiled_id_checks(expected: dict[str, list[str]]) -> dict[str, dict[str, Any]]:
    if not expected:
        return {}
    if not COMPILED_JSON.exists():
        return {key: {"ok": False, "missing": ids, "reason": "compiled JSON not found"} for key, ids in expected.items()}

    compiled = load_json(COMPILED_JSON)
    out: dict[str, dict[str, Any]] = {}
    for packet_key, ids in expected.items():
        compiled_key, compiled_id, _packet_id = SECTION_ID_FIELDS[packet_key]
        records = compiled.get(compiled_key, [])
        present = {str(record.get(compiled_id, "")).strip() for record in records}
        missing = [item for item in ids if item not in present]
        out[packet_key] = {
            "ok": not missing,
            "expected": ids,
            "missing": missing,
            "section": compiled_key,
            "section_count": len(records),
        }
    return out


def formula_errors_found(formula_errors: Any) -> bool:
    text = str(formula_errors or "").strip()
    if not text:
        return False
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            return True
        if record.get("kind") == "notice" and "matched 0 entries" in str(record.get("message", "")):
            continue
        return True
    return False


def summarize(updater_output: dict[str, Any], packet: dict[str, Any], expected: dict[str, list[str]]) -> dict[str, Any]:
    changed = updater_output.get("changed", [])
    render = updater_output.get("renderResult") or {}
    summary: dict[str, Any] = {
        "mode": updater_output.get("mode"),
        "saved": updater_output.get("saved", False),
        "packet": updater_output.get("packet"),
        "workbook": updater_output.get("workbook"),
        "changed": [
            {
                "sheet": item.get("sheetName"),
                "range": item.get("range"),
                "rows": item.get("rows"),
            }
            for item in changed
        ],
        "expectedIds": expected,
        "formulaErrorsFound": formula_errors_found(updater_output.get("formulaErrors")),
        "renderDir": render.get("outDir"),
        "backupPath": updater_output.get("backupPath"),
    }
    if updater_output.get("saved") and not updater_output.get("compileOutput"):
        summary["compiledJson"] = "not regenerated (--no-compile)"
    elif updater_output.get("saved"):
        summary["compiledJson"] = str(COMPILED_JSON)
        summary["compiledChecks"] = compiled_id_checks(expected)
    if packet.get("backupLabel"):
        summary["backupLabel"] = packet["backupLabel"]
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fast wrapper for the safe image-boundary workbook packet workflow."
    )
    parser.add_argument("--packet", required=True, type=Path, help="Workbook update packet JSON.")
    parser.add_argument("--apply", action="store_true", help="Save workbook. Default is dry-run.")
    parser.add_argument("--workbook", type=Path, default=DEFAULT_WORKBOOK)
    parser.add_argument(
        "--render",
        choices=["none", "changed", "all"],
        default=None,
        help="Render mode. Default: changed for dry-run, all for apply.",
    )
    parser.add_argument("--no-compile", action="store_true", help="Skip compiled JSON regeneration on apply.")
    parser.add_argument("--full-json", action="store_true", help="Print full updater JSON after the summary.")
    args = parser.parse_args()

    if args.render is None:
        args.render = "all" if args.apply else "changed"

    packet = load_json(args.packet)
    expected = packet_expected_ids(packet)
    updater_output = run_updater(args)
    summary = summarize(updater_output, packet, expected)

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.full_json:
        print("\n--- full updater output ---")
        print(json.dumps(updater_output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
