# Reference Workflow

Read this before extracting, inspecting, or mapping an offline Claude reference.
The goal is to shorten reference discovery without weakening the requirement to
render and measure the actual UI.

## Reference Extraction Accelerator

When offline Claude HTML files are available, create a machine-generated
inventory before doing manual mapping unless the task is a tiny single component
or the helper cannot run. Use the manifest to save time; do not treat it as
verification.

Run from the target project or working directory:

```bash
python3 /Users/point/.codex/skills/claude-to-a-tee/scripts/extract_reference.py \
  path/to/claude.html \
  --out .claude-reference
```

For environments with Python Playwright available, add rendered measurement and
screenshots:

```bash
python3 /Users/point/.codex/skills/claude-to-a-tee/scripts/extract_reference.py \
  path/to/claude.html \
  --out .claude-reference \
  --render --screenshots \
  --viewport 1440x900 --viewport 820x1180 --viewport 390x844
```

Use `reference-manifest.md` and `CLAUDE_TO_A_TEE_WORKLOG.md` as the first draft
of the coverage ledger, controls ledger, asset inventory, breakpoint list,
route/state signal list, and parity table seed. Reuse a previous manifest only
when the recorded SHA still matches the current Claude HTML. Manually render and
inspect the reference after using the helper; hidden states, computed geometry,
product mapping, behavior exceptions, and release-gate decisions remain
human-agent responsibilities.

## Reference State Inventory

Before editing, determine whether the Claude HTML is a single component, a
single page, or a multi-screen app. Do not assume from the filename, screenshot,
or first visible layout.

For bundled Claude HTML, inspect both the rendered UI and the embedded
JavaScript/state model. Search for signals such as `screen`, `tab`, `view`,
`step`, `modal`, `dialog`, `route`, `setScreen`, `setTab`, `onClick`, form
handlers, localStorage keys, and generated view-model sections.

Navigate from the initial view to every reachable page, route, screen, tab,
drawer, modal, and responsive-only state. Click every visible control, including
controls that appear static. Record the outcome as `state change`, `navigation`,
`modal/dialog`, `visual-only`, `no-op/static reference`, or `broken reference
setup`; never guess hidden behavior from a static Claude mock.

Create a coverage ledger before implementation with one row per reachable
surface:

- reference surface or state name;
- how to open it in the reference;
- visible controls/actions;
- observed outcome after clicking or operating each visible control;
- data shown and whether it is mock, static, or product-backed;
- target product mapping;
- implementation decision: implement, adapt, omit, or defer;
- reason for any omission or adaptation;
- decision label: `Claude adopted`, `product UX preserved`, `hybrid`, or
  `needs user decision`;
- evidence and risk when current product UX wins over Claude;
- product UX contracts at risk: persistence, routing, progressive disclosure,
  keyboard/focus, non-happy states, permissions, destructive safety, data
  density, responsive interaction, media handling, search click-through, or
  scroll choreography;
- verification required.

Also create a functional controls ledger for every visible action in each
surface. Include controls that are below the fold, inside drawers/rails, hidden
behind expanders, or shown only after scrolling. For each control, record:

- label/icon and source section;
- intended state transition from the Claude UI or handoff;
- target product read path and write path;
- permission/security boundary;
- expected success, failure, loading, and persisted-after-reload state;
- automated or manual verification performed.

Include inherited target controls in this ledger even when they are absent from
the Claude reference. Their decision must be `make real`, `make passive`,
`remove`, or `defer with user-approved reason`; `looks disabled enough` is not
a valid terminal state.

Do not mark a surface complete while this ledger contains a handoff-declared
control with no real write path, no product-approved omission, or no exercised
terminal state.

Do not start implementation until this ledger covers the default rendered state,
all navigation targets, tabs, forms, dialogs, onboarding/step flows, empty/error
states, and responsive-only states that appear in the reference.

Do not let the ledger become passive documentation. Keep it current as a release
gate: every row must end in one of `matched`, `behavior exception`, `visual
exception`, `deferred with user-approved reason`, or `not done`. A `not done`
row blocks claims of completion and blocks deploy.

Before editing, produce a user-facing or worklog decision summary for any row
where Claude will not be followed exactly:

```text
component | decision | why | evidence | risk | verification
```

This summary is mandatory for preserving current product UX over Claude. It is
also mandatory for hybrid choices that keep product behavior while adopting
Claude presentation.

When the decision preserves or hybridizes current product UX, include the
existing selector, test, route, or screenshot evidence that will guard it after
the visual change. If no guard exists, add a focused check instead of changing
tests to accept the loss of that behavior.

## Route Component Manifest

Before editing a multi-route reference, create a route-by-route component
manifest from the rendered Claude HTML. Do this even when the task sounds like a
single-page restyle, because Claude often puts product-defining components on
secondary routes.

For each route or screen, record:

- route name/path and how to open it in the reference;
- first-viewport structure: breadcrumb, masthead, hero, lead story, banner,
  carousel, pinned card, side rail, CTA, media panel, and nav state;
