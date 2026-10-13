---
name: github-actions-usage
description: Measure and reduce GitHub Actions runner minutes, repeated CI work, and artifact/cache usage while preserving required coverage. Use for Actions usage or cost audits and workflow optimization; route actual failed runs to github-actions-repair.
---

# GitHub Actions Usage

Optimize the measured source of usage while preserving the release contract.
For a narrow follow-up, inspect only the affected workflow and consumers; a
historical audit is appropriate when requested or needed to choose an investment.
Use `$github-actions-repair` for causal failures and `$release-gate` before
authorized publication. This skill does not authorize spending, visibility,
credential, retention, or production changes beyond the user's request.

## Measure the right quantity

- Separate workflow elapsed time, summed executed job time, per-job rounded
  minutes, and actual billed amount. Sharding can improve elapsed time while
  increasing total runner work. A current artifact-size snapshot is not billed
  GB-hours. Failed/cancelled executed jobs still consume resources; skipped or
  unallocated jobs do not become usage merely because a run exists.
- Use a bounded window, all run attempts, paginated jobs, and explicit excluded
  or incomplete records. Group by workflow/event/mode/runner and inspect the
  latest 3–5 comparable successes for a current baseline. Keep collection time,
  method, tested SHA and run links with the result. Read specific steps to locate
  setup, download, build, test and upload costs.
- Prefer billing usage/report data for monetary claims. Metadata duration is an
  estimate, not an invoice. Gross usage and discounts can coexist with zero
  billed amount and an exhausted included allowance. Never call zero billing
  proof of remaining quota. Check job annotations for pre-run billing blocks.
- Repository visibility is time-dependent. If it changed, confirm the timestamp
  from available audit evidence and split interpretation at that boundary.
  Today's public flag cannot establish historical free/private usage. Record
  unknown history instead of inventing it. Do not change visibility to avoid
  costs without explicit authorization. A visibility/runner change can also
  confound before/after speed comparisons.
- Recheck current official pricing/limits when relevant; do not copy remembered
  rates or future pricing proposals as effective policy. Use existing read-only
  billing access; missing CLI scope does not authorize broadening credentials.
  A scoped browser view is a useful fallback. Keep private billing records out
  of public repo documentation unless the user explicitly requests publication.

## Choose changes from evidence

1. Avoid duplicate work before adding caching or more runners. Compare same-SHA
   events and attempts; a scheduled repeat, distinct build mode, required merge
   revision or authenticated deployment check can be legitimate. Reuse valid
   evidence instead of blindly dispatching again after push. Preserve intended
   cron coverage and unrelated runs.
2. Use a conservative allowlist for cheap docs-only checks. Keep required check
   names present; top-level path skips can leave required checks pending. Require
   proof that unchanged runtime was tested on the exact base, with complete job
   results. Missing history/API evidence, unknown paths and manual full runs
   must fall back to full coverage. Rename detection must not hide a runtime
   deletion. The aggregate gate must explicitly validate intended skips and
   reject missing, failed, cancelled or unexpectedly skipped dependencies.
3. Install only the browser engines actually used by each suite. Trace defaults,
   environment/CLI overrides and wrapper scripts. Chromium headless-shell-only
   installation requires a headless launcher without a full-browser channel or
   extension requirement. Keep cross-browser coverage where it is exercised.
4. Keep deterministic dependency installs and correct cache keys. setup-node's
   npm cache stores package downloads, not `node_modules`; restoring that folder
   before `npm ci` is wasteful. Measure browser cache transfer plus OS dependency
   setup before adding it. Never cache secrets or authenticated application state.
5. Move builds to shared artifacts only when all flags, toolchains and generated
   outputs match consumers. Preserve isolated fixtures when tests mutate files.
   More shards, reusable YAML, or a faster wall clock alone do not demonstrate
   lower usage. Avoid redundant archive transfer or broad dependency upgrades.
6. Scope artifacts and future retention to actual debugging/recovery needs.
   Historical deletion does not refund already accrued storage. Preserve backups
   and failure evidence; do not delete existing artifacts/caches as a default
   optimization, or change recovery policy to meet an unrelated usage target.

## Verify and report

Run focused selector/gate regressions for routing changes, YAML/Actions lint,
and affected consumer checks. For install-only edits, a semantic consumer audit
plus the relevant exact-SHA remote run is usually enough; avoid a duplicate full
local suite. Batch supported repairs before one remote run. Follow measured
diagnostic checkpoints, not blind polling or timeout inflation.

Record changes, preserved coverage, local and remote evidence separately.
If quota prevents runner allocation, finish local validation and report that
remote proof is blocked; don't bypass checks or buy capacity implicitly. Savings
remain estimates until comparable post-change runs support them. Estimate per
eligible run first, then project monthly impact only with observed frequency.
Update the project's runbook/AGENTS with concrete decisions and ownership;
keep project IDs, credentials and transient run histories out of this skill.

Close the rollout record after remote verification: replace stale pending or
not-yet-provisioned wording, record the final SHA/run/attempt and deployment
stage, and retain superseded failures as dated evidence. Keep full-mode proof
separate from docs-mode proof; a successful full run does not validate an unused
shortcut. Observe docs selection on the next genuine eligible change rather than
pushing an artificial benchmark. Update the canonical handoff instead of leaving
the only final receipt in an ignored local audit directory.

## Primary references

Consult relevant current sections; no need to reload all sources for every edit.

- [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [Runner pricing](https://docs.github.com/en/billing/reference/actions-runner-pricing)
- [Billing reports](https://docs.github.com/en/billing/reference/billing-reports)
- [Required check skips](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks)
- [setup-node cache](https://github.com/actions/setup-node#caching-global-packages-data)
- [npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci/)
- [Playwright CI](https://playwright.dev/docs/ci#caching-browsers)
- [Chromium headless shell](https://playwright.dev/docs/browsers#chromium-headless-shell)
- [Repository visibility changes](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility)
