---
name: ui-ux-orchestrator
description: Central router for UI/UX work when the user is unsure which design, UX, visual QA, or interaction skill to call. Use when the user broadly asks to improve, polish, audit, redesign, QA, make an interface feel right, choose UI/UX skills, or route design-quality specialists, including Claude/Figma/reference handoffs, implementation planning, visual consistency, product UX preservation, state coverage, flows, accessibility, data-heavy UI, forms, mobile/responsive QA, and snapshots.
---

# UI UX Orchestrator

Use this skill when the request is broad, blurry, or says things like "UI/UX",
"make it better", "design skill?", "not sure which skill", "Claude design",
"check the flow", or "visual QA". Route to the smallest set of UI/UX skills that
covers the risk.

## Routing

- `$ui-ux-expert`: broad design lens for any visible user-facing UI work,
  including screens, layouts, components, decks, docs, and prototypes.
- `$design-direction`: north star, visual direction, critique, brand/product
  feel, public vs admin direction, Claude prompts.
- `$design-quality-review`: shared `[FACT]` / `[CRAFT]` / `[PD]` language,
  rule IDs, severity model, screenshot QA protocol, calibration drills, and
  definition-of-done templates.
- `$visual-diagnosis`: name why a UI looks cheap, cramped, scattered, generic,
  heavy, low-trust, unfinished, or otherwise visibly off.
- `$domain-taste`: category-specific density and conventions for admin, SaaS
  ops, dashboards, ledgers, editorial, learning, landing, and mobile screens.
- `$information-architecture-ux`: navigation, grouping, hierarchy, screen
  purpose, sequencing, and progressive disclosure.
- `$interaction-design`: autosave, undo, bulk actions, optimistic updates,
  permissions, interruption recovery, and destructive flows.
- `$mobile-native-feel`: safe areas, touch targets, keyboard behavior, sheets,
  gestures, and native-feeling mobile interaction.
- `$design-system-architect`: token layers, component taxonomy, variants,
  galleries, drift metrics, and design-system governance.
- `$art-direction-imagery`: image selection, crops, focal points, hero media,
  thumbnails, placeholders, captions, and asset states.
- `$typography-refinement`: type scale, prose measure, line-height, multilingual
  behavior, numeric data, dates, units, and truncation.
- `$motion-choreography`: motion timing, easing, choreography, feedback,
  overlays, scroll motion, and reduced-motion alternatives.
- `$accessibility-beyond-basics`: screen-reader flow, cognitive load, low
  vision, complex widgets, data visualization, zoom, and forced colors.
- `$reference-implementation-critique`: measured reference-vs-implementation
  critique across geometry, rhythm, hierarchy, density, weight, affordance, and
  states.
- `$taste-calibration`: paired works/fails specimens, weekly drills, and the
  smallest-change loop for improving design taste.
- `$consistency-audit`: site-wide or app-wide consistency across requirements,
  inferred patterns, layout, components, typography, copy, interaction, and
  shared-component implementation.
- `$claude-to-a-tee`: exact offline Claude HTML/reference implementation or
  parity audit, including product UX vs Claude balancing.
- `$product-ux-contracts`: preserve existing real UX while redesigning or
  restyling; routing, persistence, scroll, permissions, safety, media, search.
- `$ui-state-matrix`: default/hover/focus/selected/disabled/loading/empty/error
  and other non-happy UI states.
- `$interaction-flow-qa`: click through complete user/admin journeys and prove
  routing, state, data, permissions, and feedback.
- `$design-system-guardian`: tokens, primitives, component variants, consistency,
  design-system drift.
- `$accessible-interaction`: keyboard, focus, ARIA semantics, contrast, touch,
  reduced motion, modal/drawer accessibility.
- `$data-dense-ux`: tables, lists, dashboards, filters, pagination, bulk actions,
  operational density.
- `$form-flow-ux`: create/edit forms, validation, dirty state, save/cancel,
  autosave, server errors, mobile keyboard.
- `$mobile-web-qa`: responsive/mobile/tablet/Safari/touch/safe-area verification.
- `$snapshot`: mandatory post-implementation/post-audit visual proof,
  comparisons, provenance, and product UX contract evidence before final
  response.
- `$placeholder-image`: image sourcing, crop, visual media choices.
- `$release-gate`: commit, push, deploy, PR, handoff, production/preview smoke.
- `$usage-budget-gate`: choose fast, standard, deep, or release depth before
  broad UI/UX audits, Claude parity, responsive matrices, or release checks.

