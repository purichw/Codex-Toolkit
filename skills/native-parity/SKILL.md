---
name: native-parity
description: Keep native iOS/Android apps aligned with web or product source-of-truth behavior. Use when the user asks why native differs from web, or for Expo/React Native builds, web-native data parity, shared backend contracts, native screen parity, mobile design handoffs, device build gates, App Store/TestFlight readiness, and avoiding static sample-app drift.
---

# Native Parity

Use this skill when a native app must preserve the product contract of a web app,
backend, design reference, or shared domain model.

## Source Of Truth

Separate:

- **product contract:** data, auth, permissions, persistence, sync, analytics,
  feature flags, and backend behavior;
- **platform contract:** navigation chrome, gestures, safe areas, permissions,
  push/deep links, offline behavior, app store/build constraints;
- **visual contract:** native design handoff, web parity target, or exact Claude
  reference when supplied.

Native should not become a static sample app unless the user explicitly asks for
a throwaway prototype.

## Required Context

Locate:

- native app root, package manager, build docs, environment files, and platform
  config;
- shared data contracts, API/Firebase/backend routes, local storage, sync, and
  migrations;
- route/screen map, navigation structure, tabs/sheets/modals, and deep links;
- current design references for iOS/Android and any web parity source;
- typecheck, lint, unit/e2e/device build commands.

Use `$claude-to-a-tee` for exact design reference parity, `$mobile-web-qa` only
for web responsive checks, `$snapshot` for mandatory visual evidence before the
final response when a native/web screen, design reference, or parity screenshot
is in scope, and `$release-gate` before package/deploy/handoff.

Use `$efficient-execution` to keep native checks ordered: validate shared
contracts and type/build errors before slower simulator/device passes, then run
device coverage only for changed screens or release gates.

## Native Boundaries

- Do not replace real backend state with static demo data.
- Keep native-owned local state clearly separate from web localStorage or browser
  cache unless a migration is explicitly implemented.
- Preserve auth/session and permissions across reload/reopen where the product
  requires it.
- Empty states must point to real create/connect/retry actions.
- Shared contracts changed for native must be regression-tested against web when
  web still consumes them.

## Parity Workflow

1. Identify touched screens/flows and their product-owned data contract.
2. Compare native UI against the relevant design/web/reference source.
3. Map every visible action to a real backend/local state transition or a
   documented passive/disabled state.
4. Implement using native patterns while preserving product behavior.
5. Verify typecheck/build/export and at least one representative device/simulator
   path when practical.
6. Use `$snapshot` automatically before the final response when native visual
   parity, screen implementation, screenshot comparison, or handoff evidence is
   part of the task. Do not wait for the user to ask. If no device/browser
   snapshot can be captured, state the coverage gap.
7. Update parity docs/readme/build notes when contracts or gates change.

## Build And Verification

Run project-defined commands first. Typical evidence:

- TypeScript/typecheck or native lint;
- platform export/build command;
- simulator/device smoke for changed screens;
- backend/auth/data flow with a real or seeded account;
- shared web regression when contracts changed;
- `$snapshot` evidence for visual parity, changed screens, or screenshot/video
  comparison when a visible screen is in scope.

## Closeout

Report native screens touched, source-of-truth references, backend/shared
contracts checked, build/export evidence, snapshot evidence when UI was visible,
device coverage gaps, web parity risk, and follow-on release gate.
