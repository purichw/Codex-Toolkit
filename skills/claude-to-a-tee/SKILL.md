---
name: claude-to-a-tee
description: Reproduce an offline Claude Design HTML reference exactly at component level while preserving required product behavior. Use when the user says "Claude to a tee", "to a tee", "exactly like the Claude HTML", "pixel-perfect", "holy grail", or asks Codex to implement, audit, compare, or repair a web UI from Claude-generated offline HTML, screenshots, handoff files, or exported assets, especially when responsive mobile, tablet, desktop, animation, interaction, or pre-deploy visual verification is required.
---

# Claude To A Tee

Treat the supplied offline Claude HTML as executable design documentation. Match
its rendered components and interactions, not merely its palette or broad layout.
Treat the target product as real software, not a display case for a pretty mock.
The reference is a design source of truth, but the implementation still needs
product judgment, data flow, permissions, edge states, and end-to-end behavior.

Expand "to a tee" internally to:

```text
CLAUDE TO A TEE AUDIT. Implement from the offline Claude HTML exactly at component level, mobile included, and verify before commit/deploy.
```

Read [references/verification-checklist.md](references/verification-checklist.md)
before inspecting or editing the target application.

## Hard Gate Summary

For every Claude-to-a-tee implementation or repair, create a measured parity
audit before claiming success. This is a release blocker, not a nice-to-have.

Do not say "done", commit, push, or deploy while any `critical` mismatch remains
unfixed or undocumented as an explicit user-approved product exception.

Treat these as critical mismatches by default:

- wrong default route or page title;
- wrong global shell geometry: header, nav, masthead, footer, page margins;
- wrong primary component geometry: hero, cards, register grids, side rails,
  modals, tabs, filters, forms, or CTAs;
- wrong number/order of visible reference items, unless product data makes that
  impossible and the alternative is documented;
- missing reachable Claude route, tab, modal, form, empty state, or responsive
  state;
- product behavior kept in a way that also changes Claude's visual geometry
  without being documented as a visual exception;
- screenshots or metrics captured from the wrong route, loading state, login
  state, stale build, or selector miss.

Before release, produce a compact measurement table with one row per high-risk
component and per required viewport:

```text
component | viewport | reference x/y/w/h/style/count | implementation x/y/w/h/style/count | delta | status
```

Use browser-computed values where possible. A broad screenshot comparison is not
enough. If exact parity is intentionally impossible, the row must say whether
the divergence is behavioral only or visual+behavioral, and why the visual delta
is acceptable.

## Establish The Contract

Apply this source-of-truth order:

1. The user's newest explicit requirement.
2. The supplied offline Claude HTML, CSS, JavaScript, assets, and rendered states.
3. Existing product behavior, data contracts, tests, accessibility, and i18n.
4. Older handoff notes and screenshots.

Preserve newer product behavior when it intentionally differs from Claude. Match
Claude exactly everywhere else, and report intentional divergences.

Split every intended divergence into two labels:

- `behavior exception`: the product keeps real data, APIs, auth, routing, media,
  persistence, or permissions while preserving Claude's visible geometry.
- `visual exception`: the product intentionally changes Claude's layout,
  spacing, copy, item count, assets, colors, or component state.

Behavior exceptions are allowed when needed. Visual exceptions require explicit
documentation and should be treated as failed Claude-to-a-tee parity unless the
user accepts them or the reference cannot support a real product path.

Do not silently reinterpret "to a tee" as general polish. Treat spacing,
typography, geometry, states, animation, assets, and responsive overrides as
acceptance criteria.

Do not treat a shell-level restyle as a Claude-to-a-tee implementation. When the
reference changes navigation, tabs, buttons, audio controls, cards, modals,
completion states, or other reusable primitives, audit and update every product
surface that uses those primitives. A matching overview page with old nested
interactions is incomplete.

Also do not silently reinterpret "to a tee" as "copy every front-end surface even
when it cannot work." Before editing, separate the contract into:

- the visual contract: what the reference literally renders;
- the design principles: hierarchy, density, rhythm, palette role, interaction
  model, and the reason those choices work;
- the product-functional contract: what the target app can actually support with
  its current auth, APIs, data model, permissions, assets, and user workflows.

