---
name: design-quality-review
description: Apply the shared design-quality rule language, severity model, screenshot QA protocol, calibration library, and definition of done for UI reviews. Use when Codex needs rigorous UI design QA, rule IDs, [FACT]/[CRAFT]/[PD] tagging, S1/S2/S3 severity, screenshot capture protocol, calibration drills, PR review notes, definition-of-done language, or routing among design-quality specialist skills.
---

# Design Quality Review

Use this as the shared operating layer for high-standard UI review. It owns the conventions, rule IDs, severity model, screenshot QA protocol, critique templates, calibration drill, and definition of done for the design-quality specialist suite.

Use `$ui-ux-expert` as the broad design lens when implementation or critique touches a visible user-facing surface. Use `$snapshot` automatically before the final response for any visual implementation, audit, comparison, or QA evidence; do not wait for the user to ask.

## Reference Bundle

The original Claude Design files are preserved verbatim in `references/design-quality/`. Use this quick path:

- [README.md](references/design-quality/README.md) for guide structure.
- [00-conventions.md](references/design-quality/00-conventions.md) for `[FACT]`, `[CRAFT]`, `[PD]`, severities, rule IDs, and screenshot transforms.
- [appendix-a-screenshot-qa-protocol.md](references/design-quality/appendix-a-screenshot-qa-protocol.md) for capture conditions, 25-item pass, PR review format, automation subset, and cadence.
- [appendix-b-notes-and-checklists.md](references/design-quality/appendix-b-notes-and-checklists.md) for design intent, designer-question, QA checklist, definition-of-done, critique-comment, and guide-growth templates.
- [12-taste-calibration.md](references/design-quality/12-taste-calibration.md) for paired specimens and calibration drills.

## Specialist Routing

- `$visual-diagnosis`: cheap, cramped, scattered, generic, heavy, low-trust, unfinished, or hard-to-name visual defects.
- `$domain-taste`: category density and conventions for admin, SaaS ops, dashboards, ledgers, editorial, learning, landing, and mobile screens.
- `$information-architecture-ux`: navigation, grouping, hierarchy, screen purpose, sequencing, and progressive disclosure.
- `$interaction-design`: autosave, undo, bulk actions, optimistic updates, permissions, interruption recovery, and destructive flows.
- `$mobile-native-feel`: safe areas, touch targets, keyboard behavior, sheets, gestures, and platform-native feel.
- `$design-system-architect`: token layers, component taxonomy, variants, galleries, drift metrics, and governance.
- `$art-direction-imagery`: image selection, crops, focal points, hero media, thumbnails, placeholders, captions, and asset states.
- `$typography-refinement`: type scale, measure, line-height, multilingual behavior, numeric data, dates, units, and truncation.
- `$motion-choreography`: motion timing, easing, choreography, loading feedback, overlays, scroll, and reduced-motion alternatives.
- `$accessibility-beyond-basics`: screen-reader flow, cognitive load, low vision, complex widgets, data visualization, zoom, and forced colors.
- `$reference-implementation-critique`: reference-vs-implementation comparison across geometry, rhythm, hierarchy, density, weight, affordance, and states.
- `$taste-calibration`: paired works/fails specimens, weekly drills, and smallest-change taste improvement.

## Workflow

1. Read `references/design-quality/README.md` and `references/design-quality/00-conventions.md` before using rule IDs, severities, or `[FACT]` / `[CRAFT]` / `[PD]` labels.
2. Choose the smallest specialist skill that matches the visible risk; do not load every specialist by default.
3. Use `$snapshot` automatically for visual evidence, and use Appendix A when a formal capture set or release-grade QA result is needed.
4. Record defects with tag, severity, observable measurement, rule ID, and proposed fix.
5. Separate product decisions from craft defects. A `[PD]` needs a decision or documented default, not a taste debate.
6. Use Appendix B for design intent notes, designer questions, PR templates, and definition-of-done language.

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
