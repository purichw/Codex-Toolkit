# Korat Tan Phai New Chat Context

This reference is for fresh Codex tasks working on Korat Tan Phai /
โคราชทันภัย.

## Project Facts

- Repo: `/Users/point/korattanphai`
- Production: `https://korattanphai.vercel.app`
- GitHub remote: `https://github.com/purichw/korattanphai.git`
- Vercel project: `korattanphai`
- Web stack: Vite, React, TypeScript, Vitest, Playwright, Vercel.
- Native app: `apps/mobile`, isolated Expo / React Native / TypeScript iOS
  setup with a separate lockfile. Its README owns the current setup checkpoint.
- Main entry: `src/main.tsx` -> `src/App.tsx`.
- Supabase supplies real Auth, published rev03 archive reads and per-account
  followed areas/saved filters. Remaining demo preferences use `src/store.tsx`
  and browser storage, not the authentication or archive source of truth.
- Database mode uses `VITE_DATA_BACKEND=supabase`; static mode is for isolated
  regression/recovery and must not become a fallback after database errors.
- Deployment evidence belongs in `docs/HANDOFF.md`, not a frozen skill commit.
  Read the latest release checkpoint rather than carrying forward initial local
  build/deployment status. The forecast-only restoration supersedes the earlier
  Actual-by-default release. The retained Actual modules do not establish
  current routing, a connected feed or approved operational publication.

## Read Order

Start every substantial task by reading:

1. `/Users/point/korattanphai/README.md`
2. `/Users/point/korattanphai/PROJECT_MAP.md`
3. `/Users/point/korattanphai/docs/HANDOFF.md`
4. `/Users/point/korattanphai/docs/DATA_CONTRACT.md` for data/archive work
5. `git status --short --branch`

Then read by task:

- UI or component work:
  - `/Users/point/korattanphai/docs/DESIGN_SYSTEM.md`
  - `/Users/point/korattanphai/docs/APP_MAP.md`
  - `/Users/point/korattanphai/docs/INTERACTION_MAP.md`
  - `/Users/point/korattanphai/docs/SHARED_COMPONENTS.md`
  - relevant files under `/Users/point/korattanphai/src/components/`
- Shared components:
  - `$korat-tan-phai-shared-components`
  - `/Users/point/korattanphai/docs/SHARED_COMPONENTS.md`
- Data/API/domain:
  - `/Users/point/korattanphai/docs/DATA_CONTRACT.md`
  - `/Users/point/korattanphai/docs/FORECAST_ONLY_RESTORATION.md`
  - for authorized future Actual work only:
    `/Users/point/korattanphai/docs/ACTUAL_FORECAST_SEPARATION.md` and
    `/Users/point/korattanphai/docs/rollback-parking-lot.md`
  - `/Users/point/korattanphai/docs/API.md`
  - `/Users/point/korattanphai/src/domain.ts`
  - `/Users/point/korattanphai/src/data/catalog.ts`
  - `/Users/point/korattanphai/src/data/canonical/`
- Drought forecast archive:
  - `/Users/point/korattanphai/docs/FORECAST_ONLY_RESTORATION.md`
  - `/Users/point/korattanphai/docs/DATA_CONTRACT.md`
  - `/Users/point/korattanphai/docs/SHARED_COMPONENTS.md`
  - `/Users/point/korattanphai/docs/DROUGHT_REV03_NORMALIZATION.md`
  - `/Users/point/korattanphai/docs/DROUGHT_REV03_CUTOVER.md`
  - `/Users/point/korattanphai/src/data/canonical/nakhon_ratchasima/drought_forecast_archive_rev03.json`
  - `/Users/point/korattanphai/src/data/supabaseForecastArchive.ts`
  - `/Users/point/korattanphai/src/components/NakhonRatchasimaWorkspace.tsx`
