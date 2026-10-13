---
name: coin-quest-ledger-logic
description: Implement, audit, or debug Coin Quest Ledger Party Ledger behavior. Use when working on Coin Quest Split or Quest Log math, payer/participant logic, who owes whom, Add by Character ID, Add Guest, guests, Reminders invites, direct invite links, Character IDs, Firebase persistence, or settlement regressions.
---

# Coin Quest Ledger Logic

Use `$ledger-logic` for reusable shared-ledger math, identity, invite/guest, and
verification workflow. This skill is the Coin Quest overlay: project docs,
known Character ID rules, settlement fixture, and commands.

## Overview

This skill keeps Party Ledger logic changes grounded in the current Coin Quest
contracts. Use it before editing participant entry, invites, guests, split modes,
settlement, Character ID handling, or Reminders behavior.

## Required Context

From the repo root, read these before implementation:

- `Memory.md`
- `INVITES_AND_GUESTS.md`
- `SITE_MAP_AND_INTERACTIONS.md`
- `data-contracts.md`
- `shared/pointy-logic.js`
- `trip/app.js` and `trip/index.html` for UI/state wiring
- `tests/unit/pointy-logic.test.mjs`
- relevant Playwright tests in `tests/e2e/coin-quest-ledger.spec.mjs`

If the user asks for exact Claude visual parity, also use `$reference-to-a-tee` and
`CLAUDE_TO_A_TEE_QA.md`.

Use adjacent skills when the task crosses boundaries:

- `$ledger-logic` for the global ledger model, settlement, identity, and test
  workflow.
- `$coin-quest-admin-ops` for Admin Portal user/board lifecycle or Super Admin
  behavior affected by ledger data.
- `$coin-quest-native-parity` for native/web parity, Expo app, or shared
  settlement/account contracts.
- `$firebase-account-management` or `$firebase-security-rules` for Auth,
  Firestore Rules, Admin SDK, service-account, or production access changes.
- `$regression-hunter` when a ledger bug suggests repeated settlement,
  participant, invite, or normalization failures.
- `$efficient-execution` for running pure ledger checks before slower UI or
  deploy gates.
- `$release-gate` before commit, push, deploy, or handoff.

## Non-Negotiable Rules

- Real "other hero" additions are Character-ID-only.
- A real Character ID must resolve an existing character/account record before
  invite. Never mint a new Character ID from arbitrary input.
- Do not ask for or validate "Other hero's name" in the real-character path.
  Names come from the target account/character.
- Duplicate visible names are allowed. Do not add duplicate-name blocking.
- The action for adding another real character is `Invite`, not `Confirm Character`.
- Invited users receive a Reminders notification and can Accept or Decline within
  24 hours. Decline needs a confirmation dialog.
- Direct party invite links can join immediately only after login; unauthenticated
  users must be routed to login first.
- `Add Guest` is the board-local alternative: enter display name, choose hero,
  and do not create a real Character ID, user, or registry record.
- Guests must be omitted from real character XP/registry sync.
- Settlement uses pairwise per-expense obligations with reciprocal pair netting.
  Do not replace it with global creditor/debtor rerouting.
- Keep web/native settlement expectations aligned.
- Preserve satang: use the shared money helpers and half-satang comparison
  threshold, not a one-baht cutoff that silently clears a remaining balance.
- Invitation attempts have unique IDs; legacy IDs remain readable. Re-read the
  current account, character and board, then commit reply + membership together.
  Reject expired/replied/archived attempts instead of replaying them.
- Persist freshly read board snapshots transactionally. Deep merge must not
  resurrect removed nested keys. Preserve unknown fields and concurrent work.
- Account deletion detaches a real member into a board-local guest while keeping
  names, expenses, shares and financial obligations; remove registry/access links.

## Known Regression Case

For the fixture with Pointy, PP, and PPP:

- `PPP -> Pointy`: `฿1,000`
- `PPP -> PP`: `฿333.33`
- `PP -> Pointy`: `฿666.67`

Add or preserve unit coverage whenever settlement math changes.

## Workflow

1. Confirm the affected flow: participant entry, invite/reminder, guest handling,
   expense split mode, settlement list/map, export/import, or profile sync.
2. Apply `$ledger-logic` to define actor types, identity keys, split/settlement
   model, invite/guest behavior, and worked examples.
3. Trace persisted shape through `data-contracts.md` and normalization in
   `shared/pointy-logic.js`.
4. Patch shared pure logic first when possible, then patch `trip/app.js` UI/state
   glue.
5. Preserve i18n through `lang.js` or local bilingual copy maps.
6. Run targeted verification:
   - math/normalization: `npm run test:unit`
   - syntax/UI state wiring: `npm run test:syntax`
   - invite/reminder/mobile flow: targeted Playwright or `npm run test:e2e`
   - commit/deploy request: full `npm test`
   - Firestore transactions/invites/Admin cleanup: `npm run test:backend` using
     isolated `demo-coin-quest` emulators, plus native contract tests when shared
     behavior changes
7. Update `INVITES_AND_GUESTS.md`, `data-contracts.md`, or `SITE_MAP_AND_INTERACTIONS.md`
   when behavior or persisted shape changes.

## Closeout

Report the affected flow, shared contract files checked, adjacent skills used or
intentionally not needed, tests run, and web/native/admin risk if any.
