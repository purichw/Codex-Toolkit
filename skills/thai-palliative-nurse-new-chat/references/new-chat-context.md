# TPNA context routing

This guide locates current facts. It is not a release report. Resolve all
project-relative paths against the selected checkout/worktree; the default is
`/Users/point/Website Projects/thaipalliativenurse`.

## Required entry documents

1. `AGENTS.md` — repository constraints and source ownership.
2. `docs/HANDOFF.md` — dated runtime checkpoint, latest owner decisions and known
   limitations. Confirm local Git state; the checkpoint can age.
3. `README.md` — setup, service identity and documentation index.
4. `PROJECT_MAP.md` — current routes, interactions and source owners; read the
   relevant sections rather than historical evidence by default.

| App | Work directory | Vercel target | Runbook |
| --- | --- | --- | --- |
| Association | Repo root | `purich-w/thaipalliativenurse` at `https://thaipalliativenurse.vercel.app` | `docs/DEPLOYMENT.md` |
| Conference | `apps/tpna2569/` | `purich-w/tpna2569` at `https://tpna2569.vercel.app` | Verification and release in `docs/TPNA2569.md` |

Check the intended Git revision independently of the canonical Vercel domain.
Use the selected app's checkpoint in `docs/HANDOFF.md` for dated evidence.

## TPNA 2569 conference portal

Start with `docs/TPNA2569.md` for the route map and app contracts. The source
paths below are relative to `apps/tpna2569/`.

| Area | Owners and checks |
| --- | --- |
| Editorial content, fonts and routing | `public/content/conference.json`, `src/content-schema.mjs`, `src/startup.ts`, `src/page-loaders.ts` and `src/navigation.ts`. Keep the validated content and font readiness contract. |
| Shared controls and navigation | `src/components/ConferenceShell.tsx` and `conference-shell.css` own the shared DeepXWorks credit and sizing. `ActivityHeader.tsx` supplies the compact quiz and tree shortcuts. Keep game action heights in `Action` and its stylesheet. |
| Registration and account | `src/pages/ActivityEntry.tsx`, `shared/member-number.mjs`, `src/activity-entry.ts` and `src/membership-fixtures.ts`. Check the searchable prefix, custom category and member/guest field rules with `test:activity-entry`. The format check grants preview points. The event code is the server credential for rewards. |
| Game Zone and quiz | `src/pages/GameDashboard.tsx`, `KnowledgeGame.tsx`, `QuizResult.tsx` and `src/quiz/`. Check container width with the demo dock open. Use `test:activity-sequence` for prerequisites and `test:quiz-motion` for card transitions. |
| Comment tree | `src/comment-tree/`, `shared/comment-tree-rules.mjs` and `server/comment-tree.mjs` own 50–500 character validation, comment receipts, owner-first sorting and text-only edits. Use the service tests and `test:comment-tree`. |
| Rewards | `src/prize-wheel/` and `server/prize-wheel.mjs` own the blue draw, automatic raffle entry and gold invitation. Keep the booth coupon reference distinct from the raffle confirmation. Use `test:prize-wheel` or `test:gold-wheel`. |
| Demo and Admin | `src/demo/` owns same-tab controls and isolated fixtures. `src/admin/` owns the workspace with public-read and sample sources. The app README and `DEMO_QA.md` link the current contracts and dated checks. |

Use the portal README for setup. Use `?demo=0` on a full load to exercise the
regular flow in a demo-enabled build. On a release candidate or canonical domain,
exercise the UI with fictional demo state and use read-only live API probes.
Use the local API preview for service writes and receipt recovery.

## Association site owners

