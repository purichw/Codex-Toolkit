# Mongkol Wela New Chat Context

Use this as a task-scoped pickup map. Reviewed 2026-10-11 against code at
`303d84c`. Prefer current on-disk files over memory; dated release evidence is
not a new production check. Do not inspect other chats to fill gaps.

## Project

- Primary checkout: `/Users/point/Website Projects/hora-astro`. Use the current
  task's selected worktree when present. Resolve every repo-relative path below
  against that checkout, not automatically against the primary copy.
- Production: `https://mongkolwela.vercel.app`
- GitHub: `purichw/Mongkol-Wela`; the legacy `purichw/hora-astro` remote redirected
  there during the September release. Verify current remote for release work.
- Stack at reviewed revision: Astro 7.3.5, Vercel adapter 11.0.11, bundled
  `src/scripts/` and `src/styles/`, authoritative live CMS, Playwright.
- Mostly prerendered pages; popular/mu/sacred details and sitemap use live CMS SSR.
  Static output is `dist/client/`, deployment output `.vercel/output/`.
- Main product direction: Thai-first auspicious life companion. Current product focus is the temple side: temples, sacred places, merit routes, mu/sacred collections, all-Thailand temple directory, and trip planning.
- Important positioning: the temple side should feel like a practical sacred-place and auspicious-trip guide, not primarily a horoscope/tarot site.

## Read Order

For an unfamiliar checkout or broad task, start with `AGENTS.md`,
`git status --short --branch`, relevant sections of `Architecture.md` and
`Roadmap.md`, then the documentation index in `README.md`. For tiny follow-ups
with context already loaded, read only owner files and relevant contracts.

Then choose by task:

- Admin/CMS: `CMS.md`, `docs/cms-workspace-coverage.md`, `src/scripts/admin/`,
  `src/scripts/cms-runtime.js`, `src/lib/live-content.js`, `api/admin/`.
  `public/admin/content/live.json` and `default.json` are seeds, not live authority.
- Place URLs/identity: `docs/temple-slugs.md`, `src/data/temple-slugs.js`,
  `src/data/temple-english-names.js`, `src/data/temple-cms.js`,
  `src/lib/temple-routing.js`, `src/lib/temple-slug-format.js`.
- Tarot research/content: `docs/tarot-redesign.md`,
  `docs/research/tarot-78-deep-research-prompt.md`, the Tarot section below and
  the editorial import boundary in `CMS.md`.
- Temple product/design direction: `docs/mongkolwela-temple-project-context.md`, `docs/mongkolwela-temple-pages-design-spec.md`
- Temple routes/components/data: `Architecture.md`, `src/pages/temples/**`, `src/components/Temple*.astro`, `src/data/temple*.js`, `src/data/*temples*.json`
- Home: `src/pages/index.astro`, `src/styles/home.css`, `src/scripts/home-motion.js`,
  `src/scripts/carousel.js`, `src/layouts/BaseLayout.astro`.
- Planner: `src/pages/temples/planner/index.astro`, `src/styles/temple-planner.css`,
  `src/scripts/temple-planner.js`, `src/scripts/planner/`, `src/data/temple-planner.js`,
  `api/temple-planner/`.
- Map/list/detail: `src/components/TempleMapOverlay.astro`,
  `src/components/TempleDetail.astro`, `src/styles/place-detail.css`,
  `src/styles/temple-map.css`, `src/scripts/temple-map.js`,
  `src/scripts/temple-directory.js`, `src/scripts/temple-detail.js`.
- All-Thailand directory: `src/pages/temples/thailand/index.astro`,
  `src/pages/assets/data/temples-thailand-index.json.ts`,
  `public/assets/data/temples-thailand.json`, `src/scripts/temple-directory.js`.
- SEO, bot, and crawler controls: `src/pages/robots.txt.ts`, `src/pages/llms.txt.ts`, `src/pages/sitemap.xml.ts`, `src/lib/seo.js`, `vercel.json`, `scripts/apply-vercel-firewall.mjs`, `scripts/smoke-production.mjs`
- UI redesign: `docs/shared-ui.md`, `docs/mockup-adaptation-lessons.md`, then the
  specific route's design/adaptation note linked from `README.md`.
- QA/release: `Roadmap.md#release-workflow`, `package.json`, `playwright.config.ts`,
  `tests/runtime/`, `tests/e2e/`, `.github/workflows/`.

## Skills To Use

Use the current on-disk `SKILL.md` each time a skill is invoked.

