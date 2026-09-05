---
name: reference-to-a-tee
description: Reproduce or audit a UI against supplied image files, screenshots, HTML/CSS, rendered prototypes, or mixed design references from any source. Use for reference-to-code, screenshot-to-UI, exact visual matching, pixel-perfect implementation, or to-a-tee repair while preserving real product behavior. Supports image-only work without requiring HTML. Formerly claude-to-a-tee.
---

# Reference To A Tee

Reproduce the supplied design at component level while preserving the target
product's real behavior. References may come from a designer, Figma exports,
Claude, another tool, an existing site, or a set of image files. The creator does
not determine authority; the user's chosen reference and version do.

## Select The Reference Mode

| Mode | Reference evidence | Required approach |
| --- | --- | --- |
| HTML | Runnable HTML/CSS or a rendered prototype | Inspect the rendered source and available code; measure computed geometry and exercise reachable states within scope. |
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
- Before changing product code or behavior:
  [product-contract.md](references/product-contract.md).
- Before claiming implementation is complete or publishing:
  [verification-checklist.md](references/verification-checklist.md) and
  [release-gate.md](references/release-gate.md).

Choose the path by the evidence and touched risk. A narrow component request
does not authorize a whole-site redesign or a backend feature inferred from an
icon. Account for all supplied relevant artifacts and all requested deliverables
using `$efficient-execution`.

## Operating Loop

1. Identify the active request, reference mode, target routes/components, and
   required viewports. Inventory supplied files, versions, states, and assets.
2. Inspect the actual evidence before edits: render runnable references, open
   image references with the available image viewer, and inspect the target app.
   Do not work from memory or invent source measurements that are unavailable.
3. Build a compact surface/component ledger. Separate observed facts,
   source/computed measurements, image measurements, inferences, and unknowns.
   For broad pages, include the supplied below-fold regions and repeated items.
4. Map components and visible controls to product-owned files, data, permissions,
   and behavior. Record static/no-op behavior only after observing an executable
   reference; behavior absent from a still image is unknown, not a no-op.
5. Before edits that could overwrite UX, record what follows the reference,
   what preserves product UX, any hybrid choice, evidence, risk, and verification.
6. Implement in small component passes: shell, navigation, primary content,
   repeated rows/cards, overlays, and supplied lower-page regions. Match visual
   geometry, hierarchy, density, typography, assets, and state rather than just
   colors. Preserve usable semantics and existing product architecture.
7. Render the implementation, exercise relevant interactions, and compare each
   requested surface at the correct state, crop, scale, and viewport. Fix material
   mismatches and refresh only evidence affected by the latest edits.
8. Complete the mode-aware gate. Distinguish verified visual coverage, product
   behavior verification, assumptions, accepted exceptions, and remaining gaps.

## Visual And Product Contracts

Capture shell/header geometry, page rhythm, layout constraints, type hierarchy,
card/list dimensions, borders, radii, shadows, colors, media frames, and states.
Use exact source/computed values when available and authoritative. Image-only
measurements describe visible pixels, not hidden CSS, DOM, font identity,
breakpoints, sticky behavior, or animation timing.

Do not flatten useful nested scroll regions, sticky subpanels, virtualization,
pagination, selected-state persistence, deep links, focus behavior, or real
actions merely because a reference omits them. Missing states in an image are
not evidence that the product should lose those states.

Use this decision ledger when product or visual choices diverge:

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

Report the mode, reference identities, target source/build, compared surfaces,
measured parity, `$snapshot` evidence, behavior checks, exceptions, assumptions,
and blocked or unverified items. In image-only mode, claim visual parity only
for observed regions/states; responsive adaptations and inferred interactions
are product decisions verified in the implementation, not recovered source facts.

Required observed components and requested product behavior must be implemented
and verified before declaring completion. Missing reference DOM or unseen mobile
states do not prevent completion of the agreed image-only scope. Missing evidence
for a requested claim, failed checks, and unaccepted critical mismatches do.
Commit, push, and deploy only within the user's authorization and apply
`$release-gate` for the requested action. After an authorized deploy, verify the
changed deployed surface and assets before claiming deployment success.
