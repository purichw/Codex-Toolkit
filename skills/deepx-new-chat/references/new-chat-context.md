# DeepX project context

Reconciled against repository docs on 2026-10-17 (Asia/Bangkok). Treat this as an
orientation map, not a live production report. Re-read current source and docs;
update this reference when an explicitly approved product decision changes.

## Project and services

- Primary checkout: `/Users/point/Website Projects/DeepX`.
- Repository: `https://github.com/purichw/DeepX`; primary branch `main`.
- Public site: `https://deepxsolution.com`; Content Studio: `/admin`.
- `deepxtech.vercel.app` and `www.deepxsolution.com` are legacy aliases with
  permanent 308 redirects to the canonical domain, preserving path and query.
- Vercel scope/project: `purich-w/deepx`.
- Supabase project: `yazamwbukbtetzqmqcpm` at
  `https://yazamwbukbtetzqmqcpm.supabase.co`.
- Recorded Auth configuration uses the canonical Site URL and exact
  `https://deepxsolution.com/admin` redirect. Verify current settings if touching
  auth/domain routing; preserve needed development redirects.

DeepX turns AI/data research into usable enterprise solutions, with project-based
research collaboration and a path toward reusable products. The Business Model
Canvas is in `docs/PROJECT_BRIEF.md`. “Deep Tech” is the category, not another brand.
Do not invent client claims, partnerships or performance metrics.

## Architecture and source owners

React 19 + TypeScript + Vite serve a public anchor-based homepage and a Supabase
CMS. The public page and explicit draft preview use the same Website renderer.

| Area | Source / reference |
| --- | --- |
| Setup and operating constraints | `AGENTS.md`, `README.md`, `package.json` |
| Architecture, routes and interactions | `docs/PROJECT_MAP.md` |
| Public rendering, navigation and dialogs | `src/App.tsx` |
| Validated content contract and published fetch | `src/content.ts` |
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

- Desktop is approved and explicitly protected by the owner. Keep mobile work
  inside the relevant breakpoint; verify desktop if shared CSS could affect it.
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

## CMS and data contracts

- Public users read published content only. Signing in never grants admin rights
  by itself: privileged RPCs check confirmed identities against the server-owned
  allowlist. Private admin identities and audit records must stay private.
- Preserve server drafts, expected-revision checks, immutable snapshots,
  authenticated actor attribution and atomic publication. Do not substitute
  direct browser table writes for guarded RPCs.
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
- Runtime body content reads the CMS; SEO/social metadata is built at deployment.
  CMS publication does not trigger a deploy. Metadata changes need a rebuild.
  Do not silently rewrite CMS contact information because the domain changed.

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

For authorized release work, follow the current runbook. The recorded command is
`vercel deploy --prod --yes --scope purich-w --no-wait`; inspect the returned
deployment with `vercel inspect <deployment-url> --scope purich-w`. An initial CLI
message is not readiness: confirm Ready, intended revision, aliases and actual
assets on `https://deepxsolution.com`. Protected immutable deployment URLs may
show a login page and cannot substitute for canonical-host verification.

Track push, CI if configured, build and promotion separately; diagnose failures
or lack of progress before repeating commands. Do not create duplicate deploys
or deploy again solely for documentation closeout. Previous browser evidence
does not establish physical iPhone/Safari or OS reduced-motion testing; state
which environments were actually exercised.
