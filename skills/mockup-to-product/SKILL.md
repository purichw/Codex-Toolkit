---
name: mockup-to-product
description: Implement, refine, or compare real product UI from image files, screenshots, HTML/CSS, prototypes, or mixed references. Preserve composition, design character and product behavior while adapting layout, assets, content and responsive behavior. Use for screenshot-to-UI, mockup-led redesigns, repeated visual rework, or explicitly scoped exact matching. Not for inspiration-only design.
---

# Mockup To Product

Treat the approved mockup as the visual source of truth for a working product.
Reproduce it as closely as possible with real text, controls and behavior; do not
flatten the screen into a screenshot or reinterpret it as loose inspiration.
Own the implementation and review: the user should not need to point out each
missing icon, surface treatment, alignment, mobile adjustment or lower-page section.

**Adapt the implementation; preserve the design intent.** Flexibility is not
permission to omit observable details or call a different composition complete.

## Mockup Authority And Real Conflicts

Unless an established product decision actually conflicts, implement the chosen
mockup as closely as possible: artwork, typography (size/weight/line height),
alignment, spacing, proportions and detail all count. This is especially true of
new screens; do not invent a conflict or reinterpret them as loose inspiration.
Existing shared components are implementation constraints to evaluate, not an
automatic reason to keep a visibly different appearance. Extend/reuse their
appropriate variant while preserving their product behavior.

Honor the user's exact scope, including requests such as "change only the image,
keep the layout". If a new popup replaces an existing popup, or a screen in a
complete flow differs from its standalone mockup, use the user's explicit choice
of old/new and specified regions. When that choice is unresolved and materially
changes the result, show the concrete conflicting screen/region and ask which
version or combination to use; continue independent work. Do not silently merge
incompatible versions, redesign unaffected regions, or ask again about a choice
the user has already resolved. A genuine behavior constraint must be named and
traced to its product decision, not inferred from implementation convenience.

## No Shortcuts On Reference Fidelity

Do not reduce the requested visual quality to save implementation effort, time,
or tokens. Proportional scope limits unrelated work; it does not excuse missing
details within the requested surface. Functional completion and visual fidelity
are separate acceptance criteria: passing tests cannot close a visible design gap.

When illustrated materials define the reference, preserve their actual character:
the silhouette and ornament of a title banner, layered/beveled frame edges, paper
texture and curls, faint scene motifs, optical type weight, and control relief.
A generic rounded rectangle, flat border, geometric tree, default icon or gradient
is not an adequate substitute solely because it fills the same space. Use clean
source artwork or reconstruct separate decorative assets with image generation
when needed; keep text, hit targets and stateful controls native and accessible.
Do not flatten the complete screen into an image to imitate fidelity.

Match material tone as well as shape: paper warmth, mottling, aged versus polished
metal, rim thickness, bevels and small controls such as a plus medallion all belong
to the reference's theme. A themed frame does not excuse a generic icon/button.
Measure text clearance to the visible inner artwork edge (including folds/curls),
not just to a transparent asset's bounds or the widget's declared padding.

Preserve the natural aspect ratio of recognizable artwork and circular ornaments;
do not squash a lamp, medallion or frame to fill a convenient rectangle. Separate
decorative layers from growing text surfaces. Stretch only a suitable plain
surface region while preserving its edges and motifs. If the existing art cannot
support the composition, redraw, regenerate or recompose it instead of squeezing
it, hiding the clipped part, or accepting a substitute that misses the reference.

Define native text-safe bounds separately from the asset rectangle, leaving
clearance from visible leaves, books, curls and other decoration. Text must fit
those bounds at the relevant language and text scale without unintended overflow
or clipping. Reflow the content and adapt or redraw its surface as needed; do not
mask the defect with clipping or smaller illegible type. Text/art overlap or
off-frame treatment is intentional only when the selected mockup explicitly
shows it; identify that source detail rather than inventing an exception.

Before handing off, personally compare the rendered whole composition and the
defining details against the reference at matched scale. If material differences
remain, continue the in-scope repair; do not relabel them as adaptation, report
the work as finished, or make the user discover them. A fidelity complaint means
revisit the reference and the failed material/composition choice, not merely add
another small spacing or color adjustment. If an actual constraint prevents a
match, state that concrete constraint and what remains unfinished.

