---
name: global-quick-design-spec
description: Export concise implementation-ready UI design specs quickly from screenshots, existing source files, CSS, routes, prototypes, or live app state. Use when the user asks for a quick/fast design spec, lightweight design handoff, concise page spec, screenshot-to-spec export, or "export FAST spec" and wants a reusable Markdown artifact without redesigning or modifying app code.
---

# Global Quick Design Spec

## Overview

Create a compact Markdown design spec from the smallest reliable source set:
usually the provided screenshot plus relevant component/CSS files. Optimize for
speed, implementation usefulness, and low context cost.

## Default Output

If the user asks to export, create a file instead of only replying inline.

- Prefer `docs/design-handoffs/<page-or-surface>-design-spec.md` when that folder
  exists.
- Otherwise use `docs/<page-or-surface>-design-spec.md`.
- If no repository or docs folder is available, provide the spec inline.
- Do not modify app code unless the user explicitly asks for implementation.

Target length: 120-180 lines. If the user says "very fast" or gives a line cap,
honor the cap.

## Fast Workflow

1. Inspect the provided screenshot or visual artifact.
2. Identify the page/surface name, route, and likely source files.
3. Use `rg` to find matching component classes, route names, headings, and CSS.
4. Read only the relevant component and style ranges.
5. Check existing `docs/design-handoffs/` examples if the repo has them.
6. Use `$snapshot` automatically before the final response when a
   live/renderable UI, screenshot set, prototype, or visual reference is in
   scope. Capture current wide/context evidence plus mobile when responsive
   behavior matters. If no fresh snapshot can be captured, record the supplied
   artifact used and the remaining visual risk.
7. Write the spec in one pass using the concise template below.
8. Run no tests for docs-only export; mention that no tests were run.

If exact values are easy to extract from CSS, include them. If not, describe the
design role rather than inventing values.

## Concise Template

Use these sections by default:

```markdown
# <Page/Surface> Design Spec

Source:
- Screenshot: <provided / path / description>
- Runtime surface: <route or component>
- Implementation files: `<file>`, `<file>`

## Purpose
<2-5 bullets describing what this page must do.>

## Visual Direction
<Short description of the existing aesthetic. State that the existing design
system should be preserved.>

## Layout
<Shell, major regions, grid/flex behavior, ordering, important breakpoints.>

## Components
<One short subsection or bullet group per visible component/control. Include
labels, behavior, and important states only.>

## Tokens And Styles
<Existing CSS variables, colors, type, spacing, radius, shadows. No new palette.>

## Responsive Behavior
<Desktop/tablet/mobile rules and collapse order.>

## Accessibility
<Labels, keyboard, focus, dialogs, aria/status/error requirements.>

## Guardrails
<What future implementers must not break or redesign.>

## QA Checklist
<Short checklist for visual, responsive, interaction, and state verification.>
```

## Content Rules

- Prefer concrete implementation hooks: class names, component names, route
  names, props, CSS variables, and exact copy.
- Preserve the current product language and visual system.
- Separate observed facts from inferred recommendations when needed.
- Keep prose tight. This is a handoff, not a design essay.
- Do not create a new brand direction, landing page, or redesign unless asked.
- Do not include unrelated source archaeology.

## Final Response

Report the created file path with a clickable link when possible. Mention any
important limitation, such as "docs-only, no tests run" or "source not found, spec
based on screenshot only." Include the `$snapshot` evidence captured, or explain
why no fresh snapshot was available.
