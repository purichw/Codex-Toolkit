---
name: information-architecture-ux
description: Structure navigation, grouping, hierarchy, progressive disclosure, screen purpose, and sequencing so user-facing UI is understandable.
---

# Information Architecture UX

Use this when the problem is organization: users cannot tell where they are, what matters, what comes next, or how content/actions are grouped.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [03-information-architecture.md](../design-quality-review/references/design-quality/03-information-architecture.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Write the screen purpose as one question before changing layout.
2. Map navigation, landmarks, headings, grouping, and primary action to that purpose.
3. Apply progressive disclosure only to secondary or rare work; keep core status and next action visible.
4. Separate empty, zero-results, loading, error, and permission-limited states in both copy and layout.
5. Capture `$snapshot` evidence and confirm the page still reads when nav is covered or blurred.

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
