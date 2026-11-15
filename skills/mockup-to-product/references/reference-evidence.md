# Reference Evidence And Comparison

Use for image-led implementation, mixed-source conflicts, uncertain measurements
or reference/app comparison. This improves judgment; it does not make every
mockup pixel-exact or require a measurement ledger for routine design choices.

## Select The Evidence

Open the original images relevant to the requested surface. Identify their
source/version, route or component, visible state, language, content and coverage
(viewport, full page, mid-page or crop). A contact sheet helps navigation but
does not replace inspecting details at readable resolution. Inline attachments
can use their attachment identity; never invent a local path or source hash.
Use hashes when versions or reused evidence need disambiguation, not by habit.

Separate device frames, browser chrome, slide padding, annotations, perspective
and occluded regions from actual product UI. A cropped screenshot does not prove
the absence of navigation, lower-page content, controls or hidden states.

For mixed images/HTML, choose authority per surface/state. The user's selected
image may supersede old HTML for one region while the HTML remains useful for
assets or other regions. Check whether differences are merely data, locale,
scroll or open disclosures before treating them as conflicts. Do not average
incompatible versions, assume HTML outranks images, or treat modification time
as user approval. Ask only about an unresolved choice that materially changes
the result; continue independent work.

## Distinguish Facts From Implementation Choices

| Evidence | Supports |
| --- | --- |
| Observed | Visible hierarchy, content, ordering, alignment, crop or selected state. |
| Image-measured | Pixel or normalized bounds, spacing and sampled color, with scale/confidence noted. |
| Source-measured | Values from selected matching source, computed styles or authoritative metadata. |
| Inferred | Proposed CSS, font, token, breakpoint, behavior or reconstructed artwork. |
| Unknown | Occluded content, unavailable source assets, hidden states or unestablished scale. |

A screenshot does not prove font identity, DOM structure, flex versus grid,
exact tokens or shadow algorithms. Compression, antialiasing, transparency and
color profiles affect samples. OCR is a starting point: visually verify text,
especially Thai, small labels and numbers. Mark unreadable content rather than
inventing it. Locate supplied or product assets before substituting; a screenshot
of an image is not its original asset. Keep source originals unchanged.

## Calibrate Only As Far As The Decision Needs

- Keep image pixels separate from CSS pixels. Screenshot dimensions and DPI
  metadata do not establish browser DPR, zoom or resize history.
- Identify the content crop origin and dimensions. With known CSS width, use a
  uniform scale: `css_x = (image_x - crop_x) * css_width / crop_width`; apply the
  same scale to both axes. Full-page image height is document coverage, not
  necessarily viewport height. Verify the source is a flat, uniformly scaled view.
- If scale is unknown, use normalized proportions or image pixels and name a
  provisional implementation viewport. Do not present inferred CSS as measured
  source truth. Ask for dimensions only when an explicit requirement depends on
  them; normal responsive composition can proceed with judgment.
- Never stretch axes independently, resize each component separately or distort
  the reference to fake alignment. Perspective or heavily compressed images
  lower confidence; prefer flat source frames when supplied.

Start with hierarchy, overall proportions, density and image/text balance, then
component relationships and character. Measure the disputed or high-impact
properties, not every pixel. Explicit exact constraints need evidence adequate
to those properties; any tolerance must reflect resolution/scale uncertainty,
not be widened after seeing a failure. Otherwise choose coherent product values
without recording each spacing adjustment as a deviation.

## Unseen Behavior And Widths

A still image cannot establish hover/focus, transitions, backend operations,
permissions or scroll mechanics. Preserve known product contracts; do not infer
destructive actions or new features from a decorative icon. Label necessary
new behavior as an implementation decision, not recovered source behavior.

Multiple supplied widths show arrangements, not exact breakpoint locations.
Choose robust content-driven breakpoints and test relevant interpolation, long
text and zoom. With desktop-only input, a requested mobile design is an adaptation,
not verified mobile-reference parity. Unknown states do not justify disabling
supported behavior. Use the relevant responsive/native specialist when needed.

## Compare Like With Like

Use [snapshot](../../snapshot/SKILL.md) automatically, following its current
Before/After and reference requirements. Compare the selected reference with
the actual changed build, not a stale capture or a different environment. Note
route, viewport, content, language, auth/data state, query/selection, scroll,
overlays and loaded fonts/media when they affect the comparison. Distinguish
draft/Preview/published states. Reuse evidence only while its relevant inputs
remain valid; recapture after the final relevant edit.

Use separate, aspect-preserving desktop and mobile crops. Label any inferred
scale and exclude only non-product framing. Inspect normal viewing size and
readable details; a miniature full-page overview cannot prove text quality.
Full-page or flow claims require all requested sections/steps, including supplied
below-fold regions. A local repair needs its surrounding composition and affected
viewports, not a tour of the entire host application.

Record a short expected-versus-observed note for a small repair. For broader work,
use a compact scope list or table only when useful:

`surface/state | source/version | observed vs inferred | owner | check | result`

Optional overlays/diffs can locate discrepancies after valid alignment, but
cannot prove behavior, complete coverage or an invented similarity percentage.
Personally inspect the images, repair concrete in-scope defects, and re-render.
Unknown evidence is not a pass and cannot conceal a visible mismatch. Explain
material adaptations and unresolved constraints, without demanding user approval
for routine implementation choices already within scope.

Product contracts, accessibility and release authorization remain with their
existing owners; this reference does not replace their checks or authorize push.
