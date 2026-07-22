---
name: firebase-account-management
description: Design, audit, debug, or explain Firebase account creation and account management flows. Use when the user asks about Firebase Auth users, signup/login, Google/email-password providers, Firestore user profiles, admin edit/delete/create operations, Firebase Admin SDK, service accounts, custom claims, security rules, Spark vs Blaze billing requirements, or whether admins can manage users/data in a Firebase-backed app.
---

# Firebase Account Management

Keep billing, permissions, and architecture separate. Do not claim that a Firebase
admin feature requires Blaze unless current official Firebase docs or the active
project state proves that exact feature requires billing.

## First Principle

Spark can support Firebase Authentication and Firestore reads/writes/deletes
within free quotas. Account creation and admin CRUD over Firestore documents do
not automatically require Blaze.

Blaze is about billing-enabled capacity and features that require a billing
account. It is not a blanket prerequisite for:

- email/password signup;
- Google sign-in;
- reading or writing Firestore user/profile documents within quota;
- admin UI edits that are authorized by Firestore Security Rules;
- server-side user management through Firebase Admin SDK when the trusted server
  runs on an already-available backend such as Vercel or another separately
  billed/runtime-managed backend.

## Verify The Actual Project

1. Identify Firebase project id, app config, SDK versions, and runtime surfaces.
2. Inspect Auth providers, Firestore collections, user/profile document shape,
   security rules, backend API routes, and service-account usage.
3. Check whether admin actions target Firebase Auth users, Firestore documents,
   Storage files, custom claims, or app-local state. These have different
   permission paths.
4. Check billing state directly when the question is about Spark vs Blaze:
   `gcloud beta billing projects describe <project-id> --format=json`.
   `billingEnabled: false` means the project is not Blaze-enabled.
5. For billing-sensitive claims, verify current official Firebase docs because
   product limits and plan gates can change.

## Permission Model

Separate these paths:

- **Client SDK + Rules**: Browser/mobile code can create accounts and edit
  Firestore documents when Auth state and security rules allow it.
- **Admin SDK + Service Account**: Trusted backend code can manage Auth users,
  bypass Firestore rules, set custom claims, or perform destructive admin tasks.
  Protect this behind server-side authorization.
- **Firebase Console**: Project owners/editors can manually manage data/users
  according to Google Cloud IAM and Firebase Console permissions.
- **App Admin UI**: App-level admin roles are custom product logic. Verify the
  role source, allowlist, claims, rules, and backend checks.

Do not expose Admin SDK credentials to client code. Do not rely on hidden UI
controls as authorization. Security must live in Firestore Rules and trusted
server checks.

Use `$firebase-security-rules` when the account flow depends on Firestore/Storage
rules, Admin SDK endpoint authorization, service-account env vars, or production
access guarantees.

Use `$snapshot` automatically before the final response when Firebase account
work includes a visible signup/login/recovery/profile/admin account-management
UI, responsive account flow, or visual audit. Do not wait for the user to ask.
If the task is security/billing/docs-only and no UI can be rendered, state that
no fresh snapshot was available.

Use `$efficient-execution` to avoid over-auditing Firebase: map the exact
operation layer first, then verify only the provider, rule, endpoint, billing, or
profile path that can affect that operation. Escalate to official docs or live
project checks for billing-sensitive or recently changed platform claims.

## Operation Matrix

Map the requested operation before designing or changing code:

| Operation | Primary layer | Verify |
| --- | --- | --- |
| Signup/login/recovery | Firebase Auth + client UI | provider config, authorized domains, Auth state, profile creation |
| User profile edit | Firestore document + rules | owner/admin allow/deny, validation, stale session |
| Admin edit/delete user data | App role + backend or rules | server-side auth, audit log, recovery/tombstone |
| Manage Auth users/custom claims | Admin SDK backend | service account, allowlist/roles, token refresh |
| Storage/avatar/media access | Storage rules + metadata | read/write rules, file ownership, cleanup |
| Billing/plan question | Firebase/GCP project state | official docs or live billing state |

## Spark vs Blaze Decision

Use this decision flow:

1. Is the feature simple Auth or Firestore CRUD within quota? Spark may be
   enough.
2. Does it exceed no-cost quotas or need paid overflow? Blaze is needed.
3. Does it use a Firebase/Google Cloud feature that explicitly requires billing?
   Blaze is needed for that feature.
4. Does it require privileged user management? Use Admin SDK on a trusted
   backend; Blaze is not automatically the deciding factor unless the chosen
   backend or Google Cloud/Firebase runtime requires billing.
5. Is the backend Firebase Cloud Functions or another Firebase-managed runtime?
   Check the current Firebase plan requirements for that runtime before
   asserting Spark support.

When unsure, say what is verified, what is inferred, and what must be checked in
Firebase Console or official docs.

## Build Or Audit Checklist

- Auth providers enabled and authorized domains configured.
- Signup/login/recovery flow creates both Auth user and app profile document.
- Public ids, usernames, display names, and character ids have clear uniqueness
  rules and tombstone/reclaim behavior when relevant.
- Firestore Rules enforce owner/admin reads and writes.
- Admin UI authorization is checked server-side for privileged actions.
- Admin SDK credentials are stored only in backend environment variables.
- Delete behavior is explicit: disable, soft delete, hard delete, tombstone, data
  export, and rollback/recovery implications.
- Tests cover success, permission denied, duplicate/reclaim, unauthenticated, and
  stale-session cases.
- Documentation names the actual plan, project id, env vars, and deploy/rules
  commands.
- Visible account or admin-account UI has `$snapshot` evidence before closeout.

## Closeout

Report which layer each operation used, what was verified vs inferred, billing
evidence when relevant, tests/checks run, snapshot evidence when UI was visible,
and remaining account/security risk.

## Answering Plan Questions

When asked “do we need Blaze?”:

1. Check the project billing state if local credentials allow it.
2. Identify the exact requested account/admin operation.
3. Map it to Client SDK, Admin SDK, Console, or backend route.
4. State whether Spark supports the operation in principle, what quota/feature
   limits apply, and what evidence was checked.
5. Avoid absolute billing claims without current docs or live project evidence.
