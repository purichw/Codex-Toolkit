# Image Reference Workflow

Use for image-only work and for mixed references whose visual authority includes
images. Implement from the supplied pixels without requiring HTML. Do not feed
image bytes into the HTML extractor.

Apply [operating-guide.md](operating-guide.md) first. Exact image matching can
use fast effort for a small property repair; precision and uncertainty rules
remain the same, but a full inventory/measurement table is not required.

## Inventory And Inspect

Open every image relevant to the requested surface with the available image
viewer. Preserve originals and identify the source/version and relevant pixel
dimensions/crop. Record hashes when tracking multiple versions, reusing evidence,
or required by a handoff; a fresh direct comparison can use the actual source
path/attachment identity without a hash inventory. For inline-only images,
record the attachment identity; do not invent a filesystem path or hash.

Record what each image depicts: route/screen, component, visible state, language,
content, overlays, and top/full-page/mid-page/crop coverage. Separate different
screens and variants; do not combine them into one invented page. Use a contact
sheet for navigation when helpful, then inspect original-resolution details.

Identify device frames, browser chrome, annotations, padding around the design,
perspective, and obscured regions. These are not product UI unless the brief
explicitly says so. A cropped image says nothing about components outside it.

## Calibrate Coordinates

- Record image-pixel width/height separately from CSS viewport width/height.
  Screenshot pixels alone do not establish device pixel ratio, browser zoom, or
  resize history. Image DPI metadata is not browser DPR evidence.
- When the content region is known, record its crop origin and size. With a
  known CSS width, derive the uniform scale from content pixels to CSS pixels;
  subtract the crop origin before mapping coordinates. A full-page image's height
  is document coverage, not necessarily viewport height.
- When scale or viewport is unknown, keep measurements in image pixels or
  normalized ratios. Choose and record a provisional implementation viewport,
  compare proportions, and state that exact CSS values are inferred. Ask for
  dimensions only if their uncertainty blocks a material acceptance requirement.
- Do not independently stretch axes or resize each component to manufacture a
  match. For perspective mockups or compressed images, disclose the reduced
  measurement confidence and prefer supplied flat frames when available.

## Build Component Contracts

For component/page reconstruction map the visible hierarchy: shell/header/nav,
main columns, rails, sections,
cards/rows, text blocks, controls, overlays, media frames, and visible footer.
Measure anchor positions, bounding boxes, repeated gaps, alignments, line wraps,
item count/order, media aspect ratio, border/radius, and color roles.

For a fast repair, inspect the affected property and its surrounding relationships
instead of measuring all these groups. For each value used to support a claim,
retain evidence type and confidence; a short note is sufficient for a single fix:

| Evidence | What it supports |
| --- | --- |
| Observed | Visible content, order, selected state, alignment, or crop. |
| Image-measured | Pixel or normalized bounds, gaps, sampled colors, with scale and uncertainty recorded. |
| Source-measured | A value from matching authoritative source or metadata, when supplied. |
| Inferred | Proposed CSS layout, font family/weight, spacing token, breakpoint, or behavior. |
| Unknown | Occluded content, unavailable original assets, hidden states, or unestablished scale. |

Do not claim a font family, DOM hierarchy, flex/grid choice, exact color token,
or CSS shadow merely from visual resemblance. Anti-aliasing, compression, color
profiles, and transparency can alter sampled values. OCR may seed text, but
visually verify it, especially small text, numbers, and non-Latin scripts; mark
unreadable content rather than inventing it.

Locate supplied/product assets before substituting. A screenshot of an image is
not its original source asset. Record unavailable fonts, icons, or media and any
substitution. Do not implement the entire screenshot as one background image;
build semantic components and real controls. Preserve product-required assets.

## Behavior And Responsive Limits

A still image cannot establish hover, focus, transitions, scroll mechanics,
backend behavior, permissions, or hidden pages. Preserve existing product
contracts; use explicit handoff requirements for new behavior. For an otherwise
unspecified control, choose a conventional behavior within the requested scope
and label it inferred, or ask when the choice materially changes product scope.
Do not infer destructive actions or new backend features from an icon alone.

Multiple widths can show layout changes, but do not prove the exact breakpoint
between them. Record observed arrangements and choose robust breakpoint values;
test interpolation and long content as implementation QA. When only desktop is
supplied and mobile is requested, build a coherent mobile adaptation, exercise
touch/focus/overflow, and label it an adaptation rather than mobile-reference
parity. An unseen state is not a visual exception or a reason to disable it.

## Mixed Reference Conflicts

Map each artifact to version, surface, state, and authority. A user-selected newer
image can override old HTML for that region while matching HTML remains useful
for other regions or assets. Do not silently average conflicting designs.
Use metadata and handoff context to resolve apparent differences such as scroll,
locale, data, or open overlays. Document the choice; ask only when a material
conflict remains unresolved. Never promote old CSS over an explicitly chosen image.

## Compare And Converge

Capture the rendered implementation at the calibrated viewport and equivalent
route/data/state. Use `$snapshot` for labeled side-by-side views; keep original
and compared regions identifiable. Compare high-impact geometry first, then
typography, media crop, detail, and states within the requested scope. Include
supplied lower-page content for page-level claims, not merely because a button
repair happens to be on a long page.

For several measurements or a formal audit use a table such as the following;
for a fast repair use a brief measurement/uncertainty note and current comparison:

```text
component | reference file/state | evidence type | reference bounds/units |
implementation bounds/units | calibration | delta/tolerance | status
```

Set reasonable tolerances from resolution, scale confidence, and importance
before evaluating a match. Do not adjust tolerance to conceal a known mismatch.
Optional overlays or pixel differences can help after registration, but a global
similarity score cannot prove component coverage or interaction correctness.

Mark measured visible matches `matched`; mark observed mismatches `not done` or
document accepted visual exceptions. Keep unobservable properties in an evidence
limits list, outside pass/fail visual coverage. Report the precise visible scope
verified and any responsive/behavior assumptions. Use
[release-gate.md](release-gate.md) before completion or publishing.
