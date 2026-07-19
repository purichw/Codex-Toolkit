# Mongkol Wela New Chat Context

Use this as the pickup map for a fresh Codex chat. Prefer current on-disk files over memory from any prior thread.

## Project

- Repo: `/Users/point/Website Projects/hora-astro`
- Production: `https://mongkolwela.vercel.app`
- GitHub: `purichw/hora-astro`
- Stack: Astro static site, plain public CSS/JS, Vercel, optional Supabase-backed Admin Portal content, Playwright.
- Main product direction: Thai-first auspicious life companion. Current product focus is the temple side: temples, sacred places, merit routes, mu/sacred collections, all-Thailand temple directory, and trip planning.
- Important positioning: the temple side should feel like a practical sacred-place and auspicious-trip guide, not primarily a horoscope/tarot site.

## Read Order

Always start with:

1. `/Users/point/Website Projects/hora-astro/AGENTS.md`
2. `/Users/point/Website Projects/hora-astro/Architecture.md`
3. `/Users/point/Website Projects/hora-astro/Roadmap.md`
4. `/Users/point/Website Projects/hora-astro/README.md`
5. `git -C "/Users/point/Website Projects/hora-astro" status --short --branch`

Then choose by task:

- Admin Portal, CMS content, navigation, or page registry: `CMS.md`, `public/admin/content/live.json`, `public/admin/content/default.json`, `src/config/site.js`
- Temple product/design direction: `docs/mongkolwela-temple-project-context.md`, `docs/mongkolwela-temple-pages-design-spec.md`
- Temple routes/components/data: `Architecture.md`, `src/pages/temples/**`, `src/components/Temple*.astro`, `src/data/temple*.js`, `src/data/*temples*.json`
- Home page or animation work: `src/pages/index.astro`, `public/assets/css/home.css`, `public/assets/js/home-motion.js`, `public/assets/js/carousel.js`, `src/layouts/BaseLayout.astro`
- Planner: `src/pages/temples/planner/index.astro`, `public/assets/css/temple-planner.css`, `public/assets/js/temple-planner.js`, `src/data/temple-planner.js`
- Map/list/detail UX: `src/components/TempleMapOverlay.astro`, `src/components/TempleDetail.astro`, `public/assets/css/temple-map.css`, `public/assets/js/temple-map.js`, `public/assets/js/temple-directory.js`, `public/assets/js/temple-detail.js`
- All-Thailand temple directory: `src/pages/temples/thailand/index.astro`, `public/assets/data/temples-thailand.json`, `public/assets/data/thailand-boundary.geojson`, `public/assets/js/temple-directory.js`
- SEO, bot, and crawler controls: `src/pages/robots.txt.ts`, `src/pages/llms.txt.ts`, `src/pages/sitemap.xml.ts`, `src/lib/seo.js`, `vercel.json`, `scripts/apply-vercel-firewall.mjs`, `scripts/smoke-production.mjs`
- QA and release: `package.json`, `playwright.config.ts`, `tests/e2e/**`, `.github/workflows/**`

## Skills To Use

Use the current on-disk `SKILL.md` each time a skill is invoked.

- New-chat onboarding: `$mongkol-new-chat`
- Website maintenance/source vs generated artifacts: `$site-maintainer`
- Release readiness, commit, push, deploy, handoff: `$release-gate`
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
- Offline HTML / clickable prototype exports: `$export-html` or `$global-export-html`
- Full design specification: `$global-full-design-spec`
- Production smoke or asset checks: `$prod-smoke-harness`, `$production-asset-smoke`
- Admin/CMS operations: `$admin-ops`
- Efficient batching / CI usage control: `$efficient-execution`, `$usage-budget-gate`

## Durable Product Rules

- Thai-first. Do not build English variants unless explicitly requested.
- Temple side is temple-first, not fortune-first: emphasize places, routes, worship/merit context, and trip planning over divination.
- Preserve the warm sacred visual system: warm paper background, lacquer red, restrained gold/yellow aura, jade/green support states, and deep brown/ink text.
- Use real/place imagery where possible. Use the muted auspicious placeholder only as fallback.
- Do not turn operational or data-dense pages into landing pages. Planner and directory pages need useful density.
- Preserve internal scroll containers and table/map dimensions unless the task explicitly changes them.
- Preserve card/list/detail journeys: search/filter -> compare -> detail/map/planner.
- Keep confidence/help UI honest and visitor-facing. Do not hide uncertainty by inventing data.
- Use the exact source text for the all-Thailand temple directory: `ระบบทะเบียนวัด สำนักงานพระพุทธศาสนาแห่งชาติ`.
- All-Thailand temple directory data must come from the provided `Report_Temple 2.numbers` source only unless the user explicitly changes direction. Do not scrape/export that data from websites.
- Admin Portal page registry/navigation is code-owned in `public/admin/content/live.json`; keep `default.json` in sync for the same page/nav entries.
- Bump `assetVersion` in `src/layouts/BaseLayout.astro` when changing public CSS/JS. Bump query strings in `public/styles.css` when imported CSS needs cache invalidation.
- Do not commit generated artifacts: `node_modules/`, `dist/`, `.astro/`, `.vercel/`, `outputs/`, root `preview-*.png`, `.DS_Store`.
- The project was moved out of iCloud; use `/Users/point/Website Projects/hora-astro` as the canonical working copy.

