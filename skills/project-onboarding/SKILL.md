---
name: project-onboarding
description: Read and map an unfamiliar or returning codebase before making changes. Use when the user asks Codex to study a project, audit project docs, continue work from handoff files, understand architecture, plan an architecture redesign, do an Extra High architecture pass, find commands, identify deploy paths, identify relevant follow-on skills, summarize current state, or prepare a safe implementation plan across any repository.
---

# Project Onboarding

Build a reliable mental model before editing. Prefer local project truth over
assumptions, and keep the output short enough to be useful during active work.

## Intake

1. Identify the workspace root, git state, package manager, framework, and
   important top-level folders.
2. Use `rg --files` before broader search. Read project-local instructions and
   docs that match the task, especially:
   - agent/handoff: `AGENTS*`, `CLAUDE*`, `HANDOFF*`, `Memory*`, `PLAYBOOK*`;
   - project process: `README*`, `CONTRIBUTING*`, `CHANGELOG*`, `RELEASE*`,
     `ROADMAP*`, `TODO*`;
   - architecture decisions: `ARCHITECTURE*`, `ADR*`, `RFC*`, `DECISION*`,
     `docs/**`;
   - environment/deploy: `.env.example`, `.env.*.example`, `Dockerfile*`,
     `docker-compose*`, `.devcontainer/**`, `.github/workflows/**`,
     `.openai/hosting.json`, `vercel.json`, `netlify.toml`, `firebase.json`;
   - API/data/security: `openapi*`, `swagger*`, `schema*`, `graphql*`,
     `firestore.rules`, `storage.rules`, `SECURITY*`, `PRIVACY*`;
   - design/product handoff: `DESIGN*`, `STYLEGUIDE*`, `UX*`, `FIGMA*`,
     `WIREFRAME*`, `PROTOTYPE*`.
3. Inspect build/test/dev commands from package files, lockfiles, Makefiles,
   workspace config, toolchain config, CI workflows, deployment config, and
   scripts.
4. Inventory app entry points, route structure, data/storage layer, auth,
   external services, styling system, test surface, and known generated assets.
5. Check `git status --short` and protect existing user changes.

## Efficient Intake

Read enough to act safely; do not turn every task into a full architecture pass.
For returning projects, start from current maps/handoffs plus `git status`,
changed files, package scripts, and deploy config. Deep-read only the docs and
source areas that can affect the user's requested outcome.

Stop onboarding and move into implementation when you know the owner files, data
or runtime surface, relevant commands, risky unknowns, follow-on skills, and
verification path. Escalate to the Extra High pass only when the user asks for
architecture work or the change crosses module, data, auth, deploy, or product
contract boundaries.

## Skill Routing

After the initial map, name any specialized skills that should take over or run
alongside onboarding. Do not load every skill up front; use the matching skill
only when the user request or project evidence points to it.

- `$efficient-execution`: choose a faster safe path, reuse current evidence,
  define stop rules, or optimize slow checks without lowering quality.
- `$docs-cartographer`: create/update site maps, module maps, architecture
  docs, onboarding docs, handoff docs, or Extra High architecture documents.
- `$regression-hunter`: one bug suggests repeated patterns, stale constants,
  duplicated logic, brittle selectors, or similar regressions elsewhere.
- `$release-gate`: before commit, push, deploy, merge, PR, handoff, or after
  substantial code/UI/data/auth/config/deploy changes.
- `$uat-environment`: production-like preview/UAT setup, seeded test data, auth
  bypass policy, environment isolation, promotion gates, or deciding what needs
  UAT before production.
- `$snapshot`: capture, crop, compare, or present screenshots/visual evidence.
- `$admin-ops`: admin portals, privileged actions, lifecycle operations,
  destructive actions, audit logs, CMS/admin UX, or Admin SDK endpoints.
- `$ledger-logic`: collaborative ledgers, expenses, splits, settlement,
  participants, invites, guests, and shared financial contracts.
- `$native-parity`: native iOS/Android app parity with web/product contracts,
  Expo/React Native builds, shared backend contracts, or device build gates.
- `$ui-ux-orchestrator`: broad or unclear UI/UX work where the right design,
  state, flow, accessibility, or visual QA skill is not obvious.
- `$design-direction`: design briefs, visual north stars, critique, public/admin
  UX direction, Claude prompts, and implementation guardrails.
