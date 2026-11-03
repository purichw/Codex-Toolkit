# DeepX project context

Reconciled against source, repository docs and the verified release on
2026-11-02 (Asia/Bangkok). Treat this as an
orientation map, not a live production report. Re-read current source and docs;
update this reference when an explicitly approved product decision changes.
Region-selection preference updated 2026-11-03; the dated deployment evidence
below has not been re-audited solely for that documentation update.

## Project and services

- Primary checkout: `/Users/point/Website Projects/DeepX`.
- Repository: `https://github.com/DeepXWorks/DeepX.git`; primary branch `main`.
- Public site: `https://deepxworks.com`; shared Content Studio: `/admin`.
- `deepxsolution.com`, `www.deepxsolution.com` and `deepxtech.vercel.app` are legacy aliases with
  permanent 308 redirects to the canonical domain, preserving path and query.
- Vercel scope/project: `purich-w/deepx`.
- Active Supabase project: `mgvgldzqjcsedombmrxr` at
  `https://mgvgldzqjcsedombmrxr.supabase.co`, region `eu-west-1` (Ireland).
- Recorded Auth configuration uses the canonical Site URL and exact
  `https://deepxworks.com/admin` redirect, with the documented localhost callbacks.
  Verify current settings for auth/domain work. Sessions do not migrate between
  origins or Supabase projects; never copy tokens to bypass a fresh sign-in.
- The previous DeepX database `yazamwbukbtetzqmqcpm` is recovery/history, not the
  current target. Glenonchy is a separate project. Stale integration-managed URL
  variables once pointed to Glenonchy, but the application consumes
  `VITE_SUPABASE_URL` / `VITE_SUPABASE_PUBLISHABLE_KEY`. Read
  `docs/SUPABASE_PROVENANCE.md` before investigating or changing integrations;
  do not remove unrelated resources based on a shared organization name.

The owner declined a new paid Supabase organization on 2026-11-02: **keep the
current database and add no recurring cost**. Free-project capacity blocked the
proposed Singapore migration. Functions now run in `dub1`, near the existing
database; static assets still use Vercel's delivery network. No Asia migration,
paid upgrade, project pause/deletion or credential change was performed. Use
`docs/PERFORMANCE.md` for the rationale and prerequisites if migration is reopened.

On 2026-11-03 the owner set a cross-project default: select **Thailand first**,
otherwise the closest suitable supported **Asian region to Thailand**, with
backend and database placed near each other. Follow the shared
[region policy](../../project-onboarding/references/region-defaults.md) for new
resources or an authorized migration. This does not revoke DeepX's existing
Ireland/no-new-cost exception or authorize infrastructure changes now.

DeepX turns AI/data research into usable enterprise solutions, with project-based
research collaboration and a path toward reusable products. The Business Model
Canvas is in `docs/PROJECT_BRIEF.md`. “Deep Tech” is the category, not another brand.
Do not invent client claims, partnerships or performance metrics.

## Product routes and content

| Surface | Current route / contract |
| --- | --- |
| DeepX Works / AI | `/`, established dark corporate site |
| Product Studio | `/studio`, white software-house wing |
| สำรวจไอเดีย / Explore Ideas | `/studio/ideas`, shared white Studio shell |
| Category listing | `/studio/ideas/:categorySlug` |
| Shared Concept detail | `/studio/ideas/:categorySlug/:ideaSlug` |
| Interactive website Concept | The valid item's `/demo` suffix, when enabled |
| Shared CMS | `/admin`, one guarded draft/publication workspace |

The owner reserved `/catalogue` and `/studio/catalogue` for possible future use:
**do not add redirects or Ideas aliases there**. Internal `catalogue` code/schema
names remain valid. Preserve search/filter query state and category membership.
Invalid, private, disabled or mismatched public item routes return real HTTP 404.
Parent idea pages are discoverable; demos are `noindex,follow` and excluded from
the sitemap. SEO setup never guarantees immediate Google indexing or ranking.