## Choose This Approach

- Use this skill when the user allows judgment in dimensions, structure,
  responsive composition, real assets or content while asking for the mockup's
  overall design. Routine visual choices within that scope do not need approval.
- Exact/to-a-tee/pixel-perfect requests stay in this workflow. Treat the user's
  specified surfaces/properties as constraints, use reliable source values or
  calibrated image evidence there, and disclose what cannot be established.
  Do not silently relax an explicit constraint, but do not extend it to every
  inferred breakpoint, spacing choice or unrelated screen. A supplied image or
  this skill's name alone does not impose pixel-exact implementation.
- Inspiration-only requests belong to general design direction. If intent is
  materially ambiguous, ask once; do not repeatedly ask about already-approved
  visual freedom. A reference alone does not authorize new features or a
  site-wide redesign.

Load `ui-ux-expert` when available for baseline craft. This skill owns reference
interpretation and product translation, not a second exact-reproduction mode.
Use product/design judgment by default; do not turn normal implementation
choices into exceptions requiring permission. Preserve explicit constraints.

Automatically load [snapshot](../snapshot/SKILL.md) at the start of visual work,
before changing an existing rendered surface, and use it again after the final
visual edit. Reference-led work requires `Reference + Development`; revisions
require `Before + After` too, normally one `Reference | Before | After/Dev`
comparison. Do not wait for the user to request evidence or point out omissions.
A narrow repair uses a narrow contextual comparison, not a whole-site audit.

## Establish A Small Design Brief

Inspect the actual selected reference and current rendered product. Accept
images, HTML or mixed references; missing HTML is not a blocker. Resolve authority
per surface when artifacts disagree. The user's latest chosen direction wins,
not a filename or modification time.

Use [reference evidence](references/reference-evidence.md) when reading images,
resolving mixed-source authority, calibrating measurements or comparing renders.
Separate observed, image-measured, source-measured, inferred and unknown claims.
For runnable HTML, use [HTML reference workflow](references/html-reference-workflow.md)
only as needed; its optional extractor inventories HTML, not images or UI quality.
Read these references for their triggered question, not as a mandatory checklist.

For a page, note the following once; for a small repair, a few lines suffice:

| Preserve | Translate | Adapt | Do not infer |
| --- | --- | --- | --- |
| Real journeys, data/CMS ownership, semantics, permissions, focus, scroll and responsive constraints | Hierarchy, grouping, density, proportions, image roles, icon character, material and decorative language | Dimensions, grid, breakpoints, crop, wrapping, component structure and mobile arrangement within authorized scope | New destinations, metrics, fields, backend behavior or interactions from decorative mock elements |

Name what makes this design recognizable and what the user has allowed to change.
Record only material tradeoffs. Do not require a ledger entry or approval for
every spacing adjustment. Ask before changing product meaning, removing a
capability, exceeding scope, or contradicting an explicit design decision.

When a project has accumulated an approved visual language, locate its maintained
design contract before adding local exceptions. Keep project-specific materials,
fonts, navigation and component owners there; reusable skills should carry the
method rather than that project's theme. A newer regional correction can supersede
part of a mock without replacing its other approved regions.

Identify the product state shown, not just the route: empty versus populated,
draft versus committed, active query, selected items and open disclosures can
change the composition. Use a comparable real state for review; do not remove
required results or choices to match an illustrative screenshot's height.

For layered or animated products, identify the owner of each layer: scene
artwork, character/animation package, native controls, and actual product rules.
Keep a short source-to-use mapping when several packs overlap. A static pose or
decorative control does not override a supplied animation manifest or real flow.
Apply each character/media correction to all affected variants, including both
female and male when present, not only the one shown in the complaint. Check
their portraits, scale, sharpness and touched animation states together.

## Read The Whole Requested Surface

Review at three scales before implementing, not only the first visible section:

1. **Composition:** dominant task, hierarchy, shell, section rhythm, image/text
   balance, whitespace, density, and where the page changes material or mood.
2. **Components:** footprint, image frame, title/meta/action grouping, alignment,
   orientation, proportions, text measure and neighboring relationships.
