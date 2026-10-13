---
name: mongkol-new-chat
description: Onboard or refresh project context for Mongkol Wela / hora-astro. Use for new-chat or handoff prompts, project documentation/skill updates, required reading, or context pickup before temple, place URL, admin/CMS, Tarot editorial research, QA, or release work.
---

# Mongkol New Chat

## Purpose

Prepare a fresh Codex chat to work safely on Mongkol Wela without relying on stale conversation memory. This skill is an onboarding router: read the current on-disk docs and skill files, then produce a concise starter prompt or context checklist for the next chat.

## Workflow

1. Use the current task's selected checkout/worktree. The primary checkout is a
   fallback location, not an instruction to leave an active worktree:

```text
/Users/point/Website Projects/hora-astro
```

2. Inspect status in that selected checkout before edits:

```bash
git status --short --branch
```

3. Read the shared new-chat shape:
   `/Users/point/.codex/skills/project-onboarding/references/new-chat-template.md`.
4. Read `references/new-chat-context.md` from this skill.
5. Read only task-relevant project docs and source owners from the reference.
   Treat dated release notes as historical evidence, not a fresh production check.
6. If the user asks for a prompt, return a copy-ready prompt for a new chat. If the user asks to continue work, summarize what was read and proceed with the relevant task.
7. For documentation updates, reconcile claims against source and dated evidence;
   keep project facts in project docs and the reference, not global design skills.

## Required Discipline

- Use current on-disk skill files when a skill is named. Do not rely on older remembered skill behavior.
- A starter prompt does not authorize creating, reading, monitoring or messaging
  another chat. Stay in the current chat unless the user explicitly identifies
  and authorizes the other task and scope.
- Do not commit, push, deploy, rollback, revert, remove, or delete work unless the user explicitly asks in the current task.
- Preserve routes, journeys, internal scroll containers, permissions, form behavior, data contracts, responsive constraints, and customized component geometry unless the task explicitly changes them.
- Keep the site Thai-first. Approved English/romanized place URL slugs are not
  English locale pages; preserve those URLs, aliases and stable CMS/planner keys.
- Published CMS content is authoritative; bundled JSON is bootstrap, not failover.
  A research prompt/proposed schema is not completed content or CMS support.
- Use proportional verification. Documentation-only changes need reference and
  diff checks, not screenshots/builds. Visible UI changes need current targeted
  browser/snapshot evidence; expand coverage for responsive/shared-contract risk.
- For rollback-like requests, use `$rollback-guardrail` before changing files.
- For commit, push, deploy or release readiness, use `$release-gate` and the repo
  release workflow. A plain context handoff does not itself require a release pass.

## Reference

Read this when the skill triggers:

```text
/Users/point/.codex/skills/mongkol-new-chat/references/new-chat-context.md
```

Use the shared starter-prompt shape from:

```text
/Users/point/.codex/skills/project-onboarding/references/new-chat-template.md
```
