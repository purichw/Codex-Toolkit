---
name: reference-to-a-tee
description: Reproduce or audit a UI against supplied image files, screenshots, HTML/CSS, rendered prototypes, or mixed design references from any source. Use for reference-to-code, screenshot-to-UI, exact visual matching, pixel-perfect implementation, or to-a-tee repair while preserving real product behavior. Supports image-only work without requiring HTML. Formerly claude-to-a-tee.
---

# Reference To A Tee

Reproduce the supplied design at component level while preserving the target
product's real behavior. References may come from a designer, Figma exports,
Claude, another tool, an existing site, or a set of image files. The creator does
not determine authority; the user's chosen reference and version do.

## Choose Fidelity And Effort Separately

- **Exact:** default for explicit `$reference-to-a-tee`, to-a-tee, pixel-perfect,
  or match-this-reference requests. Match the requested observable properties
  using authoritative values or justified image tolerances. Unknown source
  properties remain unknown; exact does not mean claiming impossible certainty.
- **Faithful adaptation:** use when the user asks to adapt the design to named
  product, brand, content, or device constraints. State what remains fixed and
  which dimensions may change. Permission to adapt mobile does not loosen desktop
  fidelity; unspecified differences are not automatically accepted.
- **Inspiration only:** when the user wants mood or ideas rather than a match,
  use `$ui-ux-expert` or `$design-direction`; do not impose or claim a parity gate.

Choose fast, standard, or deep effort from the changed risk, independently of
fidelity. A one-property exact repair can be fast. A broad adaptation can be deep.
"Faster" does not authorize lower fidelity or missing deliverables. A scoped
current comparison, not the amount of paperwork, proves the requested result.
Use [operating-guide.md](references/operating-guide.md) for the effort matrix.

## Select The Reference Mode

| Mode | Reference evidence | Required approach |
| --- | --- | --- |
| HTML | Runnable HTML/CSS or a rendered prototype | Inspect the relevant rendered source/code; measure requested properties and exercise affected or explicitly requested states. |
| Image-only | PNG, JPEG, WebP, or another viewable image; screenshots or crops without executable source | Inspect the actual images, record image-space measurements and uncertainty, and compare with the rendered implementation. HTML is not a prerequisite. |
| Mixed | Images plus HTML, prototype, assets, or handoff notes | Map authority per surface/state/version. Use source values only where they still describe the chosen visual reference. |

For a viewable format the current tool cannot open, use an available standard
decoder or conversion tool and preserve the original. Missing HTML is not a
blocker for image-only work. An unreadable required image is an evidence blocker;
do independent work while obtaining usable evidence.

## Source Of Truth

1. Follow the user's current explicit requirements, scope, and designated version.
2. Use the selected reference for observable presentation, content, and states.
   In mixed mode, record which artifact owns each conflicting surface; HTML does
   not automatically outrank an image. File modification time alone is not proof
   of design authority.
3. Preserve product-owned routing, data, auth, persistence, accessibility,
   security, i18n, performance, tests, and operations unless intentionally changed.
4. Use older references and handoff notes only where they remain applicable.

Record decisions when these constraints conflict. Apply established product
requirements and already-authorized exceptions without asking again. Ask about
an unresolved choice only when it materially changes the requested outcome;
continue independent work meanwhile.

## Read The Relevant Guidance

- Scoping or planning: [operating-guide.md](references/operating-guide.md).
- Inspecting HTML or mixed references:
  [reference-workflow.md](references/reference-workflow.md).
- Image-only work, crops, multiple screenshots, or image-led mixed references:
  [image-reference-workflow.md](references/image-reference-workflow.md).
- Product behavior or shared/structural contracts at risk:
  [product-contract.md](references/product-contract.md), relevant sections only.
- Component/flow reconstruction, formal audit, or broader verification:
  [verification-checklist.md](references/verification-checklist.md), checks for
  the actual scope/risk rather than the entire checklist.
- Publishing or broad implementation closeout:
  [release-gate.md](references/release-gate.md). A micro repair uses the fast-path
  evidence and Completion below; it does not require every reference document.

Choose the path by the evidence and touched risk. A narrow component request
does not authorize a whole-site redesign or a backend feature inferred from an
icon. Account for all supplied relevant artifacts and all requested deliverables
using `$efficient-execution`.

## Operating Loop

1. Identify fidelity, effort, input mode, requested properties/surfaces, and
   required viewports. Identify the supplied evidence relevant to that scope.
2. Inspect the actual evidence before edits: render runnable references, open
   image references with the available image viewer, and inspect the target app.
   Do not work from memory or invent source measurements that are unavailable.
3. Keep only the notes needed to support the claim. A fast repair needs a short
   reference/property/check note, not a ledger, worklog, or parity table. Broader
   work maps components/states and distinguishes facts, measurements, inferences,
   and unknowns, including below-fold coverage for broad page claims.
4. Map affected code and behavior. Exercise controls whose appearance/state is
   requested or whose behavior could change; do not tour every visible control
   for an isolated style fix. Flow reconstruction still covers the agreed flow.
   Absent behavior in a still image is unknown, not a no-op.
