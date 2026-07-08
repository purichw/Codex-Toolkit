#!/usr/bin/env python3
"""Print source-of-truth project paths for the image-boundary iteration project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path("/Users/point/outputs/nudity_reference_prompting")
REFS = ROOT / "References for Codex"

PATHS = {
    "projectRoot": ROOT,
    "references": REFS,
    "workbook": REFS / "sensitive_figure_reference_prompting_glossary.verification-2026-06-24.xlsx",
    "compiledJson": REFS / "sensitive_figure_reference_prompting_glossary.compiled.json",
    "compiledMinJson": REFS / "sensitive_figure_reference_prompting_glossary.compiled.min.json",
    "evalCases": REFS / "sensitive_figure_reference_prompting_glossary.eval_cases.json",
    "generatedAssets": REFS / "generated_assets",
    "scripts": ROOT / "scripts",
    "fastWorkbookUpdater": Path("/Users/point/.codex/skills/image-boundary-iteration/scripts/fast_workbook_update.py"),
    "inbox": ROOT / "inbox",
    "archive": ROOT / "archive",
    "newChatHandoff": REFS / "new_chat_handoff_prompt.md",
    "communicationPreferences": REFS / "codex_communication_preferences.md",
    "rejectionTriggerIndex": REFS / "rejection_trigger_index.md",
    "imagenNotes": REFS / "imagen_rejection_efficiency_notes.md",
    "visualBaselines": REFS / "rpg_guy_visual_baselines.md",
    "watercolorBathhouseNotes": REFS / "watercolor_bathhouse_branch_notes_2026-07-05.md",
    "watercolorBathhouseBaselines": REFS / "watercolor_bathhouse_visual_baselines.md",
    "moonlitCelestialFountainNotes": REFS / "moonlit_celestial_fountain_branch_notes_2026-07-05.md",
    "moonlitCelestialFountainBaselines": REFS / "moonlit_celestial_fountain_visual_baselines.md",
    "workbookWorkflow": REFS / "workbook_update_workflow.md",
    "excelSafety": REFS / "excel_update_safety_notes.md",
}


def info(path: Path) -> dict:
    exists = path.exists()
    out = {"path": str(path), "exists": exists}
    if exists:
        st = path.stat()
        out["size"] = st.st_size
        out["mtime"] = int(st.st_mtime)
    return out


def latest_assets(limit: int) -> list[str]:
    assets = PATHS["generatedAssets"]
    if not assets.exists():
        return []
    files = [p for p in assets.iterdir() if p.is_file()]
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return [str(p) for p in files[:limit]]


def main() -> int:
    parser = argparse.ArgumentParser(description="Show project source-of-truth paths.")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--latest", type=int, default=5, help="Number of latest generated assets to show.")
    args = parser.parse_args()

    data = {key: info(path) for key, path in PATHS.items()}
    data["latestAssets"] = latest_assets(args.latest)

    if args.json:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return 0

    print("Image boundary iteration project status")
    for key, item in data.items():
        if key == "latestAssets":
            continue
        status = "OK" if item["exists"] else "MISSING"
        print(f"- {key}: {status} {item['path']}")

    print("\nLatest generated assets:")
    for path in data["latestAssets"]:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
