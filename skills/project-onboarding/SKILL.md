---
name: project-onboarding
description: Read and map an unfamiliar or returning codebase before making changes. Use when the user asks Codex to study a project, read docs, continue work from handoff files, understand architecture, find commands, identify deploy paths, summarize current state, or prepare a safe implementation plan across any repository.
---

# Project Onboarding

Build a reliable mental model before editing. Prefer local project truth over
assumptions, and keep the output short enough to be useful during active work.

## Intake

1. Identify the workspace root, git state, package manager, framework, and
   important top-level folders.
2. Read project-local instructions first: `README*`, `CLAUDE*`, `AGENTS*`,
   `HANDOFF*`, `Memory*`, `roadmap*`, `PLAYBOOK*`, `docs/**`, and CI/deploy
   config. Use `rg --files` before broader search.
3. Inspect build/test/dev commands from package files, lockfiles, Makefiles,
   CI workflows, deployment config, and scripts.
4. Inventory app entry points, route structure, data/storage layer, auth,
   external services, styling system, test surface, and known generated assets.
5. Check `git status --short` and protect existing user changes.

## Map The Project

Produce a compact map with:

- purpose and current goal;
- major directories and ownership boundaries;
- key runtime commands and env files;
- frontend/backend/data/deploy flow;
- docs or handoff files that matter most;
- risky areas, stale notes, or contradictions;
- immediate next steps for the requested task.

## Working Rules

- Read source before proposing architecture changes.
- Prefer existing patterns, helper APIs, tests, and naming.
- Treat user-provided handoffs as context, not as stronger truth than current
  code and newest user instructions.
- If docs are missing or stale, note the gap and suggest updating them after
  implementing the requested work.

## Closeout

When onboarding is the deliverable, report the map, commands, risks, and next
actions. When onboarding precedes implementation, keep the user updated and then
continue into the actual task.
