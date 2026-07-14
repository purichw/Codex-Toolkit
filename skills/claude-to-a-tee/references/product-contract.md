# Product Contract

Read this before mapping Claude UI into product code or changing target app
behavior. The visual source of truth is Claude; the engineering source of truth
is the product.

## Establish The Contract

Apply this source-of-truth order:

1. The user's newest explicit requirement.
2. The supplied offline Claude rendered UI, CSS, assets, and visible states.
3. Existing product behavior, data contracts, tests, accessibility, i18n,
   security, performance, and production operations.
4. Older handoff notes and screenshots.

If the handoff changelog marks a version as current, or says a visible edit
"writes real state", treat that as an acceptance criterion. Do not reinterpret
those controls as mock-only because the target app lacks an existing endpoint.
First map the needed product-owned write path (API, Firestore document, CMS,
storage, or state reducer), implement it when it is within the requested scope,
and only then classify anything truly impossible as a blocker or user-approved
defer. A missing backend hook is implementation work, not a visual exception.

Preserve newer product behavior when it intentionally differs from Claude and
has evidence of product value. Match Claude exactly everywhere else, and report
intentional divergences.

Split every intended divergence into two labels:

- `behavior exception`: the product keeps real data, APIs, auth, routing,
  media, persistence, permissions, performance architecture, accessibility,
  security, tests/selectors, analytics hooks, or operations while preserving
  Claude's visible intent and geometry.
- `visual exception`: the product intentionally changes Claude's layout,
  spacing, copy, item count, assets, colors, or component state.

Behavior exceptions are allowed when needed. Visual exceptions require explicit
documentation and should be treated as failed Claude-to-a-tee parity unless the
user accepts them or the reference cannot support a real product path.

## Prove Product UX Before Preserving It

Do not preserve current product UX merely because it already exists. Preserve it
over Claude only when evidence shows it is more complete, safer, or more useful.

Valid evidence includes:

- functional completeness: real search/filter/save/auth/data behavior where
  Claude is static, mock-only, or no-op;
- task success: the product completes a user/admin/learner flow Claude does not
  complete;
- state coverage: loading, empty, denied, disabled, validation, failure,
  persisted-after-reload, long-label, localized, mobile keyboard, or offline
  states;
- container behavior: useful sub-containers, internal scroll regions, sticky
  subpanels, virtualized lists, active-item auto-scroll, or scroll restoration
  that Claude omits or flattens;
- operational safety: role checks, confirmations, audit logs, tombstones,
  rollback, destructive-action safeguards, or permission-denied paths;
- accessibility, mobile, performance, or reliability evidence;
- tests, documented product rules, production usage, analytics, support notes,
  or known regression history.

Use this pre-implementation ledger:

```text
Component:
Claude behavior/UI:
Current product behavior/UX:
Evidence current is better:
Decision: Claude adopted / product UX preserved / hybrid / needs user decision
Reason:
Implementation rule:
Verification:
Risk:
```

Default to `hybrid` when current UX is proven better: preserve Claude visual
language, geometry, hierarchy, rhythm, and component feel while keeping the
product's stronger task flow, state model, container behavior, or safety
behavior. Default to `Claude adopted` when the current product advantage is
unproven. Use `needs user decision` when both choices are product-valid but
imply different UX, scope, or release risk.

Do not flatten an existing sub-container, nested scroll region, sticky subpanel,
virtualized list, or scroll-restoration behavior just because a newer Claude
HTML uses a simpler page flow. Restyle it to Claude when possible, but preserve
the product container when it improves task success, information density,
keyboard/touch handling, active-item navigation, or mobile usability. If the
container is removed, document the evidence, risk, and user acceptance.

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
- the engineering contract: target-owned data, auth, routing, persistence, lazy
  loading, load-more/pagination, virtualization, scrub/sticky mechanics,
  responsive input behavior, accessibility, security/privacy, tests/selectors,
  analytics hooks, CMS/content pipelines, and operations.

Treat Claude JavaScript and demo interactions as evidence of intended visible
states, not as architecture to clone. When mechanics conflict, keep the
product-owned mechanism and reproduce Claude's visible intent: geometry,
hierarchy, density, tone, perceived motion, and terminal states.

