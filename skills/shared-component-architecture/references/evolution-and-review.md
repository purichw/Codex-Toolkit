# Evolve and review shared components

Use this reference when extracting existing UI, changing a shared contract, migrating consumers, or deciding whether sharing should continue. Treat its architectural defaults as recommendations to adapt to the project; follow existing ownership and release rules.

## Contents

1. Inventory the component and its consumers
2. Make the smallest compatible extraction
3. Classify the contract change
4. Verify the risks that changed
5. Migrate and release deliberately
6. Keep vendor boundaries proportionate
7. Split components when their contracts diverge
8. Record decisions briefly
9. Apply the approach to practical cases

## 1. Inventory the component and its consumers

Read the repository instructions, component implementation, related styles, tokens, types, and existing examples before editing. Identify the installed UI library and use its established accessible controls before implementing a complex dialog, combobox, or date picker yourself.

Trace the actual consumption paths:

- Search direct imports and exported symbols with `rg`; inspect path aliases and public entry points.
- Follow relevant re-exports, wrappers, and consumers of wrappers.
- Inspect registries, lazy imports, generated mappings, or string-based component names only when the project uses those mechanisms.
- Search selectors, documented CSS hooks, and tests affected by markup or class changes.
- Identify externally distributed consumers separately; repository search cannot prove their absence.

Record which consumers were found and which remain unknown. Use existing ownership records or ask the project maintainer when ownership blocks a consequential decision. Never invent a team, reviewer, or approval requirement. For a small project, a named maintainer or existing project owner is sufficient.

Keep shared UI independent of feature internals. Prefer feature-local composition over importing another feature's private component. Allow a deliberate, narrow public domain API when the dependency is meaningful, documented, and acyclic; do not move business logic into generic UI merely to satisfy a folder rule.

## 2. Make the smallest compatible extraction

1. Observe existing behavior at representative consumers. Record meaningful differences before deciding they are accidental duplication.
2. Establish the common responsibility, stable inputs, outputs, and variation points. Keep unsettled or divergent behavior local.
3. Extract the smallest useful shared unit. Preserve defaults, accessible names, event semantics, state ownership, and layout assumptions initially.
4. Migrate representative consumers with different constraints, then remaining known consumers within the agreed scope.
5. Remove superseded code only after its consumers have moved. Keep a temporary adapter only for an identified migration need.

Preserve mounted identity and user-entered state when reorganizing component trees. Check whether changes reset selection, focus, input, or open overlays. Avoid combining extraction with an unrelated redesign or business-rule change; separate independently reviewable decisions when their effects would otherwise be difficult to diagnose.

Do not write tests merely to reproduce trivial implementation details. Add characterization tests when observable behavior is uncertain and the extraction could regress it.

## 3. Classify the contract change

Treat the component contract as more than its prop names.

| Contract surface | Check before calling a change compatible |
| --- | --- |
| Inputs and outputs | Defaults, required values, event payloads, callback timing, controlled/uncontrolled behavior |
| Semantics | Element type, accessible name, label association, error relationship, heading level |
| Interaction | Keyboard behavior, focus return, submit behavior, disabled and loading behavior |
| Presentation | Layout responsibility, dimensions, wrapping, responsive behavior, theme tokens, supported CSS hooks |
| Integration | Public imports, dependency requirements, rendering environment, supported extension points |

Adding an optional prop with unchanged defaults can be compatible. Adding it while changing default behavior may not be. Renaming a prop, changing a callback's meaning, switching a button into a link, or removing a supported CSS hook can break consumers without causing a type error.

Distinguish intended fixes from promised behavior. An accessibility fix may be necessary even when consumers relied on the defect; describe the effect and update those consumers rather than silently preserving the defect.

## 4. Verify the risks that changed

Select checks from the contract and impact radius. Reuse the project's existing runner and component examples; do not require a new toolchain for a modest component change.

| Change | Useful evidence |
| --- | --- |
| Props or callback contract | Type checks where applicable; an interaction asserting the intended consumer outcome |
| Focus, keyboard, or form behavior | Browser interaction through names/roles/labels; submit and focus assertions |
| Shared styles or tokens | Representative consumer renders across themes, containers, and responsive widths |
| Data-to-UI mapping | Boundary examples for valid, missing, and unknown input values |
| Feature extraction | Integration check for the affected user journey and retained state |

