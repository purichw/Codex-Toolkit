---
name: shane-thai-image-assets
description: Generate, reuse, crop, replace, optimize, and QA image assets for the Shane Thai learning app. Use when the user mentions Shane Thai images or when Codex works on vocabulary images, lesson card artwork, Unit image generation, badge images, image asset mapping, crop/centering fixes, placeholder replacement, or visual asset reuse decisions for this project.
---

# Shane Thai Image Assets

Use `$course-image-assets` for the reusable educational image asset workflow.
This skill is the Shane Thai overlay: exact asset paths, helper
functions, audits, and style constraints.

Use this skill before adding, replacing, mapping, cropping, or auditing images in the Shane Thai app.

## Project context

- Repo: `/Users/point/Website Projects/thai-flashcards`
- Main-course visual assets: `src/assets/main-course/visuals/<filename>.webp`
- Visual helper: `src/data/mainCourseVisuals.ts`
- Main-course image mapping: use `mainCourseVisual(filename, alt)` for course visuals and `visualHint(filename, alt)` for shared visual hints.
- Main-course image audit: `tools/audit-main-course-images.mjs`
- General asset audit: `tools/audit-assets.mjs`
- Badge assets: `public/assets/badges/` and `public/assets/badges/thumbs/`
- Mascot assets: `public/assets/mascots/` and `src/assets/mascotRegistry.ts`

Common commands:

```bash
npm run images:audit
npm run images:audit:check
npm run assets:audit
npm run test:data
npm run build
node tools/audit-main-course-images.mjs --json
```

Use adjacent skills when the task crosses boundaries:

- `$course-image-assets` for the global educational image contract, semantic
  reuse, generation, crop, and closeout.
- `$shane-thai-audio-generator` when lesson data, vocabulary IDs, prompts, or UI
  controls change alongside images.
- `$placeholder-image` for generic sourcing/crop judgment outside Shane-specific
  warm educational assets.
- `$reference-to-a-tee` when card/image layout must match Claude Design exactly.
- `$mobile-web-qa` and `$snapshot` when rendered card crop/responsive evidence is
  needed.
- `$efficient-execution` for batch scoping, semantic-audit first passes, and
  avoiding broad regeneration when deterministic crop or reuse is enough.
- `$release-gate` before commit, push, deploy, or handoff.

## Core rule

Reuse only when the existing asset is truly correct. If no correct asset exists, generate or create a new one. Never fill a missing word with a merely similar image.

Bad example: using a coffee-table image for `กุญแจ` because no key image is available.
Correct action: generate a new key image and map it to the key vocabulary item.

## Asset decision workflow

1. Identify the exact Thai item, English meaning, lesson, and semantic context.
2. Search existing asset mappings and files first:
   - Search `src/data` for the item ID, Thai, English, and current `mainCourseVisual(...)` call.
   - Search `src/assets/main-course/visuals` for exact or near-exact filenames.
   - Run `npm run images:audit` when looking for missing main-course card images.
3. Reuse an asset only when all are true:
   - It depicts the same concept, not just a nearby category.
   - It matches the same meaning where Thai has ambiguity.
   - It is clear at small flashcard size.
   - It is well centered and not awkwardly cropped.
   - It fits the app’s warm educational visual language.
4. Generate a new asset when:
   - No exact asset exists.
   - The available asset is semantically wrong.
   - The available asset is low quality, off-center, over-cropped, cluttered, or confusing.
   - The word has a different meaning from a reused Thai homograph.
5. Wire the asset through the existing helper:
   - Place main-course card art in `src/assets/main-course/visuals/<slug>.webp`.
   - Reference it as `mainCourseVisual('<slug>', '<clear alt text>')`.
   - Use `visualHint(...)` only for shared visual hints from `src/assets/visual-hints`.
6. Preserve existing assets unless intentionally replacing them with a better, verified version.

## Meaning and dedupe rules

- Same Thai + same meaning: reuse the same asset across units when quality is good.
- Same Thai + different meaning: use separate ids/assets.
  - `ถูก` = cheap and `ถูก` = correct should not share an image.
  - `เบา` = light in weight and `เบา` = quiet/soft should be separate or explicitly context-sensitive.
- Same category but different object: do not reuse unless the item intentionally represents the category.
- Claude Design placeholders do not override real product assets. Keep real app assets unless the user explicitly asks to remove or replace them.

## Lesson vocabulary image theme

Use a warm, cozy educational illustration style:

- soft storybook / watercolor / gentle hand-drawn feel
- cream, muted green, and warm natural colors
- friendly and beginner-readable
- simple clean background, with light botanical/grass details only when helpful
- clear single subject or clear paired contrast for adjectives/antonyms
- no embedded text in vocabulary/lesson images
- avoid clutter, tiny details, photorealism, harsh lighting, and high-saturation game art

