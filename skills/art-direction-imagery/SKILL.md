---
name: art-direction-imagery
description: Select, crop, place, and verify UI imagery, thumbnails, hero media, placeholders, loading media, captions, focal points, and asset states.
---

# Art Direction Imagery

Use this when images, video stills, thumbnails, hero media, placeholders, or generated assets affect the UI quality. The goal is intentional media, not stock-like decoration.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Read Before Acting

- Shared vocabulary and severity: [00-conventions.md](../design-quality-review/references/design-quality/00-conventions.md).
- Main reference for this skill: [07-art-direction-imagery.md](../design-quality-review/references/design-quality/07-art-direction-imagery.md).
- Screenshot/release-grade QA: [appendix-a-screenshot-qa-protocol.md](../design-quality-review/references/design-quality/appendix-a-screenshot-qa-protocol.md).
- Design intent, PR notes, and checklists: [appendix-b-notes-and-checklists.md](../design-quality-review/references/design-quality/appendix-b-notes-and-checklists.md).

Read the main reference completely before making rule-backed claims. Read Appendix A before formal visual QA, release evidence, or screenshot capture matrices. Read Appendix B before producing handoff, PR, or definition-of-done language.

## Workflow

1. Decide the image job: evidence, atmosphere, object inspection, person, place, step, or placeholder.
2. Set aspect ratios, focal points, captions, alt behavior, loading placeholders, and failure states before styling.
3. Check crops at each breakpoint so faces, objects, text, and critical edges survive.
4. Pair with `$placeholder-image` or project image-asset skills when sourcing/replacing assets.
5. Use `$snapshot` and, when deployed media is involved, `$production-asset-smoke`.

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
