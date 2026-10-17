# Native evidence tooling — optional, local, not a quality judge

Use an existing project runner when it already captures the right native states. The bundled Python
helper is a small fallback. It does **not** install SDKs, build/install apps, navigate flows, select
correct fixtures, recognize the screen, inspect images, or verify true build provenance. It never
reports “beautiful” or “native behavior passed.” Python 3.10+ standard library only.

## Preflight

```sh
python3 scripts/native_evidence.py preflight
```

This reports host/tool presence without running SDKs or touching a device. For actual work identify
OS/device, available build/test commands, and an image viewer/vision reviewer. Android capture requires
an authorized explicit `adb` device. iOS capture requires a booted Simulator with `xcrun simctl`; physical
iPhone screenshots can be attached from an existing capture workflow instead. Confirm local CLI syntax.

## Plan and initialize

Copy `templates/evidence-plan.example.json` outside the installed skill, edit **all** REPLACE values,
and keep only relevant variants/cases. Record actual logical dimensions separately from pixel size.
Use an immutable data/fixture identity and a build identity that includes source/dirty changes, assets,
locks and any JS/Dart update. Initialize a **new** folder per build; never overwrite an earlier run.

```sh
python3 scripts/native_evidence.py init --plan /path/to/plan.json \
  --out /path/to/review/build-001 --build-id 'actual-build-source-bundle-id'
```

The helper freezes the plan and hashes it. The build ID is operator-declared, not cryptographically
attested against the installed app. CI/reviewer installation logs are needed for stronger provenance.

## Capture one state

Build/install through your normal tooling, enter the declared state with the declared fixture, wait
for that state's readiness, and verify the app/build. Then explicitly authorize capture:

```sh
python3 scripts/native_evidence.py capture --run /path/to/review/build-001 \
  --case android-form-keyboard --observed-build-id 'actual-build-source-bundle-id' \
  --confirm-ready
```

Every attempt is retained, including failures. The script uses explicit device IDs and no shell
interpolation. It captures the full display; it cannot tell whether the keyboard/screen/data are
actually right. Do not disable screenshot protection, access controls or user privacy to make it work.
Use synthetic/test data. `adb` can start its normal local server as part of a requested capture.

For a genuine native screenshot captured by another tool (e.g. physical iPhone):

```sh
python3 scripts/native_evidence.py attach --run /path/to/review/build-001 \
  --case ios-form-default --file /path/to/actual-native.png \
  --observed-build-id 'actual-build-source-bundle-id' \
  --provenance 'Captured from test device/build using the existing project runner'
```

This copies the file and labels provenance **operator-declared**; it cannot authenticate it. Never use
this command to relabel a browser screenshot, illustration or mock as native evidence.

## Inspect, record a judgment, and check coverage

Open the image. Review the actual state, context and relevant neighbors using [visual review](visual-review.md).
After inspecting, record a useful reason, not a generic score:

```sh
python3 scripts/native_evidence.py review --run /path/to/review/build-001 \
  --case android-form-keyboard --reviewer 'human-or-agent-name' \
  --verdict acceptable --notes 'Describe what was inspected and what remains untested.'
python3 scripts/native_evidence.py check --run /path/to/review/build-001 --require-reviewed
```

Allowed recorded verdicts: `acceptable`, `needs-repair`, `indeterminate`. A CLI flag cannot prove that
an image was understood or even opened. The checker verifies plan/hash/file consistency, required
captures and recorded review coverage only. A recorded acceptable judgment is not independently verified.
It refuses missing/stale/corrupt records but a malicious operator can fabricate self-consistent evidence.
For stronger review, an independent runner must capture the final build and a human must inspect it.

Exit codes: 0 = requested structural/coverage checks complete; 1 = invalid input/integrity/tool failure;
2 = missing capture or requested review, or latest recorded judgment still needs repair/indeterminate.
The `check` JSON keeps `visual_quality` and `native_behavior` as `not_assessed_by_checker`.

## Native interaction and assistive tests

Use the project's XCTest/XCUIAutomation, Android instrumentation, native RN E2E, Flutter integration
tests, or existing manual test workflow. Log actual commands/results and scenario-specific observations.
The helper only handles still-image capture and records; it has no general UI-driving or video API.
Keep behavior videos/traces and assistive-use results next to the run with references in the review.
Required dynamic checks remain required even when every still capture is present.

## No native runtime available

Deliver the scoped implementation/spec and explicit PARTIAL/BLOCKED checks. Continue useful work but
never substitute a web preview as native validation. Do not invent device IDs, build successes, native
screenshots or voice/touch test outcomes. Sources for capture tooling: [D5, A6](sources.md).

Use one writer per run directory; atomic metadata writes are not a concurrency lock. Do not run parallel captures/reviews into one manifest.
