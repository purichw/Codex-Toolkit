---
name: admin-prototype-reconciliation
description: Reconcile a new admin/CMS/dashboard prototype, Claude/Figma/offline HTML, or design-side data model against a live production admin system before implementation. Use when Codex must compare prototype fields, components, workflows, draft/publish states, revisions, auth/roles, navigation/settings, or store APIs with existing live code and data, classify already-live vs net-new vs conflicting pieces, preserve production contracts, and produce a confirmed diff before merging.
---

# Admin Prototype Reconciliation

Use this skill before implementing an admin prototype into a real product. The
prototype is evidence of desired UI and workflow; the live admin/data layer is
authoritative for production contracts until an explicit migration changes it.

Use `$admin-ops` for operational safety, `$claude-to-a-tee` for exact prototype
UI parity, `$data-dense-ux` for dense admin lists/tables, `$form-flow-ux` for
editors/drafts/saves, `$product-ux-contracts` for preserving proven behavior,
and `$release-gate` before shipping.

## Core Rule

Do not implement from a prototype until the live-path diff is confirmed. A
beautiful admin mock can hide field renames, missing server checks, fake
publish buttons, unbuilt uploads, old snapshot shapes, and incompatible route
or auth assumptions.

If the user asks to reconcile first, deliver the diff only. Do not write code
until explicitly asked or until the task moves from audit to implementation.

## Required Inputs

Collect the smallest set that proves both sides:

- prototype admin files: HTML, JS store, fixtures, handoff docs, screenshots,
  reference manifests, or design contracts;
- live admin files: routes, shells, editors, backend APIs, data adapters,
  validators, auth/role checks, publish/revision endpoints, tests;
- live read/write data source: Firestore/RTDB/REST snapshot, SQL tables, CMS
  APIs, generated JSON, or server-side cache;
- production constraints: deploy target, public read rules, localization,
  media upload/storage, rollback/revisions, audit logs, and mock/unbuilt list.

Prefer source over docs. Docs are hypotheses until confirmed against live code.

## Reconciliation Workflow

1. Read the prototype contracts and identify every collection, singleton,
   store method, visible component, and lifecycle state.
2. Read the live source paths in full for content reads, admin writes, schema
   validation, auth/permission boundaries, publish/revision endpoints, and
   public consumption.
3. Build a field map for each collection and singleton:

```text
Prototype path | Live path | Status: exact / rename / missing / conflict / net-new | Evidence | Merge rule
```

4. Classify every prototype component:

```text
Component | Classification: already live / net-new / conflicting | Live evidence | Merge note | Mock/unbuilt risk
```

5. Resolve gating decisions before editing:
   - What does "published" mean in live production?
   - Are status/visible/order/pinned fields live, documented only, or net-new?
   - Is localization already present, partially present, or a migration?
   - Which public routes read this data and how do they filter it?
   - What schema does the write path enforce?
   - What revision/rollback API already exists?
6. Identify prototype-only UI or fake behavior. Decide whether to hide it,
   make it real, adapt it to a live equivalent, or defer with a documented
   blocker.
7. Produce the confirmed diff and only then plan implementation.

## Classification Rules

- `already live`: production has the capability or data, possibly under another
  name or shape. Keep live authoritative and adapt the prototype.
- `net-new`: no production equivalent exists and adding it does not alter an
  existing live contract. Safe to add after normal risk checks.
- `conflicting`: prototype touches a live surface but changes field shape,
  lifecycle, route, permission, validation, persistence, or visible workflow.
  Merge carefully and document the migration or adapter.

Never call a feature net-new just because the UI looks different. Trace the
data and operation first.

## Contract Preservation

Preserve server-side guarantees, not only UI affordances:

- public reads filter only the intended live/published content;
- localization fallback is deterministic and documented;
- ordering, visibility, pinning, drafts, reviews, and publish states are
  honored consistently between admin and public surfaces;
- admin writes pass live validation and required top-level keys;
- auth/role checks remain server-backed;
- media upload/crop fields store deployable or externally reachable assets;
- rollback/revision UI uses real APIs or is hidden/deferred.

## Common Traps

- Prototype `status: published` exists, but live treats "in snapshot" as
  published.
- Prototype has `en/de` objects, but live content is monolingual.
- Prototype store methods look 1:1 with Firestore but live writes a whole
  validated snapshot.
- Prototype has pinned/order/visible fields documented but not persisted.
- Admin cards show upload/drop zones while production has no upload backend.
- Dashboard counters, scheduled publishing, rollback points, roles, or detail
  body copy are mock-only.
- Public events or posts come from a separate path, hardcoded array, or fixture
  rather than the admin snapshot.
- UI publish buttons mutate local state while production requires tokened
  server endpoints and schema validation.

## Deliverable Format

For audit/reconciliation tasks, answer with:

```text
Source files read:
Field map:
Component classification:
Gating decisions:
Public read verdict:
Write-schema requirements:
Revision/rollback API:
Mock/unbuilt list:
Live contradictions with prototype docs:
Implementation recommendation:
Do-not-implement-yet blockers:
```

For implementation tasks, keep the reconciliation tables as a working ledger
and update them when code reveals a new mismatch.
