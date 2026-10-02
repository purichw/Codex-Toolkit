---
name: github-actions-repair
description: Diagnose and repair failed GitHub Actions runs, recurring Run failed emails, and CI or deployment-smoke failures. Use when investigating workflow logs, missing Actions secrets, setup timeouts, or flaky checks; ordinary pre-release verification belongs to release-gate.
---

# GitHub Actions Repair

Restore meaningful checks with the smallest evidence-backed fix. Keep project
names, branches, URLs, account details, and secret values in project-specific
configuration, never in this global skill.

## Establish the failing target

- Map the notification to repository, workflow, event, branch, commit SHA, run
  ID, attempt, and failed job/step. An old email is evidence of a historical
  failure, not proof that the current revision is broken.
- Compare the failing attempt with the latest relevant runs and code changes.
  Distinguish a subsequent fix from a successful rerun of unchanged code; the
  latter alone does not prove a flaky test is repaired. Cancelled, skipped, and
  pending jobs are not successful checks.
- Prefer the available GitHub connector or authenticated `gh` CLI. Use the
  browser for evidence unavailable through those tools, such as live logs.
  Read the first causal error and surrounding lines, not just the final exit
  code or every log from every workflow.
- Before editing, inspect repository instructions and git status. If the local
  checkout is dirty or stale, use a suitable isolated checkout without copying
  unrelated changes. Verify the intended source revision and deployment target;
  the default branch may differ from the deployed branch.

Useful read-only commands, with placeholders resolved from observed evidence:

```sh
gh run list --repo OWNER/REPO --limit 10
gh run view RUN_ID --repo OWNER/REPO --json status,conclusion,headSha,event,headBranch,jobs,url
gh run view RUN_ID --repo OWNER/REPO --log-failed
gh secret list --repo OWNER/REPO --json name,updatedAt
```

If an earlier attempt matters, select that attempt explicitly. Secret listings
show provisioning metadata, not whether credentials work or are accessible to
the specific job.

## Choose the fix from the evidence

| Failure class | Decision |
| --- | --- |
| Runner, package mirror, browser download, or setup timeout | Identify the slow/failing setup step and compare observed durations. Repair that dependency path while retaining trusted sources and signature checks. Set a bounded setup/job allowance and a separate test timeout when useful; do not automatically increase every timeout or copy another runner's mirror workaround. |
| Missing secret, wrong secret scope, or rejected login | Read the workflow and harness for exact names, repository/environment scope, target URL, and account role. Check whether the triggering event can receive secrets. Verify real authentication after provisioning. |
| Product/build/assertion regression | Inspect the failing assertion and owning source at the tested SHA. Fix the actual behavior and run its targeted check before broader CI. |
| Browser-test timing or focus failure | Reproduce or establish the readiness/focus race from evidence. Wait for the relevant application state and target the intended control. Preserve the product assertion; arbitrary sleeps, catch-all retries, and wider tolerances are not a diagnosis. |
| Event, checkout, branch, or deployment mismatch | Compare trigger payload, checkout ref, job environment, and deployed revision. A green run against another branch or URL does not validate the reported failure. |

Do not silence failures by disabling workflows, removing assertions, adding
`continue-on-error`, skipping required authentication when secrets are absent,
or muting notifications unless that specific behavior change is requested and
its impact is clear. Do not bundle unrelated dependency/action upgrades or
deprecation warnings into a focused repair.

## Provision credentials without broadening access

- Use the exact variable names already consumed by the workflow and harness.
  Do not assume every project uses the same smoke-secret names.
- Check names, scope, and update timestamps without printing values. Limit any
  local configuration search to the authorized project and relevant keys; do
  not dump `.env` files, credential stores, or the full process environment.
- An application smoke account is an account on the application under test,
  not the user's GitHub login. Use the approved dedicated account with the
  needed role. For live checks, apply `$prod-smoke-harness`.
- When values are missing, provide the exact secret names and destination
  settings. Let the user enter credentials directly into the secret store;
  do not ask them to paste passwords into chat. Confirm presence, then test
  authentication. Never echo values already supplied or include them in logs,
  commits, screenshots, or the closeout.
- Check environment selection/protection and event restrictions before assuming
  a listed secret reaches a job. Preserve restrictions on untrusted fork code;
  do not expose secrets by weakening permissions or changing to a privileged
  event merely to make the test pass.

## Rerun and verify within scope

1. Inspect what the workflow will do before rerunning or dispatching it. Some
   jobs deploy, publish packages, send messages, or mutate live data. The skill
   does not grant authority for those actions; use existing user authorization
   and applicable project rules, and resolve any uncovered consequential action.
2. For a confirmed provisioning or transient infrastructure issue, rerun the
   failed jobs on the intended original revision when appropriate. For a code
   change, test the revision containing the fix. Before dispatching, verify the
   ref and inputs; never accept a stale default branch just because it is the
   default. A rerun may still execute dependencies or external side effects.
3. Normally allow one unchanged diagnostic rerun when evidence suggests a
   transient cause. If the same failure recurs, inspect it before another
   attempt. Do not retry until green or cancel unrelated runs to save time.
4. For workflow edits, inspect the diff, validate YAML/shell using available
   project tools, and verify triggers, permissions, checkout, and timeouts.
   Apply `$release-gate` for authorized publishing. Do not run all local suites
   for a setup-only change when targeted checks and the relevant remote run
   provide the required evidence.
5. Record the resulting run ID and tested SHA. Follow required runs to a
   terminal result using bounded waits and modest polling/backoff. Reuse an
   existing watcher within this authorized chat/scope; inspect live logs for a meaningful stage change or stall,
   rather than repeatedly dumping them. Report useful milestones and any
   pending evidence without implying success.
6. For deployment smoke, confirm both the checked-out revision and the actual
   deployed build/URL when the harness supports that verification. A locally
   passing harness or an HTTP 200 alone does not prove authenticated behavior.

Stop when the requested failures have a supported diagnosis and the relevant
checks pass on the intended final revision/target. If access, credentials, or a
service outage blocks that result, finish independent authorized work and name
the exact remaining blocker. Do not turn a completed repair into ongoing
monitoring or inspect other chats without the user's request.

## Closeout

Keep the report short: cause, change and destination, tested SHA/target, links
to terminal results, and any remaining blocker or skipped broader check.
Distinguish fixes made now from historical issues already fixed upstream.
A historical failure notification does not become a prediction about future
runs; claim only what current evidence proves.
