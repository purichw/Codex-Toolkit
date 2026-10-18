# Project New Chat Template

Use this reference when a project-specific `*-new-chat` skill prepares a starter
prompt, handoff prompt, or context checklist for a fresh Codex chat.

## Purpose

A new-chat prompt should make the next Codex session useful quickly without
relying on stale conversation memory. It should say what to read, what product
contracts to preserve, what actions are unauthorized, and what evidence is
expected for the likely task.

Project-specific `*-new-chat` skills own project facts. This template owns the
shared shape only.

## Starter Prompt Shape

```text
We are continuing the <project name> project at:
<absolute project path>

Before doing work, use $<project-new-chat-skill> and read current on-disk docs,
not prior memory. Start with:
- <required doc 1>
- <required doc 2>
- <required doc 3>

Then read task-specific docs from:
<project-new-chat reference path>

Important constraints:
- Current repo files and current docs are source of truth unless I explicitly
  change direction.
- Do not commit, push, deploy, rollback, revert, remove, migrate, or touch
  production data unless I explicitly ask in this current task.
- Before every push or deploy not explicitly requested for the current changes
  and target, ask me and wait for confirmation. Prior completed tasks, repo
  policy, handoffs, and passing checks are not permission. Push and deploy need
  separate authorization, including auto-deploy triggered by a push or rerun.
  Do not ask again for an action already explicitly requested within that scope.
- Preserve routes, data contracts, storage keys, auth/session behavior,
  responsive constraints, and project-specific product decisions unless
  explicitly in scope.
- If a named skill is used, read its current on-disk SKILL.md first.
- UI work needs current browser/snapshot evidence when renderable.
- Release work must use $release-gate; rollback-like work must use
  $rollback-guardrail first.

After onboarding, summarize what you read and continue with my task if I gave
one; otherwise wait for the next instruction.
```

## Required Sections

When returning a new-chat handoff or checklist, include only sections that help
the next session:

- project path and product purpose;
- required read order;
- task-specific docs/source areas;
- durable product rules and do-not-touch constraints;
- skills to load for common task categories;
- safe commands and verification commands;
- release/deploy/rollback authorization rules;
- known branch/workflow auto-deploy triggers and the separately authorized
  push/deploy scope, or an explicit note that approval is still needed;
- current status or latest known phase only when current docs support it.

## Rules

- Prefer absolute project paths and exact file names.
- Keep project facts in the project-specific `references/new-chat-context.md`;
  do not duplicate a long project memory in the prompt.
- Mark stale or inferred context clearly instead of presenting it as fact.
- Do not include secrets, real credentials, session tokens, or private customer
  data.
- Do not authorize commit, push, deploy, rollback, destructive file operations,
  migrations, or production data changes unless the user explicitly did so in
  the current task.
- For UI projects, require snapshot/browser evidence only when a rendered target
  is available and the current task changes or judges visible UI.
