# Operating Guide

Start with the requested outcome, fidelity, effort, and HTML/image-only/mixed
input mode. Scope discovery to the affected surface and its direct dependencies.
Account for all requested work without treating every reference file as a request
to implement the entire product.

## Fidelity Is Not A Workload Tier

Use the fidelity rules in [../SKILL.md](../SKILL.md): exact by default for an
explicit invocation/matching request, faithful adaptation only within requested
flexibility, and design skills for inspiration-only work. State an assumption
and proceed when intent is clear. Ask one focused question only when an unresolved
choice would materially change the outcome; do not ask the user to select a mode
for every task. Speed requests never silently lower fidelity.

## Effort Matrix

| Effort | Use when | Sufficient evidence / stop rule |
| --- | --- | --- |
| Fast | An isolated copy, spacing, type, radius, crop, or other visual-property repair with understood ownership and no shared/structural/behavioral risk. | Inspect the relevant reference and target, check the requested property and likely regression, and show one current contextual Reference/Development pair. A short note suffices; stop when the local claim is supported. |
| Standard | One component, route, or narrow flow needs reconstruction/adaptation or several visual properties change. | Map the affected states/controls, measure meaningful geometry, exercise changed behavior, and compare representative required states/viewports. Use brief notes; a small table only when it helps. |
| Deep | Broad pages/flows, shared defaults/layout, routing, auth/data, scroll/focus, uncertain ownership, or material conflicting references/failed targeted checks. | Keep a coverage/decision ledger and test the affected contracts and requested surfaces. Broaden only where dependencies or failures justify it. |
| Release overlay | An authorized commit, push, deploy, merge, or release. | Add action-specific checks from `$release-gate`, including endpoint verification when applicable. Publishing a tiny repair does not itself require unrelated UI tours or an entire parity ledger. |

New CSS that changes shared defaults, wrapping, hit areas, sticky positioning, or
focus behavior may exceed fast scope despite a one-line diff. Choose risk from
actual effects, not line count. Conversely, the name `reference-to-a-tee`, an
image attachment, or a request for exactness alone does not imply deep effort.

## Fast Path

1. Identify the requested property/region and authoritative evidence. Inspect
   the relevant supplied image or rendered HTML state and the actual target.
2. Read owner source and nearby selectors/dependencies. Preserve existing
   behavior; choose the smallest useful measurement or observation for the fix.
3. Make the focused edit. Check diff hygiene and the expected visual result;
   exercise behavior only where the edit could affect it or the user requested it.
4. Use `$snapshot` automatically for a current contextual comparison of that
   region. Include a relevant hover/focus or adjacent state when it could regress;
   no full-page capture, all-controls tour, or full viewport matrix by default.
5. Close with the change, reference, checked scope, and any material uncertainty.
   Keep the note in conversation or existing task context; no new tracking file,
   extractor output, hash table, or pixel-diff report is required for a fresh
   direct comparison. Retain enough identity to distinguish source versions.

Reused evidence still needs matching relevant source/build, reference, viewport,
and state conditions. Unknown image scale must still be acknowledged; use image
units or ratios instead of inventing CSS values. Never conceal a known mismatch
by inflating tolerance, cropping it out, or calling it an adaptation after failure.

## Read Path

- Fast isolated repair: the Fast Path above and the entrypoint's source/evidence
  rules suffice; consult deeper references only when the touched risk needs them.
- Component/flow HTML inspection: [reference-workflow.md](reference-workflow.md).
- Images, crops, or mixed-reference authority:
  [image-reference-workflow.md](image-reference-workflow.md).
- Product implementation: [product-contract.md](product-contract.md).
- Completion or publishing: [verification-checklist.md](verification-checklist.md)
  and [release-gate.md](release-gate.md).

Inspect the reference with its actual medium: run executable source or open the
image. Inspect the existing product before replacing components. A screenshot
file is already rendered reference evidence; it needs inspection and calibration,
not fabricated HTML or invented interactive states.

## Working Notes

For standard work use a brief note; for broad work use one compact ledger or an
existing project note. Keep only applicable fields and split it only when size
makes it easier to maintain. The HTML extractor produces a seed, not completed
evidence. Do not require this full template for fast repairs.

```text
REQUESTED DELIVERABLES AND STATUS:
FIDELITY / ALLOWED ADAPTATIONS / EFFORT:
MODE: HTML / image-only / mixed
REFERENCE FILES / HASHES / VERSIONS:
AUTHORITATIVE ARTIFACT PER SURFACE / STATE:
IMAGE DIMENSIONS / CROP / SCALE / VIEWPORT CONFIDENCE:
COVERAGE: surface | component | observed state | product mapping | status
CONTROLS: observed appearance | specified or unknown behavior | product action
VISUAL CONTRACT: fact / source-measured / image-measured / inferred / unknown
DECISIONS: reference adopted / product UX preserved / hybrid / needs user decision
ASSETS / MISSING ORIGINALS:
MEASURED PARITY / TOLERANCES:
PRODUCT CONTRACTS AND CHECKS:
SNAPSHOT EVIDENCE:
ASSUMPTIONS / ACCEPTED EXCEPTIONS / BLOCKERS:
```

Image-only unknowns should stay explicit. Classify a missing reference property
as an evidence limit rather than leaving a mandatory HTML checkbox unfinished.
A supplied-but-uninspected image relevant to the claim or an unimplemented
requested component is still unfinished work. Merely appearing in a reference
does not bring a component into the implementation scope.

For broad screens, implement and verify component groups before proceeding to
the next group. Preserve evidence across interruptions; reread changed inputs or
new reference versions, and invalidate only affected comparisons. Close against
all active deliverables rather than only the most recently discussed component.

## Maintainer Review Cases

These are expected decisions, not executed browser or model evaluations.

| Request / evidence | Expected interpretation |
| --- | --- |
| Match one button radius exactly from known HTML | Exact + fast if local and isolated; inspect that state/value, compare the region, no all-control tour or ledger. |
| Match one label from a cropped image with unknown scale | Exact within observed scope + fast; inspect image/target, retain uncertainty, no invented CSS dimensions or whole-page claim. |
| Adapt the desktop design to mobile while keeping desktop exact | Split fidelity by surface; verify mobile adaptation and desktop parity without loosening desktop requirements. |
| Use the images only for inspiration | Route to UI/UX design; no claim of reference parity. Keep applicable visual QA/snapshot rules. |
| Do the same exact job faster | Reduce unrelated discovery/notes; preserve acceptance criteria and current comparison evidence. |
| One-line change affects a shared layout or keyboard focus | Escalate by affected contracts/consumers, not line count. |
| Reconstruct a supplied multi-screen interactive flow | Track all requested surfaces/states/actions; do not hide incomplete coverage behind fast mode. |
| Required evidence fails or a mismatch remains | Fix or report the blocker; never silently switch fidelity or enlarge tolerances to pass. |