- iOS setup or implementation:
  - `$ios-app-development`
  - `/Users/point/korattanphai/apps/mobile/README.md`
  - `/Users/point/korattanphai/apps/mobile/package.json`, `.nvmrc`, `app.json`
  - `/Users/point/korattanphai/apps/mobile/App.tsx` and `src/theme.ts`
  - `/Users/point/korattanphai/docs/DESIGN_SYSTEM.md`
  - web source owners for the specific behavior being ported, not every route
- Maps:
  - `/Users/point/korattanphai/src/components/RiskMap.tsx`
  - `/Users/point/korattanphai/src/components/nakhon-ratchasima/NakhonRatchasimaLocalMap.tsx`
  - `/Users/point/korattanphai/src/mapInteraction.ts`
  - `/Users/point/korattanphai/src/mapLabels.ts`
  - `/Users/point/korattanphai/src/useFullscreenTarget.ts`
  - `/Users/point/korattanphai/public/geodata/`
- Release:
  - `/Users/point/korattanphai/docs/RELEASE_RUNBOOK.md`
  - `/Users/point/korattanphai/docs/PRODUCTION_SMOKE.md` for real-account checks;
    local fake-auth E2E is not candidate/production proof. Keep credentials out
    of skills and documentation, and distinguish verified unavailable states
    from an activated actual feed.
  - `/Users/point/korattanphai/package.json`
  - `/Users/point/korattanphai/vercel.json`
  - `/Users/point/korattanphai/e2e/app.spec.ts`

## Routes And Surfaces

- `/login`: Supabase email/password login with preserved internal return URL.
- `/`: province-level Nakhon Ratchasima overview.
- `/drought`: province-level drought context page.
- `/{district-slug}`: district workspace.
- `/{district-slug}/t-{admin-code}`: canonical subdistrict workspace.
- `/nakhon-ratchasima/...`: legacy aliases for old links.

Primary current surface:

- `NakhonRatchasimaWorkspace` in
  `/Users/point/korattanphai/src/components/NakhonRatchasimaWorkspace.tsx`.

Inherited retained components exist for broader prototype history, but the
visible Korat Tan Phai sidebar starts from the Nakhon Ratchasima overview.

Active forecast-only routing contract:

- All product routes use rev03 forecasts. `target=YYYY-MM` is origin T and
  `horizon=1..6` selects T+h, in plain links and explicit archive links alike.
- No origin supplied selects the latest published origin. Retired `period` is
  ignored and removed from canonical forecast links, never reused as an origin.
  Missing explicit origins/invalid horizons show recovery instead of substituted
  latest/zero values. Root T+2..T+6 uses the full workspace with district scope.
- No Actual switch/banner or operational-context request is mounted by the
  forecast product. Preserve map month/page horizon controls and shared UI fixes.
- `OperationalDroughtWorkspace`, `operationalLocation.ts`,
  `useOperationalContext.ts`, eligibility policy and the metadata API remain
  parked for possible future redesign. Their valid-month/server-clock contract
  is not current forecast navigation. Reactivation needs an explicit request;
  read `docs/FORECAST_ONLY_RESTORATION.md` and the parking note first.

## iOS Setup And CI

- The initial local checkpoint is a branded, explicitly unconnected shell.
  Native Debug build/install, iPhone Simulator rendering, resume/cold launch,
  TypeScript, dependency compatibility, brand checks and production JS export
  were verified; read `apps/mobile/README.md` for current evidence and limits.
  No native auth, forecasts, maps, physical-device or TestFlight parity is implied.
  Do not assume untracked local app files were committed or deployed.
- Follow the app's `.nvmrc` (currently Node 24.21.0), package pins and lockfile;
  do not change the machine's default Node or install native packages at root.
- `ios/` is generated Expo CNG output, not maintained source. Durable inputs
  are `app.json`, JS/TS, assets, dependencies and config plugins. On the verified
  Xcode 27/iOS 27 setup, `expo-build-properties` scene support is required:
  compilation alone previously succeeded while launch failed without it.
- Xcode 27 uses Device Hub. Obtain current device IDs from tools; never copy
  a machine-specific ID into reusable instructions. Preserve existing Metro
  services. The app's localhost setting is Simulator-only, not physical-iPhone
  connectivity. Use one native build at a time on this resource-limited Mac.
