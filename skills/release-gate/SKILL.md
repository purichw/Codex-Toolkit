---
name: release-gate
description: Fast, risk-tiered verification before commit, push, deploy, release, merge, PR, or handoff. Use when the user asks for a final check, readiness check, commit, push, deploy, ship, release, merge, PR, handoff, or "is this safe"; also use after substantial code, UI, data, auth, configuration, or deployment changes before publishing.
---

# Release Gate

Block avoidable releases with the smallest trustworthy evidence set. Optimize for
speed by separating commit, push, and deploy gates, using targeted checks first,
and escalating only when the diff increases risk.

Use `$efficient-execution` when the user asks to make commit/push/deploy faster
or when the gate is taking longer than the risk justifies.
Use `$usage-budget-gate` before broad release checks when the correct depth is
unclear or the user asks to control usage.

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

## Hard Stops

- **Rollback-like work**: if the diff follows rollback, revert, reset, remove,
  undo, discard, back-out, or mid-work direction changes, use
  `$rollback-guardrail` before releasing. Do not commit, push, deploy, or hand
  off until the checkpoint path, restore note, impact, and follow-up
  verification are known.
- **Unresolved parking lot**: stop when `docs/rollback-parking-lot.md` or an
  equivalent restore note contains unresolved items that affect the release
  surface, unless the user explicitly accepts shipping with those items parked.
- **Prototype/component not wired**: stop when a new Claude/Figma/prototype UI
  component, handoff, or standalone export exists in the diff but the live app
  route has no screenshot, snapshot, smoke test, or interaction evidence proving
  that it renders and behaves in the real product.
- **Removed verification**: stop when rollback-like work deletes or bypasses
  tests, smoke coverage, route checks, or snapshots for behavior that is still
  expected product scope.

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
  Use `$uat-environment` when production-like preview/UAT evidence is needed
  before promotion.

## Check Packs

Use these as starting packs, then adapt to repo-defined commands:

- **Docs-only:** inspect diff, run `git diff --check`, docs lint/build when the
  repo defines one, and confirm no generated runtime artifact changed
  accidentally.
- **Frontend UI:** targeted lint/typecheck/build, browser route check, console
  and failed request check, `$snapshot` evidence when visual, `$mobile-web-qa`
  when responsive/mobile risk exists, `$ui-state-matrix` for non-happy states,
  `$interaction-flow-qa` for journeys, and `$product-ux-contracts` when real UX
  contracts could be lost.
- **Claude parity:** use `$claude-to-a-tee`; require rendered reference/app
  comparison and measured parity evidence before release.
- **Forms/data-dense/accessibility:** use `$form-flow-ux`, `$data-dense-ux`, or
  `$accessible-interaction` when those surfaces are touched; verify the relevant
  state, flow, keyboard/focus, and snapshot evidence before release.
- **Consistency/consolidation:** use `$consistency-audit` and
  `$design-system-guardian` when shared primitives, duplicated components, or
  site-wide UI patterns are changed; verify affected usages keep layout,
  dimensions, states, and behavior.
- **Firebase/rules/auth:** use `$firebase-security-rules` or
  `$firebase-account-management`; run tests/emulator or scoped live checks
  appropriate to risk, and document deploy/rollback path.
- **UAT/preview promotion:** use `$uat-environment` for T3-T5 changes that need
  production-like verification. Record UAT URL, build/version, data fixture,
  auth mode, roles tested, skipped checks, and rollback.
- **Generated image/audio assets:** run the relevant audit/check scripts, verify
  data mappings, inspect representative rendered UI, and avoid broad
  regeneration unless requested.
- **Production media/assets:** use `$production-asset-smoke` after deploy or
  preview promotion when the diff touches images, videos, CSS backgrounds,
  generated assets, CMS media, external embeds, service-worker asset handling,
  or placeholder/fallback logic. A local screenshot or page-level HTTP 200 does
  not prove deployed media is healthy.
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
  deploy only when authorized, then verify the deployed URL or artifact. For
  production deploys with UI/auth/data/admin/config risk, prefer UAT/preview
  evidence before promotion.
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
- Do not require UAT for docs-only or tiny non-runtime changes. Use it where it
  reduces production risk, not as a blanket ceremony.

## Reusable Evidence

Reuse previous evidence only when it still proves the current diff: same commit
or changed files, same dependency/build config, same target URL or artifact,
same reference hash, same viewport/auth/data state, and no relevant failures
since the evidence was captured.

Good reuse examples: a still-healthy dev server for the same branch, a Claude
reference manifest with the same HTML SHA, targeted tests already run after the
latest edit, or CI for the exact pushed commit. Stale screenshots, old preview
URLs, pre-hydration captures, and checks run before the last relevant edit are
not release evidence.

## Decision

Proceed only when the diff matches the requested scope, evidence covers the
highest-risk touched surface, failures are unrelated or disclosed, key
interactions still work, visual changes have browser evidence when relevant,
the deploy target is known and reachable, and risky changes have an obvious
rollback or recovery path. If rollback-like work happened during the task, the
decision must include the rollback checkpoint path, restore note status, and
whether any parked work is intentionally shipping.

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