- `$product-ux-contracts`: preserve routing, persistence, internal scroll,
  permissions, destructive safety, media fallbacks, search click-through, or
  proven UX while redesigning/restyling.
- `$ui-state-matrix`: default, selected, disabled, loading, empty, error,
  success, permission, long-text, localization, and responsive UI states.
- `$interaction-flow-qa`: click through complete user/admin journeys and prove
  route, state, data, permissions, persistence, and feedback.
- `$design-system-guardian`: prevent design-system/token/component drift across
  buttons, cards, tables, forms, nav, dialogs, and reusable primitives.
- `$accessible-interaction`: keyboard, focus, ARIA/semantics, contrast, reduced
  motion, touch targets, modal/drawer accessibility, or mobile keyboard.
- `$data-dense-ux`: tables, admin dashboards, lists, ledgers, filters,
  pagination, bulk actions, virtualized lists, and operational panels.
- `$form-flow-ux`: create/edit forms, validation, dirty state, autosave, save,
  cancel, reset, server errors, permission denied, uploads, and mobile keyboard.
- `$site-maintainer`: website projects with source/build/deploy artifact
  boundaries, generated output, service workers, tests, work logs, or hosting.
- `$tts-audio-assets`: reusable TTS audio generation, reuse, naturalness QA, and
  playback asset mapping.
- `$course-image-assets`: reusable educational/vocabulary image generation,
  semantic reuse, crop, mapping, and QA.
- `$export-html`: create standalone/offline HTML exports or clickable prototypes
  from live/product screens for design handoff, Claude Design, or state review.
- `$claude-to-a-tee`: implement or audit exact UI parity from offline Claude
  HTML, screenshots, exported assets, or Claude Design handoffs.
- `$mobile-web-qa`: mobile/tablet/Safari/Chrome-on-iPhone responsive QA, touch
  targets, safe areas, keyboard behavior, or horizontal overflow.
- `$placeholder-image`: source, replace, generate, crop, or audit website/app
  images and placeholder media.
- `$firebase-account-management`: Firebase Auth users, signup/login, providers,
  user profiles, custom claims, Admin SDK user management, or account flows.
- `$firebase-security-rules`: Firestore/Storage rules, Admin SDK endpoints,
  service-account env vars, billing/security assumptions, or production access.
- `$openai-docs`: OpenAI API, model, Codex, or OpenAI product docs/questions.
- `sites:sites-building` / `sites:sites-hosting`: site build/deploy work,
  especially when `.openai/hosting.json` exists.
- `$notenwert-maintainer` / `$notenwert-design-direction`: Notenwert project
  implementation, CMS/admin, deploy prep, or visual direction; use with
  `$site-maintainer` / `$design-direction` for reusable workflow.
- `$shane-thai-audio-generator` / `$shane-thai-image-assets`: Shane and His
  Thai lesson audio, Chirp TTS, vocabulary images, badges, or lesson artwork;
  use with `$tts-audio-assets` / `$course-image-assets` for reusable workflow.
- `$coin-quest-ledger-logic`, `$coin-quest-admin-ops`,
  `$coin-quest-native-parity`: Coin Quest Ledger web/admin/native work; use
  with `$ledger-logic`, `$admin-ops`, or `$native-parity` for reusable workflow.
- `$image-boundary-iteration`: nudity_reference_prompting image iteration,
  boundary-forward non-explicit image prompting, logging, or visual baselines.

If multiple skills match, state the order and why. Read each selected skill's
`SKILL.md` before acting on that part of the task.

## Map The Project

Produce a compact map with:

- purpose and current goal;
- major directories and ownership boundaries;
- key runtime commands and env files;
- frontend/backend/data/deploy flow;
- docs or handoff files that matter most;
- relevant follow-on skills and why they apply;
- risky areas, stale notes, or contradictions;
- immediate next steps for the requested task.

Use this shape when onboarding itself is the deliverable:

```text
Project:
Current goal:
Docs read:
Commands found:
Architecture map:
Data/auth/deploy flow:
Relevant skills:
Risks / stale docs:
Safe next steps:
Unknowns needing audit:
```

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
- architecture docs, ADRs/RFCs, API schemas, env/deploy/security docs, and
  places where documentation conflicts with current code;
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
