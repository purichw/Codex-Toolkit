---
name: release-gate
description: Fast, risk-tiered verification before commit, push, deploy, release, merge, PR, or handoff. Use when the user asks to commit, push, deploy, ship, release, merge, open a PR, check readiness, or make sure a feature is safe; also use after substantial code, UI, data, auth, configuration, or deployment changes before publishing.
---

# Release Gate

Block avoidable releases with the smallest trustworthy evidence set. Optimize for
speed by separating commit, push, and deploy gates, using targeted checks first,
and escalating only when the diff increases risk.

## Fast Protocol

1. Confirm the intended action and target: commit, push, PR, preview,
   production deploy, package, static artifact, docs-only, or handoff. If the
   target is obvious from the request and repo state, state the assumption and
   continue.
2. Inspect scope before checks: `git status --short`, staged files, unstaged
   files, recent diff, and changed filenames. Do not include unrelated user
   changes without explicit intent.
3. Classify the highest-risk touched surface: docs/assets-only, narrow code,
   frontend UI, shared runtime behavior, API, data model, auth, build config,
   deployment config, migrations, environment variables, tests, or generated
   assets.
4. Choose the shortest evidence path that covers that risk. Prefer targeted
   commands for changed packages/files/tests before full-suite commands. Run
   independent checks in parallel when possible.
5. Summarize evidence, failures, and skipped checks. Never skip a relevant
   check silently.

## Risk Tiers

- **T0 docs/static metadata**: inspect scope and diff. Run docs generation or
  spelling/link checks only when the repo defines them or docs are published as
  a built artifact.
- **T1 narrow non-runtime changes**: run focused formatting/linting or the
  nearest targeted test. Skip browser/build checks unless the touched files feed
  a runtime bundle.
- **T2 runtime code**: run targeted tests plus the relevant typecheck, lint, or
  build command defined by the repo. Escalate to broader tests when the changed
  code is shared across packages or has no focused test.
- **T3 frontend UI**: run the app or reuse a healthy existing dev server, verify
  the changed route with browser automation when available, and check console
  errors plus failed network/asset requests. Capture screenshot or interaction
  evidence for visual work.
- **T4 data/auth/API/config risk**: run the relevant build/tests and inspect
  environment variables, migrations, storage, cron jobs, feature flags, rules,
  or rollback path when touched.
- **T5 deploy/release**: use the platform's deployment skill/tooling when
  available and verify the resulting URL or artifact, not only the local build.

## Check Packs

Use these as starting packs, then adapt to repo-defined commands:

- **Docs-only:** inspect diff, run `git diff --check`, docs lint/build when the
  repo defines one, and confirm no generated runtime artifact changed
  accidentally.
- **Frontend UI:** targeted lint/typecheck/build, browser route check, console
  and failed request check, `$snapshot` evidence when visual, `$mobile-web-qa`
  when responsive/mobile risk exists.
- **Claude parity:** use `$claude-to-a-tee`; require rendered reference/app
  comparison and measured parity evidence before release.
- **Firebase/rules/auth:** use `$firebase-security-rules` or
  `$firebase-account-management`; run tests/emulator or scoped live checks
  appropriate to risk, and document deploy/rollback path.
- **Generated image/audio assets:** run the relevant audit/check scripts, verify
  data mappings, inspect representative rendered UI, and avoid broad
  regeneration unless requested.
- **Sites deploy:** when `.openai/hosting.json` exists, use Sites tooling and
  verify the deployed URL/artifact, not just local build.

## Gate By Action

- **Commit**: require clean scope, intentional staged files, and checks matching
  the changed risk tier. Do not run deploy checks for commit-only work.
- **Push**: verify branch/upstream, run any missing checks expected before CI,
  and push only the current intended branch.
- **PR/merge**: include the checks above plus CI status or clearly disclose that
  CI was not available.
- **Deploy**: confirm target, run build/test evidence appropriate to the risk,
  deploy only when authorized, then verify the deployed URL or artifact.
- **Handoff**: report diff scope, checks run, skipped checks, known risks, and
  next command or recovery path.

## Speed Rules

- Use repository-defined commands first: package scripts, Makefile, justfile,
  task runner, monorepo filters, affected/changed-test modes, and CI hints.
- Prefer cached and targeted checks when risk is low; escalate to full-suite
  checks for lockfile/dependency changes, shared build config, auth/data/API
  changes, broad refactors, flaky focused results, or production deploys.
- Reuse running dev servers when healthy. Start a new server only when needed
  for verification, and stop or report long-running sessions clearly.
- Do not ask for confirmation for routine checks when the user already asked to
  commit, push, or deploy. Ask only when the target is ambiguous, the operation
  is destructive, production-impacting beyond the request, or expected to take a
  long time with no targeted alternative.
- If a full check is slow and a targeted check covers the changed surface, run
  the targeted check first and disclose whether broader CI/build coverage
  remains pending.

## Decision

Proceed only when the diff matches the requested scope, evidence covers the
highest-risk touched surface, failures are unrelated or disclosed, key
interactions still work, visual changes have browser evidence when relevant,
the deploy target is known and reachable, and risky changes have an obvious
rollback or recovery path.

Use this compact decision format:

```text
Action/target:
Changed scope:
Risk tier:
Checks run:
Checks skipped and why:
Failures:
Decision:
Rollback/recovery:
```

## Commit And Deploy Hygiene

- Use concise commit messages describing the behavior or docs changed.
- Push the current branch only when asked or when repo policy requires it.
- Deploy only when asked or already authorized by the task.
- After deploy, verify production/preview URL and report commit SHA, deploy URL,
  checks run, skipped coverage, and any residual risk.
