---
name: course-image-assets
description: Generate, reuse, crop, map, audit, and QA educational course image assets across projects. Use when the user needs vocabulary or flashcard images, lesson card art, visual hints, badges, semantic image mapping, inclusive learning imagery, crop/centering fixes, placeholder replacement for course content, or generated educational illustrations.
---

# Course Image Assets

Use this skill when images teach or identify course content. Project-specific
skills should provide exact paths, commands, helpers, and visual style.

## Core Rule

Reuse only when the existing asset is semantically correct. If no correct asset
exists, generate, source, or create a new one. Never fill a missing item with a
merely similar image.

## Asset Decision Workflow

1. Identify the exact learning item, meaning, lesson, context, and target
   component.
2. Search existing mappings, files, manifests, and audit reports first.
3. Reuse only when the asset depicts the same concept, same sense of ambiguous
   terms, correct context, readable small size, good crop, and matching style.
4. Generate/create a new asset when the existing one is wrong, unclear,
   off-center, cluttered, low quality, over-cropped, or semantically ambiguous.
5. Wire through the project's canonical helper/manifest, not ad hoc paths.
6. Preserve existing assets unless intentionally replacing them with a better,
   verified version.

Use `$placeholder-image` for general web image sourcing, `$snapshot` for visual
evidence, `$mobile-web-qa` for responsive card/crop checks, `$tts-audio-assets`
when course data/audio changes together, and `$release-gate` before shipping.

Use `$efficient-execution` for batches: audit semantic mappings first, reuse
verified assets, fix deterministic crop/resize issues locally, and generate
only items whose meaning or quality actually fails.

## Meaning And Deduplication

- Same term + same meaning: reuse when quality is good.
- Same term + different meaning: separate images or explicit context.
- Same category but different object: do not reuse unless the lesson item is the
  category itself.
- Design mock placeholders do not override real product assets unless the user
  explicitly asks to replace them.

## Generation Workflow

When generating raster images, use the system `imagegen` skill/tool. Before the
image call, state the exact prompt, target item, meaning, crop/aspect needs, and
intended file/use. After the tool returns, do not add extra text in the same
response; inspect and continue in the next step.

Prompts should include:

- target object/action and learning context;
- educational illustration or project-defined style;
- centered subject, simple background, enough padding, square/card-safe
  composition;
- no text, letters, labels, watermark, or UI unless the asset type requires it.

For people-centered learning images, include natural diversity when it helps the
meaning and does not distract. Avoid stereotypes, joke framing, sexualized cues,
or identity labels unless explicitly requested.

## Crop And QA

Every asset must pass:

- subject centered and fully visible;
- enough padding on all sides;
- readable at card/thumbnail size;
- no competing accidental object;
- correct alt text and stable filename;
- rendered UI crop checked where the image appears;
- audit scripts/tests/builds run when project data or assets changed.

Use deterministic crop/resize/format tools for local fixes instead of
regenerating good imagery.

## Closeout

Report which items/assets changed, whether each was reused/generated/recropped
or left unchanged, mapping helpers/manifests updated, audits/tests run, rendered
crop evidence, and any semantic compromises.
