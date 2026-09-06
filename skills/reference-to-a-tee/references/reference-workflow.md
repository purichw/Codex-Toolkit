# HTML And Mixed Reference Workflow

Use when runnable HTML or prototypes are supplied. For image inputs, also use
[image-reference-workflow.md](image-reference-workflow.md); image-only work does
not need this HTML path.

Apply the fidelity/effort choice from [operating-guide.md](operating-guide.md).
This is a menu for the affected scope, not a requirement to tour a prototype for
every style edit. For a fast repair use its Fast Path and inspect only the source,
computed values, and states needed for the requested property and touched risk.

## Inventory Accelerator

For broader work, optionally seed an inventory when it will save discovery time:

```bash
python3 /Users/point/.codex/skills/reference-to-a-tee/scripts/extract_reference.py \
  path/to/reference.html --out .design-reference
```

Optional rendered measurement, with Python Playwright available:

```bash
python3 /Users/point/.codex/skills/reference-to-a-tee/scripts/extract_reference.py \
  path/to/reference.html --out .design-reference \
  --render --screenshots --viewport 1440x900 --viewport 390x844
```

If using the helper, read `reference-manifest.json`, `reference-manifest.md`, and
`REFERENCE_TO_A_TEE_WORKLOG.md`. Treat generated routes and component candidates
as discovery hints, not exhaustive coverage. The helper's rendered probe samples
initial states; it does not exercise every control or certify parity. It accepts
HTML only and cannot analyze PNG/JPEG/WebP images.

Reuse a manifest only when relevant source and dependencies still match. Read
external CSS, fonts, scripts, and assets when they affect the visual contract;
the HTML file hash alone does not identify changes in external dependencies.
Use a fresh output folder when regenerating seeds so a completed worklog is not
overwritten.

## Inspect The Actual Reference

1. Identify the selected source version, related assets, image references, and
   handoff notes. In mixed mode, establish which artifact owns each surface.
2. Render runnable source with available browser tooling. Check the initial
   route, title, load state, missing assets, and reference setup before measuring.
3. Inspect the states and exercise the controls needed for the requested result
   or affected behavior. For flow reconstruction, cover all requested steps and
   actions; for an isolated visual repair, do not click unrelated controls simply
   because they appear nearby. Record observed outcomes or unknowns as relevant.
4. Inspect HTML/CSS/JavaScript and search state/route handlers for surfaces that
   initial rendering misses. Record source breakpoints, selectors, assets,
   transitions, and component structure. Demo code is evidence, not architecture
   to copy into the product.
5. Capture relevant viewport/state baselines. Use supplied screenshots to select
   states and, where designated, visual authority. Investigate disagreement;
   do not assume HTML must win over a newer selected image.
6. Inspect the target's existing routes, data, permissions, containers, controls,
   selectors, and tests before replacing its presentation.

Record a blocked HTML setup and continue from usable image evidence if it meets
the requested scope. Label the mode change and unavailable source claims; do not
pretend the executable reference was inspected. If an exact source-dependent
claim is required, disclose that remaining blocker.

## Coverage And Controls

For broad reconstruction keep rows for requested surfaces/states/actions. For a
local repair use a short property/check note; no full coverage table is required:

```text
surface/state | reference artifact/version | how observed/opened | controls |
observed result or unknown | target component/data/action/permission |
decision | preserved product contract | verification | status
```

For broad coverage include supplied below-fold regions, repeated item count/order,
responsive-only controls, and affected inherited product controls. A narrow
property repair does not expand to all other features of its host page. In mixed
mode, image-only states may have unknown reference behavior; apply the image
workflow rather than pretending to have clicked them.

For multi-screen work, record each affected route's first-viewport and lower-page
components, active navigation, overlays, empty states, media, and responsive
variants. Treat featured/pinned/lead/hero/carousel presentation as layout
contracts; map product data explicitly and do not invent duplicate suppression
or sorting rules. A missing secondary-route component is still a mismatch when
that route is in scope.

Before edits that involve a material tradeoff, classify it as `reference adopted`,
`product UX preserved`, `hybrid`, or `needs user decision`. Include reason,
evidence, risk, and a check that guards preserved behavior. Record requested
omissions or deferrals; do not silently implement a subset of the agreed scope.

## Visual Layer And Component Contracts

Use authoritative source or computed values for layout mode, width/min/max,
wrapping, font metrics, padding/gap/margins, borders, radius, shadow, media sizing,
and breakpoint overrides. For conflicting image-led regions, measure the image
and mark source values from older HTML as non-authoritative.

Measure shell/header/nav, page title, primary content, repeated cards/tables,
media frames, overlays, and lower-page structure supplied within scope. Record
page height, section offsets, internal scroll bounds, sticky timing, and first/
last reachable items when relevant to the actual rendered reference. Match
reference motion only when observed or explicitly specified; preserve product
motion required for usability and accessibility.

For multiple measurements or formal/broad audits, keep a parity table with
source identity, units, viewport/state, reference and implementation values,
delta/tolerance, evidence type, and status. One measured fix can use one short
note with its comparison evidence instead. Use computed values for both sides
where source is available; do not infer approximate CSS
from a screenshot when matching authoritative source exposes the value.

Work component by component. Keep geometry faithful while preserving data,
auth, route, persistence, focus, nested scroll, virtualization, loading, and
error contracts described in [product-contract.md](product-contract.md).
