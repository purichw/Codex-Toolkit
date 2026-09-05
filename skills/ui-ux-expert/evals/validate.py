"""Validate evaluation inputs and emit solver briefs separately from rubrics.

This does not run design evaluations or establish visual quality.
"""

import argparse
import json
import re
import sys
from pathlib import Path


FOCUS = {"diagnosis", "tradeoffs", "contextual_rules", "alternatives", "evidence"}


def validate_pack(pack):
    errors = []
    if not isinstance(pack, dict):
        return ["pack must be an object"]
    if type(pack.get("schema_version")) is not int or pack["schema_version"] != 1:
        errors.append("schema_version must be 1")
    cases = pack.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a nonempty list"]
    seen = set()
    covered = set()
    for index, case in enumerate(cases):
        label = f"case[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{label} must be an object")
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case_id):
            errors.append(f"{label} needs a kebab-case id")
        elif case_id in seen:
            errors.append(f"duplicate case id: {case_id}")
        else:
            seen.add(case_id)
        if case.get("provenance") not in ("synthetic", "sanitized-real"):
            errors.append(f"{label} needs explicit provenance")
        if case.get("provenance") == "sanitized-real":
            for field in ("source_note", "permission_note"):
                if not isinstance(case.get(field), str) or not case[field].strip():
                    errors.append(f"{label} needs {field}")
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            errors.append(f"{label} needs a task prompt")
        for field in ("setup", "review_criteria", "failure_modes", "focus"):
            values = case.get(field)
            if (not isinstance(values, list) or not values
                    or any(not isinstance(v, str) or not v.strip() for v in values)):
                errors.append(f"{label}.{field} must be nonempty text items")
            elif field == "focus":
                unknown = set(values) - FOCUS
                if unknown:
                    errors.append(f"{label} has unknown focus: {sorted(unknown)}")
                covered.update(set(values) & FOCUS)
    if FOCUS - covered:
        errors.append(f"missing focus coverage: {sorted(FOCUS - covered)}")
    return errors


def format_case(case, review=False):
    lines = [f"Case: {case['id']}", f"Provenance: {case['provenance']}"]
    if review:
        lines += ["Review criteria:", *[f"- {x}" for x in case["review_criteria"]]]
        lines += ["Failure modes:", *[f"- {x}" for x in case["failure_modes"]]]
    else:
        lines += ["Task:", case["prompt"], "Required fixture setup:"]
        lines += [f"- {x}" for x in case["setup"]]
        lines += ["Missing fixtures block rendered evaluation; do not invent evidence."]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pack", type=Path, default=Path(__file__).with_name("cases.json"))
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--case", help="emit task and setup only for the solver")
    group.add_argument("--review-case", help="emit the separate reviewer rubric")
    args = parser.parse_args(argv)
    try:
        pack = json.loads(args.pack.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    errors = validate_pack(pack)
    if errors:
        print("\n".join(f"ERROR: {e}" for e in errors), file=sys.stderr)
        return 1
    selected = args.case or args.review_case
    if selected:
        case = next((c for c in pack["cases"] if c["id"] == selected), None)
        if case is None:
            print(f"ERROR: unknown case: {selected}", file=sys.stderr)
            return 1
        print(format_case(case, review=args.review_case is not None))
    else:
        print(f"OK: {len(pack['cases'])} scenarios; input structure only, no design evaluation run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
