---
name: consistency-audit
description: Audit website or app consistency across UI, UX, frontend implementation, and shared components while preserving existing behavior and product surface area. Use when checking whether layouts, components, typography, spacing, colors, icons, copy tone, interaction patterns, responsive behavior, states, forms, data-dense screens, intentional/coexisting variants, deliberate component sizing/customization, or supposedly shared primitives are consistent with project requirements, design principles, inferred product patterns, pattern weight, and historical stability; also use to prevent consistency fixes from inventing new UI/features/content, bias uncertain differences toward provisional product decisions, exercise conservative best judgment when context is insufficient, and find duplicate components/CSS that should be consolidated without breaking layout, size, or behavior.
---

# Consistency Audit

Use this skill to answer: "Does the product feel and behave like one coherent
system?" Audit consistency without redesigning, expanding the product surface,
or flattening valid contextual variants.

Use `$usage-budget-gate` before whole-site audits, `$design-direction` for
visual principles, `$design-system-guardian` for tokens/primitives,
`$product-ux-contracts` for behavior that must not be flattened,
`$ui-state-matrix` for state coverage, `$interaction-flow-qa` for journeys,
`$accessible-interaction` for keyboard/focus, `$data-dense-ux` for tables/lists,
`$form-flow-ux` for forms, `$snapshot` for evidence, and `$release-gate` before
shipping fixes.

## Source Of Truth

Rank consistency sources:

1. Newest user requirement.
2. Project design principles, brand/design docs, Figma/Claude handoff,
   styleguide, component docs, and acceptance criteria.
3. Existing shared components, tokens, utilities, tests, and dominant production
   patterns.
4. Inferred patterns from repeated real screens when docs are missing.

Do not invent a new system during an audit. If requirements conflict with the
current product, report the conflict and the recommended owner decision.

## Guardrails

Treat "nothing breaks" as a release criterion. A consistency fix must not remove
routes, flatten proven journeys, replace internal scroll containers, hide
existing content, change permissions, alter data contracts, break forms, reduce
accessibility, or change layout dimensions unless the user explicitly asks for
that change.

Consistency is not universal standardization. Do not change component size,
shape, density, spacing, layout footprint, or custom treatment when it appears
intentional, context-specific, or not part of a reusable pattern. Standardize
only when comparable components share the same role, context, constraints, and
contract, or when the user explicitly asks for standardization.

Do not add new product surface area during a consistency audit. Avoid adding new
sections, pages, navigation items, buttons, controls, animations, content,
imagery, data fields, copy blocks, onboarding, filters, or abstractions just
because they seem useful or would make the design feel more complete.

Add only when the addition fills a missing piece of an already-established
pattern. Before adding, prove all of these:

1. Comparable screens/components already have the piece, or an explicit
   requirement says it should exist.
2. The absence is an outlier, regression, incomplete state, accessibility gap,
   missing shared variant, missing token, missing copy/state, or missing test.
3. The addition does not introduce a new journey, permission, data entity,
   business rule, layout model, or content strategy.
4. The addition can be verified without breaking dimensions, scroll behavior,
   routing, responsive behavior, or component contracts.

When uncertain, report the idea as a recommendation or design decision, not as
part of the consistency fix. Prefer aligning outliers back to a dominant proven
pattern over expanding the whole product around a new outlier.

## Insufficient Context

If no rule clearly applies and the available context is too thin to prove a
dominant pattern, exercise best judgment instead of stalling. Use the most
conservative reversible choice that preserves existing behavior, product surface
area, layout dimensions, and user journeys.

When using judgment under uncertainty:

1. State the assumption and why the available evidence is insufficient.
2. Prefer preserving current working behavior over redesigning.
3. Prefer the smallest consistency adjustment over broad normalization.
4. Prefer leaving a suspected intentional variant alone over flattening it.
5. Mark the decision as provisional and list what evidence would change it.

