---
name: firebase-security-rules
description: Audit, implement, or debug Firebase security and access-control boundaries. Use when the user asks about Firestore Rules, Firebase Auth authorization, permission-denied errors, custom claims, Admin SDK endpoints, service-account env vars, Spark vs Blaze billing assumptions, emulator/rules tests, production data access guarantees, or whether a Firebase-backed app is actually secure.
---

# Firebase Security Rules

## Overview

This skill separates Firebase capability questions from actual deployed access
control. Use it for Firebase Auth, Firestore Rules, Admin SDK endpoints,
service-account setup, Spark/Blaze claims, or "is this secure?" questions.

## Required Context

For any repo, first locate the Firebase config, rules files, backend Admin SDK
entrypoints, deployment target, and environment variable source. Use
`$firebase-account-management` when the task is primarily account lifecycle,
Auth users, providers, custom claims, or admin user management.

Use `$efficient-execution` for scoped security work: start with the rule or
endpoint that gates the reported access path, then expand only to adjacent
collections, storage buckets, claims, or Admin SDK calls sharing the same
authorization invariant.

For Coin Quest Ledger specifically, read:

- `SECURITY_AND_FIREBASE_RULES.md`
- `ACCOUNT_MANAGEMENT_IMPLEMENTATION.md`
- `ADMIN_PORTAL_IMPLEMENTATION.md` when Admin is involved
- `data-contracts.md`
- `firestore.rules`
- `firebase.json`
- API files under `api/` when privileged backend behavior is involved
- `.github/workflows/test.yml` and `DEPLOYMENT_AND_ROLLBACK_RUNBOOK.md` when deploy
  or secrets are involved

## Core Rules

- Do not infer plan limits from vibes. Verify Spark/Blaze/billing-sensitive
  claims with local config, CLI output, or official Firebase/Google docs.
- Firebase Auth signup/login and Firestore CRUD can work on Spark within quotas.
  Blaze is only required for features or quota paths that require billing.
- Client SDK permissions are controlled by Security Rules; Admin SDK bypasses
  rules and must be protected by server-side authentication/authorization.
- `?test=1`, local gates, and browser-only checks are regression helpers, not
  production security.
- Public Firestore reads/writes are real public access, even if the UI hides the
  data.
- Display privacy flags are not database authorization.
- Do not deploy rules casually; treat rules deploys as production changes with
  rollback notes.

## Test Strategy

Choose the smallest trustworthy security evidence:

- **Static/rules syntax:** inspect `firestore.rules`, `storage.rules`,
  `firebase.json`, and run repo-defined lint/syntax checks.
- **Local behavior:** use Firebase Emulator when available for allow/deny cases,
  especially owner/admin/public access.
- **Scoped live check:** use only when emulator coverage is absent or the bug is
  deployment-specific; use test accounts and avoid destructive production data.
- **Deploy verification:** confirm project id, deploy target, rollback command,
  and post-deploy access behavior.

Never count hidden UI, `?test=1`, or local-only gates as production security
evidence.

## Workflow

1. Identify the question: Auth provider, rules access, Admin SDK endpoint, billing
   plan, env vars, deploy, or hardening.
2. Inspect actual repo files and deployed/configured project identifiers.
3. Distinguish three layers in the answer or patch:
   - Firebase Auth identity.
   - Firestore/Storage Security Rules for client SDK access.
   - Admin SDK backend operations that bypass rules.
4. If changing rules, update docs and plan a Firebase rules deploy:
   `npx firebase-tools deploy --only firestore:rules --project <project-id>`.
5. If changing Admin SDK endpoints, verify token checks, allowlists/roles,
   audit logging, env readiness, and destructive-action confirmation.
6. Verification depends on risk:
   - syntax/docs: `git diff --check`
   - app behavior: targeted tests or `npm test`
   - live security/rules: Firebase emulator or carefully scoped live test account
   - deploy/rollback: follow the repo deployment runbook

## Closeout

Report the project id checked, rules/endpoints touched, allow/deny cases tested,
emulator or live evidence used, deploy/rollback status, and residual security
risk.
