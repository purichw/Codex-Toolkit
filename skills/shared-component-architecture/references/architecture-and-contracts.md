# Architecture and contracts

## Contents

- Start with representative flows
- Put code at the narrowest useful boundary
- Define import direction and public surfaces
- Write the component contract
- Separate state, data, and policy
- Preserve styling and responsive ownership
- Respect runtime and dependency cost
- Apply a small first implementation plan

## Start with representative flows

Inspect the existing project before proposing directories. Read repository instructions, route conventions, current component library, aliases, state/data tools, styling system, and release boundaries. Preserve conventions that already express ownership clearly.

For a new application, inventory a few real screens that exercise different responsibilities: a listing, a detail or edit form, and a modal or empty state. Include long Thai/English content and narrow/wide layouts. Use product flows to discover repeated responsibilities; do not extract components by drawing a box around every visual rectangle.

Classify each candidate as a primitive, neutral composition pattern, domain component, or page composition. Record actual consumers or the known design contract that justifies first-use sharing. Implement one real flow, then check the next consumer before expanding the API. Establish recognizable primitives early when their behavior is already known; defer speculative combinations.

## Put code at the narrowest useful boundary

Use this illustrative map only when the project lacks an adequate structure. Do not create empty folders, force a migration, or prescribe every layer for a small application.

| Example location | Responsibility | Example |
| --- | --- | --- |
| `src/app/` or the framework's route directory | Compose routes, providers, layouts, and feature entry points | Booking page route |
| `src/features/bookings/` | Own booking UI, domain state, business mappings, and use-case adapters | BookingEditor, BookingStatusBadge |
| `src/features/membership/` | Own membership UI and policy | MembershipReview, MembershipStatusBadge |
| `src/shared/ui/` | Provide generic semantic primitives | Button, Field, Badge, tested Dialog wrapper |
| `src/shared/layout/` or `patterns/` | Compose neutral visual/interaction patterns | PageHeader, EmptyState, FormActions |
| `src/shared/styles/` | Own semantic tokens and shared styling conventions | Surface, spacing, focus and status tones |
| `src/shared/lib/` | Hold small genuinely domain-neutral helpers | Class-name composition, generic ID utility |

Keep feature-local components, hooks, styles, and tests close to their owners. A hook or utility does not become application-wide merely because it is reusable. Do not place booking calculations in `shared/lib` to bypass dependency rules.

Use a package boundary only when real consumers need independent distribution or compatibility guarantees. A second product name alone does not require a monorepo or a published UI package. If multiple domains truly share a scheduling engine, identify its stable data model, owner, and contract explicitly; keep cancellation, approval, pricing, and permissions in the appropriate domain policy.

## Define import direction and public surfaces

Adopt this default direction, adapted to the repository:

| Caller | May depend on | Avoid |
| --- | --- | --- |
| Route/app composition | Feature public entry points, shared UI/patterns, application infrastructure | Deep imports into another feature's implementation |
| Feature | Its own internals, shared layers, declared infrastructure interfaces | Accidental peer-feature internals and cycles |
| Shared pattern | Shared primitives, tokens, neutral helpers | Booking/member stores, route files, product-specific schemas |
| Shared primitive | Tokens and narrowly justified neutral helpers/vendor primitives | App configuration imports, network/query policy, domain types |
| Neutral helper/token layer | Lower-level neutral code where needed | Imports back into UI or feature layers |

Permit a deliberate dependency on another domain's narrow public API when ownership and coupling are appropriate. Document the reason and prevent cycles. Do not move business concepts into generic UI just to make the import graph look flat.

Expose only deliberate entry points. A local `index.ts` may export a component and its supported types. Do not export every helper or use one global barrel that indiscriminately connects unrelated features and runtimes. Keep implementation files private by convention or tooling. Use package exports when a package is actually distributed.

