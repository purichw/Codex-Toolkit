---
name: prod-smoke-harness
description: Set up, document, run, or audit safe production/preview smoke harnesses for web apps across projects, especially after deploys, release-gate checks, authenticated smoke needs, test-account policy questions, Playwright/browser smoke automation, production screenshot evidence, or requests like "use harness", "set up harness", "prod smoke", or "can we smoke test production".
---

# Prod Smoke Harness

## Overview

Use this skill to create or run a project-safe smoke harness for live or preview environments. The pattern is global, but credentials, routes, permissions, and cleanup are project-specific; never assume one project's smoke account or harness works everywhere.

## Core Rules

- Prefer a dedicated dummy smoke account with the least privilege needed.
- Never use real user accounts, personal accounts, admin accounts, production customer data, or private credentials for routine smoke checks.
- Do not mutate production data unless the harness explicitly allows it and includes cleanup or reset steps.
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
- Environment variables for non-dummy credentials:
  - `PROD_SMOKE_URL`
  - `PROD_SMOKE_USERNAME`
  - `PROD_SMOKE_PASSWORD`
  - role-specific variants when needed
- A clear list of non-mutating checks and any approved mutating checks.
- Cleanup/reset instructions for every allowed mutation.

Do not add a permanent test account, secret, or admin role in code. If account creation is required, use the project's admin path, seed tooling, or documented backend with explicit user approval.

## Running A Harness

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
5. Capture `$snapshot` evidence:
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
