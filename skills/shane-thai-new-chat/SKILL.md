---
name: shane-thai-new-chat
description: Onboard a fresh Codex chat for the Shane and His Thai project. Use when the user asks for a new-chat prompt, handoff prompt, context pickup checklist, required docs/skills/setup for Shane Thai, or wants a future chat to know what to read before learner, admin, content, audio, image, Firebase, QA, deploy, or consistency work.
---

# Shane Thai New Chat

## Purpose

Prepare a fresh Codex chat to work safely on Shane and His Thai without relying on stale conversation memory. This skill is an onboarding router: read the current on-disk docs and skill files, then produce a concise starter prompt or context checklist for the next chat.

## Workflow

1. Treat the repo as:

```text
/Users/point/Website Projects/thai-flashcards
```

2. Inspect current state first:

```bash
git -C "/Users/point/Website Projects/thai-flashcards" status --short
```

3. Read the shared new-chat shape:
   `/Users/point/.codex/skills/project-onboarding/references/new-chat-template.md`.
4. Read `references/new-chat-context.md` from this skill.
5. Read only the project docs relevant to the next task, using the required-doc order from the reference.
6. If the user asks for a prompt, return a copy-ready prompt for a new chat. If the user asks to continue work, summarize what was read and proceed with the relevant task.

## Required Discipline

- Use current on-disk skill files when a skill is named. Do not rely on older remembered skill behavior.
- Do not commit, push, deploy, rollback, revert, or remove work unless the user explicitly asks in the current task.
- Preserve existing behavior, routes, progress keys, data contracts, internal scroll containers, responsive constraints, and customized component geometry unless the task explicitly changes them.
- For UI work, provide snapshots or screenshots in the final handoff.
- For rollback-like requests, use `$rollback-guardrail` before changing files.

## Reference

Read this when the skill triggers:

```text
/Users/point/.codex/skills/shane-thai-new-chat/references/new-chat-context.md
```

Use the shared starter-prompt shape from:

```text
/Users/point/.codex/skills/project-onboarding/references/new-chat-template.md
```