The 2026-11-02 publication includes four Fitness demos (Private, Active, Everyday,
Rhythm) and seven Beauty demos (Editorial, International, Personal, Private,
Future, Open, Botanical). The repeated “Beauty 5” requests produced separate
Future and Open concepts; preserve both. These are CMS-editable fictional website
demonstrations, not working clinic/fitness backends or real client testimonials.
Preserve Concept labels and simulated consultation behavior; do not silently
create appointments or send enquiries. Actual enabled records/counts come from CMS.

Some README/Catalogue/per-demo entries still describe earlier private drafts or
local-only checkpoints. Use the newest applicable `docs/RELEASE.md` entry and
current source/data to resolve status, not those old labels. Release evidence
does not grant authorization for a new release or establish future health.

## Architecture and source owners

React 19 + TypeScript + Vite serve the Home, Studio, Ideas and demo route families
with a shared Supabase CMS. Live pages and explicit draft preview share renderers.
Catalogue HTML/SEO and sitemap use fresh-content Vercel functions; Home/Studio
metadata is generated at build time.

| Area | Source / reference |
| --- | --- |
| Setup and operating constraints | `AGENTS.md`, `README.md`, `package.json` |
| Architecture, routes and interactions | `docs/PROJECT_MAP.md` |
| Public rendering, navigation and dialogs | `src/App.tsx` |
| Route entry and lazy modules | `src/main.tsx` |
| Validated content contract and published fetch | `src/content.ts` |
| Studio and shared product UI | `src/studio/`, `src/components/ProductHeader.tsx`, `ProductCard.tsx`, `product-theme.css`; `docs/STUDIO.md` |
| Ideas routing, search/filter and CMS schema | `src/catalogue/`, `docs/CATALOGUE.md` |
| Ideas index and shared rails | `src/catalogue/IdeasRail.tsx`, `ideas-home.css`; `docs/IDEAS_HOME.md` |
| Shared Concept detail | `src/catalogue/ConceptDetail.tsx`, `concept-detail.css`; `docs/CONCEPT_DETAIL.md` |
| Category-only demo navigation | `src/catalogue/DemoShowcase.tsx`, `demo-navigation.ts`, `demo-showcase.css`; `docs/DEMO_NAVIGATION.md` |
| Eleven website demo renderers | `src/demos/`; relevant `docs/FITNESS_*DEMO.md` / `docs/BEAUTY_*DEMO.md` |
| Initial HTML/React loading handoff | `scripts/boot-html.tsx`, `src/components/BootHandoff.tsx`, `LoadingScreen.tsx`, `loading-model.ts`; `docs/LOADING.md` |
| Shared error UI and real HTTP status | `src/errors/`, `server/error-*.ts`, `api/error.mjs`; `docs/ERRORS.md` |
| Fresh public HTML/SEO and sitemap | `scripts/catalogue-seo.ts`, `server/catalogue-handler.ts`, `server/sitemap-handler.ts`; `docs/SEO.md` |
| Route assets and regression gate | `scripts/route-preloads.mjs`, `scripts/check-route-bundles.mjs`; `docs/PERFORMANCE.md` |
| Brand, breakpoints and layout | `src/styles.css` |
| Video/poster rendering and playback | `src/components/HeroMedia.tsx` |
| Mobile ecosystem ticker / other rails | `src/components/PartnerTicker.tsx`, `src/components/Rail.tsx` |
| Shared CTA and detail actions | `src/components/Action.tsx` |
| Auth, content editor and draft/publication | `src/cms/`, `docs/CMS.md` |
| Schema, RLS and guarded RPCs | `supabase/migrations/`, `supabase/tests/` |
| Asset provenance and original mockups | `docs/ASSETS.md`, `docs/references/` |
| Deployment workflow and dated evidence | `docs/RELEASE.md` |

`supabase/content/initial-content.json` is a historical bootstrap/local fixture,
not a production fallback. `dist/` is generated output; never hand-edit it.
`artifacts/` holds ignored QA evidence, so it may be absent in another checkout.

## Accepted visual behavior

These details reflect the latest accepted layout in the docs at reconciliation.
Preserve the intent; inspect current selectors before editing measured values.