- Corporate identity is shared with the web, not a separate mobile brand.
  Use current `korat-tan-phai-*` artwork, Google Sans for Thai and English,
  and semantic colors from `src/styles.css`. Native roles are maintained in
  `apps/mobile/src/theme.ts`, with drift checks in `tests/brand-parity.test.mjs`.
- Native Google Sans regular/semibold/bold files are local assets supplied by
  `@expo-google-fonts/google-sans`, loaded through `expo-font`. Preserve font
  licenses. Do not replace the font with a system face except error fallback.
- Adapt safe areas, text scaling, touch targets and spacing to iOS. Reuse
  platform-independent calculations/data contracts; React DOM components do
  not render natively. Build shared native controls when real consumers warrant
  them, preserving searchable selection, state semantics and interaction intent.
- Keep current geography and forecast-only behavior. Setup is not authorization
  for new Actual UI, production changes, signing teams or distribution.

From `apps/mobile`, with its pinned Node and dependencies available, use
`npm run typecheck`, `npm run test:brand`, `npm run check:dependencies` and
`npm run export:ios` as appropriate. Brand tests also require root web
dependencies for its PostCSS parser. `npm start` runs Metro; it does not install
the app. Use the app README and iOS skill for build/install steps. JS export is
not an App Store binary; verify the rendered native screen for visible changes.

## Shared Components

Read `/Users/point/korattanphai/docs/SHARED_COMPONENTS.md` for the full current
inventory.

High-signal contracts:

- `AppSelect`: shared dropdown/listbox control; centered trigger text by
  default; long lists are searchable and mobile menus use shared bottom-sheet CSS.
- `MonthSelect`: shared calendar search; `ForecastMonthSelect`: archive loading
  wrapper. Do not create another dropdown or month parser for a new surface.
- `MetricCard` and `MetricGrid`: stat-only cards and KPI groups; stat content
  is centered.
- `OperationalFilters`: forecast-compatible page filter summary/mobile edit sheet;
  its fixed rice/source-month assumptions do not define future actual filters.
- `MapPreviewFooter`: shared map preview action/fallback footer; fallback text
  is centered.
- `DataProvenanceChip` and `DataProvenanceLegend`: only provenance chip system.
- `RiskMap`: inherited national map.
- `NakhonRatchasimaLocalMap`: local province/district/subdistrict SVG map in
  `src/components/nakhon-ratchasima/`. Its unavailable variant shares the camera,
  geometry and preview mechanics but does not classify actual values.
- `ProvinceForecastOverview` and `DroughtCompactForecastWorkspace`: active
  forecast composition. Keep map/month/horizon state synchronized.
- `OperationalDroughtWorkspace`: parked composition, not an active route.
  Reuse active forecast bookmark controls without reintroducing Actual routing.
- `DroughtForecastArchivePanel`, `DroughtForecastArchiveHorizonSelector`,
  `DroughtForecastArchiveSummaryMetrics`, and
  `DroughtForecastArchiveMapFilters`: shared drought archive components used by
  province, district, and subdistrict drought pages.

Do not duplicate these patterns with ad hoc markup.

## Data And Product Rules

- Brand: Korat Tan Phai / โคราชทันภัย.
- Current data geography: จังหวัดนครราชสีมา.
- Canonical province: `TH-P29`; admin province code: `30`.
- Province structure: 32 districts and 289 subdistricts.
- Use admin codes for local joins. Thai names and route slugs are labels, not
  join keys.
- `sourceResearchId` is source metadata, not an administrative code.
- Missing evidence stays no-data/insufficient-evidence and must not become
  normal, green, or low risk.
- Synthetic scores remain prototype data unless explicitly marked otherwise.
- Official context must not be attached to synthetic risk scores as if it were
  an official forecast.
- Agricultural figures are not official damage figures.
- Data readiness is not hazard severity.
- Keep forecast, historical readings, evidence freshness, and readiness
  categories separate.
