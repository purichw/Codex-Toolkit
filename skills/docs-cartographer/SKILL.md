---
name: docs-cartographer
description: Create or update project documentation that maps site structure, modules, data flow, interactions, ownership boundaries, commands, and where to find things. Use when the user asks to document how a project works, make the repo easier to navigate, create site maps, architecture maps, target-state architecture plans, module maps, interaction docs, onboarding docs, memory docs, handoff docs, Extra High architecture documentation, or "where is X?" project guides.
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
5. Note which follow-on skills apply, such as `$project-onboarding`,
   `$release-gate`, `$reference-to-a-tee`, `$mobile-web-qa`, `$firebase-*`, or
   project-specific skills.

## Consolidate Before Creating

Prefer improving the canonical doc over adding another isolated note. Create a
new document only when the information has a distinct audience or lifecycle.

Use `$efficient-execution` when documentation work is getting broad. Update the
smallest canonical document that will make future work faster. Do not remap the
whole repository for a narrow doc change unless the user asked for onboarding,
architecture, or a full handoff.

Stop discovery when the doc can answer: where the thing lives, how it connects,
how to run or verify it, what must not break, and which skill or owner should
handle the next step.

Use this placement rule:

- **current-state navigation:** project map, site map, module map, interaction map;
- **future-state design:** architecture plan, migration plan, target-state map;
- **operating memory:** playbook, handoff, release runbook, work log;
- **domain contract:** data contract, API schema, Firebase/rules, asset/audio map.

If two docs overlap, merge the reusable facts into the canonical doc and leave a
short pointer in the older doc when local convention expects it.

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

For target-state architecture plans, include:

- current-state map: what exists now and where;
- desired bounded contexts and ownership rules;
- dependency direction rules and forbidden imports;
- data contract map for client state, persistence, API, Firestore, storage,
  generated assets, and admin-only operations;
- migration phases with “ship/no-ship” gates;
- compatibility strategy for old data, old routes, generated assets, and
  existing user progress;
- verification matrix: unit, data contract, Firebase/rules, e2e, responsive,
  visual parity, asset/audio/image audits, and production smoke;
- risk register with mitigations and rollback notes.

Separate facts from proposals. Label uncertain claims as `needs audit` and
avoid presenting aspirations as current behavior.

Use Mermaid diagrams when relationships are easier to scan visually. Keep
diagrams simple and labels quoted when punctuation appears.

## Output Templates

For a project map, use:

```text
Purpose / current goal
How to run / verify
Top-level directories
Routes and entry points
Data/auth/storage/deploy flow
Important docs and generated assets
Relevant skills
Risks / stale notes / contradictions
Next actions
```

For a handoff, use:

```text
Current state
What changed
Commands run
Files and docs touched
Open risks / blocked items
Recommended next skill or gate
```

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
- Keep docs navigable: one clear map is better than scattered fragments.
- Include verification or owner/source-of-truth notes for operational claims.
- After editing docs, run markdown/lint checks if the repo defines them.
