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
visuals. If the user says "to a tee", also use `$claude-to-a-tee`.

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
- Native uses the same Firebase project and account contracts:
  `users/{uid}`, `usernames/{username}`, `characters/{id}`, and `trips/{id}`.
- Native-owned module state lives in `playerModules/{uid}` for Debt Dragon,
  Treasury, and Compare.
- Web Debt/Treasury/Compare localStorage stores are not automatically migrated.
- Never replace real backend state with static Claude/sample finance data.
- Empty states are acceptable only when tied to real create/log actions.

## Pre-Build Gates

Before a physical iPhone build/install:

1. Design parity gate: compare touched screens against the latest Claude iOS and
   Android exports. Check native chrome, title spacing, cards, sheets, bottom
   tabs/FAB, typography scale, asset usage, loading, empty, and error states.
2. Backend gate: sign in or create a real Firebase account and verify dynamic
   Firestore-backed data for the touched flow.
3. Source gate: run `npm run typecheck` from `mobile/`, then export/build as
   documented in `mobile/IOS_BUILD_NOTES.md`.

## Verification

- Native TypeScript: from `mobile/`, run `npm run typecheck`.
- iOS bundle export: `npx expo export --platform ios --output-dir /tmp/coinquest-mobile-export`.
- Root web regression after shared contract changes: from repo root, run
  `npm test`.
- Use `$snapshot` automatically before the final response when changed native
  screens, web parity surfaces, Claude exports, or visual comparisons are part
  of the task. Do not wait for the user to ask; state any simulator/device
  capture gap.
- Update `NATIVE_WEB_PARITY.md` and `mobile/README.md` when contracts or gates change.

## Closeout

Report native screens/flows touched, shared contracts checked, web parity risk,
native build/export evidence, snapshot evidence when UI was visible, adjacent
skills used or intentionally not needed, and remaining device coverage gaps.
