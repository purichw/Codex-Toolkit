---
name: claude-design-reference-bundle
description: Create a Claude Design handoff/reference bundle from a live web page, local route, screenshot set, or prototype. Use when the user asks for snapshot + full design spec, Markdown files for Claude Design, a visual replication package, a design handoff bundle, or a faster alternative to standalone HTML/to-a-tee export that still preserves product behavior and implementation constraints.
---

# Claude Design Reference Bundle

Create a compact upload-ready bundle that helps Claude Design replicate an existing page without requiring a standalone HTML export. The bundle should combine screenshots, measured design notes, product context, state coverage, and a clear prompt.

## Workflow

1. Confirm the source surface and scope:
   - Route/URL or local file to inspect.
   - Page(s), viewport(s), and states to include.
   - Whether the goal is replicate/polish, redesign, or exploratory variants. Default to replicate/preserve.

2. Capture visual evidence:
   - Render the real page, not just source files.
   - Capture desktop and mobile by default.
   - Capture relevant states when they affect design: menus, filters, search result, empty state, modal/drawer, accordion open, sticky/floating UI.
   - If the user supplied screenshots, copy or reference them in the manifest and treat them as authored evidence.

3. Scaffold the bundle:
   - Prefer `scripts/create_bundle.mjs` when a URL is renderable and Playwright is available.
   - Use manual screenshots if the surface needs login, existing browser state, or special setup.
   - Read `references/bundle-files.md` before filling the Markdown files.

4. Fill the Markdown files:
   - Write for Claude Design as the next consumer.
   - Include concrete geometry, tokens, typography, spacing, data counts, behavior constraints, and intentional exceptions.
   - Mark unknowns explicitly instead of guessing.
   - Keep product truth intact; do not make the bundle silently conform to mock-only screenshots.

5. Gate quality:
   - Read `references/quality-gate.md` before finalizing.
   - Check that screenshots, metrics, Markdown, and prompt all describe the same route/state.
   - Report remaining visual or behavior exceptions.

## Output Shape

Create one directory per bundle, usually under the project `outputs/` folder:

```text
outputs/<page-or-route>-claude-design-bundle/
├── MANIFEST.md
├── PROJECT-CONTEXT.md
├── DESIGN-SPEC.md
├── REFERENCE-STATES.md
├── IMPLEMENTATION-CONTRACT.md
├── CLAUDE-DESIGN-PROMPT.md
├── metrics.json
└── screenshots/
    ├── desktop.png
    └── mobile.png
```

Use short, stable file names. If there are multiple routes, group screenshots by route slug.

## Helper Script

Run from the target project root so dependency lookup and relative output paths match the project:

```bash
node /Users/point/.codex/skills/claude-design-reference-bundle/scripts/create_bundle.mjs \
  --url http://127.0.0.1:4324/temples/popular/ \
  --out outputs/temples-popular-claude-design-bundle \
  --name temples-popular \
  --ready "[data-popular-temple-grid]" \
  --viewports desktop=1440x1800,mobile=390x1200 \
  --session-storage mongkolwela.loader.v2.seen=1 \
  --local-storage mongkolwela.pdpa.analytics=declined
```

For simple click states:

```bash
node /Users/point/.codex/skills/claude-design-reference-bundle/scripts/create_bundle.mjs \
  --url http://127.0.0.1:4324/temples/popular/ \
  --out outputs/temples-popular-claude-design-bundle \
  --state province-open=".temple-province-accordion summary" \
  --state map-open="[data-temple-map-open]"
```

The script creates baseline screenshots, `metrics.json`, and Markdown skeletons. The agent must still inspect and edit the Markdown; generated text is a starting point, not the final spec.

## References

- Read `references/bundle-files.md` when creating or editing bundle documents.
- Read `references/quality-gate.md` before reporting completion.

## Rules

- This is not a standalone HTML export.
- Do not redesign unless the user explicitly asks.
- Preserve product behavior, data contracts, responsive constraints, route links, permissions, loading/empty/error states, and measured item counts.
- When a screenshot/mock differs from the real product, label it as a behavior or visual exception instead of quietly changing the product truth.
- Include enough detail for Claude Design to avoid inventing layout, copy, data counts, and interactions.
