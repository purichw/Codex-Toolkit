---
name: thai-palliative-nurse-new-chat
description: Onboard or refresh work on the Thai Palliative Nurse association site or TPNA 2569 conference portal. Use for TPNA handoffs, setup, documentation sync, or a new-chat prompt, including the conference activities and Demo Control Center.
---

# Thai Palliative Nurse New Chat

Make the next TPNA task usable from current files, without depending on the old
conversation. This skill onboards the current chat; it does not create, read,
monitor or delegate to another chat.

## Bounded intake

1. Prefer the user's selected checkout/worktree. Otherwise start at
   `/Users/point/Website Projects/thaipalliativenurse` and verify the repo and
   revision against the task. For conference work, confirm the checkout contains
   `apps/tpna2569/`. Use verified Git revisions or an existing up-to-date
   worktree to read newer docs when the primary checkout is behind. Preserve
   pending work in each checkout.
2. Read its `AGENTS.md` and run `git status --short --branch`. Preserve unrelated
   changes. Read `docs/HANDOFF.md`, `README.md` and the relevant sections of
   `PROJECT_MAP.md`.
3. Read `/Users/point/.codex/skills/project-onboarding/SKILL.md` and this skill's
   [context routing guide](references/new-chat-context.md). Load only documents
   needed for the current task. Do not scan old chat histories or every QA image.
4. Distinguish current source, dated verification, original mockups and missing
   evidence. Latest explicit owner decisions win; reconcile stale documentation
   with source rather than reinstating obsolete UI.
5. Briefly state the current scope and relevant constraints, then perform the
   supplied task. If only orientation was requested, summarize and wait.

## Choose the application

- For TPNA 2569, the conference URL, Game Zone, Demo Control Center or its Admin
  workspace, work in `apps/tpna2569/`. Start with its section in
  `docs/HANDOFF.md` and the relevant `docs/TPNA2569.md` contract. Choose the
  Demo Control Center for tab-local UI review or the local API fixture for
  verified event-code behavior.
- The association site's CMS, tracking, content pages, Learning Hub and access
  gate use the repository-root app and the contracts below. Its Vercel project,
  production checkpoint and auth boundary are separate from the conference portal.

## Association site

- Use TPNA Blue from `public/theme.css` and `docs/BLUE_SCHEME.md`; do not install
  generic fallback tokens or restore the old red palette. Transparent vector
  logos share one owner, with a white footer treatment for contrast.
- Read `docs/SHARED_COMPONENTS.md` before changing reused UI. Navigation,
  banners, fields, cards, actions, date picker and detail layout must remain
  consistent. Scope genuine page differences through variants, not copies.
- Read `docs/CMS_ARCHITECTURE.md` for editorial changes. `content/site.json` or
  the configured HTTPS provider supplies a validated published revision through
  `/api/content`; `src/cms/` owns the snapshot and shared search. Data modules
  select this content, not duplicate it. CMS administration and transactional
  member/registration APIs remain future work, separate from public content.
- Tracking has two categories, hidden-until-search results and no personal data
  in URLs/storage. Birth dates use fixed DD/MM/YYYY Buddhist years, no visible
  era suffix, 48px fields and the shared dialog-safe dropdown. The membership
  application-number label/value are centered; ordinary text fields stay left.
- Real server access is separate from local trial forms/data. Do not claim that
  a simulated success creates a member, sends mail, uploads files or verifies a
  payment. The owner permits populated fixtures without visitor-facing mock
  notices. Keep consent unchecked and the implementation boundary documented.
- Loading fonts/artwork start from HTML independently of CMS/React. Reveal orbit,
  actual-font text and progress together; preserve valid content/font/image
  gating, the initial three-second minimum and fast internal navigation. Fit
  loading and error/retry within the viewport without scrolling; restore normal
  scroll after readiness. Compact decoration first and keep gentle motion.
- Preserve hero swipe/autoplay/pause and upper-right controls that add no banner
  height. Keep detail content beside its rail. Same-page TOC/hash navigation must
  not reset to the top; `App.tsx` resets scroll only when the pathname changes.
- Preserve the complete About history, sourced founder portraits and confirmed
  bank details. Never fill space with meaningless placeholder lines.

## Learning Hub and related-project boundary

For seminar-7 learning work, read `docs/LEARNING_HUB.md` and
`docs/LEARNING_PROJECT_BOUNDARIES.md`. Overview/classroom share TPNA's own
`learning-progress.ts` / `useLearningProgress` state. Preserve course Pre-test →
ordered lessons → Post-test → learning-experience feedback; do not replace the
feedback with Hospital's scored Final Assessment. Seek notices are advisory,
not watched-time completion or real CNEU issuance.

Hospital E-Learning is a reference project, not TPNA's layout/design-system
owner. Preserve TPNA's 1200px container, Blue theme, header/footer and shared
components. The owner-approved narrow exception is video-player framing,
controls and illustrated seek popup, adapted to TPNA colors. The two repositories
have no runtime dependency or automatic synchronization. The shared YouTube key
is server-only with separate env names/auth/allowlists; no learner/session data
is shared. Related-project context does not authorize edits, releases or access
to other chats. Consult each project's source/release evidence independently.
When the request explicitly covers both products, verify each equivalent
implementation in its own app.

## Work and verification

Use `ui-ux-expert` for visible design, `mockup-to-product` for supplied mockups,
and `snapshot` for current visual evidence. Use `docs-cartographer` when project
maps or contracts change. Read each named skill when applying it; do not apply
every specialist to a tiny edit.

Follow `docs/TESTING.md` at the smallest appropriate risk tier. Docs-only work
needs path/link/metadata checks, not a build or screenshots. Shared controls need
affected-consumer and interaction checks. Release work uses `release-gate` and
the selected app's runbook with current target and source evidence. Use
`docs/DEPLOYMENT.md` for the association site or the release section of
`docs/TPNA2569.md` for the conference portal.

Never treat onboarding, a handoff, a historical approval or passing checks as
permission to commit, push, deploy, change firewall policy, roll back, delete
files or access another chat. Continue actions explicitly authorized for the
current scope without asking again. Check whether a push auto-deploys before a
release; track push, checks, build and domain promotion separately.

Do not expose secrets/session cookies or copy access credentials into handoff
prompts. Deploy the project with its server boundary, never `dist/` alone.

## Starter prompts and maintenance

When asked for a new-chat prompt, read
`/Users/point/.codex/skills/project-onboarding/references/new-chat-template.md`.
Include `$thai-palliative-nurse-new-chat`, the absolute selected checkout, the
specific next task, required read order, key constraints and any documented
remaining work. Keep it copyable and concise; do not invent a pending task or
grant release authorization. Creating a prompt does not create a chat.

The versioned source is `skills/thai-palliative-nurse-new-chat/` in the project;
the installed copy is `/Users/point/.codex/skills/thai-palliative-nurse-new-chat/`.
When updating this skill, keep both copies identical and validate with the
skill-creator validator. Keep deployment SHAs, test results and coverage limits
in the selected app's checkpoint in `docs/HANDOFF.md`. Put stable behavior in
its contract docs. Check link targets and command names after a documentation
sync.
