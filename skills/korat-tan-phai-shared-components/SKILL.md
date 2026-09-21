---
name: korat-tan-phai-shared-components
description: Preserve and reuse Korat Tan Phai shared React UI components. Use when listing, auditing, refactoring, standardizing, or changing stats, dropdowns, provenance chips, map preview cards, dashboard sections, or local map components in the Korat Tan Phai repo.
metadata:
  short-description: Reuse Korat Tan Phai shared UI components
---

# Korat Tan Phai Shared Components

Use this skill to keep the Korat Tan Phai / โคราชทันภัย component system
consistent across province, district, and subdistrict surfaces.

## Workflow

1. Work in `/Users/point/korattanphai` unless the user explicitly points to a
   different checkout.
2. Check `git status --short --branch` before edits and preserve unrelated
   user changes.
3. Read `/Users/point/korattanphai/docs/SHARED_COMPONENTS.md` before adding or
   changing any shared-looking component.
   For actual/archive or temporal behavior, also read
   `/Users/point/korattanphai/docs/ACTUAL_FORECAST_SEPARATION.md`.
4. Inspect the owner file and nearby CSS before editing. Most visible component
   styling lives in `src/styles.css`.
5. Use `rg` to find all current usages before changing a shared component
   contract.
6. If the change creates, removes, renames, or materially changes a shared
   component contract, update `docs/SHARED_COMPONENTS.md` in the same pass.

## Component Rules

- Use `MetricCard` and `MetricGrid` for stat-only cards. In
  `NakhonRatchasimaWorkspace.tsx`, prefer `OfficialMetricCard` where that local
  wrapper is already the pattern. Stat-only card content is centered.
- Use `AppSelect` for visible product dropdowns and filter selects. Its trigger
  text is centered by default; use `align="start"` only for an intentional
  scan-left layout.
- Use `OperationalFilters` for page-wide filter summaries and mobile filter
  bottom sheets when its source-month/rice semantics fit. The operational
  actual view composes shared `MonthSelect`/`AppSelect` instead; do not import
  forecast-specific crop or T+ assumptions merely to reuse a whole container.
  Local map filter rails still use `AppSelect`.
- Keep option scrolling inside the dropdown's own scroll container. Map filter
  fields share the container-query grid; avoid tambon-specific positional rules
  that assume removed controls still exist. Mobile menu bounds must fit the
  configured viewport, not merely an overflow-expanded `innerWidth`.
- Use `MonthSelect` for searchable calendar-month controls and `ForecastMonthSelect`
  where archive request/loading ownership is needed. Keep one primary month owner
  and one archive horizon strip; actual views have no T+ control.
- Use `MapPreviewFooter` for map preview actions and fallback notes. Fallback
  notes remain centered, and preview cards must stack above lower sections when
  they overlap. Clearing a transient map selection should not immediately reopen
  a new hover preview while the map animates back.
- Use `DataProvenanceChip` and `DataProvenanceLegend` for provenance states.
  Do not create parallel provenance dots, colors, or labels.
- Use `RiskMap` for inherited national map behavior and
  `NakhonRatchasimaLocalMap` for province/district/subdistrict local map
  behavior.
- Reuse `OperationalDroughtWorkspace` across operational geographic levels and
  existing archive compositions for explicit archive intent. The shared map's
  `operationalUnavailable` variant is neutral-state presentation only, not an
  actual classification renderer. Preserve camera, preview, fullscreen and
  keyboard/touch behavior, not just visual similarity. Do not add aggregate
  forecast charts to tambon pages.
- Keep `WorkspaceBookmarks` shared. Geographic following works independently of
  forecast criteria; saving/restoring an archive filter must retain the exact
  origin/horizon. Actual valid months must not become forecast saved filters.

## Domain Guardrails

- Keep data values, joins, readiness categories, hazard severity, and source
  semantics unchanged unless the user explicitly asks for a data-model change.
- Agricultural figures are not official damage figures.
- Data readiness is not hazard severity.
- Missing evidence must not become green, normal, or low-risk UI.
- Forecast archive provenance uses `FORECAST_ARCHIVE`, not the actual-observation
  `REAL` label. Do not reuse forecast 0/1/2 colors for an unapproved actual metric.
- Clear obsolete values atomically on period/family changes. Do not restore a
  forecast cache or synthetic fixture when actual is missing or a request fails.
- Current source code and docs beat old attachments or chat memory when they
  disagree.

## Verification

For a small docs-only component inventory update, `git diff --check` is enough.
For archive UI checks, enter with explicit `mapLayer=forecast-archive`; a bare
legacy T/h URL now selects an operational valid month. Check operational states
separately so an unavailable screen cannot accidentally pass an archive UI test.
For shared UI behavior, run the relevant release-gate path for the changed
surface, usually at least:

```bash
git diff --check
npm run build
npm test
```

For visible UI implementation, refactoring, audit, responsive, or interaction
changes, load `$ui-ux-expert` and use `$snapshot` automatically before the final
response; do not wait for the user to ask. Capture the affected route/state and
breakpoint, adding representative usages when shared behavior changes. Exercise
changed interactions in the browser as well; a screenshot does not prove them.

Keep evidence proportional: a tiny visual edit needs the smallest useful current
capture, not a whole-site matrix. If rendering/capture is blocked, state why,
which supplied evidence was inspected, and what remains visually unverified.
Do not claim visual verification from a build or source-only inventory check.