3. **Character:** icon family and optical weight, filled/outline treatment,
   translucency, borders, shadows, separators, patterns and edge decoration.

Keep a compact coverage list for a full page, including header and footer if in
scope. Record detail work still pending while building the larger structure.
Do not treat motifs or transparency as optional just because they are decorative.
For a whole-surface request, annotated or repeatedly reported defects are the
minimum to fix, not an exhaustive list. Inspect unmarked peers and the enclosing
composition too. A summary's lightbulb, check markers, artwork, and spacing; a
quote's mark and attribution; and the complete share-icon set are part of those
components when shown in the reference, not optional finishing touches.
Inspect the mobile reference independently; it may express a different grouping
or priority rather than smaller desktop dimensions.

When compactness is explicit, establish a page/section height budget from the
actual reference content area, excluding device framing. Compare measured CSS
height and viewport count in equivalent language/data/disclosure states. This
is a project-specific target, not a universal number. Reordering old oversized
sections does not reproduce a compact reference. Match the complete visual
language, not only its sequence; see the compact-page lessons in
[rework-patterns.md](references/rework-patterns.md).

Map the reference's typography by role at equivalent content scale, excluding
device framing: title, H1-H4, body, metadata, and controls as relevant. Match the
actual loaded family, weights, line heights, measure, wrapping, and paragraph
spacing. Do not inherit oversized generic editor headings or enlarge every role
because the reference image is small. Keep approved defaults separate from
explicit author overrides; the default should already reproduce the design.

## Implement With Judgment

Work from composition to component geometry to visual finish. Check desktop,
tablet, and mobile early in responsive web work so the structure can support
each layout.

- Rebuild an obstructive layout when authorized. Preserve product behavior, not
  unwanted legacy geometry. Do not broaden a visual rebuild into a data rewrite.
- Use the existing shared owner for repeated semantics/behavior. Add a variant
  when contexts differ; sharing does not mean universal dimensions. If asked to
  apply across the site, map and migrate the relevant consumers, not just Home.
  Establish shared outer widths, gutters and type roles before forcing different
  task layouts into one component. A copied override or an unused shared file
  is not consolidation. For cross-page work, read
  [shared-surfaces.md](references/shared-surfaces.md).
- Prefer the established icon library or assets. Adapt visual weight and optical
  size, not only the icon's name. Compare glyph shape, stroke/fill, baseline,
  badge/background, and container proportions; use proper brand marks where
  required. A present but mismatched icon still needs correction.
  Center compact controls and grouped tiles where
  the reference calls for it; do not center all prose by default.
  Distinguish content alignment, peer-control alignment and the entire group's
  placement within its parent. Match the reference's action shape and prominence;
  a plain text link or a left-anchored group can remain a visible mismatch even
  when its labels are centered. Keep the correct interaction semantics.
- Treat transparent/opaque surfaces and motifs as design materials. Keep readable
  contrast, layering and non-intercepting decoration; support a solid fallback
  where transparency effects are unavailable. Do not add decoration to a utilitarian
  design that does not call for it.
- Give media independent responsive frames. Portrait sources, missing images,
  loading and CMS replacements must not inflate peer cards or consume text space.
  Reserve space for titles, badges and actions; test long real content.
- Compose mobile deliberately: information order, grouped actions, compact
  controls, safe areas, text wrapping and accessible touch areas. A small visible
  icon need not have a tiny hit target. Do not make the entire UI illegible just
  to match total screenshot height or a fixed column count.
  Reduce competing control rows and excess containers before shrinking type.
  Disclose secondary tools only with a visible path back; active queries, errors
  and the primary result must not disappear as a side effect of compactness.
- Keep internal scrolling, selected-state persistence, search, links, menu focus,
  intentional motion and keyboard behavior. Diagnose repeated animation at its
  own lifecycle instead of disabling desired motion; preserve reduced-motion
  support. A static reference cannot establish the absence of these behaviors.

Use the relevant shared-component or interaction specialist only when those
contracts are actually changing. See [rework-patterns.md](references/rework-patterns.md)
for concrete failure patterns, data substitutions and mobile examples.

## Handle Assets And Missing Data

