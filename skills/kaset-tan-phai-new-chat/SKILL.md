---
name: kaset-tan-phai-new-chat
description: Onboard a fresh Codex chat for the Kaset Tan Phai / เกษตรทันภัย public flood, drought, and water-risk alert project. Use when the user asks for a new-chat prompt, handoff prompt, context pickup checklist, required docs/skills/setup for Kaset Tan Phai, or wants a future chat to know what to read before UI, data, map, alerts, notifications, operations, QA, push, or deploy work.
---

# Kaset Tan Phai New Chat

## Purpose

Prepare a fresh Codex chat to work safely on เกษตรทันภัย without relying on stale
conversation memory. This skill is an onboarding router: read the current
on-disk docs and skill files, then produce a concise starter prompt or context
checklist for the next chat.

## Workflow

1. Treat the repo as:

```text
/Users/point/Kaset-Tan-Phai
```

2. Inspect current state first:

```bash
git -C "/Users/point/Kaset-Tan-Phai" status --short
```

3. Read the shared new-chat shape:
   `/Users/point/.codex/skills/project-onboarding/references/new-chat-template.md`.
4. Read `references/new-chat-context.md` from this skill.
5. Read only the project docs relevant to the next task, using the required-doc
   order from the reference.
6. If the user asks for a prompt, return a copy-ready prompt for a new chat. If
   the user asks to continue work, summarize what was read and proceed with the
   relevant task.

## Required Discipline

- Use current on-disk skill files when a skill is named. Do not rely on older
  remembered skill behavior.
- Do not commit, push, deploy, rollback, revert, remove, migrate, or touch
  production data unless the user explicitly asks in the current task.
- Treat current repo files, current docs, and canonical JSON as source of truth
  over older chat history, screenshots, attached documents, or copied specs
  unless the owner explicitly changes direction.
- Preserve routes/surfaces, data contracts, localStorage keys, GeoJSON joins,
  alert workflow gates, public-safety wording constraints, responsive behavior,
  and Thai-first language unless the task explicitly changes them.
- Treat เกษตรทันภัย as a public flood, drought, and water-risk alert product,
  not a generic dashboard. Residents and local operators must be able to
  understand risk, uncertainty, geography, freshness, and recommended actions.
- For UI work, provide snapshot or browser evidence in the final handoff.
- For release work, use `$release-gate`; for rollback-like requests, use
  `$rollback-guardrail` before changing files.

## Reference

Read this when the skill triggers:

```text
/Users/point/.codex/skills/kaset-tan-phai-new-chat/references/new-chat-context.md
```

Use the shared starter-prompt shape from:

```text
/Users/point/.codex/skills/project-onboarding/references/new-chat-template.md
```
