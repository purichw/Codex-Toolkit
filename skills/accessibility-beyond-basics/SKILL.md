---
name: accessibility-beyond-basics
description: Audit advanced accessibility for screen-reader flow, cognitive load, low vision, complex widgets, data visualization, touch, zoom, and forced-colors behavior.
---

# Accessibility Beyond Basics

Use this when basic accessibility checks are not enough: complex widgets, dashboards, charts, dense forms, low vision, screen-reader flow, cognitive load, forced colors, zoom, or touch behavior.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [10-accessibility.md](../design-quality-review/references/design-quality/10-accessibility.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Start with `$accessible-interaction` for keyboard/focus semantics, then apply the advanced checks from the reference.
2. Map headings, landmarks, labels, descriptions, live regions, error announcements, and focus restoration through the real journey.
3. Test 200% and 400% zoom, contrast/forced-colors, reduced motion, touch target spacing, and non-color encodings.
4. For charts or dense data, provide table equivalents, units, direct labels, and more than color as encoding.
5. Capture `$snapshot` evidence for focus/zoom/layout and record assistive-tech checks that were skipped.

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
