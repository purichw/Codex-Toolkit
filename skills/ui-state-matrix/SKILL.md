---
name: ui-state-matrix
description: Define, implement, audit, or verify complete UI state coverage beyond the happy path. Use for default, hover, focus, selected, disabled, loading, skeleton, empty, error, success, validation, permission denied, long text, localization, mobile keyboard, offline/stale, partial failure, and responsive component states before claiming UI work is complete.
---

# UI State Matrix

Use this skill when a UI can look finished in the happy path while important
states are missing or broken.

Use `$form-flow-ux` for form-specific state journeys, `$data-dense-ux` for
tables/lists, `$accessible-interaction` for focus/keyboard states, `$snapshot`
for visual proof, `$mobile-web-qa` for responsive state checks, and
`$release-gate` before shipping.

## State Set

Choose applicable states, not every state blindly:

- default/filled/current;
- hover/pressed/focus/focus-visible;
- selected/active/current route;
- disabled/readonly/locked with reason;
- loading/skeleton/pending/optimistic;
- empty/no result/first run;
- validation error/server error/network error;
- success/saved/completed/undo available;
- permission denied/role restricted/stale session;
- partial data/partial failure/retry;
- long text/localization/missing image/media;
- mobile keyboard/safe area/touch-only;
- reduced motion/high contrast where supported.

## Matrix

```text
Component/flow:
State:
Trigger:
Expected UI:
Data/auth condition:
Claude/reference behavior if any:
Implementation:
Verification:
Risk if skipped:
```

## Workflow

1. Inventory changed components and the states users can reach.
2. Mark states that are impossible, product-owned, or reference-only.
3. Implement state styling and behavior together; do not leave visual states
   disconnected from real product state.
4. Verify states through real triggers where practical, not only forced CSS.
5. Capture representative `$snapshot` evidence for risky visual states.
6. Add focused tests when a missing state would be silent.

## Quality Bar

- Disabled controls explain why when the reason is user-actionable.
- Loading states prevent duplicate destructive or expensive actions.
- Empty/error states offer a next action when one exists.
- Long text does not clip, overlap, or resize fixed controls unexpectedly.
- Focus and selected states are visible and consistent.
- Mobile keyboard states keep the active field and action reachable.

## Closeout

Report states covered, states intentionally skipped, screenshots/tests, and any
state that still needs real data, auth, or UAT evidence.
