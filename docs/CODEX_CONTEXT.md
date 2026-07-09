# Codex Context

This file is written for future Codex sessions. Its job is to explain what this
repository is, how to reason about it, and how to update it without losing the
user's intent.

## Current State

- Repository: `purichw/Codex-Toolkit`
- Local checkout used when this file was written: `/Users/point/Codex-Toolkit`
- Visibility at initial setup: private
- Purpose: archive and document the user's personal Codex skills
- Current skill count: 15 `SKILL.md` files under `skills/`

The first import copied personal skills from:

```text
/Users/point/.codex/skills
```

System and plugin-provided skills are not meant to be copied here.

## What This Repo Is For

Use this repository as:

- a versioned backup of personal skills;
- a catalog of when each skill should be used;
- a portable way to install skills on another machine;
- a maintenance surface for improving skill docs, references, and scripts.

Do not treat it as:

- the runtime source for every Codex session unless symlinks are intentionally
  installed;
- a place for bundled system skills or plugin cache contents;
- a public-ready package without a privacy review.

## Future-Agent Reading Order

When asked to update this toolkit, read:

1. Root `AGENTS.md` for operating rules.
2. `README.md` for repository overview and quick skill list.
3. `docs/MAINTENANCE.md` for sync, privacy, verification, and commit workflow.
4. `docs/SKILL_CATALOG.md` for descriptions and use context.
5. The relevant `skills/<skill-name>/SKILL.md` and any referenced files before
   editing a skill.

## Source-Of-Truth Decision

Before editing, decide which copy should be authoritative for the task:

| Situation | Preferred action |
| --- | --- |
| User asks to back up current skills | Sync from `~/.codex/skills` into `skills/`. |
| User asks to improve a skill in this repo | Edit `skills/<skill-name>/` and offer to sync back to `~/.codex/skills` if needed. |
| User asks to make the live Codex skill better | Edit `~/.codex/skills/<skill-name>/`, then sync the repo copy. |
| User asks for docs/catalog changes | Edit `README.md`, `docs/`, and possibly `skills/README.md`. |

If the source of truth is ambiguous and the change affects runtime behavior,
ask or make a conservative assumption and state it.

## Sync Workflow

From the repository root, refresh the repository from local personal skills:

```sh
rsync -a --delete --exclude '.system' ~/.codex/skills/ skills/
```

Then review:

```sh
git status --short
git diff --check
find skills -name SKILL.md | sort
```

Expected current skill folders:

- `claude-to-a-tee`
- `coin-quest-admin-ops`
- `coin-quest-ledger-logic`
- `coin-quest-native-parity`
- `docs-cartographer`
- `firebase-account-management`
- `firebase-security-rules`
- `image-boundary-iteration`
- `mobile-web-qa`
- `notenwert-design-direction`
- `notenwert-maintainer`
- `project-onboarding`
- `regression-hunter`
- `release-gate`
- `shane-thai-image-assets`

If the count or names change, update `README.md`, `skills/README.md`, and
`docs/SKILL_CATALOG.md`.

## Privacy And Risk Notes

Some skills intentionally contain project-specific context and local paths. That
is acceptable for a private personal toolkit, but future commits should still
check for:

- real API keys or provider tokens;
- Firebase service-account JSON or private keys;
- passwords and session cookies;
- private customer/client data;
- overly sensitive local absolute paths;
- operational details that should not leave the user's machine.

The previous broad secret scan found documentation words such as `token` and
`password`, but no actual key material. Re-scan before publishing new content.

## Documentation Contract

Keep these docs synchronized:

- `README.md`: quick public-facing overview, docs links, and compact skill table.
- `skills/README.md`: grouped index for browsing the skill folders.
- `docs/SKILL_CATALOG.md`: fuller usage context for each skill.
- `docs/INSTALLATION.md`: install and symlink instructions.
- `docs/MAINTENANCE.md`: update, privacy, verification, and commit workflow.
- `docs/CODEX_CONTEXT.md`: future-agent memory and source-of-truth rules.
- `AGENTS.md`: shortest possible operating note for Codex sessions.

When one file makes a claim about skill count, skill names, or update workflow,
make sure the others do not contradict it.

## Commit And Push Pattern

Use the `release-gate` skill before pushing. For docs-only and skill archive
updates, enough verification is usually:

```sh
git diff --check
python3 scripts/verify_skills.py --expected-count 15
```

For skill script changes, run the script's smoke-test or help path when one
exists.

## Handoff Summary

As of this document, the repository has:

- one initial commit importing all 15 skills;
- one docs commit adding catalog, install, and maintenance docs;
- this future-agent context layer.

The main thing future Codex should preserve is the distinction between live local
skills and the GitHub archive. That distinction prevents accidental overwrites
and keeps the toolkit useful both as runtime configuration and as versioned
documentation.
