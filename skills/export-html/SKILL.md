---
name: export-html
description: Create to-a-tee, live-parity standalone/offline HTML exports and clickable prototypes for design handoff, Claude Design, visual audit, or state review. Use when the user asks to export HTML, standalone HTML, offline HTML, clickable prototype, design handoff, or a file Claude/Figma/another agent can inspect, especially when the export must match an existing product screen exactly/component-perfectly or show representative UI states.
---

# Export HTML

## Overview

Create HTML exports as executable design documentation. The export must preserve the source screen's visual truth to a tee: product semantics, responsive behavior, and major states without inventing a new design.

## Non-Negotiables

- Treat "export HTML" as **to-a-tee live/source parity**, not redesign. If exporting an existing app screen, render the real app/component first and match it component-perfectly wherever technically possible.
- Do not add hero panels, decorative wrappers, marketing copy, or alternate layout concepts unless the source screen already has them or the user explicitly asks.
- Do not create a collage, summary board, contact sheet, state gallery, or multi-screen wall unless explicitly requested. The default export must behave like the live flow: one screen visible at a time, with navigation/state controls that switch screens rather than showing all screens side by side.
- Keep prototype controls separate from the exported design surface. Put them in a collapsed dev overlay, query/hash controls, or a clearly labeled non-product toolbar outside the first viewport.
- The file must open directly with `file://` unless the user asks for a server-backed prototype.
- Every visible interaction included in the export must work locally with client-side mock state. Do not leave clickable-looking controls inert.
- Verify the exported HTML in a browser before final response.

## Workflow

1. **Identify Source**
   - Record the requested screen(s), route(s), and purpose of export.
   - If the source is an existing product screen, render the live/local app first. Use screenshots and computed dimensions for important components.
   - If the source is a design file or screenshot, render/open that reference before building.

2. **Create State Inventory**
   - List every route/screen requested.
   - List normal/default, modal/popover, validation, empty, loading, success/pass, failed/error, locked/unlocked, enabled/disabled, and responsive-only states that materially change the UI.
   - Decide which states need full representation and which can be representative samples.

3. **Build Export**
   - Prefer one standalone `.html` file with inline CSS/JS.
   - Use product CSS tokens, spacing, typography, assets, copy, and real component structure wherever possible.
   - Use realistic mock data from the product. Do not use filler unless data is unavailable; label mock-only data in notes.
   - Make state switches clickable with local JavaScript.

4. **Verify**
   - Open the export with `file://`.
   - Exercise state controls and primary interactions.
   - Check desktop and mobile at minimum; add tablet when the layout changes there.
   - Check for console errors, page errors, horizontal overflow, clipped text, broken assets, and source-parity drift.

5. **Deliver**
   - Provide the absolute file path.
   - Summarize which states are included and any intentional omissions.
   - Say what verification was performed.

## Parity Standard

The export must be live/source **to a tee**: component-perfect wherever technically possible. "Close enough" is not acceptable unless the exception is documented in the export notes and final response.

- **Pixel/geometry:** match layout mode, max widths, spacing, padding, card radii, borders, shadows, and first-viewport rhythm.
- **Typography:** match font family, scale, weight, line height, letter spacing, and text wrapping.
- **Color/material:** match product tokens and surface roles. Do not "improve" palette.
- **Behavior:** match state transitions and visible terminal states, while using local mock state instead of real auth/API writes.
- **Responsive:** match mobile, tablet, and desktop breakpoints that the source supports.

When exact parity is impossible, document it as an exception in the export notes and final response.

## State Coverage Rules

Include all **major scenarios**. Do not exhaustively duplicate visually identical variants.

Required by default:

- Default/normal state for every requested screen.
- At least one success/pass/completed state when the screen has such a state.
- At least one failed/error/validation state when the screen has such a state.
- Important modal/popover/drawer states.
- Empty state and loading state when they are user-visible and distinctive.
- Disabled/locked/unlocked states when they change layout, hierarchy, or available actions.
- Mobile state and desktop state; tablet state if the layout changes materially.

Representative examples are acceptable:

- If there are 5 error messages with the same layout, include 1-2 representative errors.
- If pass/success states only differ by count, include one realistic pass state.
- If a badge/card/list can show 1, 10, or 20 items with the same layout, include the normal realistic count plus edge rows that exercise wrapping/overflow, not every count.
- If a repeated component has many item statuses, include one of each visually distinct status.

Do not omit a major state just because it is below the fold or behind a button.

## Prototype Controls

Use controls only to expose states, not as part of the product design.

- Place controls in a collapsed overlay, footer, or separate "prototype controls" region.
- Clearly label controls as mock/prototype-only.
- Do not let controls affect first-viewport visual parity.
- Ensure controls work with keyboard and click.
- Do not require network, auth, Firebase, database, or backend calls.

## Offline Asset Rules

- Prefer inline CSS/JS and local assets that work from `file://`.
- If referencing repo assets, use paths that resolve from the HTML file or copy assets into a nearby export folder.
- Do not use remote CDN assets unless the source already depends on them and offline operation is not required.
- Verify images, fonts, SVGs, icons, audio placeholders, and CSS backgrounds render.

## Export Notes To Include In The HTML

Add a small collapsed notes section or HTML comment with:

- source route/file and date;
- viewport(s) checked;
- states included;
- mock-only controls/data;
- product behavior that must be preserved;
- intentional omissions/exceptions.

## Verification Checklist

Before final response:

- `file://` export opens.
- No console/page errors.
- All prototype controls work.
- Primary states are reachable.
- Desktop and mobile layouts have no horizontal overflow.
- Text is not clipped or overlapped.
- Important components match source geometry closely.
- Assets render.
- Notes state what is mock-only.

Use Playwright or browser tooling whenever available. A final answer that says only "created the file" is incomplete.
