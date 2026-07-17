---
name: ledger-logic
description: Implement, audit, or debug collaborative ledger behavior across projects. Use when the user asks about splitting bills, who paid, who owes whom, expenses, shares, payer/participant logic, settlement math, reciprocal netting, guests vs real accounts, invites, shared financial state, import/export, persistence contracts, or ledger regression tests.
---

# Ledger Logic

Use this skill for shared ledgers where multiple people, accounts, guests,
items, payments, obligations, or settlement outputs must stay mathematically and
contractually correct.

## Core Invariants

Define the ledger model before editing:

- actor types: real users, guests, pending invites, deleted users, archived
  accounts, external contacts;
- identity keys: display name, account id, public id, invite id, guest id,
  tombstone id, or local-only id;
- ledger entries: payer, participants, shares, exclusions, adjustments,
  currency, rounding, timestamps, status;
- settlement algorithm: per-entry obligations, pairwise netting, global
  creditor/debtor simplification, or domain-specific rule;
- persistence shape: local state, database documents, import/export, sync, and
  migration behavior.

Never treat duplicate display names as unique identities. Never mint real user
IDs from arbitrary text input. Guest/local actors must not silently become real
accounts.

## Split And Settlement Rules

For every split mode, write or preserve a small worked example:

```text
entry | payer | participants | amount | expected obligations
```

Check:

- rounding across totals, decimals, zero/empty shares, and excluded actors;
- reciprocal pair netting and same-pair multiple expenses;
- deleted/archived/guest actors and whether historical entries remain valid;
- currency formatting vs stored numeric value;
- import/export and reload preserving the same settlement.

Do not replace a documented settlement model with a different simplification
unless the product explicitly changes the rule.

## Invites And Guests

Separate:

- **real-account invite:** resolves an existing account/identity before linking;
- **pending invite:** can expire, be accepted/declined, or require login;
- **guest/local actor:** board-local display entry with no real account side
  effects;
- **tombstone/deleted actor:** preserves historical ledger integrity.

Define what notifications, links, expiration, confirmation dialogs, and
post-acceptance synchronization are expected.

## Workflow

1. Identify affected flow: entry creation, split editing, participant add/remove,
   invite, guest, settlement, export/import, profile sync, or migration.
2. Trace pure calculation helpers before UI glue.
3. Patch canonical helpers or data contracts before duplicated components.
4. Preserve existing persisted data; add migration/normalization only when
   required and tested.
5. Add focused regression tests with worked examples for every math or identity
   rule changed.
6. Use `$regression-hunter` when one ledger bug suggests repeated data or math
   patterns. Use `$admin-ops` when admin surfaces can edit ledger state. Use
   `$native-parity` when web/native clients share the contract. Use
   `$efficient-execution` to run pure calculation checks before slower UI,
   persistence, or deploy verification.

## Verification

- Pure math: unit tests with explicit expected obligations.
- UI/state: create/edit/reload/delete flows in the app.
- Persistence: database/local storage/import-export shape and migrations.
- Invites: authenticated, unauthenticated, accepted, declined, expired, and
  duplicate cases.
- Release: use `$release-gate` before commit, push, deploy, or handoff.

## Closeout

Report the invariant, worked examples, data contracts touched, tests run,
identity/guest/invite implications, cross-client/admin risk, and any settlement
model assumptions.