Choose replacements by visual role: subject, focal point, light, color balance,
negative space and crop on each required viewport. A semantically related photo
with the wrong composition is not sufficient. Inspect barriers, watermarks,
unwanted clutter and the actual rendered crop before using it.

Use real product media when the subject must be accurate. Keep editorial media
in existing CMS slots when the product has them, including alt/focal point/source
metadata; do not create hard-coded competing sources. Reusable decorative brand
art may be a design-system asset instead. Preserve licenses and required credit;
a demo is not an attribution exemption. Use imagery tooling/skills as appropriate.

### Artwork Coverage And Completion

Deliver the complete artwork set shown in the requested mockup surface, not a
representative sample. Include backgrounds, hero/section illustrations, photos,
frames, custom pictorial icons and small defining ornaments, plus the required
responsive/state variants. Asset count, effort, time or tokens do not authorize
dropping artwork, simplifying its character or narrowing the agreed scope.

1. **Map the slots.** For each distinct asset, record its reference region and
   visual role, source or required creation/repair, final file and consuming
   component/CMS slot, required variants, and pending/integrated/visually-reviewed
   status. Keep this in existing work notes; no new manifest format is required.
   A narrow repair covers its touched slots and affected consumers, not unrelated
   pages. Account for lower-page assets as well as the hero.
2. **Choose by fidelity.** Reuse suitable supplied or approved art first. Match
   subject/identity, pose or silhouette, perspective, lighting, palette, material,
   detail, negative space and intended crop. "Same topic" or "similar colors" is
   insufficient. Reject unrelated stock, arbitrary generated filler and generic
   CSS shapes, gradients or library icons used in place of distinctive artwork.
   Native CSS/icons remain appropriate when they genuinely match the reference.
   One reused image is not several distinct illustrations. Intentional repeated
   motifs may share an asset; do not invent differences the mockup does not have.
3. **Complete missing art.** Use the available image generation/editing tool for
   eligible missing, occluded, blurry or incompatible artwork, following the
   recovery rules below. Do this as implementation work, not a suggestion for the
   user to finish later. Batch a large set by visual family while retaining each
   slot's subject and composition; continue through the whole in-scope set.
   Inspect and revise a mismatched result instead of accepting the first output.
   Preserve clean originals, native text/controls and explicit source, identity,
   factual-media, licensing or no-generation constraints. Tool/source constraints
   must be named as blockers; they do not permit fabricated official assets or
   silent substitutions. New spending still needs its own authorization.
4. **Integrate and inspect.** Wire each final file into its real consumer, keep
   CMS/data ownership and metadata, and check the decoded image at actual viewing
   size and in the complete composition. Compare each distinct asset to its
   reference and inspect affected crops, clarity, transparency, text clearance
   and responsive/state variants. A contact sheet may help review a large set,
   but does not replace inspection inside the real UI. A generated file, asset
   count, HTTP success or green build alone cannot close a slot.

Temporary construction placeholders and genuine loading/error fallbacks may
exist, but they cannot stand in for required artwork in the settled delivered
view. Missing, arbitrary, mismatched, unwired or unreviewed art keeps that scope
unfinished. Repair it, or report the specific blocker and outstanding slots;
do not declare fidelity, hide the gaps in cropped evidence, or call them an
adaptation. Only an explicit user-approved scope change can defer required art;
a prototype label or an agent's time estimate is not that approval.

### Incomplete Artwork: Use Imagen / Imagegen

When the mockup lacks usable visual layers—such as a background hidden behind
cards, text or a character—always use image-generation/editing tooling to recover
the missing artwork if a suitable clean source is not already supplied. Load
the available `imagegen` skill and use Imagen when exposed, or the configured
built-in `image_gen` tool. Name the actual tool/provider used; do not invent an
Imagen capability or silently switch to a paid API. If the requested provider
is mandatory and unavailable, report that specific limitation.

Within authorized visual work, this is a required asset-completion step, not an
optional suggestion to the user. Do not routinely ask them to deliver a clean
background or replace illustrated artwork with a generic gradient. Preserve an
explicit no-generation, exact-source, identity or licensing constraint; apply
generation only to eligible layers and ask only if that conflict blocks the work.

