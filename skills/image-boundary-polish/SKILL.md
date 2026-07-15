---
name: image-boundary-polish
description: Restore image quality in boundary-forward non-explicit image iterations without changing the accepted boundary level. Use when the user says an image is breaking, muddy, artifacted, needs quality polish, or needs face/hand/anatomy/water/linework cleanup before continuing an image-boundary-iteration workflow.
---

# Image Boundary Polish

## Core Contract

Use this skill for quality recovery, not boundary escalation. Keep the user's accepted image direction intact while repairing visual defects.

When this skill triggers inside the `nudity_reference_prompting` project, also use `$image-boundary-iteration` for branch routing, verdict discipline, and logging decisions. If editing or generating an image, also use the system `imagegen` skill.

Use simple Thai when talking to the user.

## Decision Rule

Choose polish when:

- the user says an accepted image is muddy, broken, artifacted, or lower quality;
- faces, hands, linework, water, lighting, skin-readability, or anatomy coherence degrade after edits;
- a boundary push has succeeded visually but the rendering needs cleanup before continuing;
- a hard boundary prompt has just blocked and the last accepted image needs rescue.

Do not choose polish when the real request is a new pose, new scene, lower waterline, fewer garments, stronger intimacy, or a higher boundary. Use `$image-boundary-iteration` for that, then return here if quality breaks.

## Workflow

1. Select the strongest accepted base, not automatically the latest image.
2. Tell the user the pass is `quality-restoration only` and that boundary level, pose, waterline/crop, and non-explicit lower-frame structure will be preserved.
3. Use a precise edit prompt when an image target exists. Preserve identity, composition, face/hair, pose, hands, lighting, medium, scene, and accepted boundary.
4. Repair only visual quality: muddy texture, broken linework, face drift, hand distortion, uneven shading, noisy water/reflections, overdone effects, and background geometry.
5. Explicitly forbid boundary changes: no lower waterline, no new reveal, no new body detail, no new costume bulk, no new pose, no new characters.
6. After image generation, do not add extra text in the same response. Wait for the user's verdict.

## Prompt Pattern

Use this structure and customize it to the branch:

```text
Use case: precise-object-edit
Asset type: <medium/branch> quality restoration
Input image: edit target; preserve the same characters, identities, composition, faces, hair, gaze, pose, lighting, scene, jewelry, hands, accepted boundary level, and non-explicit lower-frame structure.

Targeted edit only: restore image quality and clarity without changing the boundary level. Clean up muddy rendering, noisy artifacts, warped linework, uneven shading, distorted hands, face drift, fractured water/reflections, and background geometry issues. Repaint with crisp <medium> linework, polished faces, clean hair shapes, readable hands, smooth torso modeling, coherent shoulders and arms, clear scene geometry, luminous water/light, and controlled texture.

Keep the waterline/crop/lower-frame structure essentially the same as the reference image. Do not add new body detail, do not lower the water further, do not change poses, do not add clothing bulk, and do not add extra characters. Maintain tasteful non-explicit fantasy art. No text, no logo, no watermark.
```

## What Worked

The strong recurring pattern is: polishing passes survive when they are single-axis restoration passes.

Use wording like:

- `restore image quality and clarity without changing the boundary level`
- `quality restoration only`
- `preserve the waterline and lower-frame structure`
- `clean up broken or muddy rendering`
- `crisp elegant watercolor linework`
- `polished faces, clean hair shapes, readable hands`
- `smooth torso modeling and coherent shoulders and arms`
- `luminous water, marble geometry, and warm lantern reflections`

## Avoid

Do not mix these into a polish prompt:

- lower waterline or stronger reveal wording;
- direct garment-removal wording;
- explicit anatomy or lower-frame body-detail wording;
- new pose, new scene, stronger intimacy, or new camera move;
- `almost gone`, `no fabric`, `no coverage`, or similar escalation;
- large negative lists that make the image prompt feel like a safety workaround.

If the user asks for quality and a harder boundary together, split the work: polish first, then push boundary in a separate turn or prompt.

## Stop Rules

- If one polish pass drifts identity, pose, or boundary, mark it as drift and backtrack.
- If two polish attempts on the same base still melt details, switch to a cleaner accepted base or a clean redraw.
- If a boundary prompt blocks twice, stop that family. Do not retry it by disguising the same reveal language as quality repair.
- If the user passes the polish result, treat it as the working base only after the output exists and the verdict is explicit.

## Project Reference

For the `nudity_reference_prompting` project, read this living doc when doing broader documentation or handoff work:

`/Users/point/outputs/nudity_reference_prompting/References for Codex/design_polishing_playbook.md`

For longer prompt recipes, read `references/polish-prompt-recipes.md`.
