---
name: efficient-execution
description: Choose and execute the smallest quality-preserving workflow while tracking deliverables through completion. Use when the user asks to go faster, reduce usage, avoid over-auditing, prevent missed requirements, preserve unfinished work across interruptions, choose fast/standard/deep/release depth, batch checks, reuse evidence, or define reliable stop rules.
---

# Efficient Execution

Move faster by removing waste, not by removing evidence. Use this skill as a
thin operating layer with domain skills such as `$project-onboarding`,
`$release-gate`, `$reference-to-a-tee`, `$mobile-web-qa`, `$uat-environment`, or
project-specific skills.

## Core Rule

Keep the acceptance bar unchanged. Speed comes from cutting repeated discovery,
irrelevant checks, stale ceremony, serial reads that can run in parallel, and
verification that does not cover the changed risk.

Never hide skipped checks. If a check is not run, say why and what risk remains.

Track completion separately from verification depth. Cover the highest-risk
surface first, then finish every active deliverable with proportionate evidence.
Stopping additional checks does not mean the whole task is complete.

## Request Tracking And Continuity

- Keep a compact list of active requests, their acceptance criteria, status
  (`pending`, `done`, or `blocked`), and evidence. Use conversation context for
  small tasks; use an existing task note or plan for longer work when useful.
  Do not create a tracking file for every edit.
- Include requested docs, artifacts, syncs, and publishing actions as separate
  deliverables when each has its own completion condition. Record the target
  path, branch, or environment where it matters. Tracking an action does not
  authorize it; preserve the user's scope and existing authorization.
- Incorporate incoming corrections and additions while retaining unfinished
  requests. A status question does not cancel ongoing work. Replace or remove a
  requirement only when the user cancels, defers, or clearly supersedes it.
- After interruption or context compaction, recover the active list, decisions,
  completed evidence, running operations, and blockers before continuing. Check
  current source and operation state before retrying an action whose result is
  uncertain, especially a publish or data mutation.
- Before the final response, reconcile all still-active requests, including the
  latest message. Continue work that can be completed now; report actual
  blockers and remaining items explicitly without claiming full completion.

## Depth Modes

- **Fast pass:** tiny answer or edit. Read owner files and nearby selectors only,
  run `git diff --check`, and use one targeted browser/computed-style/snapshot
  check only when the change is visible.
- **Standard pass:** one component, one route, one flow, one asset batch, or
  narrow runtime logic. Read relevant source and run targeted checks for the
  touched risk.
- **Deep pass:** architecture, auth, data/admin/CMS contracts, cache/fallback
  behavior, routing, broad shared logic, migrations, destructive actions,
  broad reference reconstruction, or broad redesign. Build wider evidence before
  editing or shipping.
- **Release pass:** commit, push, deploy, PR, merge, release, or handoff. Verify
  the diff and target environment with `$release-gate`; do not repeat unrelated
  discovery.

Reference fidelity and effort are independent. An exact, isolated reference
repair can use a fast pass with current scoped comparison evidence. A skill name
or an exactness claim alone does not require deep verification; changed risks and
the scope of the claim do. Never reduce fidelity to save effort without approval.

Before expensive discovery, broad test suites, multi-route QA, or many
screenshots, state:

```text
Proposed depth:
Why:
Evidence needed:
Stop rule:
Escalate only if:
Checks intentionally skipped:
User-visible risk:
```

## Fast Loop

1. Identify the user target and all active deliverables using request tracking.
2. Classify the highest touched risk: docs/static, narrow code, runtime code,
   frontend UI, auth/data/API/config, generated assets, or production deploy.
3. Reuse evidence only when every relevant source and environment condition
   still matches; apply the evidence rules below.
4. Choose the smallest evidence path for each acceptance criterion, beginning
   with the highest risk. One check may cover several criteria. Prefer
   repo-defined targeted commands, affected-package filters, nearest tests,
   extractor manifests, and focused browser checks before broad suites.
5. Parallelize independent reads and checks. Use `rg`/`rg --files` for search
   and batch file reads. Collect every result, including failures, and keep
   operations with dependencies sequential.
6. Stop discovery once you know the owner files, data/runtime surface, relevant
   commands, affected outputs, verification path, and likely rollback. Implement
   instead of continuing to tour the project.
