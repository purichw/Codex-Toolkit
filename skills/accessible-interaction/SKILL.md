---
name: accessible-interaction
description: Design, audit, implement, or verify accessible UI interaction behavior. Use when the user asks for accessibility, a11y, keyboard-only navigation, tab order, focus traps/restore, screen reader behavior, ARIA names/states, semantic controls, contrast, reduced motion, touch targets, mobile keyboard behavior, modal/drawer accessibility, skip links, or when visual/UI changes may break non-pointer interaction.
---

# Accessible Interaction

Use this skill when an interface must work beyond mouse clicks and screenshots.
Accessibility is part of interaction quality, not a late checklist.

Use `$ui-state-matrix` for focus/disabled/error states, `$interaction-flow-qa`
for journeys, `$form-flow-ux` for forms, `$mobile-web-qa` for device behavior,
`$snapshot` for visual focus evidence, and `$release-gate` before shipping.

## Core Checks

- Keyboard can reach every interactive control in a logical order.
- Focus is visible, not clipped, and returns after modal/drawer close.
- Dialogs/drawers trap focus when open and release it when closed.
- Escape, close buttons, outside click, and cancel actions behave consistently.
- Buttons, links, inputs, toggles, tabs, menus, and accordions use appropriate
  semantics and names.
- Disabled or readonly state is conveyed visually and semantically.
- Error, success, loading, and permission states are announced or discoverable.
- Touch targets are large enough without breaking visual density.
- Reduced motion and mobile keyboard behavior do not break the flow.

## Workflow

1. Inventory changed interactive controls and containers.
2. Exercise keyboard-only path through the flow.
3. Inspect focus target, accessible name, role, state, and disabled behavior.
4. Test open/close and focus restore for modals, popovers, drawers, and menus.
5. Check contrast and motion only where the change affects them.
6. Capture `$snapshot` evidence when visible focus/layout is part of the issue.
7. Add focused tests when accessibility could regress silently.

## Common Failure Modes

- div/span clickable controls with no keyboard activation;
- focus lost after save, route change, drawer close, or validation error;
- modal backdrop traps pointer but not keyboard, or vice versa;
- hidden content remains focusable;
- selected tab visually changes but ARIA/current state does not;
- mobile keyboard hides the active input or submit action.

## Closeout

Report keyboard path, focus behavior, semantic/ARIA fixes, contrast/motion/touch
coverage, screenshots/tests, skipped assistive-tech checks, and residual risk.
