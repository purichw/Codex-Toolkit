---
name: design-system-guardian
description: Preserve, audit, or extend a product design system and safely reuse or extract shared UI components. Use for repeated UI, duplicate fixes, component consolidation, reuse-versus-local decisions, props/events/state contracts, consumer migration, shared API/default changes, component/token drift, variant sprawl, or reference integration that could break existing primitives.
---

# Design System Guardian

Use this skill when UI work could fragment the product's component language.
The goal is consistency without flattening product-specific UX.

Use `$consistency-audit` for site-wide consistency discovery before fixing a
large set of drift issues. Use `$design-system-architect` when the system needs
token-layer, taxonomy, variant, gallery, drift-metric, or governance work. Use
`$design-direction` for north-star decisions, `$reference-to-a-tee` for exact
reference parity, `$product-ux-contracts` for behavior that must survive,
`$ui-state-matrix` for variants/states, `$snapshot` as mandatory visual proof
before final response, and `$release-gate` before shipping.

## Inventory

Find the existing system before adding styles:

- tokens: color roles, spacing, typography, radii, shadows, z-index, motion;
- primitives: buttons, inputs, tabs, cards, tables, nav, dialogs, drawers;
- variants: size, density, selected, disabled, loading, danger, success;
- layout rules: max widths, grid/list patterns, panel density, sticky regions;
- icon/image rules: library, stroke weight, optical sizing, crop behavior;
- test/story/demo surfaces that prove variants.

## Decision Rule

Prefer existing components when they express the needed semantics and behavior.
Extract or extend shared UI when real consumers share a stable contract and
would benefit from the same fixes. Similar styling or a repeated occurrence
count alone does not justify merging independently evolving workflows.

Choose the narrowest useful reuse: tokens/styles, helper/hook, primitive, or
feature/domain pattern. Local composition can be the correct durable choice,
not merely temporary debt. Do not globally change defaults/tokens to satisfy one
consumer without inspecting the others. Apply the project's architecture and
existing libraries instead of creating a new abstraction style.

For extraction, consolidation, or shared-contract changes, read
[shared-components.md](references/shared-components.md). It covers applicability,
API/state/layout boundaries, incremental consumer migration, and verification.
The design-system reference's recurrence and variant-count rules are heuristics
to review applicability, not automatic mandates to extract or split components.

## Drift Checks

- Multiple button styles for the same action hierarchy.
- Cards with nearby but different padding, radii, borders, or shadows.
- Form controls with inconsistent height, focus, disabled, or error states.
- Tables/lists with different row density or action placement.
- New CSS values that duplicate tokens with tiny deltas.
- Claude/Figma values copied onto incompatible markup.
- Dark/light/brand accents used without product role.

## Workflow

1. Locate existing owner components/tokens and actual consumers within the
   requested surface. Map differences in semantics, states, data, and behavior.
2. Decide reuse, extend, extract a smaller unit, or keep local; explain only
   material tradeoffs. Use the reference workflow for extraction/contract changes.
3. When sharing is warranted, define the smallest shared contract and migrate
   in-scope consumers in bounded steps. Otherwise make the focused local change.
   Keep product behavior and unrelated user changes intact.
4. Use `$design-system-architect` only for wider system architecture; ordinary
   reuse or a local extraction does not require a full system audit.
5. Check affected variants/states and consumers with targeted tests; use
   `$ui-state-matrix` when useful. Update existing component docs/examples when
   their usage contract changed. Identify active copies or explicitly deferred
   migrations rather than claiming consolidation prematurely.
6. Use `$snapshot` automatically before final response for visible changes,
   including representative differing consumers when a shared contract changes.
   Exercise changed interactions as well. Keep capture scope proportional and
   report blocked visual checks; do not treat a build as screenshot evidence.

## Closeout

Report the reuse decision, shared contract and consumers changed, any active
duplicates or scoped deferrals, and tests/snapshots or remaining verification
gaps. For a small reuse, a short closeout is enough.
