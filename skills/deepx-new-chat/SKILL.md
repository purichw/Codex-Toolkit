---
name: deepx-new-chat
description: "Onboard or refresh context for the DeepX website and Content Studio CMS. Use for DeepX new-chat or handoff prompts, required reading, project documentation updates, or context pickup before UI, CMS, Supabase, domain or Vercel release work."
---

# DeepX New Chat

Prepare the current chat to work on DeepX using the actual checkout and current
project documentation. A request for this skill or a starter prompt does not
authorize creating or inspecting another chat.

## Start here

1. Use the current task's selected DeepX checkout/worktree. The primary checkout
   is `/Users/point/Website Projects/DeepX`; use it only when no checkout is
   already selected. Confirm the remote is `https://github.com/purichw/DeepX`.
2. Run `git status --short --branch` before edits. Preserve unrelated changes.
3. Read the current `/Users/point/.codex/skills/project-onboarding/SKILL.md` and
   this skill's [project context](references/new-chat-context.md).
4. Read `AGENTS.md`, `README.md`, `docs/PROJECT_MAP.md`, `docs/CMS.md`, and the
   latest summary plus task-relevant section of `docs/RELEASE.md` in the selected
   checkout. Then read only the source owners needed for the user's task.
5. Reconcile conflicts using current source, the latest explicit user decision,
   and dated evidence. Earlier entries in the chronological release log describe
   superseded layouts; they must not silently undo later corrections. Historical
   release notes are not proof that production is currently healthy.
6. Briefly summarize relevant status and proceed with the requested work. If no
   work was specified, report readiness without inventing changes or a release.

## Preserve the owner's decisions

- Retain the established DeepX navy/cyan visual system and Thai-first content.
  Load `/Users/point/.codex/skills/ui-ux-expert/SKILL.md` for UI work; follow the
  repo's mockup guidance while giving newer explicit decisions priority.
- **Desktop is approved: do not redesign it or let mobile fixes change it.**
  Mobile hero video stays behind the banner copy/actions, with the central logo
  and DeepX wordmark visible. Never move it into a separate media panel.
- Keep Our Ecosystem, SUT before Chula, and the CMS-owned logo order/assets.
  The current mobile ticker moves left-to-right without Play/Pause controls;
  desktop/tablet retain their original layout. Details are in the reference.
- Business copy, navigation, media, contact details and metadata are CMS-owned.
  Do not hardcode them or restore cleared content from the bootstrap fixture.
- Preserve guarded CMS writes, published-only reads, revision conflicts,
  atomic publication and authentication/allowlist boundaries.

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
