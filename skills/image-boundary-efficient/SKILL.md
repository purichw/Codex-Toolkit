---
name: image-boundary-efficient
description: Speed-preserving operating layer for image-boundary work. Use when the user asks to make Imagen/image-boundary iterations faster, cheaper, more efficient, less blocked, less retry-heavy, or asks for a fast loop without compromising quality. Also use when deciding whether to keep or remove the efficiency layer because quality is starting to fall.
---

# Image Boundary Efficient

## Core Contract

Use this as a removable operating layer over `$image-boundary`, not as a replacement for the boundary skills.

Move faster by reducing wasted generations: repeated blocked prompt families, multi-axis prompts, stale bases, unnecessary rediscovery, overlong constraints, and edits on images that already started to degrade. Do not move faster by lowering the quality bar, using lower-quality settings, hiding risk, weakening the user's boundary-forward intent, or skipping required `PASS / PARTIAL / REJECT` discipline.

Use simple Thai with the user.

## When Active

Use this skill when:

- the user asks whether Imagen can be faster;
- the user wants a faster image-boundary loop without quality compromise;
- the workflow has too many safety blocks, rejects, or drift retries;
- the prompt is getting long, redundant, or packed with multiple edit axes;
- the user explicitly invokes `/image-boundary-efficient`;
- the user wants the efficient layer added, removed, paused, or toggled.

Stop using this skill when:

- quality visibly falls, muddiness increases, or anatomy/face/hands/water break;
- the user asks to disable efficient mode;
- the next step is clearly quality restoration only;
- the route needs a careful recovery, branch reset, or exact evidence/logging pass.

When stopping it, say briefly in Thai that the efficient layer is off and route to `$image-boundary-polish`, `$image-boundary-rejection-recovery`, or normal `$image-boundary-iteration`.

## Required Pairing

Always pair this skill with the relevant image-boundary skill:

- normal continuation: `$image-boundary-iteration`;
- stronger sensual non-explicit push: `$image-boundary-safety-map`, then `$image-boundary-nonexplicit-max`;
- quality falling: remove this layer, use `$image-boundary-polish`;
- safety block or repeated reject: use `$image-boundary-rejection-recovery`;
- new image/edit generation: also use system `imagegen`.

This skill only optimizes the route and prompt shape. The downstream skill still owns safety, boundary level, recovery, polish, and verdict discipline.

## Fast Quality-Preserving Loop

Before each image call:

1. Pick the strongest accepted base, not automatically the latest output.
2. Choose exactly one active axis: `COSTUME`, `POSE`, `CROP`, `LOOK`, `INTIMACY`, `QUALITY`, `WATER`, or `LIGHT`.
3. State the route in one Thai sentence: `efficient layer active`, base/verdict, one axis, and quality bar unchanged.
4. Use a short high-quality prompt template: preserve invariants, one primary request, coverage structure, quality line.
5. Do not stack boundary push plus polish in one generation. Polish first if quality is already shaky.
6. Do not repeat a blocked prompt family with synonyms. Change HOW or backtrack.
7. Generate once, then wait for `PASS / PARTIAL / REJECT`.

After each output:

- `PASS`: promote the accepted dimension as the next efficient base.
- `PARTIAL`: preserve what worked; change one missing axis only.
- `REJECT`: stop that prompt family or backtrack; do not intensify the same wording.
- quality defect: turn efficient layer off and polish from the strongest accepted base.

## Prompt Shape

Prefer this compact structure:

```text
Use case: precise-object-edit
Asset type: <branch/medium> efficient one-axis continuation
Input image: preserve <identities, faces, hair, gaze, pose, composition, scene, lighting, hands, accepted boundary, lower-frame structure>.

Primary request: change only <one axis> by <specific visual mechanism>. Keep adult characters, strong skin-read, clear faces/hands, low visual clutter, and the accepted non-explicit boundary.

Coverage structure: preserve <water/crop/shadow/pillows/robe-edge cords/marble ledge/reflection> as the non-explicit lower-frame system. Do not add a new reveal or new body detail.

Quality: polished <medium>, crisp faces/hair, readable hands, coherent anatomy, controlled texture, no text, no logo, no watermark.
```

Keep the prompt short, but not vague. A short prompt is only efficient when it preserves the winning base and the exact one-axis request.

## Efficiency Rules

Do:

- reuse the last explicit `PASS` base;
- preserve identity, pose, crop, and accepted boundary unless the user names that axis;
- convert risky direct wording into one clean visual mechanism;
- use branch-proven HOW before inventing a new prompt family;
- stop after one block and change HOW;
- stop after two related blocks and abandon that family;
- split quality repair and boundary push into separate turns.

Do not:

- reduce resolution, quality, or polish expectations as the efficiency strategy;
- use explicit anatomy wording, sexual acts, or safety-evasion framing;
- add long negative lists that make the prompt look like a workaround;
- stack costume reduction, lower-frame structure, intimacy, pose, and polish in one call;
- keep editing a muddy image just because it is the latest;
- hide that a check, polish pass, or recovery step was skipped.

## Turn Shape

When this layer is active for image work:

1. Name the base/verdict.
2. Say `efficient layer active` in simple Thai and identify the one axis.
3. Say that quality bar and boundary safety are unchanged.
4. Provide the exact prompt.
5. Call the image tool.
6. Say nothing after successful image generation.

If quality starts falling, do not continue efficient mode. Say the layer is off and route to polish.
