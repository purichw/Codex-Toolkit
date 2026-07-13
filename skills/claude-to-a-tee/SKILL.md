---
name: claude-to-a-tee
description: Reproduce an offline Claude Design HTML reference exactly at component level while preserving required product behavior. Use when the user says "Claude to a tee", "to a tee", "exactly like the Claude HTML", "pixel-perfect", "holy grail", or asks Codex to implement, audit, compare, or repair a web UI from Claude-generated offline HTML, screenshots, handoff files, or exported assets, especially when responsive mobile, tablet, desktop, animation, interaction, or pre-deploy visual verification is required.
---

# Claude To A Tee

Treat the supplied offline Claude HTML as executable design documentation. Match its rendered components and user-visible states, not merely its palette or broad layout.
Treat the target product as real software, not a display case for a pretty mock. The reference is a UI presentation source of truth; the target product remains the source of truth for data, routing, auth, persistence, performance, accessibility, security, tests, operations, and frontend architecture.

Expand "to a tee" internally to:

```text
CLAUDE TO A TEE AUDIT. Implement from the offline Claude HTML exactly at component level, mobile included, and verify before commit/deploy.
```

Read [references/verification-checklist.md](references/verification-checklist.md)
before inspecting or editing the target application.

## Non-Negotiable Execution Gate

Use this skill as a release blocker, not as inspiration. Do not claim success,
commit, push, or deploy until this gate is satisfied, even when the user says
"continue until done".

Before editing, render and inspect both the Claude reference and the target app in the relevant state; never implement from memory, screenshots alone, or broad "looks close" judgment.

Before finalizing, produce this compact self-check in working notes or closeout:

```text
REFERENCE RENDERED: yes/no + file/hash/state/viewport
APP RENDERED: yes/no + URL/commit/state/viewport
COVERAGE LEDGER: matched / behavior exception / visual exception / not done
MEASURED PARITY TABLE: component | viewport | reference x/y/w/h/style/count | implementation x/y/w/h/style/count | delta | status
BEHAVIOR/ENGINEERING EXCEPTIONS:
VISUAL EXCEPTIONS:
BLOCKERS BEFORE COMMIT:
PRODUCTION ARTIFACT SMOKE:
```

A broad screenshot comparison is not enough. Use browser-computed geometry for
high-risk components: global shell, header/topbar, nav/sidebar, page title,
primary cards, filters/tabs, table/list rows, dialogs/drawers, history/footer,
and page rhythm. Wrong default route, stale artifact, selector miss, loading or
login state, shell geometry, primary component geometry, item order/count, or
undocumented product-driven visual change is a critical mismatch by default.

These fail the skill:

- "Claude-inspired polish" instead of component-level measured parity;
- editing first and measuring only after the user complains;
- using product CSS clamps, spacing, or old primitives when they alter Claude
  geometry without declaring a visual exception;
- shipping mock-only controls as inert UI;
- downgrading a handoff-declared feature to read-only, hidden, disabled, or
  "future API" state before first mapping and attempting the real product write
  path;
- calling real product data/auth/API differences "behavior exceptions" while
  also allowing avoidable visual drift;
- production smoke that checks only HTTP 200 or login, not the deployed
  artifact that contains the changed UI.

Behavior exceptions are allowed when they preserve Claude geometry; visual exceptions must be explicit, and critical ones require acceptance before commit/push/deploy.

## Establish The Contract

Apply this source-of-truth order:

1. The user's newest explicit requirement.
2. The supplied offline Claude rendered UI, CSS, assets, and visible states.
3. Existing product behavior, data contracts, tests, accessibility, i18n, security, performance, and production operations.
4. Older handoff notes and screenshots.

If the handoff changelog marks a version as current, or says a visible edit
"writes real state", treat that as an acceptance criterion. Do not reinterpret
those controls as mock-only because the target app lacks an existing endpoint.
First map the needed product-owned write path (API, Firestore document, CMS,
storage, or state reducer), implement it when it is within the requested scope,
and only then classify anything truly impossible as a blocker or user-approved
defer. A missing backend hook is implementation work, not a visual exception.

Preserve newer product behavior when it intentionally differs from Claude. Match
Claude exactly everywhere else, and report intentional divergences.

Split every intended divergence into two labels:

- `behavior exception`: the product keeps real data, APIs, auth, routing, media, persistence, permissions, performance architecture, accessibility, security, tests/selectors, analytics hooks, or operations while preserving Claude's visible intent and geometry.
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

Also do not silently reinterpret "to a tee" as "copy Claude's front-end
architecture." Before editing, separate the contract into:

- the visual contract: what the reference literally renders;
- the design principles: hierarchy, density, rhythm, palette role, interaction
  model, and the reason those choices work;
- the engineering contract: target-owned data, auth, routing, persistence, lazy loading, load-more/pagination, virtualization, scrub/sticky mechanics, responsive input behavior, accessibility, security/privacy, tests/selectors, analytics hooks, CMS/content pipelines, and operations.

Treat Claude JavaScript and demo interactions as evidence of intended visible states, not as architecture to clone. When mechanics conflict, keep the product-owned mechanism and reproduce Claude's visible intent: geometry, hierarchy, density, tone, perceived motion, and terminal states.

If the Claude reference includes mock-only controls, demo data, fake navigation,
or actions that the target product cannot perform, do not ship them as inert UI.
Either make the behavior real end to end, adapt the component so it expresses
the same design principles with real product behavior, or omit it and document
the intentional divergence.