| Requested area | Source owners | Read alongside |
| --- | --- | --- |
| Editorial data / CMS read API / provider | `content/site.json`, `server/content-contract.mjs`, `content-slots.mjs`, `content-repository.mjs`, `content.mjs` under `server/`, `api/content.js`, `src/cms/` | `docs/CMS_ARCHITECTURE.md`; read API is implemented, CMS admin/write flows are not |
| Global / collection search | `src/cms/search.ts`, `SearchContent` in `src/App.tsx`, collection-page filter consumers | CMS search scope; private tracking remains separate |
| Shared shell / navigation / overlays | `src/App.tsx`, `src/components/SiteHeader.tsx`, `SiteFooter.tsx`, `Brand.tsx` and their CSS | `docs/SHARED_COMPONENTS.md`, `docs/BLUE_SCHEME.md` |
| Home banner / mobile shortcuts / tracking strip | `src/components/HomeHero.tsx`, `useHorizontalSwipe.ts`, `TrackingPrompt.tsx`, `src/App.tsx`, `src/styles.css` | Shared UI hero/card contracts |
| Page banners / library cards / fields | `src/components/PageBanner.tsx`, `ResourceCard.tsx`, `SearchField.tsx`, `SelectField.tsx`, `CardHeading.tsx`, `SectionHeading.tsx` | Shared UI owner/consumer table |
| Seminars | `src/SeminarsPage.tsx`, `src/seminars-data.ts`, `src/seminars.css` | Project map seminar contract |
| Seminar-7 Learning Hub / classroom | `LearningHubPage.tsx`, `LearningClassroom.tsx`, `learning-classroom.css`, `learning-routes.tsx`, `learning-progress.ts` and `useLearningProgress.ts` under `src/` | `docs/LEARNING_HUB.md`; course-level Pre/Post then feedback, browser-local progress and responsive classroom outline |
| YouTube player / seek prompt | `src/components/LearningVideo.tsx`, `LearningVideoDialog.tsx`, `src/learning-video.css`, `src/media/`, `server/youtube.mjs`, `api/youtube/status.js` | `docs/LEARNING_PROJECT_BOUNDARIES.md`; player-only Hospital parity in TPNA Blue, server-only status key, no auto-completion |
| Knowledge / news | `src/KnowledgePage.tsx`, `src/NewsPage.tsx`, corresponding data/CSS, `src/components/FeaturedCarousel.tsx` | Project map library contracts |
| Article / seminar details / sticky rail / TOC | `src/content-routes.ts`, `src/ContentDetailPage.tsx`, `src/components/DetailSection.tsx`, `src/content-detail.css`, pathname scroll guard in `src/App.tsx` | Shared details contract; native fragment/history behavior, contextual wording and seminar-only blocks |
| About / contact | `src/AboutPage.tsx`, `src/about-data.ts`, `src/ContactPage.tsx`, associated CSS | Complete history and asset provenance in `docs/assets/` |
| Registration / SCB / attachments | `src/MembershipPage.tsx`, `src/membership-data.ts`, `src/membership.css`, `src/try-data.ts` | Project map membership contract; no upload/payment backend |
| Tracking forms / results / entry links | `src/TrackingPage.tsx`, `src/tracking-data.ts`, `src/tracking-routes.ts`, `TrackingVerificationForm.tsx`, `TrackingEmptyState.tsx` under `src/components/` | Shared tracking contract and `docs/TESTING.md` |
| Date field / picker / arrows | `src/components/BuddhistDateInput.tsx`, `buddhist-date-input.css`, `SelectField.tsx`, `controls.css`, `src/buddhist-date.ts` | Nested-dialog focus and date-specific tests |
| Buttons / font baseline | `src/components/button-typography.css`, `src/components/control-fonts.css`, `src/fonts.css`, `src/styles.css` | Shared typography roles; font faces load before app JavaScript; server button mirrors metrics |
| Loading / orbit / image readiness | `index.html`, `src/fonts.css`, `src/main.tsx`, `src/page-readiness.ts`, `public/theme.css` | Shared readiness contract and Blue scheme; `readiness-smoke.mjs` and `readiness-viewport-smoke.mjs` under `scripts/` |
| Access / session | `server/access.mjs`, `server/access-page.mjs`, `server/local-access.mjs`, `middleware.js` | `docs/ACCESS.md` before changes |
| Obfuscation / crawler / public files | `vite.config.ts`, `scripts/check-public-build.mjs`, `vercel.json`, `.vercelignore` | `docs/PROTECTION.md`; edge rules are separate from code |
| Push / deployment / rollback | `package.json`, `vercel.json`, selected Git remote | `docs/DEPLOYMENT.md`, `docs/HANDOFF.md`, `release-gate`; rollback requires its own decision |

