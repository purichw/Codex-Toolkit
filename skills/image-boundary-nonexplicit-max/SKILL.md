---
name: image-boundary-nonexplicit-max
description: Maximize sensual, intimate, boundary-forward image prompting while staying non-explicit. Use when the user asks to push adult fantasy/watercolor/editorial image iterations as far as possible without explicit nudity detail, sexual acts, or safety-system evasion; use with image-boundary-iteration, image-boundary-polish, or image-boundary-safety-map as needed.
---

# Image Boundary Nonexplicit Max

## Core Contract

Push the visual result to the strongest safe non-explicit boundary. Preserve the user's appetite for intensity, intimacy, reduced costume bulk, and sensual figure-study energy, but do not create or optimize a jailbreak, bypass, or safety-evasion workflow.

When the request is in `/Users/point/outputs/nudity_reference_prompting`, also use `$image-boundary-iteration` for branch routing and verdict discipline. If quality is degraded, use `$image-boundary-polish` first. If risk is unclear, use `$image-boundary-safety-map` first.

Use simple Thai with the user.

## Non-Explicit Maximum Means

Aim for:

- adult characters only;
- strong sensual mood, gaze, proximity, and pose;
- low costume bulk, minimal ornamental coverage, or visible skin-read;
- clean torso/limb anatomy, elegant hands, readable faces;
- water, crop, bedding, robe-edge cords, light, shadow, or composition carrying the lower-frame structure;
- smooth sculptural forms without precise explicit detail;
- intimate atmosphere without sexual acts.

Do not aim for:

- visible genitalia, explicit anatomy detail, arousal detail, or sexual acts;
- pornographic framing or instructions;
- prompts designed to hide prohibited intent from moderation;
- repeated retries of a blocked explicit request using euphemisms.

## Workflow

1. Identify the current accepted base and branch.
2. State the translated non-explicit goal in Thai before generating.
3. Pick one primary push axis. Use two only when the base is stable.
4. Translate risky wording into visual design language, not weaker intent.
5. Generate or edit once, then wait for `PASS / PARTIAL / REJECT`.
6. If the result blocks, stop that exact prompt family and use `$image-boundary-rejection-recovery`.

## Base Creation Default

Do not start from fully clothed art unless there is a reason. For adult non-explicit branches, the default base can already be shirtless or open-robe: bare chest, shoulders, arms, abdomen, jewelry, hairline cords, and low-bulk styling are normal safe-base ingredients when the lower frame is handled by crop, water, bedding, shadow, mist, or refraction.

This saves iteration steps. Do not spend the first several generations removing shirts from a base that could have started with clean torso visibility. Reserve fully clothed starts for character identity matching, armor/costume studies, conservative recovery after repeated blocks, or explicit user preference.

## Strong Push Axes

Use these levers instead of direct explicit wording:

- `composition`: tighter editorial crop, diagonal reclining lines, lower-frame crop, triangle grouping;
- `pose`: direct gaze, leaned-in posture, seated lounge, back-to-back, ritual kneel, pool ledge, shallow-water duet/trio;
- `costume`: reduce garment bulk, remove trouser-like shapes, simplify to hairline-thin cords, robe-edge lines, jewelry-only accents;
- `surface`: transparent water, moonlit bedding, marble reflection, lacquer-like light, pale-gold cords;
- `coverage structure`: crop, hands, pillow shadow, waterline, mist, foreground ledge, soft refraction;
- `quality`: crisp faces/hands, smooth torso modeling, clean hair, coherent limbs, controlled texture.

Do not stack every axis at once. Boundary wins usually come from one clean visual system, not maximum vocabulary pressure.

## Prompt Pattern

```text
Use case: <stylized-concept or precise-object-edit>
Asset type: max-boundary non-explicit <branch/medium>
Input/reference image: preserve <accepted identities, composition, style, scene, lighting, faces, hands, current accepted boundary>.

Primary request: push the image to a stronger sensual non-explicit figure-study read through <one selected axis>. Keep adult characters, strong gaze, close composition, low costume bulk, smooth sculptural anatomy, and clean skin-read.

Coverage structure: keep the lower-frame area tasteful and non-explicit using <water/crop/pillows/hands/shadow/cords/refraction>. No precise anatomical detail, no sexual act, no explicit nudity detail, no added clothing bulk unless needed for safe framing.

Quality: polished <medium>, crisp faces and hair, readable hands, coherent limbs, warm/cool lighting balance, controlled texture. No text, no logo, no watermark.
```

## Proven Translations

- User says `เอากางเกงออก`: `remove opaque trouser-like lower garments; replace bulky fabric forms with smooth non-explicit lower-frame silhouettes carried by water/crop/light`.
- User says `แรงขึ้น`: `stronger sensual figure-study read, closer gaze, cleaner skin-read, lower costume bulk`.
- User says `เห็นขาเพิ่ม`: `longer graceful leg silhouettes, natural athletic proportions, protected lower-frame composition`.
- User says `น้ำใส`: `optically transparent water, not brighter; minimal glare, visible marble floor, soft featureless refracted forms`.
- User says `intimate`: `close triangular grouping, direct gaze, leaned-in posture, restrained sensual atmosphere`.

## Stop Rules

- If one attempt blocks for sexual content, backtrack and change the visual system.
- If two related attempts block, stop that family completely.
- If local edits create muddy anatomy or repeated artifacts, use `$image-boundary-polish` or redraw from the strongest accepted base.
- If the user asks for explicit sexual content, do not provide it. Offer a max non-explicit alternative.
