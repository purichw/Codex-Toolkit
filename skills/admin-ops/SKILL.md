---
name: admin-ops
description: Design, audit, implement, or verify admin portal, CMS, back-office, or operator workflows across projects. Use when the user asks for admin panels, admin auth/roles, dashboards, user/content lifecycle, draft/publish/restore, revisions, audit logs, destructive actions, relationship maps, privileged backend actions, Admin SDK endpoints, or admin UX that must be safe for real operators.
---

# Admin Ops

Use this skill when an admin surface can change real data, permissions, content,
accounts, or operational state. Project-specific skills should add paths,
commands, vocabulary, and contracts; this skill provides the reusable admin
workflow.

## Core Contract

Treat admin UI as an operations console, not a decorative dashboard. Every
visible action must be real, intentionally passive/status-only, safely disabled
with a current reason, removed, or explicitly deferred.

Separate:

- **identity:** who is signed in;
- **authorization:** role, allowlist, claim, membership, or server check;
- **operation:** read/write/delete/publish/restore/reset/export/import;
- **auditability:** log, revision, tombstone, confirmation, rollback;
- **UX state:** loading, empty, disabled, success, failure, partial failure.

Hidden buttons, local test gates, and read-only UI are not security.

## Required Context

Before changing admin behavior, locate:

- admin routes, shells, sidebars, dashboards, tables, forms, modals, and detail
  panes;
- auth providers, role source, allowlists, custom claims, memberships, or server
  authorization checks;
- data contracts, collection/table shapes, lifecycle states, tombstones, and
  revisions;
- privileged backend routes, Admin SDK/service accounts, environment variables,
  audit logs, and destructive action confirmations;
- tests, fixtures, test-mode bypasses, seed data, deploy/runbooks, and rollback
  notes.

Use project-specific skills for domain rules, `$firebase-account-management` or
`$firebase-security-rules` for Firebase-backed admin behavior, `$claude-to-a-tee`
for exact admin UI parity, `$uat-environment` for UAT role/test-data/bypass
design, and `$release-gate` before shipping.

Use `$efficient-execution` to keep admin checks targeted: start with the changed
operation, role boundary, and data lifecycle, then expand only when a shared
admin shell, permission contract, or destructive backend path is touched.

## Operation Map

Classify the task before editing:

- **view/list/search/filter:** verify data source, pagination, empty/error state,
  and permission-filtered visibility.
- **create/edit:** verify validation, save path, conflict handling, persisted
  reload state, and audit/revision behavior.
- **lifecycle:** archive/deactivate/reactivate/restore/publish/unpublish must
  define recoverability and user-visible state.
- **destructive:** delete/reset/revoke/freeze requires backend authorization,
  confirmation, audit log, tombstone/export/rollback decision, and tests.
- **CMS/media:** draft/preview/publish, asset ownership, crop/import metadata,
  and public rendering must stay aligned.
- **relationship map:** distinguish direct records, derived relationships,
  historical links, and repeated IDs/names that may be valid.

## Workflow

1. Confirm the exact admin operation and production risk.
2. Trace read path, write path, permission path, and persisted state.
3. Preserve server-side checks for privileged actions; do not rely on UI hiding.
4. Patch shared data contracts and backend actions before UI glue when possible.
5. Keep admin UX dense, clear, reversible where possible, and explicit about
   destructive operations.
6. Verify success, failure, denied, loading, empty, stale session, reload, and
   partial data states.
7. Update admin docs, data contracts, runbooks, or architecture maps when
   behavior changes.

## Verification

Use the smallest evidence that covers the risk:

- copy/layout only: syntax/lint plus browser spot-check;
- admin UI state: targeted browser/e2e check with console/network inspection;
- data/lifecycle: unit or integration tests plus reload/persistence check;
- auth/permissions: allow/deny tests with real role boundaries or emulator;
- UAT/admin preview: auth may be bypassed only when auth is not the feature
  under test, and only through UAT/test-only gates that cannot affect production;
- destructive/backend: server authorization, audit log, recovery/tombstone, and
  rollback evidence;
- deploy/handoff: use `$release-gate`.

## Closeout

Report the operation, files/data paths touched, auth path checked, lifecycle or
rollback decision, tests/evidence, docs updated, project-specific skill used,
and residual admin risk.