Use existing resolved-import/dependency tooling when available. ESLint's `no-restricted-imports` can restrict specified imports/patterns, but a few string patterns do not prove all alias, relative, dynamic-import, or cycle rules. Check the repository's actual resolver and tools. TypeScript path aliases improve import ergonomics; they are not an architectural enforcement mechanism. See [ESLint documentation](https://eslint.org/docs/latest/rules/no-restricted-imports).

## Write the component contract

Before promoting a component, answer:

1. What user-facing responsibility does it own?
2. Which semantic element or interaction pattern does it expose?
3. Which inputs, events, and states are supported, with what defaults?
4. Who owns content, selected value, data fetching, validation, and permission decisions?
5. Who controls outer placement, inner layout, and customization?
6. What compatibility should consumers rely on, and what remains private?

Prefer concrete semantic props. Use `tone="caution"` for a visual role; map `booking.status` into that role in the booking feature. Do not make the shared Badge learn every application's status names. Let a PageHeader receive an actions slot; let the page choose a link, button, or feature command.

Use discriminated modes when mutually exclusive options otherwise create impossible combinations. For example, this illustrative TypeScript contract distinguishes owned and defaulted values:

```ts
type ValueContract<T> =
  | { mode: 'controlled'; value: T; onValueChange: (next: T) => void; defaultValue?: never }
  | { mode: 'uncontrolled'; defaultValue?: T; value?: never; onValueChange?: (next: T) => void };
```

Adapt the shape to established library conventions rather than adding a `mode` prop to every input. Specify behavior when value changes, reset occurs, or a component is remounted. Avoid switching between controlled and uncontrolled behavior during an instance's lifetime unless the actual implementation supports it deliberately. TypeScript narrowing helps model related fields; runtime inputs still require validation at their boundary. See [TypeScript discriminated unions](https://www.typescriptlang.org/docs/handbook/2/narrowing.html#discriminated-unions).

Preserve native capabilities that consumers need: `name`, `type`, `disabled`, `required`, `form`, accessible labels/descriptions, IDs, and event/ref behavior. Decide forwarding and precedence explicitly. A generic Button defaulting to `type="button"` should still allow explicit submit behavior. A link should retain navigation semantics and a real destination. Do not introduce polymorphic APIs unless multiple real semantic uses justify the complexity.

Expose a constrained set of style hooks when necessary. State which classes/slots/tokens are supported and which internal markup is private. Support an external `className` where useful, while preventing public overrides from accidentally removing mandatory behavior, labels, or critical styling. Prefer consumer wrappers for page placement instead of descendant selectors into private markup.

## Separate state, data, and policy

Shared UI may own local interaction state. A disclosure can own its open state; a field can support a documented uncontrolled mode. Statelessness is not a universal requirement.

Choose one source of truth for each fact. Keep a coordinated selection at its nearest appropriate owner, and pass values/events to children. Derive filtered rows or totals from existing data when practical instead of synchronizing copies. Keep a local draft only when the product needs a distinct editable value; document synchronization, cancellation, and reset. React's [state guidance](https://react.dev/learn/choosing-the-state-structure) and [sharing-state guidance](https://react.dev/learn/sharing-state-between-components) illustrate these principles.

Sharing a hook implementation does not automatically share state between hook instances. Choose context/store/URL state deliberately when coordination is required; do not globalize every field or dropdown.

Keep network and query-cache ownership in the domain/application layer. Pass a small view model or composable content to shared UI, and receive user-intent events. Do not make generic controls import feature stores, call a booking endpoint, read a route name to decide behavior, or choose a business-specific cache invalidation strategy.

Keep authorization enforced at the appropriate trusted boundary. UI visibility and disabled states communicate availability; they do not establish access control. Avoid coupling generic components to a particular auth provider or role vocabulary.

Use the project's translation mechanism for generic labels if it is an established shared dependency. Keep domain terminology and locale-sensitive business formatting with their owner. Make time zone and date-only versus instant semantics explicit in booking/date adapters; a generic calendar cannot decide business scheduling policy.

## Preserve styling and responsive ownership

Let the parent own placement, surrounding spacing, and available width. Let the component own its internal spacing, semantic states, focus appearance, and supported content arrangements. Use scoped styles or the repository's equivalent to prevent accidental cascade coupling.

Define semantic tokens such as surface, text, border, focus, and status tones. Theme those tokens at an application or theme boundary when the semantics agree. A client name is not a component variant. If product composition differs, create an appropriate composition over shared primitives rather than dozens of client flags.

Verify internal flexibility with Grid/Flex, shrinkable children, wrapping text, and sensible minimums. Use container queries when behavior depends on the allocated component width. Avoid encoding the whole page's breakpoints into every primitive. Inspect narrow side panels and wide columns as well as viewport sizes.

Maintain the approved design and readable Thai text across consumers. Shared components should preserve design consistency without forcing marketing pages, admin tools, and product variations into identical composition. Keep navigation destinations, headings, meaningful content, and keyboard order coherent.

Use shared data/state for desktop and mobile presentations. Different markup can be appropriate for table and agenda views; prevent duplicate IDs, exposed hidden controls, and state loss when switching. In React, state is tied to render-tree position/type/key, so extraction or conditional branches can change identity. Inspect actual behavior rather than assuming CSS similarity guarantees continuity. See [preserving state](https://react.dev/learn/preserving-and-resetting-state).

## Respect runtime and dependency cost

Preserve server/client and platform boundaries of the host framework. For React Server Components, a client module's imported dependency graph can become client code; keep interactive entry points appropriately narrow and do not pull server-only services through a shared barrel. Server-rendered content passed through a supported composition slot is a different case from importing a server-only module into client code. Verify the installed framework's rules. See [React use client](https://react.dev/reference/rsc/use-client).

Avoid making a Badge or Button import an editor, charting stack, date engine, global provider, or application bootstrap. Check meaningful bundle/runtime impact before widening a dependency used everywhere. Use established lazy-loading and code splitting where needed. Do not add memoization or virtualization without a concrete performance problem or product scale requirement.

## Apply a small first implementation plan

Deliver a practical sequence for a new project:

1. Map representative screens and responsibilities.
2. Reuse or define the minimum tokens and established primitives for the first flow.
3. Build one domain flow with local state/data ownership and public shared contracts.
4. Compare the next consumer; reuse, compose, extend, or retain separate implementation based on its actual contract.
5. Add examples and risk-based checks for the newly shared surface.
6. State ownership, dependency rules, and the change process briefly in the repository's existing documentation.

Expand the structure when a real responsibility or compatibility requirement appears. Keep the architecture understandable enough that the next developer can predict where a change belongs.