If the Claude reference includes mock-only controls, demo data, fake navigation,
or actions that the target product cannot perform, do not ship them as inert UI.
Either make the behavior real end to end, adapt the component so it expresses
the same design principles with real product behavior, or omit it and document
the intentional divergence.

## Reference State Inventory

Before editing, determine whether the Claude HTML is a single component, a
single page, or a multi-screen app. Do not assume from the filename, screenshot,
or first visible layout.

For bundled Claude HTML, inspect both the rendered UI and the embedded
JavaScript/state model. Search for signals such as `screen`, `tab`, `view`,
`step`, `modal`, `dialog`, `route`, `setScreen`, `setTab`, `onClick`, form
handlers, localStorage keys, and generated view-model sections.

Create a coverage ledger before implementation with one row per reachable
surface:

- reference surface or state name;
- how to open it in the reference;
- visible controls/actions;
- data shown and whether it is mock, static, or product-backed;
- target product mapping;
- implementation decision: implement, adapt, omit, or defer;
- reason for any omission or adaptation;
- verification required.

Do not start implementation until this ledger covers the default rendered state,
all navigation targets, tabs, forms, dialogs, onboarding/step flows, empty/error
states, and responsive-only states that appear in the reference.

Do not let the ledger become passive documentation. Keep it current as a release
gate: every row must end in one of `matched`, `behavior exception`, `visual
exception`, `deferred with user-approved reason`, or `not done`. A `not done`
row blocks claims of completion and blocks deploy.

## Interaction Depth Requirement

Do not treat a visual match of the first screen as sufficient. For every
reachable control in the reference and mapped product surface, click or operate
it until it reaches its terminal or representative states. This includes:

- every tab, route, drawer, dropdown, segmented control, filter, jump list, and
  disabled or locked navigation item;
- every reveal/hide, play/stop/replay audio, mark complete, reset, retry,
  practice-again, got-it, answer, review, shuffle, next/previous, and submit
  action;
- every modal open, cancel, close, confirm, keyboard escape, and outside-click
  behavior;
- every success, failure, completed, empty, locked, disabled, selected,
  persisted-after-reload, and reset-after-completion state;
- every keyboard/touch path that the product claims to support.

When a control affects persisted product state, verify both the immediate UI
state and the stored/reloaded state. When the reference has separate visual
completion and product-earned completion semantics, test both paths rather than
collapsing them into one.

For onboarding tours, coach marks, or spotlight overlays, verify the full step
sequence rather than only the first overlay. Each step must measure the intended
live target after any route/tab/screen switch, keep the target visually
spotlit, avoid fighting manual scroll, support skip/back/next/done and keyboard
escape, and remain usable at every required mobile, tablet, and desktop
breakpoint. Also verify the rest of the product after the tour is dismissed:
the overlay/backdrop must no longer intercept clicks, search results and
navigation targets must be clickable, and first-run onboarding state must not be
mistaken for a broken page during release smoke tests.

For tabbed learning products, verify navigation from every entry point, not just
the top tab strip. This includes overview path rows, next/previous footers,
dropdown/jump menus, locked tabs, deep links, browser back/forward, and reload.
After each navigation, confirm the URL, active tab, scroll position, completion
mark, and persisted progress agree with the product rules.

For search or deep-linkable result cards, verify the full click-through contract:
the visible result metadata must name the real destination section, the click
must route to that section rather than a generic fallback, the URL must include
the target item state when supported, and the target word/phrase/sentence must
be visible or highlighted after navigation.

For embedded scroll regions such as card indexes, sidebars, carousels, and
jump-around lists, test the scroll container itself. Confirm the first and last
items are reachable and visible inside the container, and that automatic
active-item scrolling does not fight the learner's manual scroll.

If automation output shows the wrong page, an empty selector set, missing target
selectors, a login screen, or a route that silently failed to load, discard that
evidence and rerun the audit after fixing the setup. Never count screenshots or
metrics from an unauthenticated shell, placeholder route, or selector miss as
Claude-to-a-tee verification.

## Inspect The Reference

1. Locate every supplied offline HTML, supporting file, asset, and handoff note.
2. Use `browser:control-in-app-browser` when available to render and inspect the
   offline Claude HTML. Exercise all relevant controls and responsive states.