When unsure whether a difference is an inconsistency or a product decision, bias
toward treating it as a provisional product decision. This does not mean doing
nothing. Preserve the visible behavior/geometry first, then take only safe
consistency actions around it: document the rationale, fix clearly broken states,
restore missing peer behavior when proven, remove duplicate implementation by
introducing a non-breaking variant, add tests/snapshots, or ask for an owner
decision. Do not resize, restyle, remove, or flatten the suspected product
decision until evidence shows it is accidental or the user explicitly approves.

Escalate only when the decision could break a journey, remove product surface
area, change data/permission behavior, alter shared primitives broadly, or add
new UI without missing-piece proof.

## Pattern Decisions

Compare like with like before declaring a pattern dominant. Count only screens,
containers, or components with the same product role, content shape, density,
auth/permission context, viewport family, and layout constraints. Do not mix
marketing pages, admin tools, mobile-only layouts, dense tables, and simple
content pages unless the requirement says they share one pattern.

Weight evidence in this order:

1. Explicit requirements, acceptance criteria, or confirmed design/product
   decisions override raw counts.
2. Shared source of truth such as reusable components, tokens, utilities, tests,
   docs, or design-system examples outweigh local one-offs unless stale.
3. Frequency among comparable uses matters. If five comparable pages use one
   layout and one comparable page uses another, treat the five-page pattern as
   dominant unless there is evidence the single page is intentional.
4. Historical stability matters. If an older pattern has stayed stable across
   releases, work logs, screenshots, commits, docs, or production usage, and a
   newer batch suddenly changes it without explicit instruction, treat the new
   pattern as suspect even when several new pages match each other.
5. Recency matters only when intent is visible. A recent pattern can supersede an
   older majority when tied to a stated redesign, migration, test update, or
   accepted reference.
6. Proven product UX weighs more than aesthetic reference when behavior,
   navigation, internal scroll, persistence, accessibility, or data density
   conflicts with a static design handoff.

For ties such as five pages versus five pages, do not pick by count alone. Check
shared implementation, oldest stable production behavior, newest explicit owner
decision, rollout scope, user journey risk, and blast radius. If still
ambiguous, report both patterns, why each may be valid, what evidence would
decide it, and the smallest reversible next step.

## Coexisting Variants

Not every mismatch is drift. Some variants should coexist when they express
different context, density, role, input method, priority, or component contract.
For example, an icon-only circular audio button in a compact media control and a
rectangular labeled audio button in a content list may both be correct if their
roles and constraints differ.

Preserve deliberately customized sizes and treatments. A larger card, compact
toolbar button, circular media control, wider form field, denser table action, or
custom layout footprint may be a valid product decision even when it differs
from nearby components. Do not resize or restyle it merely to match a generic
primitive unless the customization is proven accidental or incompatible with the
established pattern for that exact context.

Classify a difference as a valid coexisting variant when:

1. The variant has a named or inferable context such as compact control, primary
   CTA, dense table action, mobile affordance, admin destructive action, media
   playback, or accessibility fallback.
2. It is applied consistently within that context.
3. It preserves the same user expectation where meaning is shared, or clearly
   signals a different role where meaning differs.
4. It does not duplicate implementation unnecessarily when a shared primitive
   with variants would preserve layout and behavior.

Classify a difference as drift when comparable contexts differ without a clear
reason, one-off CSS overrides bypass shared primitives, behavior differs behind
matching visuals, or a variant appears only because a newer implementation
overwrote a proven product pattern.

## Audit Dimensions

- **Layout:** page shells, max widths, grid/list rhythm, panels, sticky regions,
  empty space, section order, responsive breakpoints.
- **Components:** buttons, links, cards, tables, forms, tabs, filters, chips,
  modals, drawers, nav, toasts, media frames.
- **Typography:** font family, scale, weights, line height, casing, truncation,
  long text, localization.
- **Visual tokens:** colors, surface roles, borders, radii, shadows, icons,
  density, motion, image crops.
- **Interaction:** hover/focus/pressed/selected/disabled/loading, keyboard,
  touch, modal close, route/back/reload, persistence.
