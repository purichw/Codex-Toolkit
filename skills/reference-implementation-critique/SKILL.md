---
name: reference-implementation-critique
description: Compare a reference design against an implementation across geometry, rhythm, hierarchy, density, weight, affordance, states, and product decisions. Use when Claude, Figma, screenshot, static mock, HTML reference, live reference, before/after UI, or production implementation needs measured side-by-side critique or parity defects.
---

# Reference Implementation Critique

Use this when comparing Claude/Figma/screenshot/reference artifacts against a real implementation. It turns “not matching” into measured axes and explicit product decisions.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [11-reference-critique.md](../design-quality-review/references/design-quality/11-reference-critique.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Capture matched `$snapshot` evidence: reference plus implementation, same viewport, state, scroll, data, and framing where possible.
2. Compare the seven axes: geometry, rhythm, hierarchy, density, visual weight, affordance, states, and document mismatched conditions.
3. Separate faithful adoption, derived values, accessibility overrides, product decisions, and deliberate deviations.
4. Cite RC axes/rules plus specialist rule IDs when a deeper cause is clear.
5. Feed reference parity and product-contract tradeoffs into `$reference-to-a-tee`; distinguish source measurements, image measurements, and unknown properties.

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
