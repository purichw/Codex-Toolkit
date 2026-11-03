---
name: thai-palliative-nurse-new-chat
description: Onboard or refresh context for the Thai Palliative Nurse / TPNA website. Use for a new-chat prompt, project handoff, required reading, setup, or documentation sync before continuing TPNA page, shared-component, tracking, access, or release work.
---

# Thai Palliative Nurse New Chat

Make the next TPNA task usable from current files, without depending on the old
conversation. This skill onboards the current chat; it does not create, read,
monitor or delegate to another chat.

## Bounded intake

1. Prefer the user's selected checkout/worktree. Otherwise use
   `/Users/point/Website Projects/thaipalliativenurse`. Verify the directory and
   repository identity before edits; do not clone or switch branches by default.
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

## Preserve the product

- Use TPNA Blue from `public/theme.css` and `docs/BLUE_SCHEME.md`; do not install
  generic fallback tokens or restore the old red palette. Transparent vector
  logos share one owner, with a white footer treatment for contrast.
- Read `docs/SHARED_COMPONENTS.md` before changing reused UI. Navigation,
  banners, fields, cards, actions, date picker and detail layout must remain
  consistent. Scope genuine page differences through variants, not copies.
- Tracking has two categories, hidden-until-search results and no personal data
  in URLs/storage. Birth dates use fixed DD/MM/YYYY Buddhist years, no visible
  era suffix, 48px fields and the shared dialog-safe dropdown. The membership
  application-number label/value are centered; ordinary text fields stay left.
- Real server access is separate from local trial forms/data. Do not claim that
  a simulated success creates a member, sends mail, uploads files or verifies a
  payment. The owner permits populated fixtures without visitor-facing mock
  notices. Keep consent unchecked and the implementation boundary documented.
- Preserve real font/image readiness, initial three-second loading introduction,
  fast internal navigation, gentle loading motion, hero swipe/autoplay/pause and
  mobile controls that add no banner height. Keep detail content beside its rail.
- Preserve the complete About history, sourced founder portraits and confirmed
  bank details. Never fill space with meaningless placeholder lines.

## Work and verification

Use `ui-ux-expert` for visible design, `mockup-to-product` for supplied mockups,
and `snapshot` for current visual evidence. Use `docs-cartographer` when project
maps or contracts change. Read each named skill when applying it; do not apply
every specialist to a tiny edit.

Follow `docs/TESTING.md` at the smallest appropriate risk tier. Docs-only work
needs path/link/metadata checks, not a build or screenshots. Shared controls need
affected-consumer and interaction checks. Release work uses `release-gate` and
`docs/DEPLOYMENT.md`, with current target and source evidence.

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
skill-creator validator. Keep changing deployment SHAs, test results and open
work in `docs/HANDOFF.md`, not in skill metadata. Update only docs affected by the
task, clearly distinguishing local state from verified production.
