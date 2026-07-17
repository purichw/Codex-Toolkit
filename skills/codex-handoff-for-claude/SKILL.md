---
name: codex-handoff-for-claude
description: Prepare implementation-ready Markdown handoffs from Codex to Claude or Claude Design, especially for UI/UX work using ui-ux-expert. Use when the user asks to hand off a screen, route, component, prototype, screenshot, design task, or implementation brief to Claude with source-of-truth rules, product contracts, visual geometry, interaction states, responsive behavior, accessibility notes, and acceptance checks.
---

# Codex Handoff for Claude

Use this skill when Codex must prepare a Markdown handoff that Claude can act on
with minimal guesswork. This is the reverse direction of `claude-design-md-request`:
Codex is packaging context, constraints, evidence, and acceptance checks for Claude.

## Core Workflow

1. Identify the target surface: page, route, modal, component, flow, prototype, or
   screenshot set.
2. Inventory the artifacts available to Codex: screenshots, standalone HTML, live
   routes, source files, design notes, previous handoffs, or product docs.
3. State source-of-truth precedence. If sources conflict, label the conflict instead
   of resolving it silently.
4. Capture `DO NOT TOUCH` boundaries and must-preserve product contracts before any
   visual or implementation recommendations.
5. Separate every claim as `FACT`, `INFERENCE`, `REC`, or `?/UNKNOWN`.
6. Write one scannable Markdown handoff with concrete sections, tables, state
   matrices, and acceptance checks.

## UI/UX Handoffs

When the handoff is for UI/UX work and Claude should use `ui-ux-expert`, read
`references/codex-handoff-prompt.md` and adapt it to the actual artifacts.

Prefer references to `ui-ux-expert` tokens and documents:

- `tokens.css` token names for spacing, type, color, radius, shadow, and motion.
- `components.md` component names plus deltas instead of re-describing common
  controls from scratch.
- `layouts.md` layout names plus deltas for app shells, dashboards, forms, content
  pages, or heroes.
- `qa-checklist.md` for acceptance checks that can be verified with screenshots,
  DOM reads, or interaction tests.

Only cite these references when they are actually relevant. If a project has its
own brand, design system, or production UI, say that local context overrides global
defaults.

## Handoff Rules

- Do not invent behavior, data, brand facts, copy, metrics, logos, or assets.
- Mark anything not derivable from artifacts as `?/UNKNOWN` or `needs owner decision`.
- Keep visual facts, interaction inferences, and product recommendations separate.
- Treat source files and existing product behavior as product-contract evidence.
- Treat screenshots and standalone HTML as visual evidence, with confidence labels
  when values are approximate.
- Include open questions only when they block implementation or product judgment.

## Output Shape

Return a single Markdown document. For UI/UX handoffs, include:

- Contract header: surface, goal, artifacts, precedence, `DO NOT TOUCH`,
  must-preserve product decisions, required states/viewports.
- Product-decision review table.
- Component map.
- Visual geometry.
- Interaction and state matrix.
- Responsive behavior.
- Assets and icons.
- Accessibility notes.
- Acceptance checklist.
- Open questions.

Keep it tight and implementation-ready: tables and short bullets beat prose walls.