- **UX contracts:** search, filters, pagination, internal scroll, deep links,
  permissions, destructive safety, media fallbacks.
- **Content:** labels, helper text, empty/error copy, button verbs, tone,
  bilingual/locale consistency.
- **Implementation:** duplicated components, duplicated CSS, one-off variants,
  shared-looking UI implemented separately, dead primitives, brittle selectors.

## Shared Component Consolidation

Do not consolidate just because two things look similar. First define the visual
and behavioral contract:

```text
Candidate:
Existing implementations:
Same role? yes/no
Same visual contract? geometry / spacing / typography / state / icon
Same behavior contract? click / route / form / permission / loading
Intentional customization? size / density / shape / footprint / context
Different context constraints:
Decision: consolidate / shared primitive + variants / keep separate / needs design decision
Safety checks:
```

Consolidate when components share the same role, visual contract, behavior
contract, and expected states. Use a shared primitive with explicit variants
when the role is shared but density, size, layout, or behavior differs by
context. Keep separate when visual similarity hides different product meaning or
risk.

Before consolidating, capture geometry and constraints: width, height, min/max,
padding, gap, font size/line height, icon size, hit target, state styles, and
responsive behavior. After consolidation, verify every usage still fits its
parent layout. Do not "fix" consistency by breaking dimensions, wrapping,
scroll, table density, or mobile layout.

## Workflow

1. Choose audit depth with `$usage-budget-gate`: route/sample/whole-site.
2. Read explicit requirements and design docs if present.
3. Inventory shared components, tokens, CSS modules, routes, layouts, and common
   UI primitives with `rg --files` and targeted search.
4. Render representative screens and capture `$snapshot` evidence for high-risk
   inconsistencies.
5. Build a weighted pattern ledger: comparable population, explicit requirement,
   current dominant pattern, coexisting variants, count, history signal,
   recency/intent signal, outliers, severity, recommended fix, missing-piece
   proof, intentional customization rationale, best-judgment assumptions when
   needed, and safety checks.
6. Trace implementation inconsistencies to duplicate components, local CSS
   overrides, missing variants, stale copy, intentional exceptions, or changed
   product context.
7. Classify every proposed change as align existing, restore removed behavior,
   fill missing piece, preserve coexisting variant, consolidate duplicate, or
   preserve provisional product decision with safe adjacent fixes, or new
   addition requiring approval.
8. Recommend fixes in phases: quick token/variant cleanup, component
   consolidation, behavior/state fixes, docs/test updates.

## Severity

- **P0:** inconsistency breaks a journey, accessibility, permission/safety, or
  data integrity.
- **P1:** shared-looking UI has divergent behavior or duplicated implementation
  that will cause regressions.
- **P2:** visual/system drift that weakens product coherence but does not block a
  task.
- **P3:** polish, naming, docs, or low-risk cleanup.

## Fix Safety

- Preserve product UX contracts; use `$product-ux-contracts` when uncertain.
- Preserve existing product surface area; do not add new UI, content, or
  behavior without explicit requirement or missing-piece proof.
- Preserve internal scroll containers, route structure, navigation, permissions,
  form behavior, data contracts, layout dimensions, and responsive constraints.
- Preserve deliberately customized component sizes, shapes, density, and layout
  footprints unless they are proven accidental or explicitly in scope to change.
- Prefer existing tokens and primitives before adding new ones.
- Add variants instead of one-off CSS when a pattern recurs.
- Snapshot before/after for user-visible fixes.
- Add or update tests when consolidation could silently break behavior.

## Closeout

Report requirements inspected, inferred patterns, outliers found, coexisting
variants and deliberate customizations preserved, duplicate components/CSS,
consolidation candidates, items intentionally left separate, pattern
weights/tie-breakers, missing-piece proof for any addition, changes deferred as
new product/design decisions, provisional product decisions preserved with safe
adjacent fixes, best-judgment assumptions made under insufficient context,
severity, recommended phases, screenshots/tests, and risks before changing
shared primitives.
