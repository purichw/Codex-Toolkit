---
name: interaction-flow-qa
description: Verify UI/UX journeys by exercising real user flows, not just static screens. Use when the user asks to click through a flow, prove it works end to end, or test search-to-result-to-detail, filter/reload/back, onboarding, navigation, modal/drawer flows, admin create/edit/publish, checkout/signup, media playback, progress/completion, destructive actions, routing, state, data, permissions, and feedback.
---

# Interaction Flow QA

Use this skill when the question is "can the user actually complete the
journey?" Screenshots support this work, but do not replace exercised flows.

Use `$product-ux-contracts` for existing journey contracts, `$ui-state-matrix`
for state coverage, `$form-flow-ux` for forms, `$accessible-interaction` for
keyboard/focus, `$snapshot` as mandatory visible flow proof before final
response, `$mobile-web-qa` for responsive flows, and `$release-gate` before
shipping.

## Flow Ledger

```text
Flow:
Entry point:
Preconditions: auth / role / data / flags / viewport
Steps:
Expected URL/state/data after each step:
Success state:
Failure/empty/denied state:
Persistence/reload/back behavior:
Evidence:
Risk:
```

## Workflow

1. Identify the primary journey and secondary entry points.
2. Set up realistic data and auth state; avoid testing only a demo shell.
3. Exercise the flow by clicking, typing, scrolling, navigating, and reloading.
4. Verify URL, selected state, data mutation, visible feedback, and persistence.
5. Check at least one negative or alternate path when the flow can fail.
6. Capture `$snapshot` evidence for key visible states before final response and
   report console/network failures when browser tools are available.
7. Add or run focused tests for journeys that are release-critical.

## Common Flows

- search result -> detail -> back -> result still selected;
- filter/sort -> reload -> share URL -> same view;
- modal open -> edit -> save -> success -> focus/scroll restored;
- admin draft -> preview -> publish -> public page updates;
- delete/reset -> confirm -> audit/undo/empty state;
- onboarding step -> next/back/skip/done -> overlay no longer blocks product;
- media play -> pause/replay/error/fallback;
- mobile nav -> route -> close drawer -> safe-area/sticky action works.

## Evidence Rules

Do not call a flow verified if automation hit the wrong route, login gate,
loading shell, stale build, selector miss, or mock-only data. Discard and rerun
after fixing setup.

## Closeout

Report flows exercised, preconditions, evidence, screenshots/tests, failures
fixed, skipped paths, and residual journey risk.
