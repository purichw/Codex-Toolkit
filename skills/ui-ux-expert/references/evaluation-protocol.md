# Evaluation Protocol

Use when changing this skill materially, investigating recurring failures, or
explicitly benchmarking it. Do not run the suite for ordinary UI edits.

## What Exists And What It Proves

[cases.json](../evals/cases.json) contains eight synthetic scenarios, not real
customer cases or observed results. They exercise diagnosis, tradeoffs,
contextual rules, alternative selection, and evidence discipline. They need the
listed fixtures before a rendered evaluation can run. Three narrow runnable
fixtures now cover dashboard, bilingual mobile form, and editorial work; the
other scenario setups still need preparation. No human scores or agent A/B
results are bundled; generalized performance remains unmeasured.

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
Omitting rubric text from a prompt is not isolation when the solver can read it
on disk. The preparation tool below excludes evals, reviewer criteria, authored
repair CSS and earlier outputs. Links to excluded evaluation resources are converted
to explicit omission notes and recorded in the preparation manifest; runtime
design guidance is retained. Mount only this prepared workspace in an
authorized isolated runner; sibling folders on a full-access machine are NOT a
security boundary. Keep the reviewer outside it. Human reviewers may inspect
criteria after judging outputs.
Use only authorized evaluation resources; this protocol does not authorize new
tasks, paid model runs, production actions, or importing private project data.

## Local Render And Fixture Commands

Requirements: Python 3.10+, Node.js, Playwright, and installed Chrome or a browser
path in CHROMIUM_BIN. Use existing bundled/runtime dependencies when available.
OUT paths below are examples and must be new, outside the skill/input folder.
No dev server is needed for these standalone local HTML fixtures.

```sh
node evals/gallery-check.cjs . /absolute/new/gallery-evidence
node evals/fixture-check.cjs evals/fixtures /absolute/new/fixture-before --record-baseline
node evals/fixture-check.cjs evals/fixtures /absolute/new/fixture-demo --calibration evals/calibration.css
python3 evals/prepare.py --skill-root /absolute/baseline/ui-ux-expert --case dashboard --out /absolute/new/baseline-solver
python3 evals/prepare.py --skill-root /absolute/candidate/ui-ux-expert --case dashboard --out /absolute/new/candidate-solver
```

Repeat preparation for mobile-form and editorial when evaluating those domains.
For a real agent run, use its prepared TASK.md and equal model/instructions/tools/
budget, then run fixture-check.cjs on the resulting app directory WITHOUT
--calibration. The runner stays outside the solver workspace. It checks all
fixtures; compare the chosen case and retain untouched cases as controls. Do not
let unrelated fixture failures alter the predeclared acceptance scope.

Gallery checks cover 1280x800, 768x1024, 390x844 and 320x800, default and long-copy
states. Fixture checks cover 1280x800, 390x844 and 320x800: filtering/action
feedback, invalid email/input retention/focus, and editorial content/bitmap.
Reports contain hashes, browser/version, measurements/checks and captures.
Open images yourself; the runner intentionally leaves them unreviewed.

--record-baseline records known failures without making the process fail;
the report still lists them. Never use it to pass a candidate or release gate.
--calibration injects AUTHOR-WRITTEN repair CSS into the same fixtures. This is
a teaching demonstration, not a solver output, A/B trial, or behavior proof for
production components. Gallery controls remain mostly static.

## Evidence Integrity Contract

[../evals/evidence.py](../evals/evidence.py) checks an independently fixed matrix
against current sources and a capture manifest. Minimal matrix:

```json
{
  "schema_version": 1,
  "source_files": ["screen.html", "screen.css"],
  "required": [{"id": "phone-error", "route": "/settings", "viewport": [320, 800], "state": "error", "checks": ["input-retained"]}]
}
```

The manifest has schema_version and captures. Each capture needs the same id,
route/viewport/state, relative PNG file, sha256, source_hashes for the complete
matrix source set, checks mapping required names to passed/failed/blocked/not_run,
and review with nonempty reviewer and note. Freeze the matrix before capture;
include all relevant sources/assets, not just the file last edited.

```sh
python3 evals/evidence.py --matrix /path/matrix.json --manifest /path/manifest.json --source-root /path/source --evidence-root /path/captures
```

The gate rejects missing states/files, stale source/image hashes, wrong routes/
viewports/states, absent review, path escapes, and non-passing required results.
Passing means metadata integrity only: it cannot choose adequate requirements,
decode design intent or prove reviewer honesty. Negative unit tests demonstrate
rejection; they do not establish taste. Keep visual/behavior/human layers separate.

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
