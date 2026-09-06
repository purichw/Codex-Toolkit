# Shared Component Decisions And Extraction

Use when repeated UI, duplicate fixes, consolidation, or a shared API/default
change makes reuse a real decision. Routine use of an existing button does not
need this whole process. Follow the current framework, directories, libraries,
and tests; do not impose a new design-system architecture on a local task.

## When To Share

Start with actual consumers, not predicted reuse. Compare their user-facing
meaning, anatomy/slots, interaction states, accessibility behavior, data needs,
and reasons to change. Extract when the stable common contract removes meaningful
duplication or keeps a correctness/interaction invariant consistent.

Repeated fixes or drifting copies are useful signals. A third occurrence is a
review prompt, not a requirement to merge; a shared invariant such as money
formatting can warrant reuse sooner. First check whether the repo or an existing
library already supplies it. Complex accessible controls often justify reuse of
proven primitives even on their first local use.

Keep implementations separate when their semantics, ownership, workflows, or
likely changes differ. Three similarly styled cards do not establish a shared
product contract. Do not invent a universal component for speculative future
screens or force unresolved product differences behind flags. A small duplication
may be cheaper and clearer than coupling unrelated features.

## Choose The Reuse Level

| What is genuinely common? | Prefer | Keep outside |
| --- | --- | --- |
| Visual roles or spacing only | Existing semantic tokens, scoped styles, or a layout utility | Unrelated markup, behavior, and business rules |
| Formatting, validation, or a calculation | Pure helper with focused tests | Rendering and page data access |
| Stateful behavior with different presentations | Existing hook/controller pattern, only if lifecycle/ownership are compatible | Feature-specific markup and unrelated side effects |
| One semantic/interactive unit with a stable state model | Existing primitive/component, or a small shared UI component | Route-specific data, permissions policy, and page layout |
| A recurring domain task and composition | Feature/domain component or pattern | Unrelated domains and application-wide assumptions |
| Appearance only, incompatible workflows, or unstable requirements | Local components/composition; share smaller pieces if useful | A generic wrapper with page-name switches |

Place the result at the narrowest common ownership boundary. Sharing inside one
feature does not imply a global `components/` export or cross-project package.
Use existing package/export conventions and avoid circular dependencies or
importing page modules back into lower-level shared code.

### Variant Or Separate Component?

Check anatomy, meaning, and state behavior. When these stay the same, an existing
variant or a small new variant may fit. Different anatomy/behavior usually calls
for composition or a separate component sharing lower-level primitives. Compare
real examples; do not decide by a fixed number of props or variant axes.

Example: loading/disabled are states of a button; size/intent are variant axes.
Use meaningful enums for exclusive choices and booleans for genuine binary
state. `isOrdersPage`, `isAdminDashboard`, or several mutually dependent flags
usually signal the wrong boundary. Do not wrap a component merely to rename
identical props unless the wrapper adds a useful domain contract.

## Define The Contract Before Extraction

Record only decisions that matter, in existing code/types/docs or a short task
note. A separate specification file is not required for a small extraction.

- **Public inputs:** minimal props, meaningful variants, supported content/slots,
  defaults, and valid combinations. Do not expose every internal CSS value.
- **Events:** callback names, payloads, timing, and async/failure behavior. Keep
  validation, propagation, loading/disabled, and duplicate-submit behavior intact.
- **State owner:** identify the source of truth for value, selection, open state,
  drafts, and requests. Preserve the existing controlled/uncontrolled model;
  avoid copying props into conflicting local state. Keep identity stable across
  rerenders so extraction does not reset focus, selection, or draft input.
- **Data/domain boundary:** keep generic presentation independent of routes,
  storage, and role-policy decisions. Pass data/events from the existing owner;
  if a domain component legitimately owns data through an established pattern,
  preserve that boundary rather than forcing all fetching into screens.
- **Layout/style boundary:** own internal anatomy; let parents own page placement
  and outer spacing unless the shared unit is explicitly a layout primitive.
  Use current tokens/variants. Keep escape hatches intentional and scoped.
