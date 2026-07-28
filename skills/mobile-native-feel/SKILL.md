---
name: mobile-native-feel
description: Design or audit mobile UI for safe areas, native controls, touch targets, keyboard behavior, thumb reach, sheets, gestures, and platform feel.
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

1. Check 390x844 and 360x800 at minimum, plus the relevant tablet size when scope includes responsive behavior.
2. Verify safe-area insets, dvh behavior, target sizes, scroll ownership, sticky actions, and keyboard visibility.
3. Prefer native/platform controls and patterns unless the product has a clear reason to differ.
4. Pair with `$mobile-web-qa` for browser/device verification and `$accessible-interaction` for keyboard/focus/touch semantics.
5. Capture mobile `$snapshot` evidence before final response.

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
