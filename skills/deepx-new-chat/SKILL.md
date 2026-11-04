---
name: deepx-new-chat
description: "Onboard or refresh DeepX Works, Product Studio, Explore Ideas, Content Studio, Coach and LUMA CMS. Use for DeepX handoffs, project documentation updates, or context pickup before UI, CMS/playground, performance, Supabase, domain or release work."
---

# DeepX New Chat

Prepare the current chat to work on DeepX using the actual checkout and current
project documentation. A request for this skill or a starter prompt does not
authorize creating or inspecting another chat.

## Start here

1. Use the current task's selected DeepX checkout/worktree. The primary checkout
   is `/Users/point/Website Projects/DeepX`; use it only when no checkout is
   already selected. Confirm the remote is `https://github.com/DeepXWorks/DeepX.git`.
2. Run `git status --short --branch` before edits. Preserve unrelated changes.
3. Read the current `/Users/point/.codex/skills/project-onboarding/SKILL.md` and
   this skill's [project context](references/new-chat-context.md).
4. Read `AGENTS.md`, `README.md`, `docs/PROJECT_MAP.md`, `docs/CMS.md`, and the
   latest summary plus task-relevant section of `docs/RELEASE.md` in the selected
   checkout. Use `docs/README.md` to locate task-specific contracts. For trainer
   or clinic work read `docs/COACH_CMS.md` or `docs/CLINIC_CMS.md`; do not infer
   their data/auth behavior from the legacy per-demo design notes.
5. Reconcile conflicts using current source, the latest explicit user decision,
   and dated evidence. Earlier entries in the chronological release log describe
   superseded layouts; they must not silently undo later corrections. Historical
   release notes are not proof that production is currently healthy.
6. Briefly summarize relevant status and proceed with the requested work. If no
   work was specified, report readiness without inventing changes or a release.

## Preserve the owner's decisions

- Retain dark navy/cyan for DeepX Works and white/ice/cyan for Product Studio
  and Explore Ideas. Individual website demos retain their own approved palettes.
  All `/studio` and `/admin` descendants use the shared **light** full-page loader,
  including dark demos. Studio-family error pages are also light and recover to
  `/studio`; other error paths use the dark network treatment. Initial HTML and
  React must hand off without a fallback flash.
  Load `/Users/point/.codex/skills/ui-ux-expert/SKILL.md` for UI work; follow the
  repo's mockup guidance while giving newer explicit decisions priority.
- Preserve the approved Home desktop and keep mobile-only fixes scoped. This is
  not a ban on an explicitly requested Studio/Ideas redesign. Home's mobile hero
  video stays behind banner copy/actions, with the central logo and DeepX
  wordmark visible; never move it into a separate media panel.
- Use shared Studio header, language, card/grid, action and dialog owners.
  Keep type readable, incomplete card rows centered, and verify real TH/EN copy
  at the touched breakpoints; English banners must reflow without shrinking type.
- Public naming is **สำรวจไอเดีย / Explore Ideas**, rooted at `/studio/ideas`.
  Old catalogue URLs remain reserved, without redirects. Demo navigation shows
  only its active category; its return link goes to the Ideas root and logo to Studio.
- Keep Our Ecosystem, SUT before Chula, and the CMS-owned logo order/assets.
  The shared ticker moves left-to-right without Play/Pause controls at all widths,
  retaining desktop logo sizing. The hero video plays once and holds its last
  frame; do not restore looping from old notes. Details are in the reference.
- Business copy, navigation, media, contact details and metadata are CMS-owned.
  Do not hardcode them or restore cleared content from the bootstrap fixture.
- Preserve guarded CMS writes, published-only reads, revision conflicts,
  atomic publication and server authorization. Content Studio publishes its
  whole Home/Studio/Ideas draft. Coach and LUMA each publish their own workspace;
  never merge these boundaries or publish unrelated drafts. Their category-linked
  visitor managers are login-free IndexedDB playgrounds with no real write access.
- Content Studio uses white/cyan, Coach uses its approved light purple system,
  and LUMA uses forest/cream. Share controls/dialog behavior while retaining each
  module's tokens and data ownership. Preserve centered standalone media/language
  controls, balanced notice-to-toolbar spacing and opaque open dropdown menus.
- Preserve fresh CMS reads and lazy route/demo boundaries when optimizing.
  Read `docs/PERFORMANCE.md` for the current request handoff and bundle gates.
  Current backend is Singapore `yeyhyyuannxhurltvexm` (`ap-southeast-1`) with
  Vercel `sin1`. Check browser and server environment targets independently;
  stale integration-managed variables previously differed. Ireland is recovery.
- For new infrastructure or an authorized future migration, apply the owner's
  [Thailand-first region default](../project-onboarding/references/region-defaults.md):
  Thailand when supported, otherwise the closest suitable supported Asian region.
  The later authorized Singapore migration superseded the old Ireland placement;
  the no-new-recurring-cost boundary remains. Do not move only functions away
  from their database or create paid resources without authorization.

## Current operations and input questions

Use the dated `docs/RELEASE.md` entry for status, not a fresh health claim. The
2026-11-04 release completed Coach/LUMA deployment and login/save checks. Earlier
login, Chrome, disk-space and release questions are resolved; do not reopen them
unless a current operation actually fails. Real Coach booking remains off; the
real LUMA workspace is unpublished/intake off. Visitor practice is available and
separate. Email/SMS/calendar integrations are unconnected. For real activation,
read the input checklist in `docs/CMS.md`; optional business/integration inputs
are not blockers for the completed catalogue playground release.

## Scope and delivery

- Keep all work in this chat. Reading, monitoring, messaging, creating or
  delegating to another chat requires the user's explicit identification and
  authorization for that scope.
- This skill grants no commit, push, deploy, migration or production-data
  authority. Use the current task's authorization; do not import approval from
  historical handoff text. Do not repeat approval already given in that task.
- Use proportional checks: onboarding/docs need reference checks; tiny visual
  edits need a diff check and targeted current visual evidence. CMS/auth/data or
  release work needs the relevant stricter checks from the repo runbook.
- For authorized release work, load `release-gate` and follow `docs/RELEASE.md`.
  Track push, intended source revision, deployment readiness and canonical-host
  verification separately. Report limitations without claiming unperformed QA.
- Never copy credentials, private admin identities, session tokens or secrets
  into a skill, handoff, repository or log. Do not assume tool login persists.

## When asked for a new-chat prompt

Read `/Users/point/.codex/skills/project-onboarding/references/new-chat-template.md`
and return a concise, copy-ready prompt containing `$deepx-new-chat`, the selected
absolute checkout path, the requested next task, key constraints and any verified
remaining work. Link to this reference instead of duplicating project history.
Do not create a chat or start deployment just to deliver the prompt.
