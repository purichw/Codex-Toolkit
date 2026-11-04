# Korat Tan Phai Continuation Context

Resolve every repo-relative path below against the current authorized worktree.
The usual root is `/Users/point/korattanphai`; do not silently switch from an
isolated worktree. This is routing guidance, not a frozen release inventory.

## Read By Task

Start with Git status, `AGENTS.md`, `README.md`, `PROJECT_MAP.md` and the newest
checkpoint in `docs/HANDOFF.md`. PROJECT_MAP indexes all maintained docs and
separates live contracts, dated verification, research and parked designs.

| Task | Read / inspect |
| --- | --- |
| Routes and journeys | `docs/APP_MAP.md`, `INTERACTION_MAP.md`, `FORECAST_ONLY_RESTORATION.md`; `App.tsx`, `AuthenticatedApp.tsx`, `NakhonRatchasimaWorkspace.tsx` |
| Shared UI / theme | `docs/SHARED_COMPONENTS.md`, `DESIGN_SYSTEM.md`, `BRAND_SURFACE_THEME.md`; current consumer/owner and scoped CSS |
| Loading / motion | `docs/LOADING_SCREEN.md`; `index.html`, `AppStartup.tsx`, `PageLoadBoundary.tsx`, `startupMotion.ts`, `app-startup.css` |
| Forecast data / cache | `docs/DATA_CONTRACT.md`, `FORECAST_SCOPED_LOADING.md`, rev03 normalization/cutover; `useForecastArchive.ts`, `data/supabaseForecastArchive.ts`, `data/forecastScope.ts` |
| CMS / import / recovery | `docs/ADMIN_CMS.md`, `CMS_FORECAST_LIFECYCLE.md`, `API.md`; `src/admin`, `server/admin-data`, `shared/dataFields.mjs` |
| Reference data / maps | `shared/cmsResources.mjs`, `src/data/cmsReferences.ts`, `src/data/localMapGeometry.ts`, `NakhonRatchasimaLocalMap.tsx`, `mapInteraction.ts`, `mapLabels.ts` |
| Search / exports | `docs/SEARCH_BEHAVIOR.md`, `FORECAST_MAP_TOOLS.md`, `FORECAST_EXCEL_EXPORT.md` |
| Auth / access | `docs/AUTH_SETUP.md`, `WORKSPACE_ACCESS.md`; `authScope.ts`, `useAuth.ts`, `supabase.ts` |
| Native | `apps/mobile/README.md`, `NATIVE_PARITY.md`, its package/lockfile/`.nvmrc`/`app.json`; `src/theme.ts`, `src/ui.tsx` |
| Release / CI | `docs/RELEASE_RUNBOOK.md`, `ACTIONS_USAGE.md`, `PRODUCTION_SMOKE.md`; current workflow and exact source SHA |
| Authorized future Actual work | `docs/ACTUAL_FORECAST_SEPARATION.md`, `rollback-parking-lot.md`, data contract; never infer activation from retained modules |

## Routes And Sessions

- `/login`: Visitor email/password entry with internal return path/query/hash.
- `/`: province forecast overview; `/drought`: six-horizon province workspace.
- `/{district-slug}`: district; `/{district-slug}/t-{admin-code}`: tambon.
- `/nakhon-ratchasima/...`: compatible geographic aliases.
- `/admin/login`: independent Admin session using the existing user directory.
- `/admin`: data management; `?view=imports`: work/drafts;
  `?view=upload`: import dialog; `?draft=...`: saved draft.
- Visitor search, bookmarks, Excel and analysis open scoped dialogs, not new
  routes. Visitor search/bookmarks occupy the top-right toolbar; account is at
  the sidebar bottom. Admin navigation stays in CMS.

All active Visitor routes are forecast-only. `target=YYYY-MM` means origin T,
and `horizon=1..6` means T+h. Plain and `mapLayer=forecast-archive` links are
equivalent. Retired `period` is ignored/removed, never converted to an origin.
Absent selection uses published latest; invalid explicit origins/horizons show
recovery. Root T+2..6 uses the full workspace while retaining district scope.