## Trigger Cues

Use these cues to select focused skills without loading every UI/UX skill:

| User cue or risk | Start with |
| --- | --- |
| "UI/UX", visible screen/component, layout, polish, redesign, or prototype | `$ui-ux-expert` |
| "looks off", cheap, cramped, scattered, generic, heavy, low-trust, unfinished | `$visual-diagnosis` |
| formal design QA, rule IDs, severity, `[FACT]` / `[CRAFT]` / `[PD]`, 25-item pass | `$design-quality-review` |
| category feels wrong, admin too roomy, ops too decorative, dashboard/ledger/editorial/learning conventions | `$domain-taste` |
| navigation confusing, hierarchy unclear, grouping wrong, screen purpose unclear | `$information-architecture-ux` |
| controls imply behavior, autosave, undo, retry, bulk actions, permissions, destructive safety | `$interaction-design` |
| mobile feels squeezed, safe areas, keyboard, sheets, gestures, touch ergonomics | `$mobile-native-feel` |
| tokens, variants, component taxonomy, gallery coverage, drift metrics, governance | `$design-system-architect` |
| images, hero media, thumbnails, generated assets, crops, focal points, placeholders | `$art-direction-imagery` |
| type scale, measure, numbers, headings, truncation, multilingual/RTL text | `$typography-refinement` |
| transitions, loaders, overlays, hover/press feedback, scroll motion, reduced motion | `$motion-choreography` |
| screen-reader flow, low vision, zoom, forced colors, complex widgets, charts | `$accessibility-beyond-basics` |
| Claude/Figma/reference vs app, before/after, side-by-side parity defects | `$reference-implementation-critique` |
| taste practice, works/fails specimens, calibration drill, smallest taste-improving change | `$taste-calibration` |

## Pick The Smallest Useful Set

Use this decision guide:

- Any visible user-facing UI work? Use `$ui-ux-expert` as the broad lens, then
  add only the focused skills needed for the risk.
- Need visual taste or direction? Start with `$design-direction`.
- Need rule-backed design QA, severity, or a repeatable review protocol? Start
  with `$design-quality-review`, then select a specialist.
- UI looks off but the defect is hard to name? Use `$visual-diagnosis`.
- Need the screen to feel right for its product category? Use `$domain-taste`.
- Navigation, grouping, hierarchy, or sequencing feels wrong? Use
  `$information-architecture-ux`.
- Interaction behavior is underspecified? Use `$interaction-design`.
- Mobile feels like squeezed desktop or misses platform behavior? Use
  `$mobile-native-feel`.
- Reference and implementation need measured comparison? Use
  `$reference-implementation-critique`.
- Need to know whether the site/app is coherent overall? Use
  `$consistency-audit`.
- Worried about usage or depth? Start with `$usage-budget-gate`.
- Have Claude HTML/reference? Use `$claude-to-a-tee`, then add contracts/states
  only where the product has real behavior at risk.
- Existing behavior might be overwritten? Use `$product-ux-contracts`.
- Looks done but states may be missing? Use `$ui-state-matrix`.
- Need to prove a journey? Use `$interaction-flow-qa`.
- Components feel inconsistent across the product? Use `$consistency-audit`,
  then `$design-system-guardian` for token/primitive fixes.
- Keyboard/focus/touch/accessibility risk? Use `$accessible-interaction`.
- Admin/table/list/dashboard density? Use `$data-dense-ux`.
- Create/edit/save/cancel form work? Use `$form-flow-ux`.
- Mobile or responsive risk? Use `$mobile-web-qa`.
- Any UI/UX implementation, redesign, restyle, visual audit, responsive pass, or
  reference comparison completed? Use `$snapshot` automatically before final
  response; do not wait for the user to ask.

## Orchestration Output

Before substantial UI/UX work, state:

```text
Goal:
Primary UI/UX risk:
Skills to use:
Why these skills:
Evidence needed:
Likely release gate:
```

Do not load every skill by default. Read and apply only the selected skill
`SKILL.md` files before acting on those parts.

## Closeout

Report which UI/UX skills were used or intentionally skipped, visual evidence,
flows/states checked, product UX contracts preserved or changed, residual risk,
and release/deploy readiness.
