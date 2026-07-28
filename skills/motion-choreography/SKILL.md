---
name: motion-choreography
description: Design, audit, or repair UI motion timing, easing, choreography, loading feedback, overlay transitions, scroll motion, and reduced-motion alternatives. Use when navigation, overlays, drawers, sheets, loading, hover/press feedback, drag, scroll, state changes, choreography, performance, or reduced-motion behavior needs design or QA.
---

# Motion Choreography

Use this when UI motion exists or should exist: navigation, overlays, loaders, drag, hover, feedback, scroll, state changes, or reduced-motion behavior.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [09-motion.md](../design-quality-review/references/design-quality/09-motion.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Identify which state change needs motion and what the motion communicates.
2. Choose duration/easing by surface size and risk; avoid unrelated decorative movement.
3. Keep motion transform/opacity-friendly and make exit faster than enter when appropriate.
4. Provide reduced-motion alternatives that preserve feedback without translation.
5. Verify by exercising the state, checking performance, and capturing `$snapshot` or short evidence at key states.

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
