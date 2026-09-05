---
name: product-ux-contracts
description: Preserve, audit, or intentionally change real product UX contracts while redesigning, restyling, implementing Claude/Figma/reference UI, or refactoring frontend surfaces. Use when the user says not to break existing behavior, a redesign lost functionality, or a UI change may affect routing, deep links, persistence, internal scroll, progressive disclosure, keyboard/focus behavior, permissions, destructive safety, loading/empty/error states, media fallbacks, search result click-through, or proven journeys.
---

# Product UX Contracts

Use this skill when a product already has useful UX behavior that must not be
lost during visual work. Visual references can restyle a contract; they should
not erase it silently.

Treat external design references as presentation source material, not product
architecture. Preserve the target app's engineering contracts for data, auth,
routing, persistence, performance, accessibility, security, testing hooks, and
production operations. When a reference interaction conflicts with product-owned
architecture, adapt the implementation to preserve the visible intent while
keeping the product contract intact.

Use `$reference-to-a-tee` for HTML, image-only, or mixed reference parity, `$ui-state-matrix`
for state coverage, `$interaction-flow-qa` for journeys, `$accessible-interaction`
for keyboard/focus, `$data-dense-ux` for tables/lists, `$form-flow-ux` for forms,
`$snapshot` as mandatory visual contract proof before final response, and
`$release-gate` before shipping.

## Contract Types

Inventory these before replacing structure or behavior:

- **Routing:** route params, hash/query, deep links, browser history, redirects,
  fallback routes, selected item in URL.
- **Persistence:** selected tabs, filters, search, draft, progress, expanded
  rows, reload, back/forward, session return.
- **Progressive disclosure:** accordions, details panels, drawers, modals,
  sidebars, step flows, show more/less.
- **Containers and scroll:** sub-containers, internal scroll, sticky subpanels,
  virtualized lists, active-item auto-scroll, scroll restoration.
- **Keyboard/focus:** tab order, focus trap, escape/outside close, focus restore,
  scroll-to-input, shortcuts, screen-reader semantics.
- **State coverage:** loading, skeleton, empty, error, denied, disabled with
  reason, validation, partial failure, stale session, retry.
- **Permissions and safety:** role visibility, allow/deny paths, readonly state,
  confirmations, undo/restore, tombstones, audit logs, rollback.
- **Data density:** pagination, load more, sorting, filtering, bulk actions,
  item counts, page-size controls, large-list performance.
- **Responsive interaction:** mobile drawer, bottom sheet, sticky footer, safe
  areas, keyboard viewport, touch targets, tablet layout.
- **Media and assets:** lazy loading, fallbacks, failed asset state, CMS
  visibility, audio/video controls, captions, poster frames.
- **Search click-through:** result metadata, real destination, target highlight,
  selected item visibility, non-generic fallback behavior.

## Decision Ledger

Before editing, classify affected contracts:

```text
Contract:
Current product behavior:
Evidence it matters:
Reference/new design behavior:
Decision: preserve / hybridize / adopt reference / remove with approval
Implementation rule:
Verification:
Risk:
```

Preserve or hybridize when current behavior is more complete, safer, tested,
documented, or user-visible in production. Adopt the reference only when the
current contract is unproven, obsolete, or intentionally superseded.

## Workflow

1. Identify the screens, routes, components, and journeys affected.
2. Search source and tests for current selectors, state keys, routes, storage,
   handlers, and e2e coverage.
3. Fill the decision ledger before changing structure.
4. Implement visual changes around preserved contracts where possible.
5. Add or update focused checks when a preserved contract could disappear
   silently.
6. Capture `$snapshot` evidence for visible contracts before final response; run
   `$release-gate` before commit, deploy, PR, or handoff.

## Verification

- Routing: direct link, reload, back/forward, invalid/fallback route.
- Persistence: change state, reload, return, clear/reset when expected.
- Scroll/container: first and last item reachable, manual scroll preserved,
  sticky elements do not cover content, no page-level overflow.
- Focus: keyboard path, escape close, focus restore, modal/drawer trap.
- Permissions: allowed, denied, readonly, disabled reason, server-side boundary.
- Safety: confirm/cancel/success/failure/undo/audit/rollback when relevant.

## Closeout

Report contracts preserved, hybridized, adopted, or intentionally removed;
evidence used; tests or snapshots run; residual UX risk; and any decisions that
need user acceptance.
