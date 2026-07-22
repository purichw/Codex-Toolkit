---
name: global-full-design-spec
description: Export comprehensive implementation-ready UI design specs from screenshots, existing source files, CSS, routes, prototypes, live app state, or design references. Use when the user asks for a full/detailed design spec, exhaustive design handoff, complete page contract, source-mapped spec, accessibility/state matrix, or a Markdown artifact that future Codex/Claude/dev work can implement from without re-discovery.
---

# Global Full Design Spec

## Overview

Create a complete Markdown design contract for a UI surface. Use this when
future implementers need enough detail to preserve layout, states, copy,
accessibility, responsive behavior, and source-level hooks without redoing the
discovery work.

## Default Output

If the user asks to export, create a Markdown file.

- Prefer `docs/design-handoffs/<page-or-surface>-design-spec.md` when that folder
  exists.
- Otherwise use `docs/<page-or-surface>-design-spec.md`.
- If no repository or docs folder is available, provide the spec inline.
- Do not modify app code unless the user explicitly asks for implementation.

Target length: as long as needed for completeness, commonly 250-600 lines. Keep
it structured and skimmable rather than verbose.

## Discovery Workflow

1. Inspect every provided screenshot, image, prototype, URL, or design reference.
2. Identify route, page/surface name, major visible components, and likely source
   ownership.
3. Use `rg` to find headings, labels, routes, class names, component names, and
   CSS selectors.
4. Read the relevant component files, style files, design-system files, and any
   existing handoff docs for local format.
5. Extract exact implementation anchors where available:
   - component/class names
   - route names
   - CSS variables
   - fixed colors
   - spacing/radius/shadow values
   - copy strings
   - data/state props
   - accessibility attributes
6. Distinguish observed source facts from inferred design intent.
7. Use `$snapshot` automatically before the final response when a
   live/renderable UI, screenshot set, prototype, or visual reference is in
   scope. Capture current wide/context evidence plus mobile when responsive
   behavior matters. If no fresh snapshot can be captured, record the supplied
   artifact used and the remaining visual risk.
8. Create the spec artifact with the full template below.
9. Run no tests for docs-only export; if app code changes are made separately,
   run the repo's appropriate checks.

Use existing project design systems and brand direction. If a UI/UX skill or
project-specific design skill is already active or explicitly required by local
instructions, follow it as the higher-level design lens.

## Full Template

Use these sections by default. Remove sections only when clearly irrelevant.

```markdown
# <Page/Surface> Design Spec

Source reference:
- Screenshot/design reference: <path, URL, or description>
- Runtime route/surface: <route/screen/state>
- Implementation files: `<file>`, `<file>`
- Styling/design-system files: `<file>`, `<file>`

## Purpose
<Primary jobs, audience, product role, non-goals.>

## Visual Direction
<Aesthetic direction, product tone, visual hierarchy, what must be preserved.>

## Implementation Anchors
<Class names, component names, route IDs, state objects, props, data contracts.>

## Layout
<Shell, page regions, grid/flex structure, spacing rhythm, ordering, scroll
behavior, sticky/fixed elements, empty/overflow expectations.>

## Component Specs
<Subsection per component. Include copy, hierarchy, interaction, states,
disabled/loading/error/success/empty variants, and source hooks.>

## Dialogs And Overlays
<Modal/backdrop behavior, focus/close rules, scroll handling, dangerous actions.>

## Typography
<Font stack, heading/body scales, weights, line-height, label styles.>

## Color And Tokens
<CSS variables, observed fixed values, semantic roles, contrast concerns.>

## Spacing, Radius, And Elevation
<Container widths, gaps, padding, border widths, radius, shadows.>

## Responsive Behavior
<Breakpoints, collapse order, mobile stacking, touch target expectations,
viewport-specific risks.>

## Accessibility Contract
<Labels, aria, keyboard path, focus, live regions, dialogs, semantic headings,
reduced motion, color-not-sole-indicator.>

## Content Rules
<Exact labels, capitalization, tone, dynamic grammar, copy constraints.>

## Guardrails
<Things future agents/devs must not break, redesign, remove, or infer wrongly.>

## QA Checklist
<Visual, responsive, interaction, state, accessibility, regression, and
production/preview checks as appropriate.>
```

## Component Depth Rules

For each important component, capture:

- user-visible copy
- structural role in the page
- default state
- active/selected state
- hover/focus state when source reveals it
- disabled/loading state
- error/success/empty state
- keyboard behavior
- source hooks/classes

Skip decorative details that do not affect implementation unless they are
visually distinctive or easy to regress.

## Source Mapping Rules

- Prefer exact source facts over visual guesses.
- Cite local file paths inside the spec when helpful.
- Include exact CSS values only when read from source or directly inferable.
- Say "observed" for screenshot-derived facts and "source" for code-derived
  facts if ambiguity matters.
- Never invent class names, tokens, routes, data props, or breakpoints.
- If source cannot be found, state that the spec is screenshot-only.

## Design Rules

- Preserve the existing product design system, typography, palette, and shell.
- Do not introduce a redesign, alternate palette, landing page, or extra
  navigation unless requested.
- Prefer native controls and established component patterns.
- Avoid card-in-card layouts unless the existing design system explicitly uses
  them.
- Keep controls, labels, and states implementation-ready rather than ornamental.

## Final Response

Report:

- the created file path as a clickable link when possible;
- whether the spec was based on screenshot only or screenshot plus source;
- what `$snapshot` evidence was captured, or why no fresh snapshot was
  available;
- that no tests were run for docs-only export, unless tests actually ran.
