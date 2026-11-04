---
name: korat-tan-phai-shared-components
description: Preserve and reuse Korat Tan Phai web UI across Visitor and Admin. Use for shared controls, cards, loading, dialogs, search, maps, forecast analysis and CMS presentation; route native reuse to the app's own primitives.
metadata:
  short-description: Reuse Korat Tan Phai shared UI components
---

# Korat Tan Phai Shared Components

Reuse current owners while preserving product, data and session boundaries.

## Workflow

1. Stay in the current authorized worktree; default project root is
   `/Users/point/korattanphai`. Check Git status and preserve unrelated edits.
2. Read `docs/SHARED_COMPONENTS.md` and relevant `APP_MAP.md` contracts from
   that checkout. For temporal/routing behavior read
   `FORECAST_ONLY_RESTORATION.md`; Actual separation is parked context only.
3. Find current consumers with `rg`, then inspect the owner and its CSS.
   Palette roles live in `src/theme-tokens.css` / `src/brand-theme.css`;
   geometry remains in existing component styles. Admin and startup have
   scoped stylesheets; do not solve every issue with a global override.
4. Reuse presentation through props/composition; readers/forms retain their
   data, mutation and auth ownership. Update SHARED_COMPONENTS when a public
   contract or meaningful consumer behavior changes.

## Shared Owners

- `AppSelect` is the dropdown owner, with searchable long lists, centered
  trigger values and a bounded mobile menu. Use `align="start"` only for an
  intentional scanning role. `MonthSelect` owns calendar search/aliases;
  `ForecastMonthSelect` adds request/loading ownership. Do not fork parsers.
- `MetricCard` / `MetricGrid` / `PageSummary` own stats and hierarchy.
  Center standalone icons, short headings, values and periods. Preserve
  leading alignment for prose, inputs and scanning lists; do not globally
  center table content. Keep icon-only controls centered on both axes and
  neighboring actions on consistent heights.
- `WorkspaceDialog` owns dialog/focus/scroll mechanics; `WorkspaceEmptyState`,
  `IrrigationEmptyState` and `ArchiveUnavailableState` supply scoped recovery.
  Use contextual icon/message/action, not bare text. Analysis height follows
  content up to its bound, with internal results scrolling.
- `SidebarBrand` and the shared account presentation preserve authentic
  artwork and the account at the sidebar bottom. Visitor search/bookmarks use
  the top-right toolbar. Admin navigation stays under `/admin`, with no
  Visitor search/export/bookmark controls. Shared appearance does not merge
  their independent sessions or cache lifetimes.
- `WorkspaceSearch` lazily opens its shared dialog; `WorkspaceBookmarks`
  preserves geographic following and exact source-T/horizon filter restoration.
- `DataProvenanceChip` / `DataProvenanceLegend` own provenance semantics.
  Forecasts use `FORECAST_ARCHIVE`, never the actual-observation label.
- `NakhonRatchasimaLocalMap` owns the active local map; `RiskMap` national
  demo was removed. `MapPreviewFooter` owns preview actions/centered fallback.
  Preserve camera, clipping, keyboard/touch selection and gesture arbitration:
  horizontal one-finger pan, vertical-first page scroll, pinch and long press.
  Clearing transient selection must not immediately reopen hover previews.
- `ForecastControls`, `OperationalFilters` and the drought workspace wrappers
  retain their forecast-specific source-month/rice semantics. One source-month
  state and one T+ horizon drive map, graph and summary. Tambon pages omit the
  aggregate bar chart; do not stretch their detail cards to fit province charts.
- `ForecastAnalysisDialog` defaults to child geography: province → districts,
  district → tambons, tambon → itself until finer data exists. Preserve search,
  sort, risk-pattern and same-target comparison semantics.
- Admin composes existing controls through `AdminWorkspace`, `AreaWorkspace`,
  `ImportSheetReview`, `ImportPayloadReview`, `ImportReviewDownloads`,
  `ForecastLifecycle` and `ImportWorkList`. Form/domain owners supply issues,
  readiness and publication state; UI reuse must not invent a second API schema.
  `useImportAutosave` owns private server checkpoints, not Visitor caches.

## Illustrated Loading Contract

Read `docs/LOADING_SCREEN.md` before changing any startup consumer.

- `AppStartup` is presentational; auth/module/page owners supply its phase.
  `index.html` mirrors its pre-JS anatomy and shares `app-startup.css`.
- 0/33/67/100% counts actual auth/module/page-read milestones (N/3), not bytes,
  requests or elapsed time. Pending work stays at its milestone. Completion
  exposes ready results or the existing error/retry; it is not API success.
- `startupMotion.ts` aligns the CSS orbit on the document timeline across
  mounts. Preserve continuous blue/amber rotation, one-shot fill interpolation,
  cancellation of superseded interpolation and reduced-motion behavior.
- `PageLoadBoundary` keeps readers mounted/measurable and pending content
  hidden/inert. It releases content, focus and scroll immediately on settlement;
  only an inert, aria-hidden, pointer-transparent 220ms completion fade remains.
  New pending work cancels exit. No forced minimum loading wait.
- Warm refresh, criteria changes and mutations stay local. Decorative imagery
  never gates readiness. Keep the existing slow reload recovery and failure paths.
- Keep live text/logo/icons/bar separate from scenery; do not flatten the
  screenshot into a full-screen UI bitmap or desaturate the gold rice.

## Domain And Platform Guardrails

Production reads published Supabase/CMS revisions with no bundled fallback.
Risk 0/1/2, workbook blank/out-of-scope, missing rows and errors remain distinct.
Readiness is not hazard severity, issuance evidence or observed damage.

The active web product is forecast-only. Bare `target=T&horizon=h` and explicit
archive URLs are equivalent; do not reinterpret them as Actual or require an
archive marker. `OperationalDroughtWorkspace` remains parked. Use current
published metadata instead of hardcoding baseline origin/count values.

Native code in `apps/mobile` uses `src/ui.tsx` and `src/theme.ts`, with shared
domain modules where portable. Web DOM components and web-only theme overrides
are not native components or proof of native parity; read NATIVE_PARITY.

## Proportionate Verification

- Internal docs/skill edits: whitespace, links, owner-path and consistency checks;
  skill-only text maintenance needs no screenshot or runtime build.
- Tiny visible change: focused diff plus one current contextual render.
- Shared behavior: targeted owner tests and representative affected consumers,
  including Visitor/Admin or mobile when the contract crosses those boundaries.
- Loading changes: auth/module/page transitions, failure/retry, reduced motion,
  real progress and no motion reset. Static screenshots cannot prove continuity.
- Release: follow the current release runbook and `$release-gate`; do not
  substitute local mocks for authenticated candidate/production checks.

Use `$ui-ux-expert` and `$snapshot` for visible implementation. Inspect captures,
exercise changed interactions, and state evidence limits. Do not automatically
run a whole-site matrix or build for a small CSS/Markdown follow-up.