- below-the-fold structure: feeds, cards, filters, sidebars, related sections,
  footers, and repeated item counts;
- stateful variants: pinned vs unpinned, empty vs filled media, carousel dots,
  selected filters, modal open states, and responsive-only substitutions;
- product container behavior: sub-containers, internal scroll regions, sticky
  subpanels, virtualized lists, active-item auto-scroll, scroll restoration, and
  page-level overflow boundaries;
- product UX contracts: state persistence, URL/deep-link behavior, progressive
  disclosure, keyboard/focus, permission states, destructive safety, data
  density, media fallbacks, search result click-through, and responsive
  interaction;
- data contract: which visible item is lead/pinned/featured, whether it should
  also appear in a feed, and what happens if product data is missing;
- target mapping: exact product component/file/selector that will render each
  Claude component.

Treat `pinned`, `featured`, `lead`, `hero`, `banner`, and `carousel` as layout
contracts, not as ordinary sorting metadata. If Claude renders a pinned story as
a lead banner, the product must render the mapped pinned item as that banner or
document a visual exception. Do not remove the item from a list/feed unless the
Claude reference does the same or the product contract explicitly requires it.

After implementation, produce a missing-component report by route:

```text
route | Claude component | product mapping | status | exception/reason
```

Every Claude component in the manifest must be `matched`, `behavior exception`,
`visual exception`, or `deferred with user-approved reason`. A missing
route-specific component is a blocking mismatch even if global typography,
colors, and the homepage match.

## Inspect The Reference

1. Locate every supplied offline HTML, supporting file, asset, and handoff note.
2. Use `browser:control-in-app-browser` when available to render and inspect the
   offline Claude HTML. Exercise all pages, controls, and responsive states.
3. Read the underlying HTML, CSS, and JavaScript. Record component structure,
   selectors, computed dimensions, breakpoints, assets, transitions, and states.
4. Capture baseline screenshots at the relevant reference viewports. Treat
   user-supplied screenshots as route/state evidence, not as a replacement for
   rendered HTML inspection.
5. Inventory the target application's current interactions and selectors before
   editing so visual work does not break behavior.
6. Inventory target sub-containers, nested scroll regions, sticky subpanels,
   pagination/page-size controls, active-item scroll behavior, and any tests
   that currently prove them before copying Claude page flow.
7. Inventory target persistence, routing/deep links, progressive disclosure,
   keyboard/focus, non-happy states, permissions, destructive safety, data
   density, media handling, search click-through, responsive interaction, and
   scroll choreography before replacing existing structure with Claude markup.

Do not infer exact values from a screenshot when the offline source exposes
them. Do not copy isolated Claude CSS onto incompatible markup and call it
complete.

## HTML/CSS Visual Layer Contract

Treat the HTML/CSS visual layer as a first-class contract before editing. Record
the rendered DOM/component structure, shell and header geometry, page spacing
rhythm, typography system, card/list geometry, border/radius/shadow/background
treatment, image/media frames, and responsive breakpoints.

Use exact source or browser-computed values from the Claude HTML/CSS when they
are available. Screenshots are required evidence for rendered state and visual
inspection, but they do not replace source/computed measurement.

The visual layer contract should become the bridge between the coverage ledger
and the measured parity table:

```text
surface | shell/header | spacing rhythm | typography | card/list geometry | media frames | breakpoints | status
```

Each row must end as `matched`, `behavior exception`, `visual exception`,
`deferred with user-approved reason`, or `not done`.

Before editing, extract a small "component contract" for every affected Claude
component. Include the source values that can visually drift, especially:
layout mode (`flex`, `grid`, wrapping), width/min/max constraints, font size,
font weight, line height, letter spacing, padding, gap, margin, border radius,
border, shadow, image sizing/crop/transparency, and breakpoint overrides. If
the offline HTML exposes a value, use that value; do not replace it with
`clamp()`, inferred sizes, or product-polish alternatives unless the user's
newer requirement explicitly asks for the divergence.

At minimum, measure the global shell and every first-viewport component:

- page title/default route;
- top bars, masthead/logo, primary nav, secondary nav;
- user-visible scroll rhythm: total height, major section offsets, and where
  chapters, sticky panels, registers/lists, and footers first become visible;
- hero top offset, section height, sticky runway, headline box, media box,
  side rail/card, CTA, and chapter/slide count;
- first repeated grid/list: item count, grid columns, card box, media box,
  metadata, title, CTA/button;
- footer height, columns, visible link set, newsletter/form state;
- modal/dialog opened from the first viewport or primary CTA;
- the same components at source-defined desktop/tablet/mobile breakpoints.

Alongside the component contract, write down the reference's design intent in
plain engineering terms. For example: "quiet operational density," "large card
for a high-trust gate," "muted forest background only on filled actions," or
"progress summary first, details second." Use those principles when the exact
reference surface is not product-appropriate.

For animation and motion, match the reference when it exists. If the Claude
reference is static, record that fact and preserve product-required behavior
without inventing decorative animation as a substitute for parity.
