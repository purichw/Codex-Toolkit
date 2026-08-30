# CoverMate New Chat Context

Use this as the pickup map for a fresh Codex chat. Prefer current on-disk files over memory from any prior thread.

## Project

- Repo: `/Users/point/CoverMate`
- Production: `https://covermate.vercel.app`
- GitHub: `https://github.com/purichw/CoverMate`
- Vercel project: `covermate`
- Stack: static Vercel site, Firebase Auth, Firestore CMS/lead storage, GA4 client analytics, Vercel serverless APIs, Playwright smoke, and localStorage fallback/session caches.
- Product: Thai/English CoverMate insurance advisor visitor site plus private owner admin/CMS and analytics surfaces.
- Admin auth: Firebase Google sign-in plus Firestore `admins/{uid}` with `active: true`.
- CMS state: Firestore-first under `sites/covermate/*`; browser localStorage is only a last-known fallback cache.

## Read Order

Always start with:

1. `/Users/point/CoverMate/README.md`
2. `/Users/point/CoverMate/PROJECT_MAP.md`
3. `/Users/point/CoverMate/docs/ADMIN_CMS_REBUILD_DECISIONS.md`
4. `/Users/point/CoverMate/docs/HANDOFF.md`
5. `/Users/point/CoverMate/docs/RELEASE_RUNBOOK.md`

Then choose by task:

- Architecture/routes/data ownership: `docs/ARCHITECTURE.md`, `docs/SITE_MAP.md`, `docs/DATA_CONTRACT.md`
- Visitor/admin interactions: `docs/INTERACTION_MAP.md`, `docs/NON_FUNCTIONAL_REQUIREMENTS.md`
- Firebase/auth/rules/CMS persistence: `docs/FIREBASE_SETUP.md`, `docs/DATA_CONTRACT.md`, `firestore.rules`, `covermate-firebase.js`, `covermate-contract.js`
- Analytics/lead reporting: `docs/ANALYTICS.md`, `admin/analytics/index.html`, `admin/analytics-data.js`, `covermate-analytics.js`
- SEO/crawler/social: `docs/SEO.md`, `robots.txt`, `sitemap.xml`, `vercel.json`, `site.webmanifest`
- UI/visual design/assets: `docs/DESIGN_ASSETS.md`, `docs/covermate-website-full-design-spec.md`, `organic.css`, `assets/`, current snapshots under `docs/snapshots/`
- External prototypes, SPEC files, or handoff packages: read the user-provided files only after the current product docs above, and reconcile them against accepted product decisions before implementing
- QA/release: `package.json`, `scripts/validate-bundles.mjs`, `scripts/smoke.mjs`, `docs/RELEASE_RUNBOOK.md`
- Admin/CMS operations: `docs/ADMIN_CMS_REBUILD_DECISIONS.md`, `docs/INTERACTION_MAP.md`, `docs/DATA_CONTRACT.md`, `admin/index.html`, `index.html`, `covermate-firebase.js`

## Skills To Use

Use the current on-disk `SKILL.md` each time a skill is invoked.

- New-chat onboarding: `$covermate-new-chat`
- CoverMate design/spec maintenance: `$covermate-design-spec`
- UI/UX routing and broad UX judgment: `$ui-ux-orchestrator`, `$ui-ux-expert`
- Screenshots/snapshots: `$snapshot`
- Release readiness: `$release-gate`
- Efficient batching: `$efficient-execution`
- Regression hunting: `$regression-hunter`, `$global-regression-hunter`
- Docs maps: `$docs-cartographer`
- Rollback/revert/remove/undo guard: `$rollback-guardrail`
- Admin operations: `$admin-ops`, `$admin-prototype-reconciliation`
- Firebase auth/rules: `$firebase-account-management`, `$firebase-security-rules`
- Mobile/responsive QA: `$mobile-web-qa`
- Interaction/browser QA: `$interaction-flow-qa`
- Forms: `$form-flow-ux`
- Accessibility: `$accessible-interaction`, `$accessibility-beyond-basics`
- SEO/social asset smoke: `$production-asset-smoke`, `$prod-smoke-harness`

## Durable Product Rules