3. Read the underlying HTML, CSS, and JavaScript. Record component structure,
   selectors, computed dimensions, breakpoints, assets, transitions, and states.
4. Capture baseline screenshots at the relevant reference viewports.
5. Inventory the target application's current interactions and selectors before
   editing so visual work does not break behavior.

Do not infer exact values from a screenshot when the offline source exposes them.
Do not copy isolated Claude CSS onto incompatible markup and call it complete.

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

## Implement At Component Level

Map each Claude component to the target DOM/component tree. Rework the affected
surface when its existing structure cannot reproduce the reference cleanly.

Match all relevant details:

- layout, wrapping, alignment, dimensions, spacing, and responsive constraints;
- fonts, sizes, weights, line heights, letter spacing, and text wrapping;
- colors, borders, radii, shadows, backgrounds, icons, images, and crops;
- inputs, placeholders, focus rings, selected, disabled, loading, empty, and
  error states;
- animation timing, transforms, overlays, modals, scrolling, and sticky regions;
- touch behavior, safe areas, keyboard behavior, hover alternatives, and
  horizontal overflow.

Reuse exact supplied assets where licensing and project constraints permit.
Preserve product logic, event delegation, data persistence, auth, i18n, and
accessibility unless the user explicitly changes them. Inspect selector and test
dependencies before renaming classes, IDs, data attributes, or DOM hierarchy.

When preserving product behavior, preserve Claude geometry first. For example,
keeping real video/media/search/map data is usually a behavior exception; it
does not automatically justify changing the media frame, card count, nav
spacing, footer structure, or section rhythm. If real product data forces a
visual change, document that as a visual exception and keep the closest possible
Claude geometry.

Project-specific exception: for the Shane and His Thai app, preserve the
project font system even when a Claude standalone uses a different typeface.
Use Google Sans across the live app unless the user explicitly asks to change
the app-wide typography. Treat this as an intentional Claude-to-a-tee divergence
for this project only.

Do not ship a silent subset. If the reference is a multi-screen app,
implementing only the most obvious page, hero, card group, or currently
requested route is incomplete unless the user explicitly approves that reduced
scope. If product constraints make a surface inappropriate, adapt it into a real
product behavior or list it as an intentional omission before continuing.

Think one step past the mock. For every visible action, answer what should
happen, where the data comes from, who is allowed to do it, what success and
failure look like, and how the state is verified after reload or on another
device when relevant. A beautiful control with no real product path is not done.

When a Claude reference shows grouping, filters, chips, tabs, dropdowns, or
jump controls, do not infer those controls from raw internal metadata such as
tags, bucket IDs, group IDs, quiz buckets, source-brief categories, or
implementation labels. First decide which groups are learner-facing product
concepts and create an explicit UI contract for them. Internal taxonomy may
remain useful for data generation, quiz balancing, analytics, or maintenance,
but it must not leak into the visible interface merely because it exists in the
data. If the reference uses a dropdown, sidebar, or other navigation primitive,
match that primitive unless a newer product requirement says otherwise. If a
unit has no meaningful learner-facing grouping, omit the group UI entirely while
preserving direct card jump/navigation where appropriate.

Do not replace a Claude reference icon, image, control, or component with a
custom approximation merely because the target app has a nearby existing
pattern. Use the reference primitive first (including glyph icons, inline SVG,
asset paths, DOM structure, and component states) unless it conflicts with a
current product requirement or cannot support the target app's real use cases.
When such a conflict exists, document the intentional divergence and preserve
the Claude geometry as closely as the real behavior permits.

Preserve product-owned required assets even when the current Claude reference
uses placeholders or omits them. For example, if the product has real badge PNG
assets, keep and integrate those badge assets instead of downgrading to Claude
placeholder medallions, unless the user explicitly asks to remove or replace
them.

Keep edits scoped to the requested surfaces, but do not retain a structurally
wrong implementation merely to minimize the diff.

When porting Claude CSS into an existing app, preserve the component contract
first and adapt the surrounding app second. Avoid "improving" dimensions,
typography, or layout rhythm from taste. General polish that changes the
contract is a regression unless it is listed as an intentional divergence.

