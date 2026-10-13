---
name: coin-quest-native-parity
description: Keep the Coin Quest Ledger native Expo app aligned with web behavior and design. Use when working on Coin Quest iOS/Android builds, Expo/native build gates, native-web data parity, playerModules, native screen parity, native Claude Design parity, or regressions where the app differs from the web source of truth.
---

# Coin Quest Native Parity

Use `$native-parity` for the reusable native/web product-contract workflow. This
skill is the Coin Quest overlay: Expo paths, project contracts, playerModules,
and web/native verification commands.

## Overview

This skill prevents native work from drifting into a static sample app. Use it
for any `mobile/` change, iOS/Android build, native screen parity check, or
web/native backend contract question.

## Required Context

Read these first:

- `NATIVE_WEB_PARITY.md`
- `mobile/README.md`
- `mobile/IOS_BUILD_NOTES.md`
- `architecture.md`
- `data-contracts.md`
- `SITE_MAP_AND_INTERACTIONS.md`
- relevant files under `mobile/src/`

If a fresh Claude iOS/Android export is supplied, inspect it before changing
visuals. If the user says "to a tee", also use `$reference-to-a-tee`.

Use adjacent skills when the task crosses boundaries:

- `$native-parity` for the global source-of-truth, native boundaries, build, and
  closeout workflow.
- `$coin-quest-ledger-logic` for settlement, participants, invites, Character
  IDs, guests, and shared ledger contracts.
- `$coin-quest-admin-ops` when native changes depend on Admin-managed account,
  board, or lifecycle behavior.
- `$firebase-account-management` or `$firebase-security-rules` for Auth,
  Firestore, Admin SDK, rules, service accounts, or production access.
- `$mobile-web-qa` only for web responsive parity, not native device testing.
- `$efficient-execution` for ordering type/build/shared-contract checks before
  slower simulator or package gates.
- `$snapshot` for mandatory visual evidence before the final response when a
  Coin Quest native/web screen, Claude export, or parity comparison is in scope.
- `$release-gate` before commit, push, deploy, TestFlight/package handoff, or
  web/native shared contract release.

## Native Boundaries

- Native is player-side only. Do not add Admin native or an Admin WebView unless
  the user explicitly changes direction.
- Native is not a WebView wrapper.
- Both clients use Firebase project `pointy-personal-toolkit`: `users/{uid}`,
  `usernames/{username}`, `userIds/{id}`, `characters/{id}`, `trips/{id}` and
  nested `users/{uid}/boardInvites`.
- Debt Dragon, Treasury and Compare share `playerModules/{uid}`. The website
  bridge is `shared/module-cloud.js`; preserve local drafts and backups, require
  an explicit choice when local/cloud snapshots conflict, and stop stale writes
  after an account switch. Refresh is explicit, not a realtime subscription.
- Native imports canonical finance/settlement logic from `shared/pointy-logic.js`.
  Replace the selected module map with `mergeFields`, preserving other modules;
  do not deep-merge removed nested records back into existence.
- Never replace real backend state with static Claude/sample finance data.
- Empty states are acceptable only when tied to real create/log actions.

## Simulator-First Workflow

- Read `mobile/AGENTS.md`, `.nvmrc` and `IOS_BUILD_NOTES.md` before building.
  The rebuild uses Expo Router (`src/app/`), Expo 57 / React Native 0.86 and
  Node 24. Use the committed versions, npm lockfile and two workers on this Mac.
- Build, install and launch the app's own binary; use `npm run build:simulator`
  and `npm run start:simulator`. Expo Go, an exported JS bundle and a browser
  phone viewport do not establish native acceptance.
- Exercise the affected flow on Simulator: tap/back, keyboard or native picker,
  loading/error, save/reopen and process relaunch when persistence is involved.
  Inspect current screenshots with build, account/state and device provenance.
- Use an authorized test account to check native ↔ Firebase ↔ web round trips
  for shared writes. Mock browser fixtures and emulator tests are separate evidence.
- The approved direction is the Coin Quest brand adapted to native mobile.
  Read `mobile/DESIGN_DIRECTION.md`; preserve website font roles: Mitr,
  IBM Plex Sans Thai and Chakra Petch. Use a supplied reference only when relevant.
- Device lock or unavailable Simulator is an explicit missing gate. Preserve
  earlier per-flow evidence without representing it as proof of later changes.
  App Store/TestFlight/Android distribution is separate from a web/API deployment.

## Verification

- From `mobile/`: `npm run typecheck`, `npm run lint`,
  `node --test tests/*.test.mjs` and `npm run check:dependencies` when dependencies change.
- Optional bundle gate: `npx expo export --platform ios --output-dir .artifacts/ios-export`.
  Rebuild the own-app binary after adding native dependencies.
- Root web regression after shared contract changes: from repo root, run
  `npm test`.
- Auth/rules/Admin/shared persistence changes also require `npm run test:backend`.
  This uses isolated `demo-coin-quest` Auth/Firestore emulators, never production.
- Use `docs/mobile-completion-worklist.md` and `docs/backend-audit-2026-10-12.md`
  for historical evidence/known limits, and the release runbook for live status.
- Use `$snapshot` automatically before the final response when changed native
  screens, web parity surfaces, Claude exports, or visual comparisons are part
  of the task. Do not wait for the user to ask; state any simulator/device
  capture gap.
- Update `NATIVE_WEB_PARITY.md` and `mobile/README.md` when contracts or gates change.

## Closeout

Report native screens/flows touched, shared contracts checked, web parity risk,
native build/export evidence, snapshot evidence when UI was visible, adjacent
skills used or intentionally not needed, and remaining device coverage gaps.
