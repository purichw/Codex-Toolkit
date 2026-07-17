---
name: claude-design-md-request
description: Draft or refine prompts that ask Claude Design to produce implementation-ready Markdown handoffs/specs from screenshots, standalone HTML, prototypes, or design references. Use when the user wants a Claude MD request, Claude handoff prompt, component mapping request, design-to-code spec request, or needs Claude output that separates visual facts from product decisions and preserves an existing app's product contracts.
---

# Claude Design MD Request

Use this skill to write a request for Claude Design that returns a Markdown handoff Codex can implement with less guesswork. The request must make Claude separate evidence from opinion, and must not treat Claude's product decisions as automatically correct.

## Core Rule

Claude can be right or wrong. Ask Claude to document what it sees and recommends, but require every product-level recommendation to be classified:

- `adopt`: clearly compatible with the existing product contract.
- `adapt`: useful direction, but must be fitted to existing behavior/data/state.
- `reject`: conflicts with product decisions, scope, accessibility, data, or implementation constraints.
- `needs owner decision`: cannot be safely decided from the artifact.

Visual facts can be extracted from Claude artifacts. Product decisions still need Codex/user judgment.

## Prompt Inputs

Before drafting the Claude request, identify these fields from the user or current task:

- `Target surface`: page, route, modal, component, or flow.
- `Artifacts`: screenshots, standalone HTML, MD, Figma notes, existing app route, or source files.
- `Goal`: visual parity, component mapping, interaction spec, responsive spec, content restructure, etc.
- `Prevail rules`: what wins if sources conflict.
- `Do not touch`: components, routes, data, copy, logic, auth, scoring, header/nav, etc.
- `Required states`: desktop/mobile, active/disabled/completed/locked/error/loading, signed-in state, progress state.
- `Known product decisions`: behavior that must remain even if Claude suggests otherwise.

If the user has not specified prevail rules, include a placeholder that forces Claude to label conflicts instead of resolving them silently.

## Claude Request Template

Use and adapt this prompt:

```markdown
You are preparing an implementation-ready Markdown handoff for Codex.

Context:
- Product/app:
- Target surface:
- Artifacts provided:
- Existing product decisions that must be preserved:
- Do not touch:
- Required routes/states/viewports:

Important:
Claude Design may propose good ideas, but your product decisions are not automatically authoritative. Separate visual facts, interaction inferences, and product recommendations. If you are unsure, mark it as unknown or needs owner decision.

Please produce a Markdown handoff with these sections:

1. Implementation Scope
- What this handoff covers.
- What is explicitly out of scope.
- What must not be changed.

2. Source Inventory and Provenance
- List each artifact used.
- For each observation, note whether it comes from HTML/CSS, screenshot, existing product behavior, or your inference.
- Mark confidence as high/medium/low.

3. Product Decision Review
Create a table:
| Item | Claude recommendation | Type: visual/interaction/product/content | Evidence | Adopt/adapt/reject/needs owner decision | Rationale | Risk if implemented blindly |

4. Component Map
For each component or region:
- Name / role.
- Purpose.
- Visible elements.
- Props/state/data it appears to need.
- Click targets and destinations.
- Dependencies on existing product contracts.

5. Visual Geometry
- Layout structure.
- Spacing and alignment.
- Typography hierarchy.
- Card/button/input geometry.
- Borders, radius, shadows.
- Color tokens or approximate colors.
- If values are estimated from screenshots, label them approximate.

6. Interaction and State Matrix
Cover default, hover/focus if visible or inferable, selected, disabled, loading, empty, error, completed, locked, and any modal/dropdown/open states. Do not invent states as final requirements; label inferred states.

7. Responsive Behavior
Describe desktop, tablet if relevant, and mobile behavior. Include what stacks, hides, scrolls, wraps, or changes size. Flag anything not visible in artifacts.

8. Assets and Icons
List images, icons, illustrations, audio controls, or other assets. Note whether assets are embedded, external, existing repo assets, or need replacement.

9. Accessibility Notes
List semantic controls, labels, focus behavior, keyboard expectations, contrast risks, reduced motion considerations, and touch target risks.

10. Implementation Acceptance Checklist
Write concrete checks Codex can verify with browser snapshots or tests. Include desktop and mobile checks when relevant.

11. Open Questions
Only include questions that block implementation or product judgment. Do not ask questions that can be answered from the artifacts.
```

## Reconciliation Rules for Codex

When using Claude's MD output:

- Treat standalone HTML/CSS as the strongest source for visual geometry.
- Treat screenshots as strong visual evidence, especially when HTML is absent or stale.
- Treat Claude MD as intent, mapping, and risk analysis, not as automatic truth.
- Preserve existing product behavior unless the user explicitly says Claude should prevail.
- If Claude suggests a product behavior change, classify it before implementing.
- If sources conflict, decide explicitly and state why; ask the user only when the risk is product-level or irreversible.
- Do not broaden scope just because Claude listed adjacent improvements.

## Quality Bar

The Claude request should reject vague design prose. Ask for concrete, implementable notes:

- Prefer "button height appears 44-48px, pill radius, left icon, label, chevron" over "make the button modern."
- Prefer "Header is out of scope; do not describe changes" over "keep global navigation consistent."
- Prefer "unknown in screenshot" over invented responsive behavior.
- Prefer "product decision, needs owner decision" over silently adopting Claude's opinion.

## Short Version

If the user wants a quick prompt, produce a compact Claude request that still includes:

`scope`, `artifacts`, `prevail rules`, `do not touch`, `component map`, `visual geometry`, `state matrix`, `responsive`, `product decision review`, and `acceptance checklist`.
