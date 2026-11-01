---
name: coin-quest-admin-ops
description: Maintain Coin Quest Ledger Admin Portal operations. Use when working on Coin Quest admin auth, Super Admin behavior, boards, users, lifecycle actions, reset/delete flows, draft/publish/restore, revisions, relationship maps, admin Firebase-backed behavior, or admin-side regressions in the Coin Quest project.
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

Start with `Memory.md` and `ADMIN_PORTAL_IMPLEMENTATION.md`, then read only
the owners relevant to the operation:

- `Memory.md`
- `ADMIN_PORTAL_IMPLEMENTATION.md`
- `SECURITY_AND_FIREBASE_RULES.md`
- `ACCOUNT_MANAGEMENT_IMPLEMENTATION.md`
- `data-contracts.md`
- `SITE_MAP_AND_INTERACTIONS.md`
- `admin/app.js`, `admin/admin-utils.js`, `admin/index.html`, `admin/admin.css`,
  `admin/design.css` and `admin/shell.js` when visuals are involved
- `api/admin-delete-status.js` and `api/admin-delete-user.js` when delete/status is involved
- `firestore.rules` when permissions are involved

`ADMIN.md` is an entry-point index. Current implementation contracts live in
`ADMIN_PORTAL_IMPLEMENTATION.md`; old prototype behavior is not a parallel spec.

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
- `$reference-to-a-tee` for exact Admin UI parity from Claude handoffs.
- `$snapshot` for mandatory visual evidence before the final response when an
  Admin screen, state, responsive layout, Claude handoff, or prototype
  comparison is in scope.
- `$efficient-execution` for targeted admin checks and avoiding unnecessary
  full-project gates.
- `$release-gate` before commit, push, deploy, or handoff.

## Live Admin Rules

- All Admin routes use Dashboard's parchment palette and the common header,
  sidebar, frame and footer, including pages whose inner content is older.
  `admin/design.css` and `admin/shell.js` own those shared surfaces.
- Board Info and User Detail are scroll-only. Do not restore detail Tabs,
  Layout toggles or stale tab state from mockups. User Detail follows Board Info's
  tavern title/section artwork; its sections stay open, while Board Info retains
  the documented responsive disclosures. Dashboard Cards/Command is still valid.
- Preserve current responsive tables/cards, real IDs/counts and action semantics.
  Sample mockup accounts, dates or controls do not authorize new data operations.
- Canonical Admin origin: `https://coinquestledger.vercel.app/admin/`. Use the
  deploy runbook and `SECURITY_AND_FIREBASE_RULES.md` for current alias/Auth
  configuration; do not restore retired hosts from historical captures.
  Firebase project `pointy-personal-toolkit` and its hosted OAuth helper are
  separate from the website hostname. Domain changes do not migrate UIDs/data
  or automatically rebrand Google's sign-in screen.
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
- Recovery and Admin reset use `api/account-recovery-core.js` through Admin SDK.
  Preserve the same UID even when recreating missing Auth. Validate identity
  ownership/current hash, honor both blocked lifecycle fields and the five-minute
  reset lease, revoke sessions and rotate the key on successful completion.
  Auth/Firestore are separate services; failure/retry is not cross-service atomicity.
- Privileged APIs require a verified allowlisted email and revocation-checked
  Firebase ID token. Never treat `/admin/?test=1` as that security evidence.
- Lifecycle transactions update user, username and User ID reservation together.
  Board publishing compares current data against the draft baseline and only
  writes changed boards. Conflict keeps the draft and must not create a revision.
- Deletion validates pointers before Auth deletion, removes module data/nested
  invites and detaches Auth-linked board members into guests while preserving
  expenses, shares and obligations. Do not reuse legacy orphan cleanup for this.
- Legacy board access is still signed-in read / active-account write. Per-board
  ACLs and existing public recovery-hash cleanup require coordinated migrations;
  do not report these as solved by the current Rules.

## Workflow

1. Identify the operation: auth gate, board edit, user edit, lifecycle, reset,
   permanent delete, draft/restore/publish, revision log, relationship map, or
   responsive layout.
2. Apply `$admin-ops` to map identity, authorization, operation, auditability,
   UX state, verification, and closeout.
3. Trace source and persistence through `ADMIN_PORTAL_IMPLEMENTATION.md` and
   `data-contracts.md`.
4. Preserve Super Admin checks and test-mode boundaries.
5. For supplied mockups, use `$mockup-to-product`; use `$reference-to-a-tee`
   when exact fidelity is requested. Inspect the current shared owners and
   nearest screen rather than copying retired prototype components/selectors.
6. Verify:
   - small copy/layout: `npm run test:syntax` plus browser spot-check
   - lifecycle/delete/reset/data: targeted unit/e2e plus `npm test` when risky
   - auth/Rules/Admin persistence: `npm run test:backend` (isolated Auth/Firestore
     emulators, guarded `demo-coin-quest` project); do not mutate production as a shortcut
   - commit/deploy request or admin persistence change: full `npm test`
7. Use `$snapshot` automatically before the final response for visible Admin UI
   changes, audits, responsive states, or prototype/live comparisons. Do not
   wait for the user to ask; state why if fresh capture is blocked.
8. Update `ADMIN_PORTAL_IMPLEMENTATION.md`, `ACCOUNT_MANAGEMENT_IMPLEMENTATION.md`,
   `SECURITY_AND_FIREBASE_RULES.md`, or `data-contracts.md` if behavior changes.

## Closeout

Report the admin operation, auth/security path checked, docs updated, adjacent
skills used or intentionally not needed, tests run, snapshot evidence when UI
was visible, and production/admin risk.
