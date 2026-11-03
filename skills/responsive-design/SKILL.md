---
name: responsive-design
description: Design, implement, or repair responsive web layouts while preserving brand, content, interaction state, and composition across narrow, medium, wide, and intermediate widths. Use for fully responsive pages, desktop/mobile/tablet reference adaptation, content-driven breakpoints, container queries, cramped layouts, or overflow repairs. Not native app design or device/browser QA alone.
---

# Responsive Design

Make the same product work and look intentional at different available sizes.
No horizontal scrollbar is a necessary check for ordinary content, not proof of
good composition, complete functionality, or accessibility.

## Scope And Routing

- Use `$ui-ux-expert` as the design lens when available. Keep the project's
  brand, components, typography and user direction; this skill supplies no theme.
- Own layout decisions and implementation. Use `$mobile-web-qa` for relevant
  browser, input, keyboard and device verification, not a second redesign pass.
- For faithful image/HTML references, use `$reference-to-a-tee` where available;
  distinguish the supplied viewport from inferred responsive behavior.
- For native iOS/Android layouts, route to `$ui-ux-expert-mobile-native` instead.
- Use `$snapshot` automatically for visible implementation or audit work before
  the final response. Inspect current captures; never wait for a screenshot
  request. Skill-text maintenance alone does not need UI screenshots.
- Load only relevant references below. Missing companion tools are a limitation
  to report, not a reason to invent evidence or install dependencies silently.

## Choose The Starting Point

Read the owner files, project instructions, real content and supplied reference
before changing layout. Record the main user task and what must remain intact:
brand/fonts, hierarchy, primary actions, data, component language and good states.

| Starting point | Responsive decision |
| --- | --- |
| New design | Plan narrow, medium and wide compositions together around the task and real content. |
| Desktop reference | Preserve the approved wide composition; recompose narrower views without losing capability. |
| Mobile reference | Preserve the approved narrow view; constrain reading width and group related content on wider views. |
| Tablet reference | Adapt toward both ends independently; do not force the same columns everywhere. |
| Existing broken layout | Reproduce the failing state, diagnose its owning constraint, and repair it without replacing healthy architecture. |

Treat source documents and demos as evidence/material, not permission to redesign
unrequested surfaces, change business logic, publish, or deploy. Ask only when a
missing fact would materially change the implementation.

## Plan The Behavior

For a substantial change, write a compact matrix: region, invariant, narrow /
medium / wide behavior, pressure that triggers the change, and risky states.
A one-control repair needs only its owner, cause and affected boundary.
Use [layout-decisions.md](references/layout-decisions.md) for the decision rules
and implementation examples.

- Start review at roughly 390 / 820 / 1440 CSS px plus the actual reference
  viewport. These are observation anchors, not compulsory breakpoints or a
  claim of complete coverage. Verify 320 CSS px reflow when claiming full-page
  responsive coverage; include intermediate widths and relevant short heights.
- Choose thresholds from content pressure. Navigation, hero and grid can change
  at different widths. Prefer intrinsic sizing; preserve the project's healthy
  query convention rather than rewriting desktop-first CSS by habit.
- Preserve hierarchy while choosing flex, wrap, new columns, recomposition,
  disclosure, or an equivalent representation. Hide decorative redundancy only;
  do not silently remove required information, actions or permission boundaries.
- Give tablet a deliberate composition and wide screens a bounded content area.
  Do not invent testimonials, statistics or features to fill available space.
- Keep role-based, readable type. Reflow text, grow its container or change the
  layout before shrinking it. Do not scale font sizes with viewport width.

## Implement At The Owner

- Reuse shared components and data/state owners. Fix repeated defects at their
  owner and verify affected consumers. CSS should not remount/reset forms,
  selected dates, filters, current page, dialogs or explicit view preferences.
- Use Grid/Flex constraints, `minmax(0, 1fr)`, `min-inline-size: 0`, wrapping,
  bounded content widths and container queries where the component's space is
  the actual constraint. Do not stack patches over an unexplained cause.
- Let text boxes grow. Avoid fixed text heights, absolute-positioned normal
  content, whole-page scaling, global `word-break: break-all`, and body-level
  overflow hiding used to conceal a defect. Check clipped text, not only edges.
- Preserve semantic DOM and reading/focus order. A disclosure is not necessarily
  a modal; choose the correct focus behavior. Width does not identify touch input.
- Keep essential two-dimensional content in a deliberate local scroll region
  with keyboard access and understandable relationships. An equivalent agenda
  or card view must share data/state and avoid duplicate active controls/IDs.
- Check real Thai/English copy, font weights, marks, long labels and error text.
  Preserve critical amounts, dates, status and terms; do not shrink them to fit.
- Keep meaningful media visible with correct aspect, focal point and loading
  behavior. `srcset`/`sizes` and art-directed `<picture>` solve different needs.

## Verify And Stop

Read [verification.md](references/verification.md) for scope selection, the
optional collector, standards and evidence limits. Before expensive QA, state
the selected widths/states, required evidence, stop rule and omitted checks.

1. Inspect source/reference and before evidence where available; never recreate
   a "before" and present it as a prior capture.
2. Render the affected layout with loaded fonts/assets and representative data.
   Inspect composition, rhythm, line lengths, CTA priority, crop, clipping and
   overlap, not just a document-width assertion.
3. Check relevant transition boundaries (B-1 / B / B+1), a width inside each
   changed range, and the previously good source viewport. Container thresholds
   require container-width evidence, not just viewport numbers.
4. Exercise actual controls and resize the same live page while relevant state
   is active. Separate page loads cannot prove state survival or focus recovery.
5. Fix observed defects causally, re-render after the final edit, and inspect the
   current `$snapshot` evidence. Use proportionate regression checks per changed
   owner, including every in-scope deliverable.

Stop when agreed behavior and visual requirements have current evidence, or
report precisely what is failed, untested or blocked. Do not keep redesigning
without an observable problem. Report preserved/adapted behavior, important
breakpoint reasons, tested route/state/viewport/engine and remaining limitations.
An exit-zero collector or structural skill validator is never a UI/UX verdict.

## Resources

- [layout-decisions.md](references/layout-decisions.md): composition, constraint
  diagnosis, CSS patterns, Thai/English content, media and state transitions.
- [verification.md](references/verification.md): proportional evidence matrix,
  collector commands, manual checks and authoritative accessibility references.
- [responsive-audit.mjs](scripts/responsive-audit.mjs): optional initial-state
  Playwright evidence collector, not an interaction or aesthetic grader.
- [responsive-audit.test.mjs](scripts/responsive-audit.test.mjs): executable
  fixture tests for the helper; run when maintaining its behavior.
- [source-notes.md](references/source-notes.md): source-kit provenance,
  intentional adaptations and limits of the supplied examples.