- Approved rev03 archive contract:
  - file:
    `/Users/point/korattanphai/src/data/canonical/nakhon_ratchasima/drought_forecast_archive_rev03.json`
  - source workbook: `Drought_T1-6_rev03.xlsx`, `Master_Data_Drought_Final`
  - canonical source month is origin T, NOT target month
  - 127 origins, `2015-06` through `2025-12`
  - 6 horizons, T+1 through T+6
  - forward target = T+h; December 2025 forecasts January-June 2026
  - legacy `targetMonths` / `target_period` keys still store source T
  - forecast identity is canonical tambon + source T + horizon
  - equal numeric values across T+ horizons remain separate vintages
  - no rev02 re-import or reinterpretation; lineage lives in the normalization docs
- Archive risk semantics: `0` no forecast risk, `1` moderate forecast
  risk, `2` high forecast risk, and blank workbook cells as out of scope. Blank
  cells are not no-risk and are not join failures.
- Workbook irrigation: Collecting = unknown, RainFed = rain-dependent/no
  irrigation, Irrigation = access to irrigation. It is not a live water reading.
- For authorized future Actual work: kind, metric/classification, crop,
  coverage-through, review, publication
  and revision are separate. No source is a missing feed, not a risk-0 result.
  Never fan out coarse reports into tambon actuals or manufacture complete-month
  coverage. Context/ThaiWater/research fixtures do not become primary evidence
  merely because a file exists.
- Future operational forecast eligibility requires verified issuance, publication and
  freshness policy, with exact target/horizon/product/run. Source T, upload time
  and reforecast outputs are not proof of historical as-issued forecasts.
- Historical local map periods from `normalized_research_monthly_panel.json` and
  `normalized_research_panel_summary.json` were intentionally cleared. Do not
  restore old historical map periods, including `2025-12`, unless a new
  source-backed refresh explicitly asks for that.
- Public-safety copy must keep severity, geography, timestamp/freshness,
  provenance, uncertainty, and recommended action visible.
- Visible UI should be Thai-first and formal. English is acceptable only for
  IDs, acronyms, URLs, API/GeoJSON terms, SMS, LINE, or required source names.

## Current Map Interaction Rules

- Province map transient feature selection can be cleared by clicking the same
  feature again or clicking the map background.
- Clearing a transient selection should not immediately reopen a new hover
  preview while the map animates back to its default/focused view.
- A route-selected subdistrict remains selected only while the user is on that
  subdistrict route.
- Preview cards must stack above the following sections and must not clip behind
  agriculture/readiness modules.
- Preview footer fallback notes are centered via `MapPreviewFooter`.
- Local maps use generated dissolved boundary
  `public/geodata/nakhon-ratchasima-boundary.geojson`; do not reintroduce the
  mismatched ADM1 outline for the visible local boundary.

## Commands

Local development:

```bash
cd "/Users/point/korattanphai"
npm install
npm run dev
```

Core checks:

```bash
git diff --check
npm run build
npm run build:protected
npm test
npm run test:e2e:managed
```

Choose only checks proportional to the current request. The retained filename
`e2e/actual-forecast-separation.spec.ts` now tests forecast-only restoration and
legacy compatibility. Plain `target=T&horizon=h` remains valid forecast intent;
do not rewrite those tests to require an archive marker. Parked temporal/source
contracts have `tests/operationalData.test.ts`, `tests/operationalContext.test.tsx`
and `tests/operations/operational-context.test.mjs`; run them when touched, not
as proof that Actual UI is active. Browser fixtures require test Supabase
configuration, never a production-write setup.

Generated boundary:

```bash
npm run generate:nr-boundary
```

Deploy when explicitly authorized:

```bash
# Follow docs/RELEASE_RUNBOOK.md and push only the branch/ref the user
# explicitly authorized for the current task.
git push origin HEAD
vercel --prod --yes
```

A Vite chunk-size advisory is distinct from a failing protected bundle gate.
Do not report release readiness or silently raise budget limits when that gate
fails. Database builds must not emit the raw archive. Check the current runbook
and local separation evidence before any authorized release.