Run the same stub scrub against the target product's inherited UI, not only
against controls copied from Claude. If an existing product button, input,
select, toggle, search field, nav item, footer action, or dashboard shortcut is
visible inside the mapped Claude surface, it must also be functional, honestly
passive/status-only, deliberately disabled with a real current-state reason, or
removed. A control that "has always been there" but now appears in the
Claude-to-a-tee surface is part of the release gate.

When the reference and handoff disagree about whether a control is mock-only,
prefer the handoff's explicit functional language. For example, controls named
Grant/Revoke, Freeze/Restore, Complete/Reset, Lock/Unlock, Mark passed, or
Re-evaluate are not safe to disable merely because the preexisting product has
no matching API. They must become real, be replaced by an equivalent real
product action, or block release until the user accepts a defer.

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

## Interaction Depth Requirement

Use the interaction-depth checklist in
[references/verification-checklist.md](references/verification-checklist.md) as
a release-blocking requirement. A first-screen visual match is insufficient:
every reachable reference control and mapped product control must be exercised
to terminal or representative states, including persisted, responsive,
scroll-container, search/deep-link, onboarding, and automation-setup failure
cases.

## Inspect The Reference

1. Locate every supplied offline HTML, supporting file, asset, and handoff note.
2. Use `browser:control-in-app-browser` when available to render and inspect the
   offline Claude HTML. Exercise all relevant controls and responsive states.
3. Read the underlying HTML, CSS, and JavaScript. Record component structure,
   selectors, computed dimensions, breakpoints, assets, transitions, and states.
4. Capture baseline screenshots at the relevant reference viewports. Treat
   user-supplied screenshots as route/state evidence, not as a replacement for
   rendered HTML inspection.
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

## Implement At Component Level

Map each Claude component to the target DOM/component tree. Rework the affected
surface when its existing structure cannot reproduce the reference cleanly.

Match all relevant details:

- layout, wrapping, alignment, dimensions, spacing, and responsive constraints;
- fonts, sizes, weights, line heights, letter spacing, and text wrapping;
- colors, borders, radii, shadows, backgrounds, icons, images, and crops;
- inputs, placeholders, focus rings, selected, disabled, loading, empty, and
  error states;
- user-visible animation states, transforms, overlays, modals, and scroll/sticky outcomes;
- touch behavior, safe areas, keyboard behavior, hover alternatives, and
  horizontal overflow.

Reuse exact supplied assets where licensing and project constraints permit.
Preserve product logic, routing, data fetching, event delegation, persistence, auth, permissions, i18n, accessibility, performance, security/privacy, analytics/test hooks, and operations unless the user explicitly changes them.
Inspect selector and test dependencies before renaming classes, IDs, data attributes, or DOM hierarchy.

Audit data-backed assets as well as repository files. When a remote CMS image,
font, video, or embed is confirmed unavailable, prefer repairing or removing it
at the source. If production permissions block that repair, quarantine only the
confirmed asset in the public runtime, preserve admin visibility for replacement,
add regression coverage, and disclose that the source record still exists. Do
not broadly suppress asset failures or silently substitute unrelated media.

When preserving product behavior, preserve Claude presentation first. Keeping real video/media/search/map data, route structure, lazy loading, load-more, virtualization, or scrub/sticky mechanics is usually a behavior exception; it does not justify changing the media frame, card count, nav spacing, footer structure, or section rhythm.
If a product contract forces a visual change, document it as a visual exception and keep the closest possible Claude geometry.

Do not confuse "respect the product engineering contract" with "do less product
engineering." If matching Claude requires a new trusted endpoint, state adapter,
audit-log action, persistence field, or regression test, build that product
plumbing unless the user narrowed scope. Hiding or disabling a feature because
the plumbing is absent is a scope decision that requires explicit user
acceptance before release.

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

### Evidence Provenance

Use the artifact provenance, default responsive matrix, and browser evidence
sections in [references/verification-checklist.md](references/verification-checklist.md)
as release-blocking checks. Reject captures from the wrong route, login/protect
screens, stale artifacts, pre-hydration shells, unsupported browser claims, or
selector misses; fix setup and recapture before claiming parity.

## Enforce The Release Gate

Do not claim completion, commit, push, or deploy a Claude-to-a-tee change until:

- relevant reference and implementation states were rendered and compared;
- the reference state/surface coverage ledger is complete, and every reference
  state is either implemented, product-adapted, explicitly omitted, or deferred
  with the reason documented;
- the route component manifest is complete for every affected route, and the
  missing-component report has no unclassified Claude components;
- the default rendered reference screen was compared against the target default
  screen, not just an internal route that happened to look similar;
- the affected component contracts were extracted from Claude and checked
  against implementation computed styles;
- page rhythm and scroll/sticky outcomes were measured beyond the first viewport where they affect visible UI, while preserving product-owned scroll, scrub, lazy loading, load-more, pagination, and virtualization mechanics;
- desktop, tablet, and required mobile viewports passed without incoherent
  overlap, clipping, or page-level horizontal overflow;
- required interactions and the product engineering contract still work;
- every visible action is either functional, intentionally disabled with a real
  reason, or removed as a documented mock-only divergence;
- browser console, page errors, failed requests, and 4xx/5xx asset responses
  were checked after live data hydration;
- the tested generated artifact and deployed build identifiers match the target
  commit, and requested/final URLs prove the intended environment was measured;
- intentional divergences and unverified coverage are disclosed;
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

For changed authenticated admin surfaces, production smoke must reach the
changed authenticated surface or an equivalent preview/test environment with the
same deployed artifact and seeded state. A smoke that stops at the login/admin
gate does not verify the changed UI and cannot close the release gate.

Report the reference files, routes/components, measured parity status, viewport
matrix, tests, browser coverage, deployed URL if any, and every intentional or
remaining divergence in the closeout.
