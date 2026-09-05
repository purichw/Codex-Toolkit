---
name: design-system-guardian
description: Preserve, audit, or extend a product design system while changing UI. Use when the user says the UI looks like different systems, asks to make components consistent, or needs to prevent component/token drift, inconsistent buttons/cards/forms/tables, typography/spacing mismatch, duplicated one-off CSS, variant sprawl, icon/radius/shadow inconsistency, cross-page visual regressions, or Claude/Figma/reference integration that could break reusable primitives.
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

Prefer existing primitives when they can express the new design. Extend a
primitive when the new pattern will recur. Use a local one-off only when the
surface is truly unique or temporary. Do not globally change tokens to satisfy
one component without checking adjacent surfaces.

## Drift Checks

- Multiple button styles for the same action hierarchy.
- Cards with nearby but different padding, radii, borders, or shadows.
- Form controls with inconsistent height, focus, disabled, or error states.
- Tables/lists with different row density or action placement.
- New CSS values that duplicate tokens with tiny deltas.
- Claude/Figma values copied onto incompatible markup.
- Dark/light/brand accents used without product role.

## Workflow

1. Locate source components and tokens.
2. Map the requested UI change to existing primitives and variants.
3. Decide reuse, extend, or local exception.
4. Use `$design-system-architect` before broad token, variant, gallery, or drift
   governance changes.
5. Update component state coverage with `$ui-state-matrix` when variants change.
6. Inspect neighboring pages that share the primitive.
7. Capture `$snapshot` evidence for the changed surface before final response;
   include one adjacent surface when drift risk is high.

## Closeout

Report primitives/tokens reused or extended, local exceptions, adjacent surfaces
checked, snapshots/tests, and any design-system debt left behind.
