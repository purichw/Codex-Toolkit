---
name: design-system-architect
description: Architect, audit, or repair design-system tokens, component taxonomies, variants, galleries, drift metrics, and token-layer governance.
---

# Design System Architect

Use this when the design system itself needs architecture: token layers, component taxonomy, variants, gallery coverage, drift detection, or governance. Use `$design-system-guardian` for narrower preservation during everyday UI changes.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [06-design-systems.md](../design-quality-review/references/design-quality/06-design-systems.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Inventory primitives, tokens, roles, variants, themes, and gallery/test surfaces before adding new values.
2. Choose whether the change is token, primitive, variant, composition, or local exception.
3. Keep semantic tokens above raw scales and avoid one-off values that create drift.
4. Add or update component gallery/state coverage when shared primitives change.
5. Run drift checks and capture `$snapshot` evidence of the component or gallery surface.

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
