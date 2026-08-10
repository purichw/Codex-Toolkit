# Codex Toolkit Agent Notes

This repository stores the user's personal Codex skills. Treat it as a private
toolkit and backup, not as a generic public package.

## First Read

When a future Codex session lands here, read these files before making changes:

1. `README.md` for the public-facing overview.
2. `docs/CODEX_CONTEXT.md` for source-of-truth rules and update workflow.
3. `docs/MAINTENANCE.md` before syncing, committing, or pushing.
4. `docs/SKILL_CATALOG.md` when choosing or documenting skills.

## Source Of Truth

The live personal skills usually live in:

```text
~/.codex/skills
```

This repository is the GitHub copy. Before changing skill content, determine
whether the user wants to edit the live local skill, the repository copy, or
both. If syncing from local skills, exclude `.system` and bundled plugin skills.
If the live local tree does not contain repo-only `global-*` aliases, do not run
a broad delete sync that removes them. Sync changed canonical folders
selectively unless the user explicitly asks to rebuild the global layer.

## UI/UX Design

For any user-facing UI, screen, layout, component, deck, doc, or prototype,
load `/Users/point/.codex/skills/ui-ux-expert/SKILL.md` and follow it. Copy
`/Users/point/.codex/skills/ui-ux-expert/tokens.css` as the default design
system only when the project has no brand, design system, production UI, or
user-provided visual direction.

After UI/UX implementation, redesign, restyle, visual audit, responsive QA,
Claude/Figma/reference handoff, or screenshot-based design work, load and use
`/Users/point/.codex/skills/snapshot/SKILL.md` before the final response. Do
not wait for the user to ask for visual evidence.

## Repository Shape

- `skills/<skill-name>/SKILL.md` is the required skill entrypoint.
- `skills/<skill-name>/references/` holds required supporting notes.
- `skills/<skill-name>/scripts/` holds reusable helpers.
- `skills/<skill-name>/agents/` holds agent metadata.
- `docs/` explains how to use, install, maintain, and understand the toolkit.
- `scripts/verify_skills.py` verifies the archived skill set.

## Safety Rules

- Keep the repo private unless the user explicitly decides to publish it.
- Review for secrets, service-account files, tokens, passwords, private keys,
  private URLs, personal data, and sensitive project details before pushing.
- Do not add generated caches, system skills, plugin cache contents, or unrelated
  local project files.
- Preserve executable bits on helper scripts.
- Use concise commits and push only the intended scope.

## Verification

For most changes, run:

```sh
git diff --check
python3 scripts/verify_skills.py --expected-count 126
```

The verifier checks skill frontmatter, folder/name consistency, Markdown links,
helper script syntax, accidental bundled/system paths, and high-confidence
secret patterns.

For skill syncs, also inspect the actual skill list when names may have changed:

```sh
find skills -name SKILL.md | sort
```
