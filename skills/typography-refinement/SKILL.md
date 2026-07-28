---
name: typography-refinement
description: Refine UI typography for multilingual text, prose measure, numeric data, headings, tables, dashboards, truncation, line-height, and typographic rhythm. Use when type hierarchy, measure, line-height, font weights, widows, data precision, tabular numbers, dates, units, truncation, localization, RTL, or multilingual expansion carry the experience.
---

# Typography Refinement

Use this when the UI is readable but not typographically disciplined, or when dense numbers, prose, multilingual content, truncation, or headings carry the experience.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [08-typography.md](../design-quality-review/references/design-quality/08-typography.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Inventory type roles, font sizes, weights, line heights, measures, numeric columns, and truncation points.
2. Check multilingual expansion, RTL/logical properties, script-specific leading, and width-based truncation where relevant.
3. Use tabular figures, alignment, precision, units, dates, and baselines consistently for data-heavy surfaces.
4. Fix widows, overlong measures, cramped leading, excessive weights, and arbitrary font-size drift.
5. Verify with `$snapshot`, grayscale/blur when hierarchy is the question, and data examples at realistic lengths.

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
