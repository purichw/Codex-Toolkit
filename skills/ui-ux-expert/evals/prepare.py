"""Prepare a solver workspace without reviewer rubrics or authored solutions.

This copies files only; it neither launches agents nor provides a filesystem
security boundary. Mount only the prepared workspace in an authorized isolated
runner before calling a comparison blinded.
"""

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


CASES = {
    "dashboard": "Improve the scanability of this synthetic orders list without removing records, actions, filtering or unknown values. Preserve numeric comparison and keyboard operation at 1280, 390 and 320 CSS px.",
    "mobile-form": "Repair this bilingual contact form on phone and desktop. Preserve all text, input, native date picker, validation and recovery. Center above-field names and native date values; keep freeform input and helper/error prose leading-aligned. Check 320, 390 and 1280 CSS px.",
    "editorial": "Polish this synthetic editorial article while preserving its serif/red publication direction, complete content and route diagram. Make long-title and narrow-screen reading coherent at 320, 390 and 1280 CSS px. Do not convert it to an operations dashboard.",
}


def prepare(skill_root, case, out):
    skill_root = skill_root.resolve()
    out = out.resolve()
    fixture_root = Path(__file__).resolve().parent / "fixtures"
    if case not in CASES or not (skill_root / "SKILL.md").is_file():
        raise ValueError("unknown case or missing skill")
    if out.exists() or out.is_relative_to(skill_root) or out.is_relative_to(fixture_root):
        raise ValueError("output must be new and outside inputs")
    sources = [p for p in skill_root.rglob("*") if p.is_file() and not any(part in ("evals", "__pycache__", ".DS_Store") for part in p.relative_to(skill_root).parts)]
    fixtures = [fixture_root / name for name in ("index.html", "fixture.css", "fixture.js")]
    if any(p.is_symlink() or not p.resolve().is_relative_to(skill_root) for p in sources):
        raise ValueError("skill input must not escape through symlinks")
    if any(not p.is_file() or p.is_symlink() for p in fixtures):
        raise ValueError("fixture inputs missing or symlinked")
    out.mkdir(parents=True)
    manifest = {"case": case, "scope": "runtime skill and raw fixtures only; no agent run", "omitted_evaluation_links": [], "sha256": {}}
    for source, relative in [(p, Path("skills/ui-ux-expert") / p.relative_to(skill_root)) for p in sources] + [(p, Path("app") / p.name) for p in fixtures]:
        target = out / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        if target.suffix == ".md":
            content = target.read_text(encoding="utf-8")
            # References may mention maintenance tooling, but must not expose rubrics.
            content, count = re.subn(r"\[([^\]]+)\]\((?:\.\./)*evals/[^)]+\)", r"\1 (evaluation-only resource omitted)", content)
            if count:
                target.write_text(content, encoding="utf-8")
                manifest["omitted_evaluation_links"].append(relative.as_posix())
        manifest["sha256"][relative.as_posix()] = hashlib.sha256(target.read_bytes()).hexdigest()
    (out / "TASK.md").write_text(
        "# Synthetic UI task\n\nLoad skills/ui-ux-expert/SKILL.md.\n\n" + CASES[case]
        + f"\n\nOpen app/index.html#{case}. Work only on this case. No network, production writes or invented facts."
        + " Preserve fixture behavior. Render and inspect actual results. Record checks, evidence and limitations.\n", encoding="utf-8")
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", required=True, type=Path)
    parser.add_argument("--case", required=True, choices=CASES)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = prepare(args.skill_root, args.case, args.out)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")
    print(f"Prepared {result['case']}; {len(result['sha256'])} hashed files. No agent run or isolation claimed.")


if __name__ == "__main__":
    main()