When the exact component cannot or should not be copied, emulate the reference's
principles rather than inventing an unrelated UI. Codex is allowed to design the
missing product-appropriate connective tissue: real empty states, confirmation
flows, role-aware affordances, data-backed summaries, trimmed navigation, and
meaningful disabled/loading states. Keep that design work visibly descended from
the Claude reference's hierarchy, spacing, tone, and interaction language.

## Verify The Implementation

1. Start the application in its normal local runtime.
2. Use `vercel:agent-browser` when available to test the implementation, capture
   comparable screenshots, inspect console errors, and exercise interactions.
3. Compare reference and implementation component by component, not from memory.
4. Verify computed styles for the values in the component contract. For any
   value the user questioned, compare the rendered implementation against the
   exact Claude source/computed value and treat mismatch as not done.
5. Verify all source-defined breakpoints. For a mobile web task, also use the
   default matrix in the verification checklist unless the project defines a
   stricter one.
6. Test content extremes, long labels, loading, empty, disabled, focus, modal,
   keyboard, and touch states that can alter geometry.
7. Run focused tests after edits, then the repository's required full test suite
   when risk or release policy calls for it.
8. Reinspect every detail the user named, even if broader screenshots look right.
9. Fill the measured parity audit table and mark every row `matched`,
   `behavior exception`, `visual exception`, or `not done`.

For responsive Claude references, verify every source-defined breakpoint and
then the default mobile/tablet/desktop matrix from the checklist unless the user
explicitly narrows the scope. At each size, test the first viewport and at least
one scrolled position for long screens. Check that intentionally scrollable
regions, such as tab strips or horizontal carousels, do not create page-level
horizontal overflow. If full-page screenshots of long mobile pages are slow or
unstable, capture viewport screenshots for key states and collect computed
layout metrics across all sizes; do not skip the size coverage.

Responsive verification must include interaction states at those sizes, not just
static screenshots. At minimum, open menus/dropdowns, switch tabs, press audio
buttons, complete/reset one activity where relevant, and inspect a scrolled
mid-page and bottom-page state on long screens.

When authentication, emulators, seeded data, feature flags, or remote state are
needed to see the real product screen, set them up before visual verification.
If the app lands on login, loading, or account-error screens, fix the test setup
first and rerun. Verification starts only after the actual mapped product
surface is visible.

Use a WebKit or real Safari verification path when Safari-specific behavior is
part of the request and such a path is available. Never label Chromium-only
testing as Safari verification. State any browser coverage limitation plainly.

If a named browser skill is unavailable, use the closest browser automation and
inspection capability in the environment, preserve the same evidence standard,
and report the substitution.

## Enforce The Release Gate

Do not claim completion, commit, push, or deploy a Claude-to-a-tee change until:

- relevant reference and implementation states were rendered and compared;
- the reference state/surface coverage ledger is complete, and every reference
  state is either implemented, product-adapted, explicitly omitted, or deferred
  with the reason documented;
- the default rendered reference screen was compared against the target default
  screen, not just an internal route that happened to look similar;
- the affected component contracts were extracted from Claude and checked
  against implementation computed styles;
- desktop, tablet, and required mobile viewports passed without incoherent
  overlap, clipping, or page-level horizontal overflow;
- required interactions and product behavior still work;
- every visible action is either functional, intentionally disabled with a real
  reason, or removed as a documented mock-only divergence;
- browser console and test results were checked;
- intentional divergences and unverified coverage are disclosed.
- the measured parity audit has no `critical` or `not done` rows;
- product exceptions are separated into behavior exceptions and visual
  exceptions;
- any visual exceptions are explicitly reported to and accepted by the user
  before release.

Commit, push, or deploy only when the user requests it or repository instructions
already authorize it.

If the user asks to commit, push, or deploy before the hard gate passes, stop and
report the blocking mismatches instead of shipping. The only exception is when
the user explicitly says to ship despite the listed mismatches.

After deploy, rerun a small production parity smoke against the deployed URL:
default route/page title, header/nav geometry, primary hero/card/grid geometry,
first primary interaction, console errors, and page-level overflow at desktop
and one mobile viewport. A production smoke that only checks HTTP 200 and basic
functionality is not enough for Claude-to-a-tee work.

Report the reference files, routes/components, measured parity status, viewport
matrix, tests, browser coverage, deployed URL if any, and every intentional or
remaining divergence in the closeout.
