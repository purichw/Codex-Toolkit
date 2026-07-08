---
name: docs-cartographer
description: Create or update project documentation that maps site structure, modules, data flow, interactions, ownership boundaries, commands, and where to find things. Use when the user asks for site maps, architecture maps, module maps, interaction docs, onboarding docs, memory docs, handoff docs, or better project navigation.
---

# Docs Cartographer

Make future work faster by documenting how the project is connected. Prefer one
clear living document over many tiny files unless separation makes navigation
materially better.

## Discover

1. Read existing docs first and avoid duplicating them.
2. Inspect routes, components, APIs, state/data stores, auth, config, tests,
   deployment files, and scripts with `rg --files`.
3. Check current code over old notes when they disagree.
4. Identify audiences: new chat handoff, future maintainer, release operator,
   designer, or product owner.

## Write Useful Maps

Include only sections that help the project:

- project overview and current state;
- directory and file map;
- route/site map;
- module ownership boundaries;
- user interaction flows;
- data flow and persistence;
- API/service/deployment map;
- commands and verification matrix;
- design source-of-truth and asset locations;
- known risks, invariants, and “do not break” rules;
- handoff checklist for next sessions.

Use Mermaid diagrams when relationships are easier to scan visually. Keep
diagrams simple and labels quoted when punctuation appears.

## Placement

- Update existing canonical docs when they already exist.
- Create new docs only when the information does not belong cleanly anywhere.
- Prefer names such as `PROJECT_MAP.md`, `ARCHITECTURE.md`, `SITE_MAP.md`,
  `INTERACTION_MAP.md`, `PLAYBOOK.md`, or `Memory.md` when local conventions do
  not already decide.

## Quality Bar

- Link to real files with exact paths when useful.
- Keep claims grounded in code or current docs.
- Mark stale or uncertain information clearly.
- Avoid writing docs that merely narrate obvious file names.
- After editing docs, run markdown/lint checks if the repo defines them.
