---
name: image-boundary
description: Global router for all image-boundary workflows in adult non-explicit image iteration. Use when the user invokes /image-boundary, is unsure which image-boundary skill applies, asks to continue PASS/PARTIAL/REJECT loops, push sensual non-explicit boundaries, recover from image safety blocks, polish quality/anatomy/water, map risk, update image-boundary docs, or coordinate multiple image-boundary skills.
---

# Image Boundary

## Core Contract

Act as the global dispatcher for image-boundary work. Keep the project direction boundary-forward and sensual where requested, but non-explicit and not safety-evasive.

Use simple Thai with the user. If image generation happens, follow `$image-boundary-iteration` and system `imagegen` discipline: show the exact prompt before generation, then wait for `PASS / PARTIAL / REJECT` after the image appears.

## Downstream Skills

Choose the minimal set and read only the needed skill files:

- `$image-boundary-iteration`: default project workflow, branch routing, verdict discipline, logging, baseline selection.
- `$image-boundary-polish`: quality, anatomy, face/hand/water/linework repair without boundary escalation.
- `$image-boundary-nonexplicit-max`: strongest safe sensual/intimate/non-explicit prompt strategy.
- `$image-boundary-rejection-recovery`: safety blocks, user rejects, failed prompt families, backtracking.
- `$image-boundary-safety-map`: risk classification before generating near the boundary.

Skill paths:

- `/Users/point/.codex/skills/image-boundary-iteration/SKILL.md`
- `/Users/point/.codex/skills/image-boundary-polish/SKILL.md`
- `/Users/point/.codex/skills/image-boundary-nonexplicit-max/SKILL.md`
- `/Users/point/.codex/skills/image-boundary-rejection-recovery/SKILL.md`
- `/Users/point/.codex/skills/image-boundary-safety-map/SKILL.md`

## Routing

Use this decision order:

1. Explicit named skill: use that skill.
2. Quality/anatomy/water/clarity defect: use `$image-boundary-polish` plus `$image-boundary-iteration`.
3. Safety block or repeated user reject: use `$image-boundary-rejection-recovery`.
4. Stronger sensual/non-explicit push: use `$image-boundary-safety-map`, then `$image-boundary-nonexplicit-max`.
5. Normal continuation from a verdict: use `$image-boundary-iteration`.
6. Docs/workbook/skill updates: use `$image-boundary-iteration` logging references and the relevant skill being edited.

## Boundary Stance

Preserve the user's intent:

- fewer costume pieces;
- stronger intimacy;
- more skin-read;
- clearer pose/body language;
- richer sensual atmosphere;
- faster iteration after a successful pass.

Keep the implementation non-explicit:

- no visible genitalia or explicit anatomy detail;
- no sexual acts;
- no jailbreak or bypass guidance;
- no repeating blocked prompt families under disguised wording;
- no sacrificing quality for boundary.

## Base Defaults

Do not treat `base` or `safe base` as fully clothed by default. In adult non-explicit fantasy/editorial branches, a strong base may start shirtless: bare torso, bare shoulders, open robe, visible chest/abdomen, and low costume bulk are acceptable starting points when the lower-frame structure remains non-explicit.

Use fully clothed or armored bases only when the user asks for them, identity/style calibration needs them, or a blocked family requires a temporary conservative reset. Otherwise, start from a skin-readable non-explicit base so the iteration does not waste steps removing shirts that did not need to be present.

## Standard Turn Shape

For image work:

1. Identify base/verdict.
2. Name route and reason in one Thai sentence.
3. Translate the user request into safe non-explicit visual language.
4. Provide the exact prompt.
5. Call the image tool.
6. Say nothing after successful image generation.

For docs/skill work:

1. Read the relevant skill(s).
2. Edit live skill files under `/Users/point/.codex/skills`.
3. Mirror important project skills under `/Users/point/outputs/nudity_reference_prompting/skills` when the project uses snapshots.
4. Validate with `skill-creator/scripts/quick_validate.py`.
5. Report paths and any unresolved validation issues.

## Recovery Defaults

- One block: backtrack and change HOW.
- Two related blocks: stop the family.
- One muddy output: polish from the strongest accepted base.
- Two muddy local edits: redraw from a clean base.
- User asks for explicit content: decline that part and offer a max non-explicit route.
