# Decide what to share

Use this guide when choosing component boundaries, reviewing duplication, or deciding whether an existing abstraction should grow. Treat the criteria as design guidance. Adapt them to the repository's established architecture and the concrete task.

## Contents

- Identify the shared contract
- Choose the smallest useful scope
- Select the appropriate action
- Design an understandable API
- Place data, state, and policy deliberately
- Apply the criteria to common projects
- Record a decision briefly

## Identify the shared contract

Inspect real consumers before extracting an existing implementation. Record what users do, what the component promises, which states it supports, and why each consumer changes. For a new project, use confirmed requirements and established design-system primitives as evidence; label speculative consumers explicitly.

Evaluate these dimensions together:

| Criterion | Evidence supporting reuse | Evidence supporting separation |
| --- | --- | --- |
| Semantic purpose | Consumers represent the same concept or interaction. | Identical shapes perform different jobs. |
| Behavior and accessibility | Keyboard, focus, validation, loading, and dismissal rules agree. | Consumers require conflicting interaction contracts. |
| Reasons for change | A correction or design decision should normally affect every consumer. | Changes repeatedly target one consumer and surprise another. |
| API coherence | A small set of meaningful inputs describes all supported uses. | Page names, unrelated modes, and exception flags accumulate. |
| Dependencies | The component belongs below its consumers and can accept explicit inputs. | It must import routes, feature stores, or unrelated domain policies. |
| Responsibility | The team can identify who maintains the contract and reviews changes. | Consumers need incompatible policies or independent release timing. |

Do not compute a score that allows strong visual similarity to outweigh incompatible semantics. A second or third use provides evidence, not automatic permission to extract. Conversely, an established Button, field-label relationship, or accessible dialog primitive can be shared at first use when its contract is already known. Keep an uncertain, rapidly changing section local until its boundaries become clearer.

Distinguish repeated markup from repeated knowledge. Two layouts may repeat a few lines while representing independent requirements. Centralize a rule when all consumers must interpret that rule consistently; avoid centralizing unrelated rules merely because their current output looks alike.

## Choose the smallest useful scope

| Scope | Suitable contents | Boundary |
| --- | --- | --- |
| Local component | A page section, experimental presentation, or helper with one clear owner | Keep beside its consumer; extract for clarity when useful. |
| Feature or domain reuse | Appointment summary, membership application status, scheduling policy adapter | Reuse across routes in that domain; import shared UI and the domain's own contracts. |
| Application-wide UI | Buttons, fields, layout primitives, neutral feedback patterns | Accept presentation and interaction inputs; avoid importing feature models or policies. |
| Cross-application package | A stable contract with actual applications depending on it | Establish compatibility, distribution, ownership, and upgrade responsibility before publishing. |

Shared does not imply globally accessible. Prefer a feature-owned public API when several routes need the same domain component. Permit a deliberate dependency on another domain's narrow public contract when the architecture calls for it; avoid reaching through its internal folders or creating a cycle.

Do not introduce a monorepo, separate package, or release workflow solely to organize one application's components. Promote scope when actual consumers and maintenance needs justify the additional coordination.

## Select the appropriate action

| Action | Choose it when | Check before proceeding |
| --- | --- | --- |
| Reuse an existing component | Its documented contract already fits. | Inspect current API and examples; avoid a duplicate with a new name. |
| Add a semantic variant | The purpose remains the same and the difference belongs to the component. | Name the intent; verify existing consumers remain correct. |
| Compose a wrapper | Shared mechanics fit, but domain wording, mapping, or policy differs. | Keep the domain wrapper in its feature. |
| Extract logic or a hook | Behavior is common while markup must differ. | Specify inputs, effects, ownership, and cleanup. |
| Retain local implementations | Requirements are independent or still unstable. | Record the intentional duplication if future reviewers could mistake it for an oversight. |
| Extract a shared component | Real contracts align and a small public API emerges. | Compare materially different consumers before generalizing. |
| Split an existing abstraction | Exceptions repeatedly change its meaning or behavior. | Preserve useful primitives and migrate callers deliberately. |

