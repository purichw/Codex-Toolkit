---
name: interaction-design
description: Design and audit real UI interactions such as forms, autosave, undo, bulk actions, optimistic updates, permissions, interruption recovery, and destructive flows.
---

# Interaction Design

Use this when controls imply real behavior: submit, save, edit, select, bulk act, undo, retry, confirm, recover, or handle permission and failure states.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [04-interaction-design.md](../design-quality-review/references/design-quality/04-interaction-design.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Inventory each user action and the state transition it creates.
2. Define feedback, pending, success, partial failure, error, undo/retry, and interruption recovery before implementation.
3. Scale friction to risk for destructive actions and bulk changes.
4. Pair with `$interaction-flow-qa` when the journey must be exercised end to end, and `$form-flow-ux` for form-specific behavior.
5. Use `$snapshot` for visible states and behavior evidence for actual transitions.

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
