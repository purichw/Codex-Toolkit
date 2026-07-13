#!/usr/bin/env python3
"""Scan a draft image-boundary prompt for project-specific risk reminders.

This is a lightweight heuristic checker. It does not decide whether a prompt is
allowed or blocked; it only highlights patterns that have caused problems in
this project.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict


@dataclass
class Finding:
    severity: str
    pattern: str
    reason: str
    safer_move: str


PATTERNS = [
    (
        "high",
        r"\b(ultra[- ]short|much smaller|tighter|less fabric area|no fabric|no coverage|no garment|no clothing|remove garment|remove clothing|garment removal)\b",
        "Direct garment/coverage reduction wording has triggered rejects in boundary-adjacent contexts.",
        "Use positive design wording such as compact polished emblem, low-bulk ceremonial mark, or streamlined ceremonial design.",
    ),
    (
        "high",
        r"\b(nude|naked|genital|genitals|explicit|porn|sex act|sexual act|underwear|bulge|crotch|explicit anatomy|anatomically correct)\b",
        "Explicit, anatomy-isolated, or porn-coded wording can change the safety interpretation.",
        "Use non-explicit sculptural or fantasy costume language, with no genital detail.",
    ),
    (
        "medium",
        r"\b(bridal carry|princess carry|romantic|lovers|face[- ]to[- ]face|charged gaze|hand resting)\b",
        "Relationship-coded wording combined with close body contact has rejected in two-character contexts.",
        "Use visual-only spacing/gaze/contact ladders or protective heroic companion pose.",
    ),
    (
        "medium",
        r"\b(lift|carry|support|weight[- ]shift|under[- ]thigh|both feet off|airborne)\b",
        "Carry/lift/support language can become a reject family when stacked with minimal costume or close contact.",
        "Climb through spacing, gaze, neutral contact, protective pose, then stronger pose.",
    ),
    (
        "medium",
        r"\b(object-as-censor|shadow-as-censor|cover with|censor)\b",
        "Censor framing implies hidden nudity.",
        "Use a visible opaque fantasy design element instead.",
    ),
    (
        "low",
        r"\b(avoid list|rejection trigger index|retrospective|workbook row)\b",
        "Operational/audit text should not leak into prompt payload.",
        "Keep the prompt task-local and use project notes only for strategy.",
    ),
]


def read_text(path: str | None) -> str:
    if path:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return sys.stdin.read()


def scan(text: str) -> list[Finding]:
    findings: list[Finding] = []
    for severity, pattern, reason, safer_move in PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            findings.append(Finding(severity, pattern, reason, safer_move))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan draft prompt for known image-boundary iteration risks.")
    parser.add_argument("prompt_file", nargs="?", help="Prompt text file. Reads stdin when omitted.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args()

    text = read_text(args.prompt_file)
    findings = scan(text)

    if args.json:
        print(json.dumps({"findingCount": len(findings), "findings": [asdict(f) for f in findings]}, indent=2))
        return 0

    if not findings:
        print("No known project-specific risk phrases found. Still apply normal prompt judgment.")
        return 0

    print(f"Found {len(findings)} project-specific risk reminder(s):")
    for i, finding in enumerate(findings, 1):
        print(f"\n{i}. [{finding.severity}] {finding.reason}")
        print(f"   Pattern: {finding.pattern}")
        print(f"   Safer move: {finding.safer_move}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
