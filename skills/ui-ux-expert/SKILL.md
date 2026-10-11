---
name: ui-ux-expert
description: Design, implement, refine, and visually verify user-facing screens, components, flows, decks, documents, and prototypes. Use for hierarchy, visual craft, responsive behavior, interaction states, design-system fit, or reference-led UI work. Not for purely backend, data, CLI, or non-visual tasks.
---

# UI/UX Expert

Make the requested experience work and look deliberate in its real medium.
Source inspection, checklist completion, and confident design prose are not
evidence of a good rendered result. Improve an observed problem, preserve what
already works, and state the limits of the evidence.

## Direction And Scope

1. Follow applicable instructions and the user's current scope. Within those
   boundaries, use explicit current visual direction/reference/brand first,
   then the existing product and design system, then project-specific guidance,
   and finally this skill's fallbacks. Clarify consequential conflicts.
2. Direction does not authorize breaking accessibility, product behavior, data
   integrity, or permissions. A mockup is not a complete feature/data schema.
3. Copy [tokens.css](tokens.css) only when no brand, production UI, local system,
   or supplied direction exists. It contains custom properties only, not a reset.
   Adapt roles, density and typography together. Never overwrite a branded
   system because one brand field is unknown.
4. Load only the references relevant to the task. Values and specimens are
   contextual examples, not universal thresholds or proof of taste.
5. Keep effort proportional: one-owner micro-edit needs a focused diff and
   current contextual render; a shared component needs affected-consumer/state
   checks; a redesign needs complete in-scope composition and flow evidence.
   Track all requested deliverables. Do not expand a small edit into a redesign.

Ask one focused question only if missing audience, direction, or task context
would materially change the result. Otherwise proceed with a stated assumption.
Use available specialists for their risk, not an automatic chain of every skill.
If a referenced skill/tool is unavailable, use the linked local guidance and
report the limitation; never claim it was invoked.

## Working Loop

1. **Understand.** Read the supplied material and owner implementation. Name the
   user task, content/data constraints, source of truth, and acceptance criteria.
   Preserve a before render when comparison is in scope.
2. **Diagnose.** Inspect the actual rendered surface. Separate observation from
   cause: e.g. "amounts wrap" is evidence; "needs more whitespace" is a hypothesis.
   Check geometry, computed type, content, or state to distinguish causes.
   Use [design-judgment.md](references/design-judgment.md) for ambiguous choices.
3. **Choose.** Select the smallest causal repair. For consequential new structure,
   compare a few viable arrangements briefly; implement only the chosen one.
   Clear references and tiny edits do not need alternative concepts.
4. **Build one useful slice.** Resolve composition, real content, type roles,
   media and important states in a representative viewport before multiplying
   screens. Start with existing tokens, primitives and owner components.
5. **Render early.** Open the real browser/app/deck/PDF output with loaded fonts,
   relevant assets and intended data. Inspect the image yourself. A path, DOM
   assertion, or screenshot tool success is not visual review.
6. **Repair and regress.** For each material defect track observation -> likely
   cause -> owner change -> matched after evidence -> regression check. Keep
   this compact; no mandatory defect quota or decision document for tiny edits.
   Fix composition/hierarchy before cosmetic polish. If the evidence contradicts
   the diagnosis, revise it rather than stacking unrelated CSS overrides.
7. **Close with evidence.** Re-render after the final visual change. Verify every
   in-scope acceptance criterion or explicitly mark it failed/missing. Follow
   [qa-checklist.md](references/qa-checklist.md); distinguish structural,
   rendered, behavioral, and comparative results.

## Craft And Interaction

- Make the actual task prominent. Quiet scanning/comparison suits operational
  tools; editorial, public and playful experiences may need different density
  and art direction. Do not make every domain look like the fallback gallery.
- Use coherent type, spacing, color and component roles, not arbitrary quotas
  for fonts, accents, weights, cards or primary buttons. Hierarchy must survive
  without color. Preserve deliberate brand choices within applicable constraints.
- Use actual representative content, images and data when authorized. Mark
  synthetic fixtures and unknown assets; never invent facts, customer metrics,
  testimonials, permissions, persistence or service availability.
- Read [user-preferences.md](references/user-preferences.md) for applicable
  controls: centered stat/KPI groups, above-field names, select values/options,
  native date/time values, and table headers. Keep body cells, freeform input,
  helper/error prose and checkbox/radio captions appropriately leading-aligned.
  These user preferences must survive refactors and responsive states.
- Use semantic controls suited to the choice model and existing interaction
  conventions. Keep navigation/back paths, immediate feedback, visible focus,
  keyboard operation, error recovery and user input through failures.
