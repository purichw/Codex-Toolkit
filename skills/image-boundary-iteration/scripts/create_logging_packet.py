#!/usr/bin/env python3
"""Create a workbook-update packet skeleton for this image-boundary project.

The packet is intentionally cautious. It prepares data for the existing
workbook_update_from_packet.mjs script but does not apply anything.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path


EMPTY_UPDATES = {
    "retestResultsLog": [],
    "passedVisuals": [],
    "promptTemplates": [],
    "adultClarityAudit": [],
}


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8").strip()
    return (args.prompt or "").strip()


def short_file_name(path: str) -> str:
    return os.path.basename(path) if path else ""


def build_packet(args: argparse.Namespace) -> dict:
    today = args.date or dt.date.today().isoformat()
    prompt = read_prompt(args)
    result = args.result
    image_path = args.image_path or ""
    rejected = "Yes" if result.lower() == "reject" else "No"
    safety_result = "Rejected" if result.lower() == "reject" and not image_path else "Safe"

    packet = {
        "backupLabel": args.backup_label or f"{args.test_id.lower()}-{today}",
        "updates": {k: list(v) for k, v in EMPTY_UPDATES.items()},
    }

    notes_parts = []
    if prompt:
        notes_parts.append(f"Prompt used: {prompt}")
    if args.learning:
        notes_parts.append(f"Learning: {args.learning}")

    packet["updates"]["retestResultsLog"].append(
        {
            "runDate": today,
            "testId": args.test_id,
            "candidateId": args.candidate_id,
            "coverageLadderLevel": args.ladder_level,
            "modelTool": args.model_tool,
            "result": result,
            "generatedPath": image_path,
            "generatedSha256": "auto" if image_path else "",
            "safetyResult": safety_result,
            "intentScore": args.intent_score,
            "driftScore": args.drift_score,
            "coverageScore": args.coverage_score,
            "tooMuchClothing": args.too_much_clothing,
            "rejected": rejected,
            "userFeedback": args.user_feedback,
            "decision": args.decision,
            "promoteTo": args.promote_to,
            "failurePattern": args.failure_pattern,
            "notes": " ".join(notes_parts),
            "reviewer": "Codex",
            "linkedWorkbookRow": args.linked_workbook_row or short_file_name(image_path),
        }
    )

    if result.lower() == "pass" and args.add_passed_visual:
        if not image_path:
            raise SystemExit("--add-passed-visual requires --image-path")
        packet["updates"]["passedVisuals"].append(
            {
                "imageId": args.image_id,
                "batch": args.batch,
                "class": args.asset_class,
                "fileName": short_file_name(image_path),
                "imagePath": image_path,
                "imageSha256": "auto",
                "visualIntent": args.visual_intent,
                "likelyPromptFamily": args.prompt_family,
                "matchedReplacementIds": args.matched_replacements,
                "intentMatch": args.intent_match,
                "driftRisk": args.drift_risk,
                "rebuildNeeded": args.rebuild_needed,
                "verificationStatus": "User Accepted / Current Prompt Known",
                "proofLevel": "User explicit pass",
                "retestNeeded": args.retest_needed,
                "safetyExposureRisk": args.safety_exposure_risk,
                "evidenceType": "Current generated pass",
                "notes": args.passed_visual_notes,
            }
        )
    elif result.lower() != "pass" and args.add_passed_visual:
        raise SystemExit("Refusing to add Passed Visuals for non-Pass result.")

    if args.audit_finding or args.audit_action:
        packet["updates"]["adultClarityAudit"].append(
            {
                "sheet": "Retest Results Log",
                "area": args.test_id,
                "finding": args.audit_finding,
                "action": args.audit_action,
                "status": args.audit_status,
            }
        )

    return packet


def main() -> int:
    parser = argparse.ArgumentParser(description="Create an image-boundary workbook update packet skeleton.")
    parser.add_argument("--test-id", required=True)
    parser.add_argument("--result", required=True, choices=["Pass", "Partial", "Reject"])
    parser.add_argument("--output", required=True)
    parser.add_argument("--image-path", default="")
    parser.add_argument("--prompt", default="")
    parser.add_argument("--prompt-file")
    parser.add_argument("--date")
    parser.add_argument("--backup-label")
    parser.add_argument("--candidate-id", default="")
    parser.add_argument("--ladder-level", default="")
    parser.add_argument("--model-tool", default="Codex image_gen")
    parser.add_argument("--intent-score", type=int, default=5)
    parser.add_argument("--drift-score", type=int, default=1)
    parser.add_argument("--coverage-score", type=int, default=5)
    parser.add_argument("--too-much-clothing", default="No")
    parser.add_argument("--user-feedback", default="")
    parser.add_argument("--decision", default="")
    parser.add_argument("--promote-to", default=None)
    parser.add_argument("--failure-pattern", default=None)
    parser.add_argument("--learning", default="")
    parser.add_argument("--linked-workbook-row", default="")

    parser.add_argument("--add-passed-visual", action="store_true")
    parser.add_argument("--image-id", default="")
    parser.add_argument("--batch", default="")
    parser.add_argument("--asset-class", default="RGUY")
    parser.add_argument("--visual-intent", default="")
    parser.add_argument("--prompt-family", default="")
    parser.add_argument("--matched-replacements", default="")
    parser.add_argument("--intent-match", default="")
    parser.add_argument("--drift-risk", default="Medium")
    parser.add_argument("--rebuild-needed", default="Yes")
    parser.add_argument("--retest-needed", default="Yes")
    parser.add_argument("--safety-exposure-risk", default="")
    parser.add_argument("--passed-visual-notes", default="")

    parser.add_argument("--audit-finding", default="")
    parser.add_argument("--audit-action", default="")
    parser.add_argument("--audit-status", default="Learned")

    args = parser.parse_args()
    packet = build_packet(args)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(packet, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote packet skeleton: {out}")
    print("Next: run fast_workbook_update.py dry-run, inspect rows, then apply only if correct.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
