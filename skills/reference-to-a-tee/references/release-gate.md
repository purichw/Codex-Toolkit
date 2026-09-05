# Reference Parity Release Gate

Apply before claiming the requested implementation complete, or before an
authorized commit/push/deploy/handoff of that implementation. Skill-documentation
maintenance itself uses structural validation and scoped review, not fictional
UI snapshots. Use `$release-gate` for the requested publishing action.

## Mode-Aware Evidence

| Mode | Sufficient reference evidence |
| --- | --- |
| HTML | Relevant source rendered and inspected, authoritative computed values recorded, required reachable states exercised. |
| Image-only | Actual images inspected, visible regions/states inventoried, dimensions/crop/calibration/confidence recorded, equivalent implementation captures compared. |
| Mixed | Per-surface authority resolved, with the applicable HTML or image evidence for each row. |

The rendered implementation and `$snapshot` reference/development comparison are
required for visual implementation claims. Image-only reference DOM/CSS, unseen
states, and unprovided breakpoints are not mandatory evidence. Record those
limits and any inferred adaptation; do not claim they were recovered or verified.

## Completion Conditions

- All active requested deliverables and observed in-scope components are mapped,
  implemented, and verified; no silent subset or uninspected supplied reference.
- The before-edit decision ledger explains preserved/hybrid product contracts,
  evidence, risks, and visual exceptions. Existing accepted decisions apply.
- Measurements and comparisons use the correct source version, route, state,
  data/auth, viewport/crop/scale, and implementation source/build.
- Image bounds are not mislabeled CSS pixels without calibration. Supplied crops
  do not stand in for full-page proof. Unknowns do not conceal visible mismatches.
- There are no unresolved critical mismatches or `not done` rows within required
  observed coverage. Material accepted visual exceptions remain explicit.
- Required interactions and preserved product contracts pass focused checks,
  including stored/reloaded results, permissions, focus, and scroll when touched.
- Required responsive views are usable without overlap, clipping, or unintended
  horizontal overflow. Label unsupported reference parity as adaptation.
- Required assets load; unavailable originals or substitutions are documented.
  Inert demo controls and unexplained broken media are not acceptable substitutes.
- Relevant checks have terminal results. Failures or missing required verification
  block a success claim; disclosure alone does not make them pass.

If only unknown source properties remain outside the agreed acceptance criteria,
complete the observed scope and report limits. If a required claim cannot be
verified or a material decision is unresolved, continue independent work and
report the exact blocker. Do not demand HTML simply to satisfy an image task.
Do not broaden work or add approval steps where the user already authorized the
decision. Publish only within the user's authorization; if the user explicitly
accepts shipping with listed mismatches, retain those exceptions in the report.

## Publishing And Deployed Verification

For commit or push, verify intended scope, branch, checks, and the resulting
commit/remote state. Do not require deployment evidence for a commit-only task.
For an authorized deployment, verify the changed surface on the intended URL
and build, including the appropriate authenticated state, geometry, primary
interaction, runtime errors, overflow, and changed media. Match the required
viewport coverage to the release risk. Use `$production-asset-smoke` when assets
changed; HTTP 200 or a login screen alone is not deployed UI evidence.

## Working Self-Check

```text
MODE / REQUESTED SCOPE:
REFERENCE INSPECTED: identities, states, and HTML render or image inspection
AUTHORITY: artifact per conflicting surface/state
IMAGE CALIBRATION: dimensions, crop, scale/viewport confidence, or not applicable
APP RENDERED: URL, source/build, state, viewport
DECISIONS / PRESERVED CONTRACTS:
COVERAGE / MEASURED PARITY / TOLERANCES:
SNAPSHOT: Reference and Development
FUNCTIONAL CHECKS / TERMINAL RESULTS:
ASSUMPTIONS / UNKNOWN SOURCE PROPERTIES:
ACCEPTED VISUAL EXCEPTIONS / BLOCKERS:
PUBLISHING RESULT / DEPLOYED CHECKS, when requested:
```

Report verified visual coverage separately from functional verification and
inferred responsive or interaction decisions. Do not claim unobserved behavior,
exact original CSS, or all-viewport pixel parity from a finite set of images.
