---
name: shared-component-architecture
description: Plan, implement, review, and evolve shared frontend components with clear reuse criteria, dependency boundaries, public APIs, state ownership, and consumer-safe migrations. Use when starting a reusable UI structure, deciding whether components should be shared, extracting duplicate UI, designing variants or wrappers, reviewing a growing shared library, or maintaining responsive marketing, catalogue, admin, and CMS frontends across pages or products. Also applies to requests about shared components, component architecture, reusable UI, โครงสร้างคอมโพเนนต์, and long-term frontend maintenance. Keep ordinary one-off markup edits scoped unless they change a shared contract.
---

# Shared Component Architecture

Build the smallest shared surface that lets real consumers evolve safely. Preserve approved design and behavior. Treat folder structure as a support for ownership and dependencies; make the actual contract and change impact explicit.

Use the project's framework, conventions, design system, and test tools. Apply these rules proportionally: a small site needs fewer layers and artifacts than a distributed UI package. Follow the user's scope and existing repository instructions. Do not introduce a framework, package, monorepo, governance ceremony, or approval step merely to apply this skill.

## Toolkit boundaries and evidence

- This skill owns reuse scope, public APIs, dependency/state ownership and
  consumer migration. Use `$design-system-guardian` for everyday token/primitive
  consistency; `$design-system-architect` for system-wide token layers, taxonomy
  or governance. Do not run all three for an ordinary one-owner repair.
- For visible work, load `$ui-ux-expert` and use `$snapshot` automatically before
  changing an existing UI and after the final visual edit. Inspect matched
  Before/After evidence, adding the supplied reference when applicable; label
  missing prior evidence honestly. Do not wait for a screenshot request.
- Use `$responsive-design` only when layout/container adaptation needs decisions.
  Architecture-only advice and skill-text maintenance do not need app captures.
- If a companion skill is unavailable, use the local contract guidance and
  report the evidence limitation instead of claiming a missing check passed.
- Extraction does not authorize destructive cleanup, package publishing, push,
  deployment, or work in another chat. Follow the current task's authorization
  and repository guardrails before those actions.

## Load only the relevant detail

- Decide whether and where to share: [sharing-decisions.md](references/sharing-decisions.md).
- Start a project or repair dependency/state/style boundaries: [architecture-and-contracts.md](references/architecture-and-contracts.md).
- Change an existing shared API, test consumers, migrate or split it: [evolution-and-review.md](references/evolution-and-review.md).
- Inspect a small React/TypeScript implementation: [example-walkthrough.md](references/example-walkthrough.md) and the specific files it identifies in `assets/component-example/`. Treat these as examples, not a mandatory stack or theme.
- Verify platform-specific claims against [sources.md](references/sources.md) and the installed framework version.

## 1. Establish the real scope before changing code

1. Read repository instructions, package manifests, aliases, routes, current UI library, tokens, and nearby implementations. Search for an existing component and its consumers before creating a new one.
2. Identify the user task, semantic role, interactions, state, accessibility obligations, responsive contexts, and expected reasons for change.
3. Identify whether the task starts new work, adds a consumer, extracts existing duplication, fixes a shared defect, or changes a public contract.
4. For existing components, inspect definitions, exports, imports, wrappers, stories, tests, and relevant dynamic registries. Record known consumers and any uncertainty in discovery.
5. Preserve approved visuals, content, routes, permissions, and behavior unless the task authorizes changing them. Do not import unrelated project assumptions or copy the bundled example's theme.

Produce a short working decision, then implement when authorized. Do not stop at a plan if the user requested implementation. Ask only about missing information that materially changes the boundary or business behavior; proceed with clearly stated routine assumptions.

## 2. Choose the narrowest useful sharing scope

| Scope | Place responsibility here when |
| --- | --- |
| Page/local | A single composition or unstable one-off behavior owns the decision. |
| Feature/domain | Multiple routes share a business concept, lifecycle, policy, or domain-specific UI. |
| App-wide UI/pattern | Consumers share stable visual/interaction semantics independent of feature business rules. |
| Cross-app package | Real independently evolving consumers need a stable contract and there is a release/compatibility owner. |

Reuse the existing component if its contract fits. Extend it for a coherent semantic variation, compose it for consumer-specific content, or retain separate components when behavior and change reasons differ. Extract a hook/function when logic is the common part. Split an abstraction when special cases consistently diverge.

Evaluate sharing against all of these questions:

- Do the consumers mean the same thing to the user and expose compatible behavior?
- Do their state, validation, keyboard, focus, and responsive contracts agree?
- Would they reasonably change together, with compatible ownership?
- Can the common API remain understandable without page-name/client-name switches or unrelated flags?
- Can dependencies flow toward stable lower-level code without pulling feature data, routing, or authorization policy into generic UI?

Use multiple real consumers as evidence, not a mandatory count. A known Button or Dialog contract can justify centralization at first use. A third superficially similar card does not prove a common abstraction. Prefer deliberate local duplication to a speculative public API that predicts unrequested features.

## 3. Establish a small architecture at project start