- New-chat onboarding: `$mongkol-new-chat`
- Website maintenance/source vs generated artifacts: `$site-maintainer`
- Release readiness, commit, push, deploy: `$release-gate`
- Rollback/revert/remove/delete guard: `$rollback-guardrail`
- UI/UX design or critique: `$ui-ux-expert` or `$ui-ux-orchestrator`
- Design system preservation: `$design-system-guardian`
- Consistency-only audits: `$consistency-audit`
- Snapshots/screenshots: `$snapshot`
- Mobile responsive QA: `$mobile-web-qa`
- Interaction/browser QA: `$interaction-flow-qa`
- Accessibility: `$accessible-interaction`
- Forms and planner-like flows: `$form-flow-ux`
- Data-dense directory/admin UX: `$data-dense-ux`
- Mockup implementation: `$mockup-to-product`; exact-match work: `$reference-to-a-tee`
- Offline HTML / clickable prototypes: `$export-html`
- Design handoffs/specs: `$codex-handoff-for-claude`
- Project documentation: `$docs-cartographer`; skill maintenance: `$skill-creator`
- Production smoke or asset checks: `$prod-smoke-harness`, `$production-asset-smoke`
- Admin/CMS operations: `$admin-ops`
- Efficient batching / CI usage control: `$efficient-execution`, `$usage-budget-gate`

## Durable Product Rules

- Thai-first. Do not build English variants unless explicitly requested.
- English/romanized place slugs are already approved; they do not add an English locale.
- Temple side is temple-first, not fortune-first: emphasize places, routes, worship/merit context, and trip planning over divination.
- Preserve the warm sacred visual system: warm paper background, lacquer red, restrained gold/yellow aura, jade/green support states, and deep brown/ink text.
- Use real/place imagery where possible. Use the muted auspicious placeholder only as fallback.
- Do not turn operational or data-dense pages into landing pages. Planner and directory pages need useful density.
- Preserve internal scroll containers and table/map dimensions unless the task explicitly changes them.
- Preserve card/list/detail journeys: search/filter -> compare -> detail/map/planner.
- Keep confidence/help UI honest and visitor-facing. Do not hide uncertainty by inventing data.
- Use the exact source text for the all-Thailand temple directory: `ระบบทะเบียนวัด สำนักงานพระพุทธศาสนาแห่งชาติ`.
- All-Thailand temple directory data must come from the provided `Report_Temple 2.numbers` source only unless the user explicitly changes direction. Do not scrape/export that data from websites.
- Published page registry/navigation belongs to the configured live CMS. Supabase
  is authoritative when configured; otherwise authenticated GitHub is authoritative.
  Source errors return 503, not seed/cache failover. Never seed over Admin edits.
- Preserve declared `managedContent` fields, explicit empty values and revision
  conflicts. Trace editor -> draft -> publication -> live read -> Visitor consumers
  for new supported fields; unsupported fields need explicit implementation.
- CSS/JS use content hashes; `src/config/styles.js` owns route CSS. Do not restore
  manual `assetVersion` or `public/styles.css` query-string bump instructions.
- Visitor collection hearts stay hidden until member accounts/favorites exist.
  Restore account-backed favorites when implementing members, not browser-only
  substitutes. The durable decision is in `Roadmap.md`.
- Do not commit generated artifacts: `node_modules/`, `dist/`, `.astro/`, `.vercel/`, `outputs/`, root `preview-*.png`, `.DS_Store`.
- The project moved out of iCloud; preserve the currently selected checkout and
  unrelated work. A matching project name does not authorize reading another chat.

## Place Identity And URLs

- The curated popular/mu/sacred collections contain 625 base records at the reviewed
  revision. This is separate from the all-Thailand directory and not a permanent
  limit on Admin-created records.
- Automatic/custom ASCII slugs are separate from immutable CMS/planner keys.
  Preserve page patches and server-maintained `slugAliases`; old URLs redirect
  directly with 308 and keep query strings. Do not regenerate IDs from new slugs.
- Renamed/deleted URLs remain reserved; hidden/deleted places return 404.
  CMS outages return 503. Detail routes and sitemap are no-store SSR, so a new
  published place/slug must work without a rebuild.
- Use `tests/helpers/temple-routing-server.mjs` for loopback in-memory publication
  tests. Historical release evidence and coverage boundaries live in
  `docs/temple-slugs.md`, not in this skill as a claim of current production health.

## Tarot Editorial Boundary

- `src/data/tarot-meanings.js` registers `tarot.tarotMeaningCards`;
  `src/scripts/tarot-data.js` registers `tarot.tarotCards`. Both have the same 78
  legacy IDs, but serve different content roles. Preserve odd spellings such as
  `the-fives-of-cups`, `the-sixs-of-swords` and `the-judgment`.
- `src/scripts/tarot-draw.js` owns selection. Daily/monthly use 78 cards;
  luck/love/money/career use 22 Major Arcana. Monthly requires ten distinct ordered
  cards; other modes require one. Retain URL parameters and storage keys.
