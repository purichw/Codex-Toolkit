---
name: image-boundary-rejection-recovery
description: Recover after image generation safety blocks, moderation rejections, user REJECT verdicts, or repeated failed boundary-forward adult non-explicit image edits. Use when the user says an image prompt was blocked, rejected, keeps failing, or quality collapsed; diagnose blocked prompt families, backtrack to accepted bases, change HOW safely, preserve non-explicit intent, and avoid repeated unsafe retries.
---

# Image Boundary Rejection Recovery

## Core Contract

Recover momentum after a block or reject without turning the task into safety evasion. Preserve the user's intended direction where allowed, but change the visual strategy when the current prompt family is unsafe, unstable, or artifact-prone.

When this triggers inside `/Users/point/outputs/nudity_reference_prompting`, also use `$image-boundary-iteration` for verdict routing. Use `$image-boundary-polish` when the issue is quality or anatomy damage. Use `$image-boundary-safety-map` when the risk boundary is unclear.

Use simple Thai with the user.

## Diagnose First

Classify the failure:

- `safety block`: the tool rejected the prompt or output.
- `user REJECT`: image generated but missed the user's goal.
- `underdelivered`: safe but too conservative.
- `quality collapse`: faces, hands, anatomy, water, linework, or texture degraded.
- `identity drift`: character identity, hair, face, scene, or branch changed.
- `local-edit saturation`: repeated edits leave ghosts, muddy shadows, duplicated limbs, or broken lower-frame structure.

Do not call a blocked prompt `almost worked`. Treat the block as evidence.

## Recovery Decision

- Safety block: stop that exact family, reduce stacked risk, and change HOW.
- User REJECT for underdelivery: preserve the accepted parts, push one axis harder.
- Quality collapse: stop boundary pushing and polish from the strongest accepted base.
- Identity drift: backtrack to the last identity-stable base.
- Local-edit saturation: redraw from a cleaner base instead of editing the latest artifact.

## Change HOW

Switch the mechanism, not just the adjectives:

- direct garment removal -> composition/crop/material simplification;
- explicit anatomy wording -> smooth sculptural figure-study form;
- lower-frame detail -> water/refraction/pillow-shadow/crop structure;
- same-frame hard edit -> fresh redraw with accepted identity and mood;
- bedroom lower-frame risk -> safe lounge/base composition first, then controlled push;
- water clutter -> optical clarity polish, then body-volume refinement;
- too much effect -> reduce caustics, glare, mist, and shadow density.

## Safe Recovery Prompt Pattern

```text
Use case: <precise-object-edit or stylized-concept>
Asset type: recovery pass for <branch/medium>
Input image: preserve <accepted identities, faces, hair, scene, lighting, composition, boundary level>.

Recovery goal: keep what worked, but change the visual mechanism from <failed HOW> to <new HOW>. Strengthen <one axis> while staying non-explicit.

Quality and safety: avoid the artifact or risk that caused the reject: <drift/block/artifact>. Keep forms smooth, featureless where needed, and gallery-safe. No explicit anatomy, no sexual act, no new reveal beyond the accepted boundary, no text, no logo, no watermark.
```

## Communication Pattern

Tell the user:

- what failed;
- what base you are returning to;
- what HOW you are changing;
- whether this is `boundary continuation`, `quality polish`, or `safe redraw`.

Example:

```text
รอบนี้ block เพราะเรา stack ช่วงล่าง + intimacy หนักไปพร้อมกันครับ ผมจะหยุด prompt family นี้ แล้วกลับไปฐานที่ผ่านล่าสุด เปลี่ยนเป็น crop/แสง/ท่านั่งแทนการสั่ง reveal ตรง ๆ
```

## Stop Rules

- Two related safety blocks: stop the family.
- Two local edits that melt details: redraw or backtrack.
- One severe identity drift: backtrack immediately.
- If the user asks for a jailbreak, bypass, or explicit sexual content, refuse that part and offer a max non-explicit continuation.