1. Inventory representative screens and distinct states. Mark likely primitives, repeated neutral patterns, domain components, and page compositions.
2. Adopt existing tokens and public UI primitives. If none exist, establish only the typography, spacing, surface, color, focus, and control contracts needed for the first real flow.
3. Keep app/route composition above domain features; keep generic UI independent of app and domain code. Expose intentional public entry points rather than deep imports into internals.
4. Implement a thin real flow and compare the next real consumer before expanding the shared surface. Make highly established interaction primitives available early without building an entire speculative design system.
5. Record only decisions that affect future consumers: purpose, owner/scope, allowed dependencies, public contract, and a representative usage. Create directories only when they have a current responsibility.
6. Use existing lint, type, package, or dependency tools to enforce important boundaries where practical. An alias or folder name alone does not enforce a boundary.

Read `architecture-and-contracts.md` for an adaptable folder map and directional rules. Keep route and feature ownership aligned with the host framework; do not force a folder migration for appearance alone.

## 4. Specify the contract before widening reuse

Define purpose, semantic element/role, inputs, outputs/events, state owner, supported states, layout behavior, and non-goals. Write at least one realistic usage; add a contrasting existing consumer when it tests the proposed abstraction. Use the compact record in `evolution-and-review.md` when the decision warrants documentation.

- Name props by semantic intent (`tone`, `size`, `onConfirm`) rather than caller identity (`isClinic`, `isMembershipPage`). Allow genuine capability flags when they express a coherent contract.
- Use a small set of meaningful variants. Investigate correlated or contradictory flags; do not apply a numeric prop limit as a design rule.
- Use slots/children for variable content and composition. Keep required semantics and accessibility obligations explicit. Do not require callers to assemble critical keyboard/focus behavior correctly from unrelated pieces.
- Preserve relevant native attributes, form behavior, labels, IDs, events, and ref/focus access as the framework/version requires. Define which attributes callers may override. Do not replace an anchor with a button or the reverse solely for styling.
- State whether an input is controlled, uncontrolled, or supports both through an explicit contract. Avoid two active sources of truth and contradictory pending/error/success states. Use union types or equivalent constraints where useful; validate untrusted runtime data separately.
- Keep business status mapping, API schemas, data fetching, authorization, analytics policy, and navigation decisions at their owning boundary. UI may receive state/data and emit events. Hiding or disabling a control is not server authorization.
- Scope internal styles and use semantic tokens. Let parents control placement; let the component control its internal layout. Provide documented customization points where needed instead of consumers reaching into private DOM/CSS.
- Preserve long Thai/English text, empty/error/loading states, keyboard access, and reduced motion. Verify the component in narrow and wide containers, not only at one viewport.
- Preserve the host's server/client boundaries and avoid adding large dependencies to widely imported primitives. Introduce memoization, virtualization, and generic factories only for measured or concrete needs.

Prefer an established accessible primitive already used in the project for Dialog, Combobox, DatePicker, Tooltip, and similar complex interactions. Add a wrapper when it contributes a stable product contract; do not wrap every vendor export automatically.

## 5. Evolve shared code with consumers in view

1. Identify the contract being changed and the affected consumers before editing.
2. Separate behavior-preserving extraction from intentional product changes where practical; do not obscure a behavior change inside a refactor.
3. Choose a compatible addition, consumer wrapper, coordinated migration, or split. Avoid permanent compatibility flags and unexplained parallel V2 components.
4. Update the source, public exports, impacted consumers, and relevant documentation/tests together for a single app. For separately released consumers, state compatibility, versioning, migration, and retirement conditions.
5. Preserve state identity and lifecycle during refactors. In React, moving component types/keys or switching rendered branches can reset state; verify actual consumers rather than assuming extracted markup is equivalent.
6. Keep deletion local to verified obsolete code. Do not remove a public export merely because an incomplete search found no usage.

When multi-product behavior differs, share stable primitives/tokens or a proven domain kernel, and retain separate policy adapters. Do not turn every client into flags on one universal component.

## 6. Verify in proportion to shared impact

- Run available type/lint/build checks needed to validate the change and import boundaries.
- Test observable behavior for risks introduced or changed: keyboard/focus, controlled state, native form submission, pending/error transitions, and event ownership. Avoid tests that only mirror implementation or assert private class names.
- Review representative consumers and edge states at relevant sizes. Include long/localized content and inspect in-layout behavior, not only isolated stories.
- Use Storybook or an existing gallery if useful; it is optional. Automated accessibility checks and screenshots cover only part of the contract.
- For migrations, verify the known consumers, obsolete API references, and fallback/removal conditions. Report limitations in consumer discovery or unavailable checks.
- Stop additional testing and redesign once every in-scope deliverable and
  required check has sufficient current evidence. A failed or missing required
  check stays failed or unverified; disclosure is not a pass. An unused shared
  file with old in-scope copies still active is not a completed migration.

## Delivery

Summarize: what is shared and at which scope; what stays local/domain-owned and why; the public API and dependency direction; affected consumers and migrations; checks actually run and material remaining limits. Include useful file references when implementing in a project. Explain decisions in the user's language.

For architecture-only work, deliver a concrete component map, dependency rules, example API, first implementation slice, and migration/review criteria. Never claim that a skill, component, test, migration, or release ran when it did not.