- `src/scripts/tarot-result.js`, `src/scripts/tarot-spread-result.js` and
  `src/scripts/tarot-view.js` render results. Minor meanings are still rank/suit
  templates; monthly reuses general advice and topics use grouped verdicts.
- `docs/research/tarot-78-deep-research-prompt.md` is a prepared prompt, not research
  results. Requested scope is 78 x six contexts x two orientations (936 blocks),
  plus 78 x ten monthly positions x two orientations (1,560 readings).
- `tarot-research-v1` is proposed research output, not a supported live CMS schema.
  Review sources/copy, map existing fields and identify new fields before import.
  Research coverage neither changes topic deck eligibility nor implements reversed
  draws. Publishing/import/behavior changes need separate task authorization.

## Scoped Commands

```bash
# Run in the selected checkout. Install only when dependencies need setup.
npm ci
npm run dev -- --host 127.0.0.1 --port 4324
npm run check
npm run build
npm run nfr:cms
npm run smoke:production
```

This is a command reference, not a mandatory sequence. Choose checks for the
current risk; use another port if 4324 is occupied. Do not install dependencies,
start a server or run production smoke just to update prose.

## Verification Defaults

- Docs/skills: factual/path validation, skill validator when applicable, diff/status.
- Tiny visible changes: owner files, diff check and one relevant visual/style check.
- Components/flows: targeted behavioral checks; desktop/mobile for responsive risk.
- Release/CMS/routing/auth/data migrations: stricter contracts and required gates.
  State scope, evidence and stop rule before broad suites. Do not run full NFR/E2E
  from momentum on a small follow-up.
- Map changes should verify Leaflet loads, markers render, no console errors, Thailand bounds are respected, and detail links work.

## Release Lessons

- Follow `Roadmap.md#release-workflow`. Track push, required CI, build readiness
  and production alias/SHA separately. Use full-SHA GitHub run queries; a short
  SHA previously hid an existing run and caused an unnecessary manual dispatch.
- Inspect Git-triggered Vercel deployment before starting CLI deployment. Do not
  create duplicate deployments or weaken gates just to finish. Investigate exact
  runs/logs at the runbook checkpoints instead of blind polling/retries.
- Use `scripts/smoke-production.mjs` with its approved harness request headers.
  Plain requests can hit Security Checkpoint 429. Protected candidates additionally
  need the existing authorized `vercel curl` flow; distinguish access checks from
  application failures without disabling firewall or exposing credentials.
- The September release still exceeded six performance budgets also present in
  its baseline. Read `docs/temple-slugs.md` before claiming a regression or clean NFR.
- Keep baseline source copies outside Astro diagnostics; `.vercelignore` does not
  necessarily exclude a copied tree from typechecking. Do not globally narrow
  checks to suppress real errors.
- Production smoke is read-only. Admin create/rename/publish tests use fixtures
  or specifically authorized UAT, never opportunistic writes to live CMS.

## New Chat Prompt Template

Use this when the user asks for a starter prompt:

```text
We are continuing the Mongkol Wela / hora-astro project at:
<absolute path of the checkout selected for this task>

Before doing work, use $mongkol-new-chat and read current on-disk docs, not prior memory. Start with AGENTS.md, git status and relevant Architecture.md / Roadmap.md sections. Use README.md and /Users/point/.codex/skills/mongkol-new-chat/references/new-chat-context.md to find task-specific owners.

Important constraints:
- Stay in the selected checkout and current chat. Do not inspect/message other chats or switch worktrees without explicit scope authorization.
- Preserve routes, journeys, data contracts, internal scroll containers, responsive constraints, and customized component geometry unless explicitly in scope.
- Keep the site Thai-first. For temple work, keep the product temple-first, practical, sacred, and not primarily horoscope/tarot.
- Live CMS is authoritative; seeds never override published edits. Keep place keys/aliases and Tarot legacy IDs stable. Research briefs are not imported content.
- Do not commit, push, deploy, migrate, write production CMS, rollback, revert, remove, or delete unless explicitly asked in this current task.
- If a named skill is used, read its current on-disk SKILL.md first.
- Scope checks to the current risk. Docs need reference/diff checks; visible UI needs targeted evidence, with desktop/mobile coverage for responsive risk.
- Rollback-like work must use $rollback-guardrail first.
- Release, commit, push or deploy work must use $release-gate and Roadmap.md's release workflow. A context handoff alone is not a release.
- Do not commit generated artifacts such as node_modules, dist, .astro, .vercel, outputs, preview PNGs, or .DS_Store.

After onboarding, summarize what you read and wait for my task unless I already gave one.
```
