---
name: project-onboarding
description: Read and map an unfamiliar or returning codebase before making changes. Use when the user asks Codex to study a project, read docs, continue work from handoff files, understand architecture, plan an architecture redesign, do an Extra High architecture pass, find commands, identify deploy paths, summarize current state, or prepare a safe implementation plan across any repository.
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

## Extra High Architecture Pass

When the user asks for a new architecture, an architecture redesign, or an
“Extra High” pass, do not stop at a directory tour. Build enough evidence to
propose a target architecture that can survive implementation.

Collect:

- runtime entry points, route graph, and major UI shells;
- bounded contexts or domains, with their source folders and current owners;
- module dependency direction, including cross-domain imports and oversized
  files;
- data contracts: local state, storage keys, Firestore/API documents, generated
  assets, and server routes;
- auth, permissions, persistence, offline/sync, deployment, and environment
  boundaries;
- design-system surfaces, visual handoff sources, and places where UI primitives
  fork;
- test coverage by surface and the gaps that would make refactors risky.

Then produce:

- current-state architecture summary;
- proposed bounded-context/module map;
- dependency rules to enforce going forward;
- migration seams that allow incremental delivery;
- phase plan with validation gates and rollback points;
- risk register: data loss, auth/security, deploy, performance, UX parity,
  generated assets, and test debt.

Mark anything inferred as inferred. Prefer “unknown / needs audit” over fake
certainty.

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
