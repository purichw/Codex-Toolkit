---
name: consistency-audit
description: Audit website or app consistency across UI, UX, frontend implementation, and shared components. Use when checking whether layouts, components, typography, spacing, colors, icons, copy tone, interaction patterns, responsive behavior, states, forms, data-dense screens, or supposedly shared primitives are consistent with project requirements, design principles, inferred product patterns, pattern weight, and historical stability; also use to find duplicate components/CSS that should be consolidated without breaking layout, size, or behavior.
---

# Consistency Audit

Use this skill to answer: "Does the product feel and behave like one coherent
system?" Audit against explicit project requirements first. If none exist,
infer the dominant patterns from the current product and mark them as inferred.

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
2. Project design principles, brand/design docs, Figma/Claude handoff, styleguide,
   component docs, and acceptance criteria.
3. Existing shared components, tokens, utilities, tests, and dominant production
   patterns.
4. Inferred patterns from repeated real screens when docs are missing.

Do not invent a new system during an audit. If requirements conflict with the
current product, report the conflict and the recommended owner decision.

## Pattern Weighting

Compare like with like before declaring a pattern dominant. Count only screens,
containers, or components with the same product role, content shape, density,
auth/permission context, viewport family, and layout constraints. Do not mix
marketing pages, admin tools, mobile-only layouts, dense tables, and simple
content pages unless the requirement says they share one pattern.

Weight evidence in this order:

1. Explicit requirements, acceptance criteria, or a confirmed design/product
   decision override raw counts.
2. Shared source of truth such as reusable components, tokens, utilities, tests,
   docs, or design-system examples outweigh local one-offs unless they are stale.
3. Frequency among comparable uses matters. If five comparable pages use one
   layout and one comparable page uses another, treat the five-page pattern as
   dominant unless there is evidence the single page is an intentional redesign.
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
decision, rollout scope, user journey risk, and blast radius. If the tie is still
ambiguous, report both patterns, why each may be valid, what evidence would
decide it, and the smallest reversible next step. Ask for an owner decision
before changing shared primitives or wiping out a proven product pattern.

Treat intentional variants as variants, not drift. Different density, viewport,
permissions, entity type, task criticality, or data shape may justify different
layouts if the difference is named and consistently applied.

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
Different context constraints:
Decision: consolidate / shared primitive + variants / keep separate / needs design decision
Safety checks:
```

Consolidate when components share the same role, visual contract, behavior
contract, and expected states. Use a shared primitive with explicit variants
when the role is shared but density, size, layout, or behavior differs by
context. Keep separate when visual similarity hides different product meaning or
risk.

Before consolidating, capture the existing geometry and constraints: width,
height, min/max, padding, gap, font size/line height, icon size, hit target,
state styles, and responsive behavior. After consolidation, verify every usage
still fits its parent layout. Do not "fix" consistency by breaking dimensions,
wrapping, scroll, table density, or mobile layout.

## Audit Workflow

1. Choose audit depth with `$usage-budget-gate`: route/sample/whole-site.
2. Read explicit requirements and design docs if present.
3. Inventory shared components, tokens, CSS modules, routes, layouts, and common
   UI primitives with `rg --files` and targeted search.
4. Render representative screens and capture `$snapshot` evidence for high-risk
   inconsistencies.
5. Build a weighted pattern ledger: comparable population, explicit requirement,
   current dominant pattern, count, history signal, recency/intent signal,
   outliers, severity, recommended fix, and safety checks.
6. For implementation inconsistencies, trace whether the outlier is a duplicate
   component, local CSS override, missing variant, stale copy, or intentional
   product-specific exception.
7. Recommend fixes in phases: quick token/variant cleanup, component
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
- Preserve layout dimensions unless the fix explicitly changes layout.
- Prefer existing tokens and primitives before adding new ones.
- Add variants instead of one-off CSS when a pattern recurs.
- Snapshot before/after for user-visible fixes.
- Add or update tests when consolidation could silently break behavior.

## Closeout

Report requirements inspected, inferred patterns, outliers found, duplicate
components/CSS, consolidation candidates, items intentionally left separate,
pattern weights/tie-breakers, severity, recommended phases, screenshots/tests,
and risks before changing shared primitives.
