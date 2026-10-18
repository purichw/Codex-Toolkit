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
Use `$github-actions-repair` when a GitHub Actions failure needs diagnosis or
repair; return here to assess readiness from the resulting evidence.
Use `$github-actions-usage` when reducing Actions minutes or storage is in scope.
Preserve required coverage and distinguish elapsed time from summed job usage;
do not dispatch duplicate full CI on the same candidate without new evidence.

For push/CI/build/promotion delays, apply the project's measured checkpoints or
`$efficient-execution` → Release Delay Checkpoints before waiting. A failed
check, missing trigger, unexpected cancellation, repeated failure or breached
checkpoint switches the work to diagnosis; it does not justify blind retries,
extra pushes or bypassing a required gate. Confirm remote state before repeating
an operation with an uncertain result. Return to this gate after repair.

## Authorization Before Action

Before every push or deploy, require an explicit user request or confirmation
covering the action, current changes, and target. If absent or ambiguous, ask
and wait. Edit/fix/test/commit/release-preparation requests, standing repo policy,
handoffs, passed checks, and approvals from earlier completed tasks do not grant
permission. Readiness is not authorization.

Push and deploy are separate permissions. Check branch/workflow auto-deploy
triggers before pushing; a push-only request does not authorize preview or
production deployment. Explain the target and obtain the missing approval
before triggering it, including through dispatches, reruns, or other indirect
commands. A deploy-only request does not authorize a separate push. Do not ask
again for the exact action and scope already explicitly requested. Finish
local-only work without publishing and report what was not pushed/deployed.

## Fast Protocol

1. Confirm the intended action and target: commit, push, PR, preview,
   production deploy, package, static artifact, docs-only, or handoff. If the
   target is obvious from the request and repo state, state the assumption and
   continue with checks; this does not supply missing push/deploy authorization.
2. Inspect scope before checks: `git status --short`, staged files, unstaged
   files, recent diff, and changed filenames. Do not include unrelated user
   changes without explicit intent.
3. List all active deliverables and their acceptance criteria, including docs,
   generated artifacts, installed copies, and the requested publishing endpoint.
   Classify the highest-risk touched surface first: docs/assets-only, narrow code,
   frontend UI, shared runtime behavior, API, data model, auth, build config,
   deployment config, migrations, environment variables, tests, or generated
   assets.
4. Map each deliverable to proportionate evidence; one check may cover several.
   Mark required checks and optional broader coverage before running them.
   When behavior changes, search the relevant tests, fixtures, and CI entrypoints
   for assumptions about the old behavior, not only changed filenames. Examples
   include visible-item counts, pagination, readiness, and selector cardinality.
   Distinguish affected consumers from similar components whose contracts remain
   unchanged. Update affected expectations and run their focused checks before
   push, including relevant integration tests located in a broader CI suite.
   Prefer targeted commands for changed packages/files/tests before full suites. Run
   independent checks in parallel when possible.
5. Collect terminal results for required operations. Summarize evidence,
   failures, and skipped checks. A queued command or pending CI is not a pass.

## Hard Stops

- **Risky rollback-like work**: use `$rollback-guardrail` to classify possible
  work loss, history rewrites, data loss, or feature removal. Require its
  checkpoint, restore note, approved impact, and verification for the risky
  path. A pause or routine reversible edit with no work loss does not require
  a checkpoint; record that classification without manufacturing parked work.
- **Unresolved parking lot**: stop when `docs/rollback-parking-lot.md` or an
  equivalent restore note contains unresolved items that affect the release
  surface, unless the user explicitly accepts shipping with those items parked.
- **Required integration not wired**: when live-product integration is an
  acceptance criterion, stop if a new component/prototype has no route and
  interaction evidence proving it works there. An explicitly standalone export
  or image-only handoff is checked as that artifact; do not invent a live-app
  integration requirement for it.
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
- **CI workflow/setup:** validate the changed YAML/shell and inspect affected
  triggers, permissions, checkout refs, and timeouts. Verify the relevant remote
  run containing the fix. For setup-only changes, targeted checks plus that run
  can provide evidence without a duplicate full local suite or new UI audit;
  preserve all existing required checks. Use `$prod-smoke-harness` when real
  authenticated deployment checks are part of the acceptance criteria.
  For changed scope/skip logic, test unavailable baseline evidence, mixed/renamed
  runtime paths and failed/cancelled/missing dependencies. Keep the final check
  present and fail closed; a documented docs-only skip must identify the exact
  passing runtime baseline. A billing block before runner allocation leaves
  remote proof pending even if local checks pass.
