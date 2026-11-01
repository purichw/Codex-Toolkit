---
name: mobile-native-feel
description: Design or audit mobile UI for safe areas, native controls, touch targets, keyboard behavior, thumb reach, sheets, gestures, and platform feel. Use when mobile web or app UI feels like squeezed desktop, has unsafe insets, hidden keyboard actions, wrong sheet/dialog behavior, weak touch ergonomics, hover-only affordances, or non-native controls.
---

# Mobile Native Feel

Use this when mobile UI feels like a squeezed desktop screen or misses platform expectations. It covers safe areas, controls, reach, keyboard, sheets, gestures, and OS-native affordance.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [05-mobile-native-feel.md](../design-quality-review/references/design-quality/05-mobile-native-feel.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Choose sizes from the project's supported targets and touched risk. For broad phone-responsive work, 390x844 and 360x800 are useful starting cases; add tablet only when in scope. A narrow iOS repair does not require Android setup or a new capture matrix. Distinguish headless viewport checks from real-device evidence.
2. Verify safe-area insets, dvh behavior, target sizes, scroll ownership, sticky actions, and keyboard visibility.
3. Prefer native/platform controls and patterns unless the product has a clear reason to differ.
4. Pair with `$mobile-web-qa` for browser/device verification and `$accessible-interaction` for keyboard/focus/touch semantics.
5. Capture mobile `$snapshot` evidence before final response.

For peer controls, include a short label beside a wrapped label and check visible
top/bottom edges, not only width or hit targets. Use content-driven equal heights
within a row and center labels; reflow at large text rather than clipping or
shrinking. In illustrated UI, reserve clearance to actual button/frame artwork,
including the bottom action after scrolling. A dedicated detail popup need not
add an accordion when the product expects its instructions to be immediately
readable. These choices follow the project's contract, not a universal skin.

## Output Shape

Prefer compact, measured notes:

```text
Defect / decision:
Tag: [FACT] / [CRAFT] / [PD]
Severity: S1 / S2 / S3 when release impact matters
Rule:
Observed:
Expected:
Fix / decision needed:
Evidence:
```

When the user only needs implementation, keep the report shorter: say what changed, what evidence was captured, and what risk remains.