- Do not commit, push, deploy, rollback, revert, or remove unless explicitly asked in the current task.
- Production implementation, current docs, and Firestore live/draft data prevail over older external prototypes, SPEC files, or exports.
- New SPEC/html/handoff references are inputs to reconcile, not automatic source of truth. Preserve accepted Product Decisions unless the owner explicitly changes them.
- Any prototype/export that renders raw `{{ ... }}`, `sc-if`, `sc-for`, `x-dc`, or `[object Object]` is incomplete and not a portable implementation target.
- `/` is the public home page. `/motor` is the dedicated motor-insurance campaign page inside the same CoverMate product. `/#motor` is only a legacy same-page alias to the home motor/insurer area.
- `/admin/login`, `/admin`, `/admin/ops`, `/admin/analytics`, `/admin/content`, `/admin/edit`, `/admin/preview`, and owner hash modes are private admin routes/states and must stay `noindex`.
- `/admin` is the Admin Portal Home and must remain reachable after sign-in.
- The Admin Portal primary modules are `Operations`, `Website content`, `Analytics`, and `Settings`.
- Website content has one main editor entry. Do not reintroduce a separate `Arrange & customise` launcher card; open the control panel from the editor via `Tools -> Panel`.
- The control panel/shell must not leak into clean public routes.
- Owner modes are `/#edit`, `/#admin`, `/#preview`, plus direct admin routes `/admin/content`, `/admin/edit`, and `/admin/preview`; clean public visitor routes must not show owner chrome even when an admin session exists.
- `Public site` / `View live site` opens a clean public route in a new tab and does not move the current Admin tab. Legacy `/?view=public` may be consumed for compatibility but must not be generated by new UI.
- `/#preview` is a private draft render with one top bar only. It requests draft/version hydration before owner-hash rendering, does not write the legacy owner marker, and exposes `Open editor`, `Public site`, and `Publish`. Do not show a dock, drawer, screen switcher, or owner reopen bar there.
- Visible admin chrome labels are English-only: `Panel`, `Edit text`, `Main`, `Public site`, `Save draft`, `Preview`, `Publish`, `Success`, `Log out`.
- Save draft and Publish use custom confirmation dialogs, progress/success feedback, dismissible toasts, and a 30-second Undo window.
- Firestore live/draft data must prevail over hard-coded or local fallback content. Fallbacks may fill missing structure only; they must not override successful remote reads.
- Insurer-count copy follows the active `insurers.items` logo data. With the current committed logo set, the count is `14`.
- All visible visitor and admin text uses the Google Sans family stack across Thai and English unless a heading/logo exception is an explicit design choice.
- Supported editable images should behave like CMS-managed content, not plain pasted image URLs, where the implementation supports it.
- UI changes need snapshot evidence in the final handoff; snapshot outputs should be shown in chat when the snapshot skill is used.

## Current Admin/CMS Status

- `/admin` is the shared Admin Portal Home with Operations, Website content,
  Analytics, and Settings.
- `/admin/content?page=home|motor` opens the owner control panel for section
  order, visibility, structured content, brand/contact, theme/data, and
  versions.
- `/admin/edit?page=home|motor` opens inline editing over the matching visitor
  page. Inline editing and the control panel can coexist; closing the panel
  keeps the editor route and dock active.
- `/#preview` and `/admin/preview?page=home|motor` are draft-only previews with
  one preview bar.
- `/motor` is live as the dedicated motor visitor page; `/` remains the full
  home page.

## Current Setup Commands

```bash
cd "/Users/point/CoverMate"
npm install
node --input-type=module -e 'import { startStaticServer } from "./scripts/lib/static-server.mjs"; const { server, baseUrl } = await startStaticServer({ ownerRoutesToRoot: true }); console.log(baseUrl); process.stdin.resume();'
npm run check:bundles
npm run smoke
COVERMATE_URL=https://covermate.vercel.app npm run smoke
```

Use targeted checks first, then broaden based on risk. The key local release checks are:

```bash
npm run check:bundles
npm run smoke
git diff --check
```

Deploy only when explicitly asked:

```bash
git push origin main
vercel --prod --yes
```

## Common Source Areas

- Visitor/admin owner bundle: `index.html`
- Admin login: `admin/login/index.html`
- Admin Portal: `admin/index.html`
- Admin analytics: `admin/analytics/index.html`, `admin/analytics-data.js`
- Shared admin session helper: `admin/session.js`
- Runtime contracts and storage keys: `covermate-contract.js`
- Firebase Auth/Firestore/CMS/leads: `covermate-firebase.js`, `firestore.rules`, `firebase.json`
- GA4 visitor analytics: `covermate-analytics.js`
- Smoke and bundle validation: `scripts/smoke.mjs`, `scripts/validate-bundles.mjs`
- SEO/static metadata: `robots.txt`, `sitemap.xml`, `site.webmanifest`, `vercel.json`, `assets/covermate-og.*`
- Insurer assets: `assets/ins/*.png`
- Brand/proof logos: `assets/logos/*`
- Design/reference CSS: `organic.css`
- Current docs: `PROJECT_MAP.md`, `README.md`, `docs/*.md`

## New Chat Prompt Template

Use this when the user asks for a starter prompt:

```text
We are continuing the CoverMate project at:
/Users/point/CoverMate

Before doing work, use $covermate-new-chat and read current on-disk docs, not prior memory. Start with README.md, PROJECT_MAP.md, docs/ADMIN_CMS_REBUILD_DECISIONS.md, docs/HANDOFF.md, and docs/RELEASE_RUNBOOK.md. Then read task-specific docs from /Users/point/.codex/skills/covermate-new-chat/references/new-chat-context.md.

Important constraints:
- Production repo files, current docs, and Firestore live CMS state prevail over older external prototypes/exports unless I explicitly reopen a Product Decision.
- Do not commit, push, deploy, rollback, revert, remove, or undo unless I explicitly ask in this current task.
- Preserve routes, Firebase/Firestore contracts, localStorage keys, noindex boundaries, admin session behavior, responsive constraints, and owner-mode UI contracts unless explicitly in scope.
- If a named skill is used, read its current on-disk SKILL.md first.
- UI work needs snapshot evidence in the final handoff.
- Release work must use $release-gate; rollback-like work must use $rollback-guardrail first.
- Treat docs/ADMIN_CMS_REBUILD_DECISIONS.md as the current admin/CMS decision authority. `/admin` is the Admin Portal Home with Operations, Website content, Analytics, and Settings. Website content has one editor entry; open the panel from `Tools -> Panel`.
- `Public site` opens a clean public route in a new tab and must not move the current Admin tab. Do not generate `/?view=public`.
- Firestore live/draft data must prevail over hard-coded and local fallback content.

After onboarding, summarize what you read and wait for my task unless I already gave one.
```
