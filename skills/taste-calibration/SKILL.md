---
name: taste-calibration
description: Calibrate UI taste with paired works/fails specimens, weekly drills, category comparisons, and smallest-change improvement loops. Use when the user wants to sharpen design taste, compare a screen against category specimens, count fail-column traits, run a calibration drill, or find the single smallest change that improves a UI.
---

# Taste Calibration

Use this when the goal is to improve taste judgment, compare a screen against category specimens, or run a lightweight recurring calibration drill.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [12-taste-calibration.md](../design-quality-review/references/design-quality/12-taste-calibration.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Pick the closest category specimen and count how many traits the current screenshot shares with the failing column.
2. Use Appendix A capture conditions for a fair comparison.
3. Name the dominant defect with `$visual-diagnosis`, then choose the single smallest change that moves the screen toward the works column.
4. Treat category content choices as `[PD]` when product ownership is required.
5. Log the score and repeat with the same method so improvement is measurable over time.

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
