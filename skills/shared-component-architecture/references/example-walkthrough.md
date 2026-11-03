# Worked example: share presentation, retain domain meaning

Use this small React/TypeScript example to inspect boundaries and public contracts. It is a source example, not a complete application or a prescribed project structure. Apply the same reasoning in the host framework.

## What to read

All paths below are relative to `assets/component-example/` in this skill.

| Files | Responsibility |
| --- | --- |
| `shared/ui/StatusBadge.tsx`, `shared/ui/index.ts` | A neutral visual primitive with readable text and semantic tones. It knows nothing about bookings or membership. |
| `shared/layout/PageHeader.tsx`, `shared/layout/index.ts` | A page-level heading, optional description, and actions slot. It owns internal wrapping and an `h1`; the page owns action behavior and surrounding layout. |
| `features/bookings/BookingStatusBadge.tsx`, `features/bookings/index.ts` | Booking vocabulary and an exhaustive mapping from a validated booking status to its label and visual tone. |
| `features/membership/MembershipStatusBadge.tsx`, `features/membership/index.ts` | A separate membership vocabulary and presentation mapping with its own reasons to change. |
| `consumers.tsx` | Two independent page compositions with Thai text and ordinary navigation links. Render one at a time under the application's normal layout. |
| `components.css` | Scoped example classes, semantic color variables, intrinsic wrapping, and forced-colors borders. |
| `contracts.typecheck.tsx` | Compile-only positive and negative examples of the public API. |

Read the primitive, both feature wrappers, and the consumers together. Seeing a component alone does not establish that its abstraction fits its callers.

## Decisions demonstrated

**The repeated shape becomes a primitive.** `StatusBadge` accepts a `tone` and visible text. Both domains need the same inline presentation, but they do not share a lifecycle. The primitive does not accept a universal business-status enum or fetch data.

**Business meaning stays in its feature.** `BookingStatusBadge` accepts only `BookingStatus`; `MembershipStatusBadge` accepts only `MembershipStatus`. Each mapping uses `satisfies Record<...>` so adding a declared status requires a corresponding presentation entry. This is a compile-time check. An API response still needs runtime validation before becoming a trusted domain value. An unknown status needs an explicit product decision at that boundary, not a cast that conceals it.

**A wrapper earns its existence.** These wrappers remove repeated domain mapping from callers and keep it consistent within each feature. A wrapper that merely renames every prop of a third-party component may not provide that value.

**Composition supplies variable content.** `PageHeader` accepts `actions` as content instead of accumulating flags such as `showCreate`, `isBookingsPage`, and `showMemberApproval`. The caller still owns valid elements, accessible names, routing, and permissions. The slot is not an ARIA toolbar or menu; adding that interaction would require its own contract. This header is intentionally page-level. Do not reuse it inside arbitrary cards and silently introduce additional page headings.

**Native semantics remain available.** The badge forwards native span attributes and allows an outer `className`. It supplies readable text and does not automatically announce every status in a table. No ref contract is exposed because this example is noninteractive. Interactive components need their own focus/ref decisions. Feature wrappers own their label and tone; supported customization does not turn private descendant markup into a public styling API.

The badge and page header intentionally exclude `dangerouslySetInnerHTML` from
their typed public props: both own their rendered content. The compile-only
negative cases cover this boundary, including inheritance through a feature
wrapper. The example heading uses a role-based rem token rather than viewport
font scaling; reflow the surrounding layout when its content needs more room.

**Dependency direction stays visible.** Consumers import the public entries of their features and shared layout. Feature wrappers import shared UI. Shared code never imports a feature or consumer. There is no top-level barrel that re-exports the entire application.

## Adapting the example

1. Inspect the existing project's primitives, translations, tokens, routes, and module rules first. Reuse them where they fit; do not copy a second badge system into an established UI library.
2. Copy only useful source files and adjust imports to the real ownership boundaries. Use the host project's React/TypeScript versions and configuration. The example is not a reason to upgrade a framework or install a new test stack.
3. Import `components.css` once at the appropriate application composition point, or translate its contracts into the existing styling system. Match the approved design. Its colors and spacing are examples, not required branding.
4. Render each sample page independently. Its data is fictional. Replace it with the feature's validated model and actual product copy before using it in a product.
5. Compile the contract examples with the host type checker, `strict: true`, and the appropriate JSX configuration. Keep `@ts-expect-error` assertions in a compile-only file outside production entry points. The compiler must report if a forbidden case becomes accepted.
6. Inspect the component in real layouts, including narrow containers, long labels, keyboard use of page actions, and the host's theme. Do not infer browser quality from a successful type check.

## A useful extension exercise

Add a new booking state and a page that displays it. Determine which public contract changed, update the booking mapping and callers, and verify the new state. Then add a membership-only policy change. Compare the affected files. If both tasks require editing a universal status switch in the shared primitive, the domain boundary has drifted.

If a new use case needs an interactive status menu, evaluate it as an interaction rather than adding click behavior to every passive badge. Reuse the visual vocabulary where appropriate, while giving the interactive control its own semantic and keyboard contract.

## Verification and limits of this asset

The source package reports prior strict TypeScript and server-render checks.
That is historical evidence, not an automatic pass for a modified copy. To
recheck this installed version, use an existing React/TypeScript test workspace:

1. Compile `contracts.typecheck.tsx` and its imported example sources with
   `strict: true`, `jsx: react-jsx`, `module: CommonJS` and `noEmitOnError: true`.
   Keep the example's relative directory structure in a separate output folder.
   Resolve React types through that workspace's normal configuration; do not
   install dependencies into a production app just to test this optional asset.
2. Run the supplied helper against that output. React and `react-dom/server`
   must resolve from the compiled directory; the helper does not install them.

```sh
node /absolute/skill/scripts/verify-example.cjs /absolute/compiled-example
```

The [server-render helper](../scripts/verify-example.cjs) checks the six feature
mappings, forwarded native attributes, escaped text, neutral default, header
slots and both page compositions. Keep the negative type cases compile-only;
never execute their emitted JavaScript or import them into production.
Review actual imports separately to confirm shared modules do not depend on
features or consumers. The helper does not enforce an arbitrary repository's
dependency graph.

These checks do not verify browser layout, focus movement, assistive technology behavior, or an application's backend. The sample intentionally has no data layer or stateful widget. Integrating it requires checks appropriate to the real consumers and any behavior you add.