- Cover applicable default, focus, hover, active, disabled, loading, empty,
  error, success and edge states. Not every component needs every state.
  Static CSS simulation never proves keyboard, focus, persistence or recovery.
- Use [accessibility-checks.md](references/accessibility-checks.md) for measured
  text/UI contrast, targets, zoom/reflow and platform limits; a visual review
  alone is not accessibility certification.
- Use [anti-slop-examples.md](references/anti-slop-examples.md) to diagnose
  generic output by task harm, not to ban isolated CSS strings. A clean lint
  result is not a taste score.

## Reference And Product Work

For image/HTML/mixed references read
[reference-led-design.md](references/reference-led-design.md). Use
`$reference-to-a-tee` for faithful targets, `$mockup-to-product` for adaptation.
Match complete anatomy, typography at content scale, density, artwork and page
rhythm. Mark inferred mobile/states separately from supplied reference evidence.
User-marked examples are the minimum defect list when whole-surface fidelity is
requested. Do not create alternative art directions for a faithful-copy task.

For CMS editing, publication, live content, or Admin workflows read
[product-redesign-contracts.md](references/product-redesign-contracts.md).
Preserve reachability, data/session ownership, fields/actions and saved meaning.
Visual authoring must show authored typography and composition while editing;
prove real controls can create it and that save/reopen and public output agree.
A richer seeded fixture is not proof of editor capability. Use audience language
and useful sample values for nontechnical operators; keep schema keys and raw
JSON out of their main task. Removing clutter does not authorize deleting data,
supported features, permissions, or production configuration.

## Shared Components

Repeated UI, copied fixes, or changes to shared defaults/APIs trigger
`$design-system-guardian`; wider token/taxonomy governance may need
`$design-system-architect`. Find existing owners and actual consumers first.
Share because semantics, behavior and reasons to change belong together, not
because two screenshots look similar. Choose the smallest useful shared unit
(tokens/styles, helper/hook, primitive, or domain component); prefer composition
to page-specific flags. Define props/events, state and layout ownership, migrate
in-scope consumers, and verify affected states and behavior plus snapshots.
A new shared file with old copies still active is not completed consolidation.
Do not create a component library for a unique tiny change. Shared appearance
does not decide auth/session or business-state boundaries.

## Snapshot And Verdict

Automatically load and use `$snapshot` for visible work before the final response;
do not wait for the user to ask. Use the smallest current contextual capture
that proves the touched result. Comparison needs matched route, content, state
and viewport; whole-page claims need whole-page evidence. Never present a
reconstructed "before" as an earlier capture.

Record source/build identity and relevant route, viewport, data/auth, scroll and
overlay conditions. Open the captures and record what you actually reviewed.
Stale, unreviewed, wrong-state or missing images cannot establish verification.
A late source change requires fresh evidence for the affected surface.

Use these scoped verdicts (details in the QA reference):
- **VERIFIED:** all required checks for the stated scope passed with current,
  inspected evidence.
- **PARTIAL:** some requirements have evidence, others are untested/missing.
- **BLOCKED:** a prerequisite prevents required verification.
- **FAIL:** a required check failed; disclosure does not turn it into a pass.

State the change, source of truth, meaningful tradeoff, evidence/checks and
remaining risk concisely. Observed improvement is not proof of user preference,
usability gains or general skill effectiveness. Practical defects must be fixed
and re-rendered; never manufacture certainty to close the task.

## Focused References

- [components.md](references/components.md): fallback visual patterns and real
  behavior contracts; the [gallery](assets/component-gallery.html) is an optional
  static specimen, never a production widget library.
- [layouts.md](references/layouts.md): category-sensitive structure choices.
- [token-map.md](references/token-map.md), [craft-defaults.md](references/craft-defaults.md):
  role-based values when a local system does not already answer the question.
- [responsive-web-design.md](references/responsive-web-design.md): content pressure,
  viewport, engine, input, keyboard, media and zoom.
- [contextual-rules.md](references/contextual-rules.md): applicability, exceptions
  and multilingual stress; [brand template](references/brand-override.template.md)
  only for an explicitly needed project handoff.
- `$ui-ux-orchestrator`: broad routing; `$visual-diagnosis`, `$domain-taste`,
  `$interaction-design` and `$design-quality-review` only when their scope applies.
- [evaluation-protocol.md](references/evaluation-protocol.md): skill maintenance,
  executable fixtures, evidence integrity and baseline/candidate comparison.
  Do not run benchmarks for ordinary UI work.
- [claude-design-learning-brief.md](references/claude-design-learning-brief.md):
  remaining learning gaps and an external critique brief.
