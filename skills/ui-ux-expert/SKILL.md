---
name: ui-ux-expert
description: Design, implement, refine, and visually verify user-facing screens, components, flows, decks, documents, and prototypes. Use for hierarchy, visual craft, responsive behavior, interaction states, design-system fit, or reference-led UI work. Not for purely backend, data, CLI, or non-visual tasks.
---

# UI/UX Expert

Improve the actual rendered experience, preserve what already works, and state
the limits of the evidence. Source inspection or a completed checklist is not
proof of visual quality.

## User Defaults — Check First

- **Readable, proportional type.** Navigation must not look tiny beside the
  page. Use a consistent scale by role, not one size for everything. When a
  header is crowded, change its layout or breakpoint instead of shrinking the
  navigation text. Verify actual Thai/Latin text at normal viewing size.
- **Centered card identity.** Center each card's icon and short heading on the
  same axis on desktop and mobile. Long headings or reading-heavy copy may use
  leading alignment; ordinary wrapping is not an excuse to abandon centering.
  Do not blanket-center long prose, form contents, tables or independent actions.
- **Plan reuse before pages.** Identify shared dropdowns, cards, banners and
  their necessary variants before implementing repeated screens; do not wait
  for inconsistent page copies to accumulate. See [Shared Components](#shared-components).
- **Balanced controls.** Center button labels/icons vertically, keep icon gaps
  and neighboring actions comfortably spaced, and size fields for their data.
  Center standalone upload/media action groups within their image, card or
  panel, including choose/replace/remove actions beneath a preview.
  Single-line inputs, selects and date triggers should share coherent heights.
  See [component contracts](references/components.md) for checks and exceptions.
- **Consistent spacing.** Give related content a clear grouping rhythm: page
  gutters, panel insets, section gaps and label-to-field gaps each have a shared
  role. Diagnose both cramped joins and oversized empty areas; repair their
  common owner and verify the rendered narrow/medium/wide composition. In
  Admin/CMS headers, check the notice-to-toolbar/first-label transition as well
  as padding inside the notice; do not fix one by enlarging the other. See
  [spacing and grouping](references/user-preferences.md#spacing-and-grouping).

These are explicit user preferences, not universal design laws. Read
[user-preferences.md](references/user-preferences.md) for type starting sizes,
card exceptions, existing form/table alignment rules and observable checks.
An explicit task-specific direction takes precedence; do not silently ignore
these defaults because old implementation happens to differ.

## Direction And Scope

1. Follow current instructions and scope. Use explicit visual direction/brand,
   then the maintained product system and project guidance, then fallbacks.
   Read relevant design contracts and owners; clarify consequential conflicts.
   Keep project-specific themes in the project.
2. Preserve accessibility, behavior, data and permissions. A mockup is not a
   complete feature/data schema or permission to remove supported capabilities.
3. Copy [tokens.css](tokens.css) only when no brand, production UI, local system
   or supplied direction exists. It defines properties, not a reset. Adapt type,
   density and roles together; one unknown brand field does not justify replacement.
4. Read only task-relevant references. Examples are not universal thresholds.
5. Match effort to risk: micro-edit → focused diff and contextual render; shared
   component → affected consumers/states; redesign → complete in-scope flow and
   composition. Track all deliverables without expanding a tiny edit.

Ask one focused question only if missing audience, direction, or task context
would materially change the result. Otherwise proceed with a stated assumption.
Use available specialists for their risk, not an automatic chain of every skill.
If a referenced skill/tool is unavailable, use the linked local guidance and
report the limitation; never claim it was invoked.

## Working Loop

1. **Understand:** read the reference and owner; identify the task, source of
   truth, constraints and acceptance criteria. Preserve a before render if needed.
2. **Diagnose:** inspect the rendered surface and computed geometry/type/state.
   "Amounts wrap" is evidence; "needs whitespace" is a hypothesis. Use
   [design-judgment.md](references/design-judgment.md) for ambiguous choices.
3. **Choose:** make the smallest causal repair. Compare alternatives only for
   consequential new structure, not clear references or tiny edits.
4. **Build one slice:** resolve content, type, composition, media and important
   states through the planned shared owners; verify that slice before multiplying
   screens. Keep genuine page differences in composition or deliberate variants.
5. **Render and repair:** inspect actual browser/app/deck/PDF output with loaded
   fonts/assets and intended data. Fix hierarchy before polish; revise a failed
   hypothesis instead of stacking overrides. Track material defects as
   observation → cause → owner fix → matched after evidence → regression check.
6. **Close:** re-render after the final visual edit and follow
   [qa-checklist.md](references/qa-checklist.md). Verify every acceptance criterion
   or mark it failed/missing. A screenshot path or DOM assertion is not a review.

## Craft And Interaction

- Make the actual task prominent. Quiet scanning/comparison suits operational
  tools; editorial, public and playful experiences may need different density
  and art direction. Do not make every domain look like the fallback gallery.
- Use coherent type, spacing, color and component roles, not arbitrary quotas
  for fonts, accents, weights, cards or primary buttons. Hierarchy must survive
  without color. Preserve deliberate brand choices within applicable constraints.
- Theme and asset changes include affected header/footer, loading, auth, overlays
  and interaction states. Check sharp logos and contrast on their actual surfaces;
  use [craft defaults](references/craft-defaults.md) for asset/theme checks.
- Use meaningful authorized content or coherent mock data, never filler just to
  occupy space. Record fixture provenance in handoff/test evidence, not automatic
  developer-facing labels in the product. See
  [content rules](references/contextual-rules.md#representative-content) for the
  boundary between an authorized simulation and claims about a real service.
- Let content reflow and containers grow; preserve deliberate image crops and
  space for sticky sidebars. Recompose mobile layouts rather than miniaturizing
  desktop. Read [responsive guidance](references/responsive-web-design.md#content-banners-and-sticky-regions)
  for hero, shortcut-grid and TOC constraints.
- Apply the user defaults through shared owners; preserve their exceptions and
  existing form/table alignment rules through refactors and responsive states.
- Use semantic controls suited to the choice model and existing interaction
  conventions. Keep navigation/back paths, immediate feedback, visible focus,
  keyboard operation, error recovery and user input through failures.
- Cover applicable default, focus, hover, active, disabled, loading, empty,
  error, success and edge states. Not every component needs every state.
  Static CSS simulation never proves keyboard, focus, persistence or recovery.
  Exercise carousel swipes/pause and open dropdowns when present; see
  [carousel behavior](references/components.md#banners-and-carousels).
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

Use `$shared-component-architecture` for reuse scope, public APIs, dependency/state
boundaries and consumer migrations. Use `$design-system-guardian` for focused
token/primitive consistency; `$design-system-architect` for wider token/taxonomy
governance. Load only the specialist needed for the changed contract.
Before page implementation, map the recurring patterns in the requested scope
to existing owners: dropdowns/fields, cards, banners, navigation and actions.
For each, decide what is shared, which content/behavior genuinely varies, and
which responsive/interaction states it must support. A brief implementation note
is enough; a one-control edit only needs its owner and affected consumers.

Reuse the existing primitive, or establish the smallest missing shared unit with
the first consumer. Define its props/events and state/layout ownership. Prove its
representative states before using it across pages; migrate in-scope existing
copies. Prefer composition and deliberate variants to separate page copies or
page-name flags. Shared appearance does not merge auth/business-state ownership.
Repair common defects at the owner and check affected consumers; active old copies
mean consolidation is unfinished. Verify that in-scope pages actually use the
shared component; a similar appearance or an unused new file is not reuse.
For a whole-site request include affected public/Admin and responsive variants.
Do not build a speculative component library.

For dropdown work, read the [chevron geometry contract](references/components.md#dropdown-chevron-geometry).
The arrow must stay inside the painted trigger with consistent end padding and
vertical centering, including narrow fields and date-picker subcontrols.

## Snapshot And Verdict

Use `$snapshot` automatically for visible work. Capture the smallest sufficient
context; whole-page claims need whole-page evidence. Match route, content, state
and viewport for comparisons. Record source/build, browser, data/auth, scroll
and overlays. Open the captures yourself. Stale, unreviewed or wrong-state images
cannot verify a change; recapture after a relevant late edit. Never present a
reconstructed "before" as an earlier capture. Skill-text maintenance alone does
not require UI captures or benchmarks.

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
- `$responsive-design`: layout composition, content-driven breakpoints and
  reference adaptation across widths; `$mobile-web-qa` for platform verification.
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
