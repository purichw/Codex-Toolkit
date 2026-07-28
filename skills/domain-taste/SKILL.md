---
name: domain-taste
description: Choose category-appropriate UI density, hierarchy, controls, and evidence for admin, SaaS ops, dashboards, ledgers, editorial, learning, landing, and mobile screens. Use when a screen feels generic, mismatched to its product category, too marketing-like for ops/admin, too sparse for data work, too dense for editorial/learning, or needs category-specific taste calibration.
---

# Domain Taste

Use this when a screen needs to feel native to its product category rather than generically polished. It turns domain intent into density, hierarchy, control placement, and evidence choices.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [02-domain-taste.md](../design-quality-review/references/design-quality/02-domain-taste.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Identify the screen category and the question the screen must answer.
2. Select the matching density tier and category conventions before styling.
3. Check category-specific state obligations, especially data age, precision, empty/zero-results, and action scope.
4. Flag product-owned choices as `[PD]` while still providing the shape of a good answer.
5. Verify with `$snapshot`; for category calibration, compare against `$taste-calibration` specimens.

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
