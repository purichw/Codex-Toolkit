# Operating Guide

Start by recording the requested outcome and choosing HTML, image-only, or mixed
mode. Scope discovery to the affected surface and its direct dependencies.
Account for all requested work without treating every reference file as a request
to implement the entire product.

## Read Path

- HTML inspection: [reference-workflow.md](reference-workflow.md).
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

Use one compact ledger or an existing project note; split it only when size makes
it easier to maintain. The HTML extractor produces a seed, not completed evidence.

```text
REQUESTED DELIVERABLES AND STATUS:
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
A supplied-but-uninspected image or an observed-but-unimplemented component is
still unfinished work.

For broad screens, implement and verify component groups before proceeding to
the next group. Preserve evidence across interruptions; reread changed inputs or
new reference versions, and invalidate only affected comparisons. Close against
all active deliverables rather than only the most recently discussed component.
