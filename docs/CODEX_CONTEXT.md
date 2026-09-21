# Codex Context

This file is written for future Codex sessions. Its job is to explain what this
repository is, how to reason about it, and how to update it without losing the
user's intent.

## Current State

- Repository: `purichw/Codex-Toolkit`
- Local checkout used when this file was written: `/Users/point/Codex-Toolkit`
- Visibility at initial setup: private
- Purpose: archive and document the user's personal Codex skills
- Current skill count: 136 `SKILL.md` files under `skills/`
- Breakdown: 79 personal skill folders (including compatibility routers),
  55 `global-*` alias skills for reusable non-project-specific workflows, and
  2 standalone global design-spec skills.

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

From the repository root, inspect local personal-skill changes with a dry run:

```sh
rsync -ani --delete --exclude '.system' --exclude '/README.md' --exclude '__pycache__/' --exclude '*.orig' ~/.codex/skills/ skills/
```

Review deletions before applying them. The live local tree may not contain the
repo-only `global-*` alias layer. If the dry run would delete `global-*` aliases
or standalone global design-spec skills, do not run the broad delete sync. Sync
changed canonical folders selectively, for example:

```sh
rsync -a ~/.codex/skills/<skill-name>/ skills/<skill-name>/
```

Then review:

```sh
git status --short
git diff --check
find skills -name SKILL.md | sort
```

Expected current skill folders:

- `accessibility-beyond-basics`
- `accessible-interaction`
- `account-recovery-key`
- `admin-ops`
- `admin-prototype-reconciliation`
- `art-direction-imagery`
- `claude-design-md-request`
- `claude-design-reference-bundle`
- `claude-to-a-tee`
- `codex-handoff-for-claude`
- `coin-quest-admin-ops`
- `coin-quest-ledger-logic`
- `coin-quest-native-parity`
- `consistency-audit`
- `course-image-assets`
- `covermate-design-spec`
- `covermate-new-chat`
- `data-dense-ux`
- `design-direction`
- `design-quality-review`
- `design-system-architect`
- `design-system-guardian`
- `docs-cartographer`
- `domain-taste`
- `dootaa-new-chat`
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
- `information-architecture-ux`
- `interaction-design`
- `interaction-flow-qa`
- `ios-app-development`
- `kaset-tan-phai-new-chat`
- `korat-tan-phai-new-chat`
- `korat-tan-phai-shared-components`
- `ledger-logic`
- `mobile-native-feel`
- `mobile-web-qa`
- `mockup-to-product`
- `mongkol-new-chat`
- `motion-choreography`
- `native-parity`
- `notenwert-design-direction`
- `notenwert-maintainer`
- `placeholder-image`
- `prod-smoke-harness`
- `product-ux-contracts`
- `production-asset-smoke`
- `project-onboarding`
- `reference-implementation-critique`
- `reference-to-a-tee`
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
- `taste-calibration`
- `tts-audio-assets`
- `typography-refinement`
- `uat-environment`
- `ui-state-matrix`
- `ui-ux-expert`
- `ui-ux-orchestrator`
- `usage-budget-gate`
- `visual-diagnosis`

Reusable non-project-specific skills also have `global-*` alias folders. The
full alias map lives in [GLOBAL_SKILLS.md](GLOBAL_SKILLS.md); keep aliases as
thin wrappers and update the canonical skill first. `global-full-design-spec`
and `global-quick-design-spec` are standalone global skills, not alias wrappers.

`reference-to-a-tee` replaces the Claude-specific implementation workflow and
supports HTML, image-only, and mixed references. `claude-to-a-tee` and
`global-claude-to-a-tee` are compatibility routers; preserve their paths without
reintroducing old HTML-only rules. See
[REFERENCE_PARITY_MIGRATION.md](REFERENCE_PARITY_MIGRATION.md) for dependencies,
legacy CLI behavior, and verification cases.

If the count or names change, update `README.md`, `skills/README.md`,
`docs/SKILL_CATALOG.md`, and `docs/GLOBAL_SKILLS.md` when aliases are involved.

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
- `docs/GLOBAL_SKILLS.md`: global alias map and project-specific exclusions.
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
python3 scripts/verify_skills.py --expected-count 136
```

For skill script changes, run the script's smoke-test or help path when one
exists.

For the UI/UX judgment/evaluation layer and the related gate corrections, read
[SKILL_JUDGMENT_AND_GATES.md](SKILL_JUDGMENT_AND_GATES.md). Its scenario pack is
synthetic and unscored; structural validation is not evidence of better taste.
The six named skills were selectively synchronized, not the entire live tree.

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
- one archive update adding `codex-handoff-for-claude` and `ui-ux-expert`,
  documenting Codex-to-Claude handoffs and a portable UI/UX design expert skill,
  and updating the verifier count to 55.
- one update adding 38 `global-*` alias wrappers for reusable non-project-
  specific skills, documenting the global alias map, and updating the verifier
  count to 93.
- one archive update adding `global-full-design-spec` and
  `global-quick-design-spec`, adding the UI/UX design rule to `AGENTS.md`, and
  updating the verifier count to 95.
- one archive update broadening `ui-ux-expert` and `global-ui-ux-expert` around
  UX behavior, flow feedback, and ideal/empty/loading/error/edge state coverage.
- one archive update adding `claude-design-reference-bundle`,
  `global-claude-design-reference-bundle`, and `mongkol-new-chat`, plus
  responsive-web guidance for UI/mobile QA and dependency cleanup guidance for
  HTML exports, updating the verifier count to 98.
- one update adding a mandatory `$snapshot` gate across UI/UX, design handoff,
  visual parity, admin/native UX, and related global alias skills. Future
  Codex sessions should capture snapshot evidence before final response for
  visible UI/UX work instead of waiting for the user to ask.
- one update refactoring `ui-ux-expert` into a smaller routed core, adding
  `craft-defaults` and `claude-design-learning-brief` references, and preserving
  the mandatory `$snapshot` gate.
- one update importing the Claude Design `design-quality` guide as
  `design-quality-review`, adding twelve specialist UI/UX quality skills and 13
  matching `global-*` aliases, wiring them into UI/UX, snapshot, accessibility,
  design-system, and Claude-to-a-tee routing, and updating the verifier count to
  124.
- one archive update adding `covermate-design-spec` and `covermate-new-chat`,
  preserving the repo-only global alias layer during sync, tightening snapshot
  closeout evidence, and updating the verifier count to 126.
- one consolidation update moving proportional-effort depth rules into
  `efficient-execution`, keeping `usage-budget-gate` as a compatibility router,
  adding a shared project new-chat template under `project-onboarding`, wiring
  project-specific `*-new-chat` skills to that template, importing
  `kaset-tan-phai-new-chat`, and updating the verifier count to 127.

The main thing future Codex should preserve is the distinction between live local
skills and the GitHub archive. That distinction prevents accidental overwrites
and keeps the toolkit useful both as runtime configuration and as versioned
documentation.