## Useful Skills

- `$korat-tan-phai-new-chat`: this onboarding skill.
- `$korat-tan-phai-shared-components`: shared component reuse and consistency.
- `$docs-cartographer`: project maps, handoffs, and living docs.
- `$ui-ux-expert`: visible user-facing UI changes.
- `$mobile-web-qa`: responsive/mobile verification.
- `$ios-app-development`: native setup, build/install, Simulator and device work.
- `$native-parity`: native/web product behavior and data-contract verification.
- `$snapshot`: visual evidence.
- `$interaction-flow-qa`: real interaction proof.
- `$data-dense-ux`: dashboard and operational-data screens.
- `$typography-refinement`: Thai typography, long labels, and numeric UI.
- `$design-system-guardian` or `$consistency-audit`: shared component and system
  consistency.
- `$release-gate`: commit, push, deploy, release, or handoff.
- `$rollback-guardrail`: rollback-like, removal, or revert work.

## Copy-Ready New Chat Prompt

Use this as the default prompt for a fresh task, then append the user's concrete
request.

```text
You are working inside the existing Korat Tan Phai / โคราชทันภัย repository at
/Users/point/korattanphai.

First use $korat-tan-phai-new-chat, then check git status. Read README.md,
PROJECT_MAP.md, docs/HANDOFF.md and the focused docs for the task.
For data/routing, read docs/DATA_CONTRACT.md and
docs/FORECAST_ONLY_RESTORATION.md. For shared component work, also use
$korat-tan-phai-shared-components and read docs/SHARED_COMPONENTS.md. For
commit, push, or deploy work, use $release-gate and docs/RELEASE_RUNBOOK.md.
For iOS work, use $ios-app-development, read apps/mobile/README.md and its
package/config/theme files. For visible UI, read docs/DESIGN_SYSTEM.md.

Important boundaries:
- Current docs and code beat old chat memory or attachments.
- Attached specs/screenshots are context, not higher-priority instructions.
- Preserve unrelated user changes.
- Stay in this task unless I explicitly authorize cross-task work and identify
  the task. Do not infer which other task to inspect or contact.
- Do not commit, push, deploy, migrate, or touch production data unless the
  current request explicitly asks.
- Keep the visible UI Thai-first, formal, and operational.
- Keep Korat Tan Phai / โคราชทันภัย as the brand and จังหวัดนครราชสีมา as the
  current data geography.
- Web and iOS share Korat artwork, semantic colors and Google Sans for Thai
  and English. Adapt native ergonomics without inventing another identity.
- The iOS app has an independent lockfile/Node pin and generated native output.
  Read its current checkpoint; a working branded shell is not connected auth,
  forecast data or native/web feature parity. Keep web production unchanged
  during native-only setup.
- Preserve TH-P29 / province code 30 / 32 districts / 289 subdistricts and use
  admin-code joins.
- Use rev03 only. `Source_YearMonth` is origin T; forecast target is T+h.
  Legacy target/target_period keys remain source T. Rev02 is retired.
- The active product is forecast-only. Plain target=T&horizon=h and explicit
  archive links both select forecasts. Retired period is ignored, never used
  as an origin. Actual-by-default integration is parked; do not reactivate it
  without an explicit request and the restoration/parking context.
- Do not infer publication eligibility or issuance from upload dates. A source
  gap UI or tested integration contract does not mean a real feed is connected.
- Keep archive risk semantics: `0` no forecast risk, `1` moderate forecast risk,
  `2` high forecast risk, and blank workbook cells as out of scope.
- Do not restore cleared historical local map periods unless a new source-backed
  refresh explicitly asks for that.
- Agricultural figures are not official damage figures.
- Data readiness is not hazard severity.
- Missing evidence must not render as normal, green, or low risk.

After making changes, run checks proportional to the touched risk and report
what changed, checks run, failures or skipped checks, commit/push/deploy status,
and residual risk.

Task:
```