Edit from the supplied reference: preserve camera/perspective, architecture,
lighting, palette, focal points and space for real UI. Reconstruct occluded
regions as a separate clean asset; remove baked text, buttons, status bars,
badges and foreground subjects that the app will render itself. Keep originals
unchanged and record which parts are reconstructed, plus source/output paths.
Never use the full mockup screenshot as a runtime background under duplicate UI.
Inspect the result on its own and in the real layout; reject changed identities,
perspective drift, seams, halos, residual text or accidental extra subjects.
Generated artwork is a derivative, never a replacement for the original visual
reference or a claimed recovered original.

### Blurry Artwork: Repair It Before Handoff

Do not leave visibly blurry media in place merely because the supplied export
is small. First check actual source resolution against rendered size and device
pixel ratio, decode/downsampling settings, parent constraints and aspect ratio.
Use the best supplied source or authored export recipe before enlarging a small
thumbnail/atlas. Fix stretching at the layout owner; sharpening cannot repair it.

If the source remains insufficient, use the image tool to enhance/upscale and
sharpen it enough to produce a visible improvement, or redraw/reconstruct the
asset at the required resolution when permitted. Preserve its subject, face,
costume, pose, silhouette, composition and material language. Compare at actual
display size and at a readable detail scale: reject crunchy edges, ringing,
invented facial details or a different character. A larger pixel count or a
filter setting alone is not proof of improvement. Do not silently fabricate an
official logo, factual product image or functional QR code.

For supplied animation packs, preserve frame IDs, timing, anchors, silhouettes
and transitions; use manifest/authoring coordinates, never guessed atlas crops.
Prefer higher-resolution source frames reconstructed with the package's own
recipe when available. Do not independently regenerate frames and introduce
flicker or identity drift. Keep actual animation; a sharp static mockup cutout
is not a replacement for a moving character. Verify every affected character
and state, record which states remain at original quality, and consider texture
memory on the target device. See the asset lessons in
[rework-patterns.md](references/rework-patterns.md).

For editable designs, prove authoring capability alongside public rendering.
Apply the visual-editing contract in
[product-redesign-contracts.md](../ui-ux-expert/references/product-redesign-contracts.md):
the live canvas shows the design, Preview checks the complete page, and real
controls support the requested insertion, ordering, placement, visibility, and
typography overrides. A template-only summary or sidebar quote is insufficient
when the user must edit or move it. Verify a UI-authored save/reopen round trip
and its rendered consumers; do not claim freedom that only seeded content has.

Separate **data differences** from **design differences**. Missing fields do not
prevent matching supported grouping, alignment and visual weight. Reflow or
rebalance truthful content; do not invent ratings, usage totals or auspicious
claims, add dead controls, or build a new backend just to fill the picture.
Prefer an existing supported equivalent when it serves the same role. A new
action is not interchangeable with a read-only fact merely because it fits the
same tile. Disclose meaningful substitutions; ask when the product decision is
material and unresolved. Do not show placeholder claims as production data.

## Review Before The User Has To

Render the changed surface and compare it with the selected reference. Separate
visual judgment from functional tests: no overflow and a green test suite do not
prove design quality. Check at actual viewing size as well as a uniform whole-page
overview when overall composition is in scope.

**Personally inspect the rendered images when assessing mockup fidelity.**
For responsive web work, open the actual desktop, tablet, and mobile renders
with an image-viewing tool and judge each viewport independently. Use the
supplied mockup widths or representative CSS widths for the product. For a
narrow change, inspect the changed region and its neighbors at the required
widths.

Compare each viewport with its own reference at matched scale. Remove only
device or slide framing when needed, preserve aspect ratio, and label inferred
CSS scale. For page-level work, inspect the top, middle, and bottom at readable
size as well as the full-page rhythm.

When the change affects screen height or viewport fit, inspect the initial
viewport before any auto-scroll and the settled scrolled state afterward. Judge
header, content and footer together, including safe-area and frame edges; fixing
one edge must not conceal another. `ensureVisible` or scrolling to the footer
proves reachability only, not that the initial composition fits. Refresh the
matching `snapshot` evidence after each accepted layout or artwork repair.