7. Verify the requested outcomes and apply the completion gate below before
   reporting evidence, skips, and residual risk.

## Batch Publishing And Recovery

- For an authorized push/deploy, finish the selected local checks and collect
  already-running release reviews before pushing the candidate. Combine their
  findings into one correction pass and refresh only affected evidence. Do not
  start extra reviews or full local suites merely to satisfy this rule.
- When CI fails, inspect the first causal failure and the affected assumptions
  or readiness conditions before another push. Search adjacent tests for that
  same failure pattern and run the relevant focused checks; do not use repeated
  full CI runs to discover predictable omissions one at a time. Use
  `$github-actions-repair` for GitHub Actions diagnosis.
- Before superseding an active run, check whether the new push cancels or
  restarts it. Batch remaining known corrections when practical, while keeping
  required remote checks and necessary fixes. Do not cancel unrelated runs.
- Follow remote checks with bounded waits and report meaningful phase changes,
  failures, or stalled work. Repeated unchanged polling is not task progress;
  diagnose an unexpected delay from run/step timings instead of restarting it.

## Release Delay Checkpoints

Before waiting on an authorized push/release, identify the exact revision,
operation IDs, required endpoint and next diagnostic checkpoint. Prefer the
project runbook or the latest 3–5 comparable successful runs: compare the same
workflow graph, full/docs mode, runner and workload. Reuse available evidence;
do not launch a benchmark or survey the entire history. One successful run is a
provisional reference, not a promised duration.

Use these starting checkpoints when the project has no better evidence:

| Signal | When to inspect |
| --- | --- |
| Failed assertion, timeout, rejected push/auth, wrong SHA, unexpected cancellation, or required check absent when the workflow finishes | Immediately, before another attempt. |
| Ordinary small push with no transfer/hook progress | 2 minutes; distinguish local hooks, transfer and remote acceptance. |
| Expected CI/deployment has not appeared after a confirmed push | 3 minutes; verify triggers/ref/integration before pushing again. |
| Queued operation or no observable progress | 5 minutes; read the current step/log timestamps. A stable status label alone is insufficient. |
| Active phase or total duration beyond comparable successful runs | Inspect at `max(1.5 × usual duration, usual duration + 2 minutes)`. Without a baseline, inspect build/CI at 10 minutes. |
| Production promotion still pending after build and exact-revision checks pass | 2 minutes; inspect check association and alias state. |

These are investigation thresholds, not new job timeouts, SLAs or reasons to
cancel healthy work. Adjust for evidenced long transfers, cold setup and actual
progress. A ready build held behind still-running, normally progressing CI is
an expected dependency wait.

When a checkpoint is reached:

1. Stop automatic retries/new pushes and identify the phase: local verification,
   hooks/transfer, trigger/queue, setup, test, build, required gate, promotion, or
   served-version verification. Check remote state if the previous result is
   uncertain. Preserve the run's diagnostic evidence.
2. Inspect identity, concurrency/superseding revisions and the first causal
   error from each failed job in one pass. For running work, inspect available
   progress before calling it stalled. Separate product regressions, stale test
   expectations, harness races and infrastructure problems using evidence.
3. State the blocker or observed progress, next diagnostic action and next
   bounded checkpoint. If healthy, continue the existing operation. If broken,
   fix the supported cause and refresh affected checks before one new attempt.
4. Allow one unchanged diagnostic rerun only with evidence of a transient cause.
   A repeated same-cause failure, or two failed repair cycles, requires revising
   the hypothesis and verification plan before another push/full run. Inspect
   direct consumers and batch all known corrections. Do not repeatedly rerun
   merely to obtain green; each attempt needs a supported correction or the
   permitted transient diagnostic retry.

Do not substitute force pushes, duplicate manual deployments, unrelated-run
cancellation, weaker budgets/assertions or bypassed checks for diagnosis. Use
`$github-actions-repair` for Actions evidence and `$release-gate` for readiness.
This rule does not grant access to other chats or additional publishing actions.

## Evidence And Operation Results

- Reuse evidence only when all conditions relevant to the claim match: source
  state including staged and unstaged edits, dependencies/build configuration,
  build or artifact version, target environment, reference hash, viewport,
  auth/data state, and generated manifest where applicable.