Actual switch/banner and operational-context reads are not mounted by forecast
routes. `OperationalDroughtWorkspace`, eligibility and metadata contracts are
parked. The old `bcbcd33` reference was docs-only; the restoration doc explains
the actual runtime revert. Do not re-enable Actual to repair a forecast bug.

Admin and Visitor share presentation, not sessions or caches. Logout affects
only its scope. CMS access requires server-verified operator membership; future
officer jurisdiction restrictions remain distinct from current compatibility
mode. No credentials belong in skill text, docs, screenshots or fixtures.

## Data And CMS

- Canonical geography: `TH-P29`, admin province `30`, 32 districts, 289 tambons.
  Source research IDs, Thai names and slugs are not administrative join keys.
- Original source: `Drought_T1-6_rev03.xlsx`, `Master_Data_Drought_Final`.
  Verification artifact:
  `src/data/canonical/nakhon_ratchasima/drought_forecast_archive_rev03.json`.
  Original baseline: 127 origins (2015-06..2025-12), six horizons and 220,218 slots.
  These are baseline facts; published metadata controls current selectable data.
- Source month is T. December 2025 T+1..6 targets January–June 2026.
  Legacy `targetMonths`, `target_period` and URL `target` still identify T.
  Equal values at different horizons remain distinct forecast vintages.
- Risk 0 = no forecast risk, 1 = moderate, 2 = high, workbook blank = out of scope.
  Missing record, request failure and unfinished CMS draft cells are separate.
  None may become a green zero. Irrigation is workbook metadata:
  Collecting = unknown, RainFed = rainfed, Irrigation = irrigation access.
- Production uses `VITE_DATA_BACKEND=supabase` and
  `VITE_REFERENCE_BACKEND=cms`. Revision checks precede cache reuse; account
  changes dispose protected caches. A failed read never falls back to static
  forecasts or research fixtures.
- `shared/cmsResources.mjs` lists five active read-only references: hierarchy,
  archive summary, tambon geometry, dissolved province boundary and Thailand ADM1.
  Bootstrap requires hierarchy/summary; authenticated Visitor entry then preloads
  geometry alongside workspace/forecast loading, sharing map requests. Admin and
  signed-out entry do not preload Visitor geometry. Retired records
  remain in history, not active bootstrap. Never reseed an old 45-resource list.
- Current CMS supports upload/review/repair, shared API validation, reviewed
  Excel/CSV download, new origins, computed readiness, private server-saved raw
  work/original bytes and recovery of a prior round into a new reviewed draft.
  Validation and explicit atomic publication remain separate; stale bases block
  acceptance. Recovery preserves other origins and immutable history.
- Generic geometry replacement, canonical-area schema changes and arbitrary
  model-output publication remain gated. An API input receipt is not a published
  forecast. Keep UI and API fields aligned through their shared schema.
- Retired national demo state, source/rainfall stubs, research map periods and
  rev02 are not active data. Do not restore them from an old screenshot or diagram.
- Data readiness is not severity, accuracy or freshness policy. Upload/source T
  does not prove forecast issuance. Agricultural values are not damage records.
  Parked Actual work needs approved source, metric/classification, review,
  geographic coverage and publication rules before it can be activated.

## Shared Presentation

Use `$korat-tan-phai-shared-components` and the living component map. Key owners:
`AppSelect`, `MonthSelect`, `ForecastMonthSelect`, `MetricCard`/`MetricGrid`,
`WorkspaceDialog`, `WorkspaceEmptyState`, `SidebarBrand`,
`WorkspaceSearch`, `WorkspaceBookmarks`, `MapPreviewFooter`,
`DataProvenanceChip`/`DataProvenanceLegend` and `NakhonRatchasimaLocalMap`.

Analysis follows province → districts and district → tambons. Tambon shows
itself until finer data exists. Tambon pages do not mount aggregate bar charts.
Map touch preserves horizontal one-finger pan, vertical-first page scroll and
pinch. Keep clipping/preview stacking, label readability and centered controls.

The web palette uses Navy / Powder / Amber with visible gold rice and authentic
logo; it does not authorize layout changes. Google Sans remains shared identity.
Keep semantic risk colors separate from decorative accents.

