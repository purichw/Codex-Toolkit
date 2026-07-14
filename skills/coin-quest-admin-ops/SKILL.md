---
name: coin-quest-admin-ops
description: "Use when working on Coin Quest Ledger Admin Portal operations: Super Admin auth, boards, users, lifecycle, reset, delete, publish/restore, revisions, relationship map, or admin Firebase-backed behavior."
---

# Coin Quest Admin Ops

Use `$admin-ops` for the reusable admin portal workflow. This skill is the Coin
Quest overlay: project paths, Firebase/Admin rules, data contracts, and known
admin vocabulary.

## Overview

This skill keeps `/admin/` changes aligned with the live implementation, not only
older Claude prototype notes. Use it before changing Admin Portal UI, account
lifecycle, reset/delete flows, publish/restore, or admin data loading.

## Required Context

Read these first from the repo root:

- `Memory.md`
- `ADMIN_PORTAL_IMPLEMENTATION.md`
- `SECURITY_AND_FIREBASE_RULES.md`
- `ACCOUNT_MANAGEMENT_IMPLEMENTATION.md`
- `data-contracts.md`
- `SITE_MAP_AND_INTERACTIONS.md`
- `admin/app.js`, `admin/index.html`, `admin/admin.css`
- `api/admin-delete-status.js` and `api/admin-delete-user.js` when delete/status is involved
- `firestore.rules` when permissions are involved

Use `ADMIN.md` as prototype/handoff history only. It is not the primary live
implementation runbook.

Use adjacent skills when the task crosses boundaries:

- `$admin-ops` for the global admin operation map, safety model, and closeout.
- `$coin-quest-ledger-logic` for participant, invite, settlement, board data, or
  Character ID rules surfaced in Admin.
- `$coin-quest-native-parity` when Admin changes affect shared native/web data
  contracts.
- `$firebase-account-management` for Auth users, custom claims, profile
  documents, service accounts, or account lifecycle.
- `$firebase-security-rules` for Firestore/Storage rules, Admin SDK endpoint
  authorization, or production access.
- `$claude-to-a-tee` for exact Admin UI parity from Claude handoffs.
- `$efficient-execution` for targeted admin checks and avoiding unnecessary
  full-project gates.
- `$release-gate` before commit, push, deploy, or handoff.

## Live Admin Rules

- Production `/admin/` uses Firebase Google Auth and allowlists
  `purich.wc@gmail.com`.
- `/admin/?test=1` is only for automated regression and is not real security.
- Real user rows must merge Firestore `users/{uid}` accounts with board-derived
  participants/admins.
- Current canon is one account equals one active Character.
- Board Admin IDs may intentionally repeat across boards; do not globally
  de-dupe them.
- Archive/Deactivate/Reactivate are recoverable lifecycle operations.
- Permanent delete is backend-only through `/api/admin-delete-user` after Firebase
  ID-token verification and Super Admin allowlist check.
- Delete keeps reusable username tombstones so same-username recreation preserves
  public User ID and Character ID.
- Admin password reset currently has Phase 1 limitations; do not call it fully
  hardened unless moved behind Admin SDK.

## Workflow

1. Identify the operation: auth gate, board edit, user edit, lifecycle, reset,
   permanent delete, draft/restore/publish, revision log, relationship map, or
   responsive layout.
2. Apply `$admin-ops` to map identity, authorization, operation, auditability,
   UX state, verification, and closeout.
3. Trace source and persistence through `ADMIN_PORTAL_IMPLEMENTATION.md` and
   `data-contracts.md`.
4. Preserve Super Admin checks and test-mode boundaries.
5. For visual work from Claude, use `$claude-to-a-tee` and preserve Admin
   vocabulary such as `page-head`, `card`, `stat`, `tbl`, `detail-grid`,
   `profile-card`, `log-list`, and modal patterns.
6. Verify:
   - small copy/layout: `npm run test:syntax` plus browser spot-check
   - lifecycle/delete/reset/data: targeted unit/e2e plus `npm test` when risky
   - commit/deploy request or admin persistence change: full `npm test`
7. Update `ADMIN_PORTAL_IMPLEMENTATION.md`, `ACCOUNT_MANAGEMENT_IMPLEMENTATION.md`,
   `SECURITY_AND_FIREBASE_RULES.md`, or `data-contracts.md` if behavior changes.

## Closeout

Report the admin operation, auth/security path checked, docs updated, adjacent
skills used or intentionally not needed, tests run, and production/admin risk.
