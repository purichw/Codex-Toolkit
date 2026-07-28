---
name: visual-diagnosis
description: Diagnose why a rendered UI looks cheap, cramped, scattered, generic, heavy, low-trust, or unfinished using observable visual rules. Use when the user says a UI looks off, wrong, ugly, AI-made, unpolished, not premium, visually noisy, too empty, too dense, low trust, or hard to critique before editing.
---

# Visual Diagnosis

Use this when a UI looks off and the cause is unclear. The goal is to name the defect precisely before editing: cheap, cramped, scattered, generic, heavy, low-trust, unfinished, or a measured subcase.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [01-visual-diagnosis.md](../design-quality-review/references/design-quality/01-visual-diagnosis.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Render the actual screen and capture `$snapshot` context before final response; use Appendix A for formal QA.
2. Run the cheap visual transforms mentally or mechanically: grayscale, blur, invert, edge/threshold, and spacing/alignment measurement.
3. Classify the dominant defect first; avoid bundling three vague diagnoses into one comment.
4. Cite the VD rule, tag `[FACT]` / `[CRAFT]` / `[PD]`, assign S1/S2/S3 when release impact matters, and propose one concrete fix.
5. After fixing, re-render and compare the same viewport/state rather than trusting the code diff.

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
