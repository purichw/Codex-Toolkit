# Reference Parity Migration

The active skill is now
[`reference-to-a-tee`](../skills/reference-to-a-tee/SKILL.md), formerly
`claude-to-a-tee`. It reproduces references from any source. Use the user's
selected artifact/version as visual authority and preserve product contracts.

## Modes

| Input | Workflow |
| --- | --- |
| HTML or runnable prototype | Render, inspect source/computed values, and exercise in-scope states. |
| Image files or screenshots only | Inspect originals, calibrate pixels/crop/viewport where possible, and separate observed, measured, inferred, and unknown properties. No HTML is required. |
| Mixed bundle | Resolve authority per surface/state/version; newer user-selected imagery can supersede older HTML. |

All implementation modes use automatic `snapshot` evidence with labeled
Reference and Development views. Image-only parity covers supplied visible
regions/states. Unseen mobile layouts, interactions, font identity, and original
CSS remain assumptions or product decisions, not recovered source facts.

## Fidelity And Effort

The workflow separates what must match from how much verification it needs:

- **Exact:** default for explicit invocation and matching/to-a-tee requests.
  Match requested observable properties; retain honest image uncertainty.
- **Faithful adaptation:** only within user-requested flexibility. Record fixed
  and flexible dimensions; mobile adaptation does not loosen desktop fidelity.
- **Inspiration only:** route to `ui-ux-expert` or `design-direction`, without
  imposing or claiming reference parity.

An isolated exact repair can use a fast pass: inspect relevant reference/target,
make the focused edit, check the property and likely regression, and show one
current contextual Reference/Development pair. No full ledger, extractor output,
all-controls tour, full-page capture, or extra Before column is required by
default. Before/after proof is still required when requested or needed to judge
the change. Broader reconstruction, shared/behavioral changes, and page-level
claims retain the corresponding coverage and required checks.

`efficient-execution` and `snapshot` use the same risk-based distinction. A
reference skill name does not itself trigger deep work. Speed does not authorize
lower fidelity, skipped deliverables, or passing failed required checks. The
[operating guide](../skills/reference-to-a-tee/references/operating-guide.md)
owns the effort matrix, fast path, and eight maintainer decision scenarios.

## Names And Dependencies

| Entry point | Purpose |
| --- | --- |
| `reference-to-a-tee` | Canonical instructions, references, HTML extractor, and tests. |
| `global-reference-to-a-tee` | Repo-maintained global alias to the canonical skill. |
| `claude-to-a-tee` | Compatibility router for old prompts and reference paths. |
| `global-claude-to-a-tee` | Legacy global alias pointing directly to the canonical skill. |

Install the canonical folder whenever installing either compatibility name or a
global alias. The old folder no longer owns implementation instructions.
Do not delete it during routine syncs: existing prompts and commands may use it.
Other skills now route to the generic name; their project-specific instructions
remain owned by those skills.
The former Shane Thai Google Sans exception now lives in
[Shane Thai context](../skills/shane-thai-new-chat/references/new-chat-context.md),
so it is preserved without becoming a global typography rule.

## HTML Helper Compatibility

The canonical command is `reference-to-a-tee/scripts/extract_reference.py`.
It accepts HTML only, defaults to `.design-reference`, and writes
`reference-manifest.json`, `reference-manifest.md`, and
`REFERENCE_TO_A_TEE_WORKLOG.md`. Use a fresh directory for new seeds to preserve
completed notes. Static extraction is inventory, not parity verification.
The helper is optional; use it when it saves discovery for the actual scope,
not as mandatory ceremony for a small repair.

The old command at `claude-to-a-tee/scripts/extract_reference.py` forwards to the
canonical implementation. It retains `.claude-reference` as its default and
also writes `CLAUDE_TO_A_TEE_WORKLOG.md` for old consumers. Existing outputs are
not renamed automatically. Image inputs are rejected with guidance to use the
image workflow. A requested but unavailable rendered probe returns a failure
status and labels any generated output as static inventory only.

## Verification

Run from the repository root:

```sh
python3 -m unittest discover -s skills/reference-to-a-tee/tests -v
python3 scripts/verify_skills.py --expected-count 138
git diff --check
```

The automated tests cover helper behavior and backward-compatible invocation;
the structural verifier does not prove agent judgment or visual matching.
Use these cases when reviewing future workflow edits:

| Scenario | Expected decision |
| --- | --- |
| Desktop PNG, no HTML | Start image mode; inspect/calibrate and compare visible UI without demanding HTML. |
| 2x screenshot or partial crop, unknown viewport | Preserve image units and crop origin; do not equate pixels with CSS pixels or claim full-page parity. |
| Desktop-only image plus mobile requirement | Verify a responsive adaptation; do not claim mobile source fidelity. |
| User-selected newer image conflicts with old HTML | Resolve that surface in favor of the selected image; reuse only still-applicable source values/assets. |
| Still image with tabs, save icon, or hidden panel | Record unknown reference behavior; preserve/specify actual product actions without inventing backend scope. |
| Runnable HTML with nested states | Inspect authoritative source geometry and controls/states affected or requested by the task; reconstruction covers the agreed flow. |
| Legacy prompt or extractor command | Route to canonical guidance and preserve old CLI outputs; never restore the old screenshots-alone prohibition. |

Behavioral confidence still requires use on a real reference and rendered target;
do not report this scenario review as a completed UI benchmark.