- **Frontend UI:** targeted lint/typecheck/build, browser route check, console
  and failed request check, `$snapshot` evidence when visual, `$mobile-web-qa`
  when responsive/mobile risk exists, `$ui-state-matrix` for non-happy states,
  `$interaction-flow-qa` for journeys, and `$product-ux-contracts` when real UX
  contracts could be lost.
- **Reference parity:** use `$reference-to-a-tee`; compare the rendered app
  with authoritative rendered HTML or inspected image references. Apply its
  mode-aware measurements, uncertainty rules, and snapshot evidence before release.
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
  and collect results from required local checks and already-running reviews of
  the release candidate before pushing the current intended branch. Resolve
  findings together; use `$efficient-execution` for batching and failed-run
  recovery. Checks that require the push itself remain explicitly pending.
- **PR/merge**: include CI status. Missing, pending, or failed required CI blocks
  merge/readiness; a permitted draft PR can report pending evidence without
  claiming the merge gate passed.
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

Reuse evidence only when all conditions relevant to the claim still match:
source including staged/unstaged edits, dependency/build config, actual served
build or artifact version, reference hash, viewport, and auth/data state. A
matching commit or URL alone is insufficient; refresh checks affected by edits.

Good reuse examples: a still-healthy dev server for the same branch, a Claude
reference manifest with the same HTML SHA, targeted tests already run after the
latest edit, or CI for the exact pushed commit. Stale screenshots, old preview
URLs, pre-hydration captures, and checks run before the last relevant edit are
not release evidence.

For CI evidence, record the run link/ID, attempt, tested SHA, relevant jobs, and
terminal conclusions. Verify that the trigger/ref covers the release candidate;
for PR merge or merge-queue runs, identify the candidate merge revision as well.
For deployment checks, also match the environment and deployed build/URL when
identifiable. A green workflow whose required test jobs were skipped does not
prove that coverage ran; confirm the required coverage actually executed.
Secret presence alone does not prove a required authenticated smoke passed.

For an explicitly supported docs-only mode, unchanged runtime evidence may be
inherited from the exact eligible base. Verify the selector's baseline run and
attempt, documented intentional skips, and successful stable aggregate gate.
Report this as validated evidence reuse; do not claim the skipped suites ran.
An unexplained skip or missing baseline still blocks the gate.

Record monitoring source and deployed target separately. A credential-bearing
monitor can pass against an older production deployment while a new candidate's
CI is still failing. That proves the monitor's access and checked routes, not
the candidate's readiness or promotion. Reuse each result only for its scope.

## Decision

An action gate passes only with clean scope, all active deliverables tracked,
and every acceptance criterion due before that action met with current evidence.
Its required checks must have passed; failed, blocked, pending, or unrun checks
required before that action block it. Disclosure is not a pass. Do not reclassify a
failed required check as optional merely to ship. An unrelated failure needs
evidence of non-impact and must not be a required gate for the target action.

Keep action readiness separate from whole-task completion: an authorized push
may be needed to start CI, but required post-push CI and deployment checks stay
pending until their terminal results are known. Report intermediate completion
honestly. Verify requested remote endpoints, not just successful local commands.
Whole-task completion requires every active deliverable and all required
post-action checks to be complete. Use `$efficient-execution` for tracking and
completion rules.

For relevant UI work require current visual/interaction evidence. For risky
changes require recovery; for risky rollback include checkpoint, restore-note
status, and explicitly accepted parked scope. A changed scope must be explicit,
not a silent omission of an unfinished deliverable.

Use this compact decision format:

```text
Action/target:
Changed scope:
Risk tier:
Deliverables / acceptance / evidence:
Required checks and terminal results:
Checks run:
Checks skipped and why:
Failures:
Decision:
Requested endpoint / confirmed result:
Rollback/recovery:
```

## Commit And Deploy Hygiene

- Use concise commit messages describing the behavior or docs changed.
- Push only with explicit user authorization for the current changes and
  branch; otherwise ask and wait, even if repo policy normally requires a push.
- Deploy only with explicit user authorization for the current changes and
  environment; otherwise ask and wait, including for auto-deploy triggers.
- After deploy, verify production/preview URL and report commit SHA, deploy URL,
  checks run, skipped coverage, and any residual risk.