5. Before edits that could overwrite UX, record what follows the reference,
   what preserves product UX, any hybrid choice, evidence, risk, and verification.
6. Implement in small passes within the requested scope: shell, navigation,
   content, repeated items, overlays, or supplied lower-page regions. Match visual
   geometry, hierarchy, density, typography, assets, and state rather than just
   colors. Preserve usable semantics and existing product architecture.
7. Render the implementation, exercise relevant interactions, and compare each
   requested surface at the correct state, crop, scale, and viewport. Fix material
   mismatches and refresh only evidence affected by the latest edits.
8. Complete the mode-aware gate. Distinguish verified visual coverage, product
   behavior verification, assumptions, accepted exceptions, and remaining gaps.

## Visual And Product Contracts

For the requested properties and potentially affected neighbors, inspect
shell/header geometry, page rhythm, layout constraints, type hierarchy,
card/list dimensions, borders, radii, shadows, colors, media frames, and states.
Use exact source/computed values when available and authoritative. Image-only
measurements describe visible pixels, not hidden CSS, DOM, font identity,
breakpoints, sticky behavior, or animation timing.

Do not flatten useful nested scroll regions, sticky subpanels, virtualization,
pagination, selected-state persistence, deep links, focus behavior, or real
actions merely because a reference omits them. Missing states in an image are
not evidence that the product should lose those states.

Use a short note for a single material divergence; use this ledger when several
product or visual choices need tracking. Do not fill empty fields by habit:

```text
Component / reference file / state:
Observed reference UI and behavior, with evidence type:
Existing product contract and evidence:
Decision: reference adopted / product UX preserved / hybrid / needs user decision
Behavior exception:
Visual exception:
Assumptions or unknowns:
Reason, risk, implementation rule, and verification:
```

A behavior exception keeps real product mechanics while matching visible intent.
A visual exception changes visible layout, spacing, content, count, assets,
colors, or state. Document material visual exceptions; apply existing acceptance
or obtain a decision for unresolved critical divergence before publishing.
Unknown source properties are evidence limits, not automatic visual failures.
Do not mark an observed mismatch as unknown to bypass the gate.

Use `$product-ux-contracts` when behavior is at risk, `$ui-state-matrix` for missing
states, `$interaction-flow-qa` for real journeys, `$accessible-interaction` for
focus/keyboard risks, and `$design-system-guardian` for shared primitives.
Use `$reference-implementation-critique` for visual defect analysis;
`$data-dense-ux`, `$form-flow-ux`, or `$admin-prototype-reconciliation` when their
specific contracts are touched. Use `$production-asset-smoke` after deployment
when changed media needs deployed evidence.

## Mandatory Snapshot Evidence

Use `$snapshot` automatically for implementation, visual repair, parity audit,
or design handoff before the final response. Show labeled `Reference` and
`Development` views side by side; the original supplied image is valid reference
evidence. Include mobile comparison when mobile reference parity is in scope.

For a fast repair, one current contextual `Reference + Development` pair of the
affected region is sufficient, plus relevant measured/behavior checks. Do not
capture the whole page, all breakpoints, or an extra Before column merely because
a reference exists. Add those only for the requested claim or demonstrated risk.
If capture is blocked, state why and what remains unverified; do not claim parity.

Align comparable regions without stretching, retouching, or regenerating the
reference. Retain the full source and record any crop/scale transform. For broad
page claims, include full-page or top/middle/bottom coverage. A supplied crop can
prove only its visible region. Record viewport assumptions when scale is unknown.

Measure implementation geometry with browser tools where available. For HTML,
compare authoritative reference computed values. For images, compare visible
landmarks, boxes, line wraps, spacing, count, and asset crops with recorded
image-to-viewport calibration. Keep visual and functional verification separate.

## HTML Extraction Helper

Only for HTML inputs, optionally seed the inventory with:

```bash
python3 /Users/point/.codex/skills/reference-to-a-tee/scripts/extract_reference.py \
  path/to/reference.html --out .design-reference
```

Add `--render --screenshots --viewport 1440x900 --viewport 390x844` when Python
Playwright is available and those viewports are relevant. The helper does not
extract UI structure from images, execute all states, or certify parity. Use the
image workflow directly for image-only tasks. Reuse manifests only for unchanged
relevant source/dependencies and retain completed worklogs separately from seeds.

## Completion

Report the fidelity and input mode, compared scope, useful evidence/checks,
material exceptions, and remaining uncertainty. Keep fast closeouts brief; use
the expanded records only when needed for broad work or publishing provenance.
In image-only mode, claim visual parity only for observed regions/states;
responsive adaptations and inferred interactions are product decisions verified
in the implementation, not recovered source facts.

Every requested property/surface and required behavior check must be complete
with current evidence; small scope is not permission to drop a requested detail.
Stop further checking when that evidence is sufficient. Do not claim a complete
component/page match from a one-property repair. Missing reference DOM or unseen
mobile states do not prevent completion of the agreed image-only scope. Missing
evidence for a requested claim, failed checks, and unaccepted critical mismatches do.
Commit, push, and deploy only within the user's authorization and apply
`$release-gate` for the requested action. After an authorized deploy, verify the
changed deployed surface and assets before claiming deployment success.