- **Accessibility/DOM:** preserve semantics, keyboard and focus behavior, ref
  contracts, label/control associations, unique IDs, and form submission meaning.
  A cosmetic extraction can still change these contracts.
- **Compatibility:** enumerate affected consumers, intentional API changes, and
  any supported temporary adapter. Do not silently change shared defaults to fix
  a single page. Do not create a compatibility layer for hypothetical consumers.

## Migrate The Real Consumers

1. Inspect owner files and use `rg` plus existing language tooling to find
   imports, re-exports, wrappers, selectors, tests, stories, and active local
   copies. Bound the search to the requested feature/package first; widen when
   the shared dependency actually crosses that boundary.
2. Record baseline behavior for affected states and representative consumers.
   For visual refactors use the existing screenshot workflow; preserve current
   data, viewport, and state so a later comparison is meaningful.
3. Choose the shared boundary and minimal contract above. Separate intentional
   design/behavior changes from mechanical extraction; do not combine an
   unrequested redesign, state-management rewrite, and component consolidation.
4. Reuse or extract the implementation and move one representative consumer
   first. Check events, state persistence, keyboard/focus, and layout before
   migrating the remaining in-scope consumers. Batch truly mechanical uses when
   the contract is already established; no per-instance ceremony is needed.
5. Replace the in-scope local copies/imports with the canonical implementation.
   Search again for old symbols, selectors, wrappers, and copied definitions;
   a matching name alone is not proof of reuse. Check actual imports/render paths.
6. Retire unused definitions/styles within the approved edit scope. Respect
   project deletion/approval rules; extracting a component does not authorize
   deleting files or unrelated features. If some consumers are intentionally
   deferred, list them and the active adapter/copies; call the migration partial.
7. Update the existing component inventory, usage examples, or stories when the
   public contract changed. Do not create a gallery framework or rewrite all
   project docs for one local extraction.

## Verify Without Expanding The Task

Cover each changed contract with the smallest relevant evidence. Use existing
type/build checks for API/import changes, focused tests for shared logic/events,
and actual browser interaction checks for state, focus, input retention, and
responsive behavior that the refactor could break. Include long/empty/loading/
error/disabled content where it is part of the component's real contract.

Use `$snapshot` automatically for visible work. Capture the changed surface and
representative consumers whose variants, context, or breakpoints differ; do not
assume one default-state gallery proves all integrations. A tiny style reuse
does not require a full gallery or whole-site capture matrix. If capture is
blocked, report the missing evidence and risk rather than claiming visual parity.

Completion requires actual in-scope consumers using the intended shared code,
preserved or explicitly changed contracts, and passed required checks. Record
unused copies, scoped deferrals, and blocked verification honestly. Tests proving
the new component works alone do not prove the old implementations were replaced.

## Review Scenarios

These are maintainer review cases, not executed runtime tests or scored results.

| Situation | Expected decision / evidence |
| --- | --- |
| Two displays must format the same monetary values identically, but have different layouts | Reuse the existing formatter or extract a helper; test precision/locale behavior. Do not merge their screens. |
| Three cards share a border but have distinct workflows and state models | Share tokens/styles if useful; keep semantic components separate. Recurrence alone does not require extraction. |
| The same accessible dropdown has been copied into several settings panels | Reuse the existing control/library or extract the stable shared control, pass values/events, and test keyboard/focus plus actual panel consumers. |
| One page needs more outer spacing around an existing component | Adjust the parent layout using current tokens; do not change the shared default or add a page-specific flag. |
| An extracted form field loses draft text or focus after a rerender | Treat as a regression; inspect identity, state ownership, IDs/refs, and event contracts before declaring completion. |
| A new shared component exists but two in-scope routes still render copied code | Consolidation is incomplete; migrate them or explicitly report the accepted partial scope. |
| Shared API changes affect consumers in another feature | Identify/test those consumers, preserve compatibility or obtain scope for migration; do not silently break them or rewrite unrelated workflows. |
| One unique label-spacing edit is requested | Use the existing token/component locally; no new abstraction, taxonomy review, or full-site benchmark. |
