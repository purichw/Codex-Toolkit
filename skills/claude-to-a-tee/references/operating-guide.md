# Operating Guide

Use this as the fast read path after `SKILL.md`. It preserves the strict
Claude-to-a-tee gate while keeping phase-specific details out of the front door.

## Quick Read Path

- **Scoping or asking what to do:** read this file and
  [reference-workflow.md](reference-workflow.md).
- **Implementing from offline Claude HTML:** read this file,
  [reference-workflow.md](reference-workflow.md), and
  [product-contract.md](product-contract.md) before editing.
- **Multi-screen, auth/admin, production, or handoff-declared behavior:** read
  all reference files before editing.
- **Verification, commit, push, deploy, PR, or handoff:** read
  [verification-checklist.md](verification-checklist.md) and
  [release-gate.md](release-gate.md) before claiming completion.

If the task touches live product behavior, hidden states, responsive layout,
auth, persistence, or release readiness, choose the larger read path.

## Do Not Read Yet Markers

These markers are for context discipline, not for skipping requirements:

- Do not load the full verification checklist during quick scoping unless the
  task is already about verification or release.
- Do not load product-contract details for a pure reference inventory, but load
  them before mapping Claude controls into product code.
- Do not load release-gate details until verification or release pressure
  appears, but load them before any claim of done, commit, push, deploy, PR, or
  handoff.

## Operating Loop

1. Confirm the newest user requirement and any supplied Claude HTML,
   screenshots, handoff notes, and assets.
2. Run the reference extractor when offline HTML is available, unless the task
   is a tiny single component or the helper cannot run.
3. Render the Claude reference, visit every reachable page/screen/state, and
   click every visible control; record static/no-op outcomes instead of
   guessing behavior.
4. Build or update the coverage ledger, controls ledger, route manifest, asset
   inventory, and parity table seed.
5. Map Claude visual components to product-owned files, data paths, actions,
   permissions, and tests.
6. Produce a decision and risk ledger before edits: what follows Claude, what
   preserves current product UX, what becomes hybrid, why, verification, and
   risk.
7. Implement component-level parity while preserving product-owned behavior; do
   not invent animation or interactions just because Claude is static.
8. Measure reference vs implementation with rendered screenshots, computed
   geometry, responsive states, interactions, and browser evidence.
9. Apply the release gate before claiming done or shipping.

## Worklog Shape

Keep a compact worklog during implementation:

```text
REFERENCE FILES:
REFERENCE HASHES:
SOURCE OF TRUTH ORDER:
COVERAGE LEDGER:
CONTROLS LEDGER:
ROUTE COMPONENT MANIFEST:
COMPONENT CONTRACTS:
DECISION LEDGER:
PRODUCT MAPPING:
PRODUCT UX PRESERVED:
BEHAVIOR EXCEPTIONS:
VISUAL EXCEPTIONS:
MEASURED PARITY TABLE:
INTERACTIONS VERIFIED:
RESPONSIVE VIEWPORTS:
TESTS:
BLOCKERS BEFORE RELEASE:
```

The extractor creates `CLAUDE_TO_A_TEE_WORKLOG.md` as a starting worklog, but
every row remains `not done` until the rendered reference, product mapping,
implementation, and release-gate verification prove it.