- Home desktop is approved and protected from unrelated redesign. Keep mobile
  fixes inside their breakpoint; verify desktop if shared CSS can affect it.
  Later explicit Studio/Ideas redesigns supersede their own earlier compositions.
- Thai is the default with an English switch and stored locale preference.
  Keep translations, readable Thai wrapping and shared centered action styling.
  Process steps and application card headings use the accepted centered layout.
- Hero media is a background **inside the banner behind copy and actions**.
  Autoplay is muted, looping and inline, with no playback controls. Desktop/tablet
  retain full-banner cover. At up to 600px, the 16:9 video frame is 170% width,
  centered horizontally at 50% of banner height, cropping empty sides while
  retaining the central logo and DeepX wordmark. No separate video panel.
- The mobile banner follows content height: no forced 640px minimum and a 33px
  action-to-expertise gap. Do not restore the large blank band below the buttons.
- Hero playback pauses offscreen/in hidden tabs; reduced motion uses the poster
  or static fallback. Media URLs remain editable through the CMS.
- Our Ecosystem remains visible. Current approved order: SUT, Chula, KMUTT,
  NSTDA, NRCT, AWS, Microsoft, Google Cloud. The supplied SUT asset leads Chula;
  published CMS records, not a component array, own order, links and assets.
- At up to 640px the logo ticker moves **left-to-right at 32px/s**, measuring a
  complete sequence for duration. There is **no Play/Pause button or reserved
  control gap**. Keep hover pause, stable keyboard-accessible original links,
  hidden duplicate links, reduced-motion static layout and visibility pause.
  Desktop/tablet use the original Rail/grid; other carousels are unaffected.
- Four industry images use owner-supplied manufacturing, logistics, smart
  agriculture and government/research visuals. Refer to asset provenance and
  current CMS media; do not replace them with earlier mockup placeholders.

For Studio/Ideas and demo work:

- Reuse `ProductHeader`/brand/language, `ProductCard`/grid and existing actions,
  dialogs and rails. Follow Home's readable scale and alignment rather than
  shrinking navigation/body text to fit. Incomplete grid rows stay centered.
- Preserve the shared white Concept detail and Ideas index compositions in
  their owner docs. English copy often occupies more space: inspect real TH/EN
  banners, headings, cards and CTAs, allowing reflow instead of clipping or tiny
  text. `docs/ENGLISH_LAYOUT_QA.md` is prior evidence, not a substitute for current QA.
- The white Studio demo bar lists enabled demos only in the active CMS category,
  in CMS order, numbered from 01 per category. Previous/next stop at endpoints.
  Its logo goes to `/studio`; “สำรวจไอเดีย / Explore Ideas” goes to the main
  `/studio/ideas`, including draft-preview routing. Sticky headers/anchors use
  the measured bar height. Each demo keeps its own visual identity beneath it.
- All `/studio` descendants use light full-page loading, even navy/black demos.
  Home and future dark routes outside Studio use dark loading; register other
  future light route families centrally. Never infer theme from OS preference.
  Shared boot HTML/critical CSS precede first paint; `BootHandoff` removes it only
  when React commits, preventing a flash of SEO fallback. Preserve no-JS and
  script-failure recovery, reduced motion and actual stages, without fake progress
  percentages or artificial waiting. Error pages retain their separate shared
  medium-blue treatment, real status and noindex.

## CMS and data contracts

- Public users read published content only. Signing in never grants admin rights
  by itself: privileged RPCs check confirmed identities against the server-owned
  allowlist. Private admin identities and audit records must stay private.
- Preserve server drafts, expected-revision checks, immutable snapshots,
  authenticated actor attribution and atomic publication. Do not substitute
  direct browser table writes for guarded RPCs.
- Home, Studio, Ideas and website demos share one draft. Publish applies the
  complete saved document, not just the editor's selected page; review its diff.
- Clearing an optional field keeps it empty. Removing a draft record affects
  public content only after publication; preserve unpublished records/history.