## Current behavior to distinguish from old references

- Eight main routes: `/`, `/seminars`, `/about`, `/contact`, `/membership`,
  `/knowledge`, `/news`, `/tracking`; details use each collection's native ID
  route. `/access` and logout are server-owned, not member-account screens.
- The owner changed the old red scheme to Blue, replaced the logo with genuine
  transparent paths and unified navigation. Existing public design comes first.
- Page copy, branding/contact settings, fees, curation and editorial detail
  sections come from one validated published snapshot per document load. Data
  modules are selectors. Do not revive hardcoded duplicates or a stale fixture
  fallback on content failure. CMS editing UI/database/staff roles are planned.
- Search shares Unicode/case/whitespace normalization and requires all query
  words across editorial text, including details and speakers. It does not yet
  provide typo tolerance, ranking, PDF-content or private-record search.
- HTML prepares loader fonts/emblem without waiting for CMS or React. Foreground
  orbit/text/progress reveal as one unit with actual fonts. External entry and
  reload retain the three-second minimum plus real readiness; fast internal
  links have none. The loader and retry fit the viewport without scrolling,
  including short landscape, and normal page scrolling returns after readiness.
- Same-page TOC and history fragments must reach their section without a reset
  to the page top. Only pathname changes trigger the app's scroll reset; initial
  document fragments wait for readiness. The sticky rail owns a separate column.
- Tracking removed All and name-only search. Membership is one-to-one with no
  count; event personal lookup can return several records. `Track No.` is the
  visible wording. Only category goes into the URL; the completion handoff is
  transient memory, not query parameters or persistent state.
- The date picker must not fall back to device-native Gregorian formatting.
  Day/month/year selects share `SelectField`; its popup portals into an enclosing
  native dialog, otherwise the body. Escape closes the inner popup first.
- Local fixtures and success/fail states are permitted. Empty decorative text
  lines and UI notices announcing mock/design-review status are not wanted.
  This approval is not backend authorization or official factual verification.
- Do not transplant the reference site's brand or domain logic. CoverMate and
  Mongkol Wela informed proportions/controls; Korat shared-component guidance
  informed reuse. TPNA owns its own UI and content contracts.

## Setup, checks and evidence

Use Node 24.x and current scripts in `package.json`. Local setup is documented
in `README.md` and `docs/ACCESS.md`; testing commands and prerequisites are in
`docs/TESTING.md`. Never print `.env*`, credential stores or session tokens.

`docs/references/` holds unchanged supplied designs; `docs/assets/` holds sources
and provenance; `public/images/` holds optimized runtime assets. Generated
`dist/` is not an edit target. `docs/qa/` is dated evidence, while
`docs/qa/release/` is ignored and may be absent in a new checkout.

Docs/onboarding need no production login, build or whole-site audit. A visible
change needs a current contextual render. A shared-control change needs the
highest-risk consumer and an ordinary peer. Do not repeat broad suites after
those pass unless new evidence widens scope. Report exactly what was checked.

## When handing off

Update `docs/HANDOFF.md` for a material checkpoint, `PROJECT_MAP.md` for changed
routes/data flow, and `docs/SHARED_COMPONENTS.md` for changed shared contracts.
Keep detailed deployment evidence local and compact; do not create a second
release merely to document the first. If asked to prepare another chat's prompt,
follow the shared New Chat template without actually opening or reading a chat.
