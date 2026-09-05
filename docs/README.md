# Documentation Index

This directory documents how to use and maintain the Codex Toolkit repository.

## Start Here

- [Codex context](CODEX_CONTEXT.md): future-agent entrypoint with repository
  purpose, source-of-truth rules, sync workflow, and safety checks.
- [Skill catalog](SKILL_CATALOG.md): what each skill does, when to use it, and
  what kind of context it expects.
- [Global skills](GLOBAL_SKILLS.md): reusable non-project-specific skills and
  their `global-*` aliases.
- [Installation and usage](INSTALLATION.md): how to install one skill, install
  all skills, or use symlinks during active development.
- [Maintenance guide](MAINTENANCE.md): how to sync local skills into this repo,
  add a new skill, review privacy risk, and verify docs before pushing.
- [Reference parity migration](REFERENCE_PARITY_MIGRATION.md): generic image,
  HTML, and mixed modes; legacy aliases, helper compatibility, and checks.
- [Design judgment and gates](SKILL_JUDGMENT_AND_GATES.md): UI/UX decision
  methods, evaluation limits, complete-deliverable gates, and rollback risk tiers.

## Repository Map

```text
.
├── README.md
├── docs/
│   ├── CODEX_CONTEXT.md
│   ├── GLOBAL_SKILLS.md
│   ├── INSTALLATION.md
│   ├── MAINTENANCE.md
│   ├── README.md
│   ├── REFERENCE_PARITY_MIGRATION.md
│   ├── SKILL_CATALOG.md
│   └── SKILL_JUDGMENT_AND_GATES.md
├── scripts/
│   └── verify_skills.py
└── skills/
    ├── README.md
    └── <skill-name>/
        ├── SKILL.md
        ├── agents/
        ├── references/
        └── scripts/
```

Not every skill has `agents/`, `references/`, or `scripts/`. `SKILL.md` is the
only required file for a skill.
