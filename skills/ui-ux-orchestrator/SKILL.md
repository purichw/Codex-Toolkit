---
name: ui-ux-orchestrator
description: Central router for UI/UX work when the user is unsure which design, UX, visual QA, or interaction skill to call. Use when the user broadly asks to improve, polish, audit, redesign, QA, or make an interface feel right, including Claude/Figma/reference handoffs, implementation planning, visual consistency, product UX preservation, state coverage, flows, accessibility, data-heavy UI, forms, mobile/responsive QA, snapshots, or deciding which UI/UX skills should run together.
---

# UI UX Orchestrator

Use this skill when the request is broad, blurry, or says things like "UI/UX",
"make it better", "design skill?", "not sure which skill", "Claude design",
"check the flow", or "visual QA". Route to the smallest set of UI/UX skills that
covers the risk.

## Routing

- `$design-direction`: north star, visual direction, critique, brand/product
  feel, public vs admin direction, Claude prompts.
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

## Pick The Smallest Useful Set

Use this decision guide:

- Need visual taste or direction? Start with `$design-direction`.
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