Exercise applicable states: default, loading, empty, error, success, disabled, and selected. Include long TH/EN text, narrow containers, and changed content volume where they stress the component. Test combinations with distinct behavior; avoid an exhaustive Cartesian product without a concrete risk.

Assert observable outcomes rather than private state, class implementation, or internal call order unless those are explicitly public contracts. This aligns with [Testing Library's user-oriented testing principles](https://testing-library.com/docs/guiding-principles/); using that particular library is optional.

Use visual comparisons for appearance changes, but inspect the diff. Screenshots alone do not establish keyboard behavior, accessible semantics, hidden-state correctness, or persistence during resize. Passing type checks does not establish runtime or visual correctness either. Report tools, consumers, and states actually checked; state remaining gaps without inventing results.

Stop when the changed risks and required gates are covered. Broaden verification only for a discovered dependency, failure, or unresolved risk.

## 5. Migrate and release deliberately

For an internal single-application component, prefer an atomic change that updates the implementation and all known consumers together. Do not introduce package versioning solely because a component is shared internally.

For an independently published or versioned library, identify its declared public API and follow its release policy. Under [Semantic Versioning](https://semver.org/), incompatible public API changes require a major version after 1.0; compatible additions use minor versions and compatible fixes use patches. Treat supported behavior and presentation hooks as part of that API when promised. Follow the package's pre-1.0 policy explicitly.

When a migration must span releases, record the replacement, affected consumers, responsible maintainer, removal condition, and target milestone agreed by the project. Keep old-to-new adapters narrow. Do not add speculative compatibility branches, invent removal dates, or leave deprecation without a tracked completion condition. Verify remaining uses before removal, and preserve a practical rollback path for consequential changes.

## 6. Keep vendor boundaries proportionate

Wrap a third-party component when enforcing a stable product contract, accessibility defaults, tokens, or integration behavior that multiple consumers need. Keep vendor-specific implementation inside that boundary where useful.

Use a vendor component directly when a wrapper would only rename identical props without protecting a meaningful policy. Do not promise effortless replacement of a complex library. Assess which capabilities and types intentionally remain vendor-specific, and document that coupling where it affects consumers.

## 7. Split components when their contracts diverge

Review a shared abstraction when each change needs consumer-specific flags, domain-name switches, incompatible lifecycle behavior, or exceptions to layout and permissions. Determine whether consumers still benefit from the same policy and reason to change.

Keep a stable primitive shared, then move divergent compositions or workflows into their feature. For example, preserve common field styling while separating membership approval from booking cancellation. Accept limited duplication when it reduces coordination and clarifies ownership. Remove obsolete variants once their consumers have moved; do not keep a growing compatibility layer as the permanent design.

## 8. Record decisions briefly

Use the existing issue, component documentation, or change description. Create a separate architecture record only for a consequential decision.

```text
Component and responsibility:
Scope and known consumers:
Inputs, outputs, defaults, and state owner:
Supported semantics, layout, and extension points:
Dependencies and maintainer (confirmed, or unresolved):
Decision: keep local / share / extend / compose / split
Reason and differences intentionally kept local:
Compatibility impact and migration/removal condition:
Evidence checked and remaining limitations:
```

## 9. Apply the approach to practical cases

**A status badge changes color.** Identify affected semantic tokens and domain mappings. Verify representative booking and membership states, readable labels, and theme contrast. Preserve domain meaning rather than applying one status enum to every feature. Treat promised visual hooks as compatibility concerns.

**Two edit dialogs look similar.** Compare validation, permissions, async submission, unsaved-change behavior, and focus return. Reuse the established dialog and form controls. Share the workflow only if these responsibilities align; otherwise keep two feature compositions around the same primitives.

**A shared card accumulates mode flags.** Inventory consumers and the purpose of every flag. Replace incompatible modes with focused feature components, or expose a small composition slot when the responsibility is genuinely shared. Migrate known consumers and delete dead branches; do not replace flags with an equally complex universal configuration object.