## Current Setup Commands

```bash
cd "/Users/point/Website Projects/hora-astro"
npm ci
npm run dev -- --host 127.0.0.1 --port 4324
npm run check
npm run build
npm run nfr:cms
npm run test:e2e
npm run test:visual
npm run smoke:production
```

Use targeted checks first, then broaden based on risk. `node_modules/`, `dist/`, and `.astro/` may be absent intentionally after cleanup; regenerate them as needed.

## Verification Defaults

- Before commit: run `git diff --check`, `npm run check`, and inspect `git status --short --branch`.
- Before deploy: run `npm run build`, then targeted smoke checks for touched routes.
- After deploy: smoke production on key route(s) plus touched route(s).
- Do not run full NFR/E2E on every small edit. Batch broader checks unless risk requires them.
- UI work should include at least one relevant desktop and mobile browser/screenshot pass.
- Map changes should verify Leaflet loads, markers render, no console errors, Thailand bounds are respected, and detail links work.

## Common Source Areas

- Shared layout/cache busting: `src/layouts/BaseLayout.astro`
- Home: `src/pages/index.astro`, `public/assets/css/home.css`, `public/assets/js/home-motion.js`, `public/assets/js/carousel.js`
- Header/footer/navigation: `src/components/Header.astro`, `src/components/Footer.astro`, `src/config/site.js`, `public/assets/js/navigation.js`
- Temple hub and collections: `src/pages/temples/index.astro`, `src/pages/temples/popular/index.astro`, `src/pages/temples/mu/index.astro`, `src/pages/temples/sacred/index.astro`
- Temple details: `src/pages/temples/popular/[slug].astro`, `src/pages/temples/mu/[slug].astro`, `src/pages/temples/sacred/[slug].astro`, `src/components/TempleDetail.astro`
- Temple data: `src/data/popular-temples.json`, `src/data/mu-temples.json`, `src/data/sacred-temples.json`, `src/data/temple-image-overrides.json`, `src/data/temple-page-banners.json`, `src/data/temple-visit-info.json`
- Thailand directory data and UX: `public/assets/data/temples-thailand.json`, `public/assets/js/temple-directory.js`
- Admin Portal API/content: `api/admin/**`, `public/admin/content/**`, `public/assets/js/admin-portal.js`, `public/assets/js/cms-runtime.js`
- Tests: `tests/e2e/**`
- Deployment/security: `vercel.json`, `.github/workflows/**`, `scripts/apply-vercel-firewall.mjs`, `scripts/smoke-production.mjs`

## New Chat Prompt Template

Use this when the user asks for a starter prompt:

```text
We are continuing the Mongkol Wela / hora-astro project at:
/Users/point/Website Projects/hora-astro

Before doing work, use $mongkol-new-chat and read current on-disk docs, not prior memory. Start with AGENTS.md, Architecture.md, Roadmap.md, README.md, and git status. Then read task-specific docs from /Users/point/.codex/skills/mongkol-new-chat/references/new-chat-context.md.

Important constraints:
- Use /Users/point/Website Projects/hora-astro as the canonical working copy.
- Preserve routes, journeys, data contracts, internal scroll containers, responsive constraints, and customized component geometry unless explicitly in scope.
- Keep the site Thai-first. For temple work, keep the product temple-first, practical, sacred, and not primarily horoscope/tarot.
- Do not commit, push, deploy, rollback, revert, remove, or delete unless explicitly asked in this current task.
- If a named skill is used, read its current on-disk SKILL.md first.
- UI work needs desktop/mobile browser or snapshot evidence.
- Rollback-like work must use $rollback-guardrail first.
- Release, commit, push, deploy, or handoff work must use $release-gate.
- Do not commit generated artifacts such as node_modules, dist, .astro, .vercel, outputs, preview PNGs, or .DS_Store.

After onboarding, summarize what you read and wait for my task unless I already gave one.
```