Images must work inside square-ish flashcard frames and remain readable when small.

## Character diversity and families

When generating images with people, vary gender presentation, skin tone, age, body type, and family structure across a unit so the course feels inclusive and LGBTQ+ friendly.

- Include same-gender couples and families naturally when the vocabulary/context fits, such as two fathers with children or two mothers with children.
- For LGBTQ+ representation, prefer clear everyday same-gender pairings over abstract identity signaling. Bias same-gender couple/family prompts toward man-man pairings about 80% of the time because they read more clearly at small card size; use woman-woman pairings for the remaining variety.
- Avoid stereotypes, joke framing, exaggerated presentation, pride flags, labels, or sexualized cues unless the user explicitly asks for them.
- Keep the scene ordinary, warm, and educational: family cooking, parents helping a child, couples shopping, friends studying, or people doing the target action.
- Do not force relationship or identity detail into images where the target item needs a single object or a neutral person for clarity.

## Crop and framing requirements

Every asset must pass these before use:

- Subject is visually centered.
- Important object parts are not cut off.
- Enough padding exists on all sides.
- Crop is square-safe.
- Tall/wide objects fit fully within the frame.
- The object remains legible at card size.
- No accidental background object competes with the target.

If a generated image is good but off-center, recrop it. If recropping cannot fix it, regenerate.

## Generation and editing workflow

When generating a new image, use the system `imagegen` skill/tool and obey its output rules. Before calling the tool, provide the exact prompt and target filename/meaning. After the tool returns, do not add extra text in that same image response; inspect and continue in the next step.

For local crop/resize/format work, use deterministic image tools rather than regenerating. Keep source scratch files out of committed/public asset folders unless they are intentional final assets.

Before wiring a generated asset:

- Inspect the image file directly.
- Confirm the subject is semantically exact for the Thai item.
- Convert/optimize to WebP when the asset belongs in `src/assets/main-course/visuals`.
- Use a stable kebab-case filename that reflects the concept, not an internal prompt name.
- Add useful alt text; do not leave generic alt such as `image` or duplicate unrelated alt text.

## Badge assets

Badge assets are an exception to the “no embedded text” guideline when the badge artwork itself intentionally includes title/ribbon text.

Badge rules:

- Preserve the dedicated badge artwork the project already has.
- Prefer the user-provided transparent PNG badge set when available.
- Optimize badges only as far as they remain crisp in the largest modal/pop-up usage.
- Locked badge visuals may be grayscale/desaturated versions of the actual badge image, not generic placeholders, unless no badge artwork exists.
- Do not replace real badge art with custom placeholder icons just because a Claude Design mockup used placeholders.

## Claude Design interaction

Claude Design standalone HTML is the component-level layout reference, but product requirements still win for assets:

- Keep Google Sans if the project requires it.
- Keep existing real assets when Claude uses placeholders.
- Match Claude component sizing and layout as closely as possible while preserving real product images.
- Check mobile and tablet versions, not only desktop.

## Generation prompt checklist

For a concrete vocabulary item, include:

- target object in English and Thai context
- warm storybook watercolor educational illustration
- centered single subject
- clean cream background
- enough padding around the object
- square composition
- no text, labels, letters, watermark, or UI

Example:

`A single small house key, centered, warm storybook watercolor educational illustration, clean cream background with subtle soft green decorative leaves near the bottom, square composition, generous padding, clear at small flashcard size, no text, no letters, no watermark.`

For paired adjective/antonym images, show the contrast clearly without text:

`Two simple objects side by side showing big versus small, warm storybook watercolor educational illustration, centered, clean cream background, square composition, no text.`

For family or people-centered vocabulary, include inclusive casting when it still keeps the target meaning clear:

`Two fathers and their child cooking together in a cozy kitchen, warm storybook watercolor educational illustration, clean cream background, square composition, generous padding, clear family relationship, no text, no letters, no watermark.`

## QA checklist before commit/deploy

- Inspect the actual image files or rendered UI.
- Verify the mapping points to the correct semantic item.
- Run `npm run images:audit:check` when main-course image mappings changed.
- Run `npm run assets:audit` when public badges, mascots, thumbnails, or other public assets changed.
- Run `npm run test:data` when course data/image mappings changed.
- Check card display size and crop.
- Check mobile/tablet if the image appears in responsive layouts.
- Confirm no unrelated asset was substituted.
- Run the project’s relevant tests/builds if code/data changed.

If audio and image/course-data mappings changed together, run the relevant audio
audit from `$shane-thai-audio-generator` too; report one combined asset map
instead of disconnected audio/image notes.

When reporting completion, mention whether images were reused, regenerated, recropped, or intentionally left unchanged.