Claude references are often static: they may omit persistence, live data,
permissions, route transitions, error paths, loading states, or animation. Treat
that absence as missing reference behavior, not as permission to break product
engineering behavior or invent unrelated UX. Preserve the product's real
behavior while making the visible UI/UX as faithful to Claude as the real
behavior permits.

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

## Implement At Component Level

Map each Claude component to the target DOM/component tree. Rework the affected
surface when its existing structure cannot reproduce the reference cleanly.

Match all relevant details:

- layout, wrapping, alignment, dimensions, spacing, and responsive constraints;
- fonts, sizes, weights, line heights, letter spacing, and text wrapping;
- colors, borders, radii, shadows, backgrounds, icons, images, and crops;
- inputs, placeholders, focus rings, selected, disabled, loading, empty, and
  error states;
- user-visible animation states, transforms, overlays, modals, and
  scroll/sticky outcomes;
- touch behavior, safe areas, keyboard behavior, hover alternatives, and
  horizontal overflow.

Reuse exact supplied assets where licensing and project constraints permit.
Preserve product logic, routing, data fetching, event delegation, persistence,
auth, permissions, i18n, accessibility, performance, security/privacy,
analytics/test hooks, and operations unless the user explicitly changes them.
Inspect selector and test dependencies before renaming classes, IDs, data
attributes, or DOM hierarchy.

Audit data-backed assets as well as repository files. When a remote CMS image,
font, video, or embed is confirmed unavailable, prefer repairing or removing it
at the source. If production permissions block that repair, quarantine only the
confirmed asset in the public runtime, preserve admin visibility for
replacement, add regression coverage, and disclose that the source record still
exists. Do not broadly suppress asset failures or silently substitute unrelated
media.

When preserving product behavior, preserve Claude presentation first. Keeping
real video/media/search/map data, route structure, lazy loading, load-more,
virtualization, or scrub/sticky mechanics is usually a behavior exception; it
does not justify changing the media frame, card count, nav spacing, footer
structure, or section rhythm.

If a product contract forces a visual change, document it as a visual exception
and keep the closest possible Claude geometry.

Do not add decorative animation, extra transitions, hover flourish, or invented
microinteractions just because the real product can support them. Add or retain
motion only when Claude shows it, the product already requires it, accessibility
needs it, or the user explicitly asks for it; then verify it does not change
Claude geometry or rhythm.

Do not confuse "respect the product engineering contract" with "do less product
engineering." If matching Claude requires a new trusted endpoint, state
adapter, audit-log action, persistence field, or regression test, build that
product plumbing unless the user narrowed scope. Hiding or disabling a feature
because the plumbing is absent is a scope decision that requires explicit user
acceptance before release.

Project-specific exception: for the Shane and His Thai app, preserve the
project font system even when a Claude standalone uses a different typeface. Use
Google Sans across the live app unless the user explicitly asks to change the
app-wide typography. Treat this as an intentional Claude-to-a-tee divergence for
this project only.

Do not ship a silent subset. If the reference is a multi-screen app,
implementing only the most obvious page, hero, card group, or currently
requested route is incomplete unless the user explicitly approves that reduced
scope. If product constraints make a surface inappropriate, adapt it into a real
product behavior or list it as an intentional omission before continuing.

Think one step past the mock. For every visible action, answer what should
happen, where the data comes from, who is allowed to do it, what success and
failure look like, and how the state is verified after reload or on another
device when relevant. A beautiful control with no real product path is not done.

When a Claude reference shows grouping, filters, chips, tabs, dropdowns, or jump
controls, do not infer those controls from raw internal metadata such as tags,
bucket IDs, group IDs, quiz buckets, source-brief categories, or implementation
labels. First decide which groups are learner-facing product concepts and create
an explicit UI contract for them. Internal taxonomy may remain useful for data
generation, quiz balancing, analytics, or maintenance, but it must not leak into
the visible interface merely because it exists in the data. If the reference
uses a dropdown, sidebar, or other navigation primitive, match that primitive
unless a newer product requirement says otherwise. If a unit has no meaningful
learner-facing grouping, omit the group UI entirely while preserving direct card
jump/navigation where appropriate.

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
