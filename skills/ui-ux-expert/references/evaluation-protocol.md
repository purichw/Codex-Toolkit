# Evaluation Protocol

Use when changing this skill materially, investigating recurring failures, or
explicitly benchmarking it. Do not run the suite for ordinary UI edits.

## What Exists And What It Proves

[cases.json](../evals/cases.json) contains eight synthetic scenarios, not real
customer cases or observed results. They exercise diagnosis, tradeoffs,
contextual rules, alternative selection, and evidence discipline. They need the
listed fixtures before a rendered evaluation can run. No before/after UI assets
or human scores are bundled; the baseline performance is unmeasured.

[validate.py](../evals/validate.py) validates the scenario pack and emits a task
brief without its review rubric. It does not call a model, render a UI, inspect
pixels, or judge taste. Structural checks passing only means the pack is usable.

From this skill directory:

```sh
python3 evals/validate.py
python3 evals/validate.py --case crowded-admin
python3 evals/validate.py --review-case crowded-admin
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s evals/tests -v
```

Use the emitted task brief with only its raw, prepared fixtures for the solver.
Keep the reviewer rubric separate; do not supply the intended solution or a
pre-filled critique. Human reviewers may inspect criteria after judging outputs.
Use only authorized evaluation resources; this protocol does not authorize new
tasks, paid model runs, production actions, or importing private project data.

## Matched Baseline And Candidate

1. Select a few affected cases plus a counterexample. Freeze the task, starting
   source, content, assets, viewports/states, and allowed tools before either run.
   Hash source/fixtures, reference images, the skill entrypoint, and supporting
   references. A renamed skill or a matching Git commit alone is not a baseline.
2. Record baseline and candidate skill revisions, model/version, available
   skills/instructions, environment, and effort budget. Change only the skill
   under evaluation when possible. Otherwise record confounders and narrow the
   conclusion. Prevent previous output or reviewer hints from leaking between
   runs; do not overwrite the user's installed skill to simulate the baseline.
3. Run in isolated authorized workspaces with equal scope and fixture access.
   Prepare fixtures once, not differently per candidate. If a fixture is absent,
   mark the rendered evaluation blocked; a text-only answer tests planning only.
4. Capture original and final surfaces with `$snapshot`, using matching route,
   viewport, zoom, content, auth state, and font/asset readiness. Keep filenames,
   hashes, and build identity. Store full context as well as useful detail crops.
5. Exercise the task and likely regressions. Record each required check as
   passed, failed, blocked, or not run, with raw evidence. Report capture failures
   honestly; do not substitute planned assertions for executed browser checks.
6. Label outputs A/B without revision names for an independent human comparison.
   Review task fit, visual hierarchy, content handling, interaction/recovery,
   brand/reference fidelity, and scope/cost. Allow ties and "insufficient evidence".
   Record reasons tied to observations; do not fabricate reviewer identity.
7. Reveal revisions after review. Report per-case wins, ties, regressions, and
   uncertainty. An agent critique is provisional, not an independent human
   verdict. One preferred screenshot or falling checklist count does not prove
   general improvement, user satisfaction, conversion, or task completion speed.

## Split The Evidence

| Layer | Appropriate checks | Cannot establish |
| --- | --- | --- |
| Python/static | Pack shape, local links, script syntax, evidence file/hash integrity where recorded. | Visual quality, working controls, compliant rendered accessibility. |
| Browser/device | Relevant overflow, geometry, focus/keyboard, state transitions, retained input, network/assets, actual screenshots. | Human comprehension, taste, or efficiency from a single run. |
| Human comparison | Contextual hierarchy, tradeoffs, brand fit, paired preference with reasons. | Generalized user outcomes without suitable participant/task evidence. |

Do not collapse these layers into a single "expert score". Required functional
or accessibility regressions block accepting a candidate even if it is prettier.
Missing evidence stays missing. Keep unchanged checks reusable when their actual
source/environment conditions match; do not repeat every test by habit.

## Record Template

Keep results in an authorized evaluation folder or existing project notes, not
the reusable skill package by default. No scored result file is pre-populated.

```text
Case / provenance: synthetic or sanitized-real
Task / acceptance criteria:
Fixture/source/reference hashes and skill revisions:
Model / instructions / budget / environment / confounders:
Original and final artifact paths / hashes / route / viewport / state:
Required check -> terminal result -> evidence:
Human reviewer / date / A-B masking: or not reviewed
Verdict: A preferred / B preferred / tie / insufficient evidence
Observed reasons / regressions / untested outcomes:
Decision: adopt / revise / needs evidence
```

## Grow A Real Case Library

After authorized project work, propose reusable lessons from actual recurring
defects. Obtain permission before copying screenshots/content across project
boundaries; remove private data and retain artifact provenance. A sanitized case
should retain realistic text lengths, data distributions, and task constraints.

Store paired original/final captures, the narrow source diff, required check
results, the accepted tradeoff, and where the fix would be wrong. Synthetic
illustrations must stay labeled synthetic and must not be called client evidence.
User feedback can support a recorded preference, not an invented usability study.

Update the owning specialist or applicability rule when evidence warrants it.
Keep unverified hypotheses marked, avoid overfitting all rules to the benchmark,
and reserve fresh cases for later review. Lessons only persist when explicitly
recorded; completing a task does not automatically train the model.