- The same commit can have a different working tree; the same URL can serve a
  different build. Either identifier alone is insufficient. After a relevant
  edit or state change, refresh the affected evidence, retaining unrelated
  evidence that remains valid.
- Track every required parallel or asynchronous operation through its terminal
  result. Check exit status and meaningful output; a launched command, session
  ID, or queued job is not proof of success. A failed check remains failed until
  fixed and rerun or explicitly reported as unresolved, never relabeled skipped.
- Confirm the requested endpoint: a created artifact exists and is usable;
  a push places the intended commit on the intended remote branch; a deploy
  reaches the intended URL with the intended version. A local success cannot
  substitute for remote evidence. Apply `$release-gate` for publishing actions.
- Resolve required running work before closeout. A dev server intentionally
  kept for the user may remain running; report its URL and status. If the user
  requests a pause or handoff, report pending operations and recovery details.

## Dependent Outputs

Inspect direct consumers and repo-defined generation or sync steps that the
change affects. Update required companion outputs within the authorized scope:
docs, catalogs, schemas, generated artifacts, installed copies, or exports as
applicable. Do not expand this into an unrelated repository audit.

When a skill update includes a maintained archive or backup, identify the
authoritative live skill and archive copy, compare their relevant contents, and
update affected catalog descriptions. Publish only when requested or already
authorized. A clean archive working tree does not establish that it matches the
live skill source. Preserve unrelated changes and repo-only aliases during
selective syncs.

## Fast Path Matrix

- **Docs/static:** inspect diff, run lightweight lint/checks only if defined or
  publishing docs as an artifact.
- **Narrow code:** read the owner files and nearest tests; run targeted
  lint/type/test first.
- **Runtime/shared code:** add or run focused regression coverage, then escalate
  to broader build/typecheck when shared contracts changed.
- **Frontend UI:** verify the changed route and primary interaction first; add
  viewport and screenshot coverage for responsive or visual-risk changes.
- **Auth/data/API/config/admin:** test allow and deny paths, persistence/reload,
  migrations/rules/env boundaries, and rollback before release.
- **Generated assets:** audit mappings and representative rendered usage before
  broad regeneration.
- **Deploy:** use `$release-gate` and verify the deployed URL or artifact; use
  `$uat-environment` for production-like evidence only when it reduces risk.

## Escalation Triggers

Run the deeper path when any of these appear:

- unknown ownership, stale docs, or conflicting handoffs;
- lockfile/dependency/build config changes;
- auth, permissions, secrets, billing, destructive operations, migrations, or
  production data risk;
- shared helpers, cross-client contracts, or generated manifests;
- broad visual-parity claims, consequential/shared responsive or accessibility
  changes, or targeted evidence insufficient for the requested visual claim;
- flaky targeted results or missing focused tests for a risky change;
- production deploy, PR merge, or user-visible release.

Stop adding checks when the acceptance criteria and relevant failure modes have
sufficient current evidence. Disclose skipped broader coverage, then apply the
completion gate. Do not keep running broad checks just because they exist.

## Do Not Save Time By

- skipping a selected skill's `SKILL.md`;
- ignoring unrelated user changes or staging unrelated files;
- using screenshots, dev servers, manifests, or build logs from stale source;
- treating UI-hidden controls as security;
- bypassing auth when auth or permissions are the feature under test;
- using production as UAT;
- shipping inert mock controls where the product needs real behavior;
- lowering safety, compliance, visual parity, or data integrity requirements.

## Completion Gate

Before declaring the task complete:

- Every active deliverable meets its acceptance criteria with current evidence;
  fixing the highest-risk item alone does not satisfy the other requests.
- Required dependent outputs are aligned, and every required operation has a
  confirmed result. Inspect the final diff/status for edits in a git repository.
- No required check is pending, failed, or silently skipped. If required
  verification is unavailable, distinguish implemented work from unverified work
  and report the blocker; disclosure alone does not make a requirement pass.
- The final response matches the active request list and distinguishes completed
  outcomes, verification, and any blocked work. Do not move authorized,
  achievable work into a suggested next step merely to end the turn.

## Closeout

Use this compact shape when speed decisions matter:

```text
Target:
Deliverables completed and evidence:
Blocked or unverified items:
Depth chosen:
Evidence reused:
Checks run:
Checks skipped and why:
Escalations triggered:
Residual risk:
Next step, only if blocked or explicitly deferred:
```
