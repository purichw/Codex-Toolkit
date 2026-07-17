# Codex Context

This file is written for future Codex sessions. Its job is to explain what this
repository is, how to reason about it, and how to update it without losing the
user's intent.

## Current State

- Repository: `purichw/Codex-Toolkit`
- Local checkout used when this file was written: `/Users/point/Codex-Toolkit`
- Visibility at initial setup: private
- Purpose: archive and document the user's personal Codex skills
- Current skill count: 53 `SKILL.md` files under `skills/`

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
rsync -a --delete --exclude '.system' --exclude '/README.md' --exclude '__pycache__/' --exclude '*.orig' ~/.codex/skills/ skills/
```

Then review:

```sh
git status --short
git diff --check
find skills -name SKILL.md | sort
```

Expected current skill folders:

- `accessible-interaction`
- `account-recovery-key`
- `admin-ops`
- `admin-prototype-reconciliation`
- `claude-design-md-request`
- `claude-to-a-tee`
- `coin-quest-admin-ops`
- `coin-quest-ledger-logic`
- `coin-quest-native-parity`
- `consistency-audit`
- `course-image-assets`
- `data-dense-ux`
- `design-direction`
- `design-system-guardian`
- `docs-cartographer`
- `efficient-execution`
- `export-html`
- `firebase-account-management`
- `firebase-security-rules`
- `form-flow-ux`
- `image-boundary`
- `image-boundary-efficient`
- `image-boundary-iteration`
- `image-boundary-nonexplicit-max`
- `image-boundary-polish`
- `image-boundary-rejection-recovery`
- `image-boundary-safety-map`
- `interaction-flow-qa`
- `ledger-logic`
- `mobile-web-qa`
- `native-parity`
- `notenwert-design-direction`
- `notenwert-maintainer`
- `placeholder-image`
- `prod-smoke-harness`
- `product-ux-contracts`
- `production-asset-smoke`
- `project-onboarding`
- `regression-hunter`
- `release-gate`
- `rollback-guardrail`
- `shane-thai-audio-generator`
- `shane-thai-export-chatgpt`
- `shane-thai-image-assets`
- `shane-thai-new-chat`
- `shane-thai-prod-smoke`
- `site-maintainer`
- `snapshot`
- `tts-audio-assets`
- `uat-environment`
- `ui-state-matrix`
- `ui-ux-orchestrator`
- `usage-budget-gate`

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
python3 scripts/verify_skills.py --expected-count 53
```

For skill script changes, run the script's smoke-test or help path when one
exists.

## Handoff Summary

As of this document, the repository has:

- one initial commit importing 15 skills;
- one docs commit adding catalog, install, and maintenance docs;
- this future-agent context layer.
- one archive update adding 2 more skills and updating the verifier count to 17.
- one archive update adding 9 more reusable/generalized skills and updating the
  verifier count to 26.
- one archive update adding `efficient-execution` and `uat-environment`,
  broadening existing skill instructions, and updating the verifier count to 28.
- one archive update adding 8 UI/UX quality skills and updating the verifier
  count to 36.
- one archive update adding `usage-budget-gate`, `consistency-audit`,
  `prod-smoke-harness`, and `shane-thai-prod-smoke`, plus related routing
  updates, and updating the verifier count to 40.
- one archive update adding `image-boundary-polish`, broadening snapshot and
  boundary-iteration guidance, and updating the verifier count to 41.
- one archive update adding the image-boundary router, non-explicit max,
  rejection recovery, and safety-map skills, plus snapshot/boundary guidance,
  and updating the verifier count to 45.
- one archive update adding account recovery, admin prototype reconciliation,
  image-boundary efficiency, production asset smoke, and Shane Thai export
  skills, plus related routing updates, and updating the verifier count to 50.
- one archive update adding `rollback-guardrail`, expanding `release-gate`
  hard stops, broadening skill trigger descriptions, and updating the verifier
  count to 51.
- one archive update adding `claude-design-md-request` and
  `shane-thai-new-chat`, documenting Claude Design Markdown handoff prompts and
  Shane Thai fresh-chat onboarding, and updating the verifier count to 53.

The main thing future Codex should preserve is the distinction between live local
skills and the GitHub archive. That distinction prevents accidental overwrites
and keeps the toolkit useful both as runtime configuration and as versioned
documentation.