Loading uses one illustrated presentation in pre-JS and React. Auth/module/page
owners drive real 0/33/67/100% readiness (N/3); no timer-based percentage.
`startupMotion.ts` aligns the eight-second orbit across mounts and interpolates
the fill only toward real milestones. Blocking reads keep children mounted but
hidden/inert; settlement immediately releases the ready page or existing error.
The 220ms completion fade is visual only. Reduced motion skips motion/fade.
Warm refresh remains local and artwork never delays readiness.

## Native Status And Limits

The native app is connected, not shell-only: existing Supabase Auth/Keychain,
scoped forecasts, geographic selection, map/chart, analysis, saved workspaces
and shared Excel writer/iOS share sheet are implemented. NATIVE_PARITY separates
source implementation, Simulator evidence and physical installation from gaps.

Important gaps include full global search, map-result overlays/report export,
some analysis/coordinate/export controls and physical-device interaction/
accessibility checks. Later web releases do not imply native parity or CMS
reference migration. TestFlight/App Store distribution is not recorded.

- Use the app's own Node pin/lockfile; no global toolchain changes.
- `ios/` is generated CNG output. Durable inputs are TS/JS, app.json, assets,
  package dependencies and plugins. Scene lifecycle support is required by the
  documented SDK/Xcode configuration.
- Native `src/ui.tsx` and `theme.ts` own UI. Share portable domain contracts;
  React DOM does not render natively. The November website skin/loading release
  did not recolor or rebuild native; base-token tests do not prove new web parity.
- Native fonts are local Google Sans assets, not runtime Google Fonts fetches.
- Localhost Metro is Simulator-only. A physical Release development-signed
  build embeds JS/assets, but still needs network for Supabase. Discover device
  IDs and verify profile validity; an old installed binary/profile may have expired.
- Excel uses the bare browser writer with native crypto and a static lazy
  require; avoid the Promise-polyfilled build or a broken outside-root split
  chunk. Read the current native README before changing these platform adapters.
- Commands from `apps/mobile`: `npm run typecheck`, `test:domain`,
  `test:brand`, `check:dependencies`, `export:ios`, as appropriate.
  A JS export is not an installed app or distribution release.

## Verification And Release

Choose the smallest checks that prove the touched risk. Internal docs/skills:
whitespace, links, owner paths and consistency. Visible fixes need current
contextual render; shared behavior needs affected consumers, failures and input
modes. Release scope uses the runbook rather than a copied direct deploy command.

Keep commit/push, exact-SHA CI, candidate readiness, promotion and post-promotion
smoke separate. Use both production backend flags explicitly and verify the hosted
`reference-backend.json` marker (`cms`, `fallback:false`). Preview skips do not
prove production smoke. A docs-mode gate inherits a proven baseline; it is not
a new runtime test. Inspect first causal errors/current progress before retries;
never force-push, weaken checks or create duplicate deploys to escape a wait.

No cross-chat inspection, messages or delegation without explicit authorization
identifying the chat. Preserve unrelated work and user data. Do not commit,
push, deploy, migrate or mutate production based on an earlier task's approval.

## Copy-Ready Continuation Prompt

```text
Work in the existing Korat Tan Phai / โคราชทันภัย project, keeping the current
authorized checkout/worktree (usual root /Users/point/korattanphai).
Use $korat-tan-phai-new-chat, check Git status, then read AGENTS.md, README.md,
PROJECT_MAP.md and the newest docs/HANDOFF.md checkpoint. Follow the focused
reading index for this task; use current code over superseded historical notes.

Preserve forecast-only source-T/horizon routing, rev03 semantics, code-based
geographic joins, Supabase/CMS revision validation without static fallback,
independent Visitor/Admin sessions and immutable reviewed publication history.
Reuse shared owners. Read LOADING_SCREEN for motion/readiness, ADMIN_CMS and
CMS_FORECAST_LIFECYCLE for no-code work, and NATIVE_PARITY for iOS limits.
Web theme/loading changes do not automatically update native.

Stay in this chat. Preserve unrelated changes. Do not commit/push/deploy,
migrate or write production data unless this request authorizes it. Run checks
proportional to changed risk and report actual evidence and remaining limits.

Task:
```