Prefer composition for varying content. Prefer a dedicated domain wrapper for stable business interpretation. Share a generic engine only when its configuration describes a coherent domain; do not disguise arbitrary branching as configuration.

## Design an understandable API

Use names that describe the component's purpose. Prefer `appearance="primary"` or `density="compact"` over combinations such as `isBlue`, `small`, `forClinic`, and `hidePartOnMobile`. A boolean is appropriate for a genuinely binary, independent state such as `disabled`; the problem is contradictory combinations and unrelated responsibilities.

Use a discriminated union when one mode requires different inputs. Keep an action button and navigation link semantically correct; do not add polymorphism unless consumers need it and the type/behavior contract remains understandable.

Use slots or children for content such as a page header's actions. Specify what the slot accepts and who owns alignment, labeling, focus, and behavior. A slot should not require callers to reconstruct the component's accessibility contract every time. Avoid generic render callbacks where ordinary composition is sufficient.

Treat growing variant counts as a review signal, not a numeric rejection rule. Ask whether variants still describe one concept. If a variant changes data requirements, user workflow, and ownership together, consider a separate component or feature wrapper.

Allow native attributes, event handlers, refs, and styling hooks where consumers need them. Define which invariants remain protected. If `className` is supported, specify its scope; do not encourage consumers to target private descendants or override focus, disabled, or layout behavior accidentally. Handle conflicting attributes deliberately rather than relying on spread order.

Keep examples of both valid usage and an invalid combination. Document meaningful defaults, loading/error behavior, responsive constraints, and extension points at the public boundary.

## Place data, state, and policy deliberately

Keep server queries, authorization, domain transitions, and business validation in their appropriate application or domain layers. Pass explicit display values and event callbacks into neutral UI. A domain container may fetch data when the repository's architecture assigns that responsibility to it; the rule is about boundaries, not requiring every component to be stateless.

Validate untrusted data at the relevant boundary. Type declarations and assertions alone do not validate a network response. Map an external status to a known domain status, then map that domain status to a visual tone. Define how unknown values appear; do not silently present an unknown status as approved. Enforce permissions server-side independently of whether the UI displays an action.

Choose one source of truth for each value. State may remain local for an independent disclosure, move to a common owner for coordinated selection, or belong to a domain controller for an application workflow. Reusing a hook shares logic; separate hook instances do not automatically share state. Specify controlled/default-value behavior when offering both patterns, and avoid switching ownership implicitly.

## Apply the criteria to common projects

| Situation | Recommended analysis |
| --- | --- |
| Marketing header and CMS header | Share appropriate primitives and tokens. Keep distinct shells when navigation structure, density, and user tasks differ. |
| Booking and membership status | Share a neutral badge; keep status vocabularies, labels, permissions, and tone mapping in their respective domains. |
| Trainer and clinic scheduling | Compare lifecycle, capacity, time-zone handling, resources, consent, and cancellation rules. Share a scheduling kernel only where these contracts align; preserve differing policy adapters. |
| Mobile agenda and desktop table | Share data and selection ownership. Use different markup when needed, with only the intended view exposed and no loss of state. |
| Several client brands | Express agreed visual differences through semantic tokens and theme scope. Keep unrelated behavior out of client-name conditionals in primitives. |
| Destructive confirmations | Reuse established dialog mechanics. Keep domain-specific consequences, required confirmation, and asynchronous behavior explicit. |

Before building a complex control, inspect the project's existing library. Adopt a suitable supported implementation where it meets the contract. Add a wrapper when it creates a useful stable boundary; avoid pass-through wrappers that merely rename every upstream prop and add maintenance without a clear benefit.

## Record a decision briefly

Capture the candidate, real consumers, shared contract, differences, chosen scope, and dependency direction in a few lines. Include the reason for intentional separation when relevant. Revisit the decision when consumers diverge or a common contract becomes clearer; avoid predicting every future use before implementing the present task.