- Every editable field must have a real consumer. Keep `docs/CMS.md` coverage
  aligned with schema and renderer changes. Shared components should retain
  equivalent behavior in live and draft preview contexts.
- Image uploads use `cms-media` (JPEG/PNG/WebP, 5 MiB); MP4 uses `cms-video`
  (30 MiB). Uploads are publicly accessible immediately. Replacements get new
  paths; overwrite/delete and private-file storage are not existing CMS features.
- Use append-only migrations and inspect target/history before application.
  Never reset the remote database. Do not expose service keys in Vite/browser code.
- Runtime body content reads the CMS. Home/Studio SEO/social metadata is built
  at deployment, so changes there need a rebuild. Ideas SEO/HTML and sitemap
  read current published content at request time. CMS publication does not deploy.
  Do not silently rewrite CMS contact information because the domain changed.

## Performance contracts

Preserve aesthetics, image fidelity, functional interactions and data freshness.
The current route shell lazily loads Home, Studio, CMS and Catalogue; Catalogue
lazily loads only the chosen demo renderer, its styles and display fonts. Keep
the whole demo/showcase inside the light Suspense boundary until it is ready.

For Ideas routes, server HTML passes the same fresh validated public response
to React in escaped `#deepx-public-content` JSON. `requestSite` validates its
shape and exact route; invalid/missing/mismatched data uses the live RPC path.
This is a per-request handoff, **not persistent content caching**. Keep drafts,
private records and disabled entries outside the public projection. Do not add
stale localStorage, build-time body seeds or silent stale fallbacks to appear fast.

Only immutable build asset metadata is cached in the function. Route preload
graphs follow static imports and select one demo, never all renderers. Preserve
CSS CORS compatibility/deduplication and lazy/async hidden SEO recovery images,
while prioritizing visible hero media. The bundle graph gate runs in `npm run build`.

`docs/PERFORMANCE.md` records before/after sizes, browser conditions, TTFB outlier
and hosting decision. Its payload reductions are unique decoded initial-viewport
assets, not compressed wire bytes, field Core Web Vitals or guaranteed load times.
Measure the changed bottleneck and stop once the touched risk is covered.

## Commands and verification

Run from the selected checkout; inspect `package.json` for current scripts.
Use `npm ci` only when dependency installation is needed. Node requires at least
22.12; the README recommends Node 24 LTS.

| Task | Command / evidence |
| --- | --- |
| Local development | `npm run dev` (normally `http://127.0.0.1:5173`) |
| Types / production bundle | `npm run typecheck`, `npm run build` |
| Content and CMS helper regression | `npm test` |
| Content-only regression | `npm run test:content` |
| Schema alignment | `npm run check:schema` |
| Final local diff | `git diff --check`, `git status --short --branch` |

Choose checks for the changed risk, not every command by default. Visible changes
need a current targeted browser check; mobile changes must respect the approved
desktop. CMS changes require touched-flow save/reopen, publish/read-back, clear/
removal behavior, stale revision rejection and non-admin denial. A transactional
SQL fixture does not prove an authenticated browser journey.

For authorized release work, follow the current runbook and recheck integrations.
At reconciliation, no GitHub Actions or Vercel Git deployment link is configured.
Push the intended source, then create one staged production deployment with
`vercel deploy --prod --skip-domain --scope purich-w --yes --no-wait
--meta gitCommitSha=<source-sha>`. Inspect Ready state, source SHA and function
regions; verify staged routes/assets using authenticated `vercel curl` (the linked
project supplies scope; do not pass `--scope` through to curl). Promote that exact
verified deployment once with `vercel promote <deployment-url> --scope purich-w`.
Confirm the project production target plus real statuses, assets and relevant
browser behavior on `https://deepxworks.com`. Protected immutable URLs can show
a login page and cannot substitute for canonical-host verification.

Track push, CI if configured, build and promotion separately; diagnose failures
or lack of progress before repeating commands. Do not create duplicate deploys
or deploy again solely for documentation closeout. Previous browser evidence
does not establish physical iPhone/Safari or OS reduced-motion testing; state
which environments were actually exercised.
