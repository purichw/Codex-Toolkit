# Design Judgment And Completion Gates

This update changes the live skills and their archive copies without renaming
`ui-ux-expert`. It is scoped to six canonical skills; unrelated local updates
are not part of this sync. Existing global aliases still delegate to canonical
skills and need no separate implementation of these rules.

## UI/UX Expert: Five Additions

1. Cause-directed diagnosis: symptom, candidate cause, discriminating check,
   targeted fix, expected result, and regression evidence.
2. Conflict resolution: preserve requirements and product contracts, state
   material tradeoffs, and distinguish visual authority from behavior authority.
3. Contextual rules: applicability, exceptions, multilingual/content constraints,
   observable checks, and provenance instead of universal pixel/count targets.
4. Selective alternatives: compare a few feasible structures for consequential
   design decisions, implement one, and skip the ceremony for micro edits or
   faithful reference implementation.
5. Evaluation: eight synthetic scenarios, a matched baseline/candidate protocol,
   independent human comparison, and an explicit separation of static, browser,
   and human evidence.

Entry point: [ui-ux-expert](../skills/ui-ux-expert/SKILL.md).
Detailed decisions: [design judgment](../skills/ui-ux-expert/references/design-judgment.md).
Rule applicability: [contextual rules](../skills/ui-ux-expert/references/contextual-rules.md).
Evaluation: [protocol](../skills/ui-ux-expert/references/evaluation-protocol.md).

The specialist source manuals remain intact. The local interpretation layer
qualifies their example values; the learning brief now identifies existing
specialist coverage separately from missing real-world evidence. No claim of
improved taste follows from adding instructions or passing structural tests.

## Related Skill Changes

| Skill | Changed contract |
| --- | --- |
| [release-gate](../skills/release-gate/SKILL.md) | Map every active deliverable to acceptance/evidence. Failed, blocked, pending, or unrun required checks block the relevant gate. A push needed to start CI is not whole-task completion. |
| [uat-environment](../skills/uat-environment/SKILL.md) | Promotion needs all pre-promotion acceptance evidence, passed required checks, current served build, isolated data, appropriate auth, and recovery. Post-deploy checks remain required after authorized promotion. |
| [design-direction](../skills/design-direction/SKILL.md) | Image-only handoffs are valid. Label scale, missing states, and adaptations; establish authority for mixed inputs rather than demanding HTML for every screen. |
| [rollback-guardrail](../skills/rollback-guardrail/SKILL.md) | Pause/discussion and understood reversible edits do not require a checkpoint. Risky work loss requires exact impact/authorization, recoverable files/data, and verification. Stricter project approval rules still apply. |
| [korat-tan-phai-shared-components](../skills/korat-tan-phai-shared-components/SKILL.md) | Automatically use snapshot for visible work, plus browser behavior checks for changed interactions. Capture blockage is unverified, not a build-only visual pass. |

Korat shared-components is newly archived, bringing the archive to 130 skills:
75 personal folders, 53 global aliases, and 2 standalone global design specs.
Do not infer that other live-only skills have also been archived.

## Verification And Limits

```sh
git diff --check
python3 scripts/verify_skills.py --expected-count 130
python3 skills/ui-ux-expert/evals/validate.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skills/ui-ux-expert/evals/tests -v
```

The 11 unit tests cover malformed packs, duplicate IDs, focus coverage, real-case
provenance notes, missing files, unknown cases, and solver/reviewer separation.
The helper emits task briefs; it does not run a model or score screenshots.

Maintainer contract-review cases (review the instructions, not a live deployment):

| Situation | Required interpretation |
| --- | --- |
| Highest-risk test passes but requested docs/artifact is missing | Task incomplete; finish or report the blocker. |
| A required check fails and is disclosed | Gate blocked; disclosure is not a pass. |
| Push starts required CI | Confirm push endpoint, keep required CI pending; no merge-ready claim. |
| UAT URL is unchanged but served build changed | Refresh affected evidence; URL equality is insufficient. |
| Only a desktop PNG exists | Accept it; label mobile behavior as adaptation and scale as unknown unless calibrated. |
| User pauses with work in progress | Stop and preserve work; do not checkpoint or discard merely because of the pause. |
| Requested one-token CSS adjustment | Scoped reversible path, targeted visual evidence; no broad benchmark/checkpoint. |
| Delete a file, remove an integration, or overwrite uncertain ownership | Risky path and exact approval under applicable project rules. |
| Standalone handoff is the entire requested artifact | Verify that artifact, not an unrequested live integration. |
| Korat screenshot capture is unavailable | Explain blockage and remaining visual risk; no visual pass from build output. |

Rendered baseline/candidate runs and independent human review have not been
performed by these static checks. No real project screenshots were imported.
Use the evaluation protocol with authorized fixtures to gather that evidence.
