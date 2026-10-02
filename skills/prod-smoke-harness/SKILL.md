---
name: prod-smoke-harness
description: Set up, document, run, or audit safe production/preview smoke harnesses for web apps across projects. Use when the user asks for "use harness", "set up harness", "prod smoke", "can we smoke test production", authenticated smoke checks, test-account policy, Playwright/browser smoke automation, production screenshot evidence, or verification after deploys and release-gate checks.
---

# Prod Smoke Harness

## Overview

Use this skill to create or run a project-safe smoke harness for live or preview environments. The pattern is global, but credentials, routes, permissions, and cleanup are project-specific; never assume one project's smoke account or harness works everywhere.

## Core Rules

- Prefer a dedicated dummy smoke account with the least privilege needed.
- Do not use personal/customer accounts, production customer data, or credentials from unrelated projects for routine smoke checks. A dedicated privileged test account is appropriate only when its role is explicitly authorized and required by the flow under test; keep its credentials in the approved secret store.
- Mutate production data only when existing user/project authorization covers the action and the harness explicitly allows it with cleanup or reset steps. Harness configuration alone does not grant permission.
- Keep secrets out of committed files and final messages. Use documented dummy credentials only when the project owner has approved them.
- Use `$release-gate` for commit/push/deploy decisions and `$snapshot` for visual evidence.
- If no approved smoke account or safe creation path exists, stop and ask the user before attempting authenticated production checks.

## Discover Existing Policy

Before creating anything, inspect the project:

- `README.md`
- `docs/playbook.md`
- `docs/memory.md`
- `docs/qa-coverage.md`
- deploy config such as `vercel.json`, `.openai/hosting.json`, Netlify config, Firebase config, or package scripts
- existing e2e helpers under `tests/e2e`, `playwright*.config.*`, `tools/`, or similar
- auth/account docs, seed scripts, and emulator/UAT docs

Record:
- production and preview URLs;
- auth providers and roles;
- existing smoke accounts or test tenants;
- allowed live mutations;
- reset/cleanup path;
- routes that prove the deployed feature works;
- console/network failure policy.

## Setting Up A Harness

When the user asks to set up a reusable harness, add the smallest project-native structure:

- A project doc such as `docs/prod-smoke-harness.md`, or update the existing playbook/memory if that is the local pattern.
- A project-native Playwright spec, script, or package command only if repeated automation is expected.
- Reuse existing workflow/harness variable names before introducing new ones.
  For a new harness without a naming convention, examples include:
  - `PROD_SMOKE_URL`
  - `PROD_SMOKE_USERNAME`
  - `PROD_SMOKE_PASSWORD`
  - role-specific variants when needed
- A clear list of non-mutating checks and any approved mutating checks.
- Cleanup/reset instructions for every allowed mutation.

Do not add a permanent test account, secret, or admin role in code. If account creation is required, use the project's admin path, seed tooling, or documented backend with explicit user approval.

## GitHub Actions Credentials And Target

When smoke checks run through Actions, read the workflow and harness for the
exact secret names and repository/environment scope. Check secret names and
provisioning timestamps without retrieving or printing values. Listed secrets
may still be unavailable to a job because of its environment or triggering event.

Missing values belong in the secret store, not in chat or committed fixtures.
Give the user the exact names and settings destination; the credentials must be
for the approved application test account. After provisioning, verify real
sign-in rather than treating secret presence as a pass. Do not silently skip
required authenticated checks when credentials are missing.

Before rerunning, inspect workflow side effects and verify the intended branch,
SHA, deployment URL, and deployed build when identifiable. Do not dispatch
against a stale default branch. For failed-run diagnosis and repair, use
`$github-actions-repair`.

## Running A Harness

Scope the following checks to the requested change and existing harness contract.
For a credential/setup-only repair, a successful run of the existing harness
that proves authentication and its required routes can provide the evidence;
reuse its reports rather than adding a separate full-site or viewport audit.
Preserve required harness checks. Add visual evidence when the change affects
layout, media, interaction, or the user explicitly requests screenshots.

1. Identify the deploy target and commit/build under test.
2. Run an HTTP smoke first:
   - expect success status;
   - verify content type and key security/cache headers when relevant.
3. Run a browser smoke:
   - capture console errors;
   - capture failed requests;
   - verify the expected title or app shell;
   - verify the primary route or feature touched by the change.
4. Run authenticated smoke only with an approved smoke account:
   - sign in;
   - verify signed-in identity;
   - exercise only safe routes/actions;
   - avoid destructive or irreversible actions.
5. When visual evidence is relevant, capture `$snapshot` evidence:
   - use a wide viewport for desktop evidence;
   - include mobile/tablet when the change is responsive;
   - include enough surrounding context to prove layout and state.

## Failure Policy

Treat these as blockers unless proven unrelated:
- deploy URL does not return a successful HTML response;
- app shell fails to render;
- auth fails for the smoke account;
- expected route/feature is missing;
- app console errors;
- failed script, stylesheet, API, auth, data, media, or asset requests;
- visual snapshot shows the wrong route, stale build, loading-only shell, or unauthenticated gate when authenticated evidence was required.

Classify and disclose possible noise:
- websocket or long-poll aborts caused by closing the browser after successful assertions;
- analytics/ad-block failures irrelevant to the product flow;
- expected 404 probes from framework internals.

Do not hide noise; label it and explain why it is not release-blocking.

## Closeout Format

Report compactly:

```text
Target:
Commit/build:
Harness account/role:
Checks:
Snapshot:
Failures/noise:
Skipped:
Decision:
```

For a new harness setup, include the files changed and the command future agents should run.
