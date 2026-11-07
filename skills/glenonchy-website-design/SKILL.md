---
name: glenonchy-website-design
description: "Implement or repair Glenonchy's public storybook website using its approved references, shared components, paper safe areas and desktop-relative responsive proportions. Use for Glenonchy website layouts, artwork, typography, sizing, stamps/seals, navigation or visual QA; not the Flutter game app or GM Console."
---

# Glenonchy Website Design

Work in the current chat. This skill does not authorize cross-chat activity,
deployment or changes to the mobile app/admin system.

## Start with the current contract

Default repository: `/Users/point/Projects/Glenonchy`.
For a fresh website context, start with
[`glenonchy-website-new-chat`](../glenonchy-website-new-chat/SKILL.md) and
`docs/website/NEW_CHAT.md`; the [website index](/Users/point/Projects/Glenonchy/docs/website/README.md)
routes page-specific references and dated release evidence.
Read its `AGENTS.md` and
[`docs/website/DESIGN_CONTRACT.md`](/Users/point/Projects/Glenonchy/docs/website/DESIGN_CONTRACT.md),
then only the owner files and references needed for the requested change.
If the repository moved, ask for its location rather than selecting another copy.
Run `git status --short --branch` before edits; preserve unrelated changes.
Load `/Users/point/.codex/skills/ui-ux-expert/SKILL.md` for UI work. Reuse the
existing brand and tokens; do not install a generic design system.

The repo design contract is the canonical decision record. Explicit user product
decisions stay in force until changed; a new mockup does not silently reverse
them. Update that record when the owner makes a new decision instead of copying
conflicting rules into multiple documents.

## Size from the desktop composition

- Treat the approved desktop hierarchy and relative sizes as the reference.
  When there is usable space, grow artwork, cards, type, spacing and decoration
  coherently. Do not leave tiny tablet elements on a large empty sheet.
- Measure both printable width and height after excluding the spine, torn edges,
  foliage, bottom landscape and controls. Never treat the full texture as safe
  content area.
- Use the shared `book-proportions.css` role sizes and existing composition
  owners. Keep each breakpoint's approved structure and use bounded fluid sizing
  within it. Do not blanket-scale the whole book or add scattered fixed-size
  overrides to individual pages.
- Preserve the typefaces, visual hierarchy, full artwork silhouette and usable
  touch targets. Enlarge stamps/seals when space permits; avoid inherited tiny
  caps and clipping the rope.
- Long content uses the shared numbered local pager inside the paper, with whole
  cards or fitting categories kept together. No subscroll or external footer.

## Preserve the product

Reuse the book shell, motion, print cache and UI primitives. Keep all four venues
and required Home news/postal details; preserve the complete desktop Home,
Our Place and Menu compositions. Keep navigation on upper-right brown leather,
sound at the upper left at every viewport size, no header wordmark, and the
largest safe book footprint.
Do not restore binder/lantern/chain; ribbon belongs only to the outer cover.
Event details remain a full book page. Read the canonical contract for the rest.

Preserve orbiting-paper loading and actual-readiness auto-open. An explicit
manual close stays closed until the next open action. Opening, closing and chapter
turning keep distinct physical motion; texture-off and paused-frame inspection
are required when changing volume/hinges. Performance work must retain artwork,
content and composition, without broken fallback layouts or flattened motion.
Opening the book or sound panel is not an audio-listening gesture by itself.

For mockup/artwork changes, apply `mockup-to-product`; for breakpoint changes,
apply `responsive-design`; for component boundary changes, apply
`shared-component-architecture`. Use approved assets or image generation when
needed, not placeholder/fallback layouts. Preserve meaningful image edges.

## Verify proportionately

Apply `/Users/point/.codex/skills/snapshot/SKILL.md`. Inspect a current rendered
screenshot with eyes before handoff. Compare composition, margins, type, artwork,
required content and empty space, then exercise the affected interaction.
For shared sizing, check representative desktop/tablet/mobile and affected
component/pagination boundaries. For a tiny tweak, one targeted visual check and
`git diff --check` are sufficient unless evidence requires escalation.
Keep screenshot URL, viewport, state and source provenance. Do not equate browser
viewports with physical device tests, or build success with visual correctness.
Check final diff/status and report the actual checks and remaining limitations.

Example invocation: `$glenonchy-website-design ปรับสัดส่วนหน้า Gallery ให้สัมพันธ์กับ desktop และตรวจภาพจริง`
