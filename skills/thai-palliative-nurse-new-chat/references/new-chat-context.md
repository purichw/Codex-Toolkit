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

The canonical site is `https://thaipalliativenurse.vercel.app`. Production runs on
Vercel; localhost is development only. The private repository's canonical owner
and Vercel scope are recorded in `docs/DEPLOYMENT.md`. Revalidate remote/integration
state for a release rather than assuming a historical alias remains current.

## Find the owner before editing

| Requested area | Source owners | Read alongside |
| --- | --- | --- |
| Shared shell / navigation / overlays | `src/App.tsx`, `src/components/SiteHeader.tsx`, `SiteFooter.tsx`, `Brand.tsx` and their CSS | `docs/SHARED_COMPONENTS.md`, `docs/BLUE_SCHEME.md` |
| Home banner / mobile shortcuts / tracking strip | `src/components/HomeHero.tsx`, `useHorizontalSwipe.ts`, `TrackingPrompt.tsx`, `src/App.tsx`, `src/styles.css` | Shared UI hero/card contracts |
| Page banners / library cards / fields | `src/components/PageBanner.tsx`, `ResourceCard.tsx`, `SearchField.tsx`, `SelectField.tsx`, `CardHeading.tsx`, `SectionHeading.tsx` | Shared UI owner/consumer table |
| Seminars | `src/SeminarsPage.tsx`, `src/seminars-data.ts`, `src/seminars.css` | Project map seminar contract |
| Knowledge / news | `src/KnowledgePage.tsx`, `src/NewsPage.tsx`, corresponding data/CSS, `src/components/FeaturedCarousel.tsx` | Project map library contracts |
| Article / seminar details / sticky rail | `src/content-routes.ts`, `src/ContentDetailPage.tsx`, `src/components/DetailSection.tsx`, `src/content-detail.css` | Shared details contract; contextual wording and seminar-only blocks |
| About / contact | `src/AboutPage.tsx`, `src/about-data.ts`, `src/ContactPage.tsx`, associated CSS | Complete history and asset provenance in `docs/assets/` |
| Registration / SCB / attachments | `src/MembershipPage.tsx`, `src/membership-data.ts`, `src/membership.css`, `src/try-data.ts` | Project map membership contract; no upload/payment backend |
| Tracking forms / results / entry links | `src/TrackingPage.tsx`, `src/tracking-data.ts`, `src/tracking-routes.ts`, `TrackingVerificationForm.tsx`, `TrackingEmptyState.tsx` under `src/components/` | Shared tracking contract and `docs/TESTING.md` |
| Date field / picker / arrows | `src/components/BuddhistDateInput.tsx`, `buddhist-date-input.css`, `SelectField.tsx`, `controls.css`, `src/buddhist-date.ts` | Nested-dialog focus and date-specific tests |
| Buttons / font baseline | `src/components/button-typography.css`, `src/styles.css`, `src/page-readiness.ts` | Shared typography roles; server button mirrors metrics |
| Loading / orbit / image readiness | `index.html`, `src/page-readiness.ts`, `public/theme.css` | Shared readiness contract and Blue scheme |
| Access / session | `server/access.mjs`, `server/access-page.mjs`, `server/local-access.mjs`, `middleware.js` | `docs/ACCESS.md` before changes |
| Obfuscation / crawler / public files | `vite.config.ts`, `scripts/check-public-build.mjs`, `vercel.json`, `.vercelignore` | `docs/PROTECTION.md`; edge rules are separate from code |
| Push / deployment / rollback | `package.json`, `vercel.json`, selected Git remote | `docs/DEPLOYMENT.md`, `docs/HANDOFF.md`, `release-gate`; rollback requires its own decision |

## Current behavior to distinguish from old references

- Eight main routes: `/`, `/seminars`, `/about`, `/contact`, `/membership`,
  `/knowledge`, `/news`, `/tracking`; details use each collection's native ID
  route. `/access` and logout are server-owned, not member-account screens.
- The owner changed the old red scheme to Blue, replaced the logo with genuine
  transparent paths and unified navigation. Existing public design comes first.
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