Review, identify the largest remaining visible gaps, fix the in-scope ones, then
open fresh renders of the affected views again. Track concrete observations such as
an oversized toolbar, displaced map, missing chevron, wrong image crop, or inflated
card body. The user should not be the first person to discover these. If the user
sets a target such as "85-90% like the mockup", treat it as a high-fidelity visual
expectation, not a calculated score or a reason to declare success with major
composition differences. Never invent a percentage from tests or your confidence.

Use five questions, not an invented numerical similarity score:

- Is the hierarchy and grouping recognizable as the selected design?
- Are density, proportions and section rhythm coherent across the requested page?
- Have the material, icon, image and decorative details been translated?
- Is each responsive layout deliberately composed, readable and operable?
- Are real content, behavior and shared consumers preserved as claimed?

### Automatic Fidelity Repair

When visual review finds a material in-scope mismatch at any viewport,
including a design that matches at only one size, **automatically open and apply
[mockup-fidelity-repair](../mockup-fidelity-repair/SKILL.md) in the same task.**
Use the same workflow for a user-reported mismatch or repeated correction.
If that workflow is already active, continue its repair loop and consult this
skill for reference interpretation as needed.

Compare the selected reference with the current render, including the enclosing
layout around any marked element. Record the expected and observed position,
scale, spacing, density, action treatment, or image role. Fix the cause at the
responsible layout or component, inspect affected peers, and repeat the review
on fresh renders until fixable in-scope differences are resolved. Revise the
diagnosis when a fix misses. See [rework-patterns.md](references/rework-patterns.md)
when helpful.

Before handoff, personally inspect fresh renders after the final visual edit
at desktop, tablet, and mobile for the affected responsive web surface. Recheck
any viewport that passed earlier, the sides of changed breakpoints, and affected
in-scope languages or states. Compare each size against its own mockup where
available. When a viewport lacks a reference, verify its reflow against the
approved hierarchy and record it as an adaptation. Report any view you could
not verify and the specific blocker.

### Capture Evidence And Verify Behavior

Use the automatically loaded `snapshot` workflow for contextual comparisons.
Capture the existing UI before editing, then the final development render; show
the original reference alongside them. For full-page work include whole-page
or top/middle/bottom coverage for the required viewports. For a tiny repair,
capture the changed area and its neighbors. Label actual viewport, state and any
inferred reference scale. Keep the original proportions and details.
New screens without an earlier implementation need `Reference + Development`;
revisions need `Reference + Before + After/Development`. If no reference exists,
use `Before + After`. Missing historical evidence must be labeled unavailable;
do not recreate it, roll back unrelated work to manufacture it, or omit an
available reference. If the skill/tool cannot be loaded or capture is blocked,
disclose the limitation and use available equivalent capture tooling.
For authoring work, include the live editor, not only Preview or the public page.
For alignment evidence, include the parent boundaries and surrounding space;
a tight crop of centered labels cannot prove the group itself is centered.

Test touched behavior and risk, not every control on the site by habit. Keep
existing dependencies and a usable dev server; do not reinstall, rebuild or run
whole-site suites on each cosmetic iteration without a reason. Reuse unaffected
evidence, but refresh the changed area and any overall composition it alters.

After a component/media migration, check the rendered asset itself, not only
its wrapper: images must load and remain visible; glyphs must have visible
geometry. Exercise the changed CMS refresh/fallback or interaction path where
relevant. Build success and DOM presence cannot detect every missing visual.

## Finish Clearly

Complete the requested scope when the review questions are satisfied, relevant
checks pass and remaining material differences are explained or resolved within
the user's authority. Do not invent source measurements or claim pixel parity,
whole-site coverage, user approval or proven time savings from a local review.
If visual capture is blocked, report what remains unverified.
Likewise, distinguish "captured" from "personally visually inspected" in evidence
notes. Keep an honest record of the views inspected and material differences;
do not imply user approval or defer a known, practical visual fix to user review.
For editor work, distinguish supported controls, persisted changes, rendered
output, and visual parity; none alone proves the others.

Keep the closeout brief: what was adopted/adapted, current visual proof, relevant
checks and remaining limitations. Do not carry a deep audit into the next tiny
follow-up. Commit, push, deploy and production writes require their own user
authorization; creating this skill does not grant them.
