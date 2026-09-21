# Debugging and verification

## Locate the failing layer before changing dependencies

| Observed symptom | First discriminating check |
| --- | --- |
| Xcode/SDK/destination unavailable | Developer directory, installed Xcode, first-launch/license status, runtime and current destination list |
| Compile/link failure | First actionable compiler/linker error, failing target, platform/architecture and dependency versions |
| Native module missing at runtime | Is this Expo Go or the expected development client? Does its binary actually include the newly added module? |
| App installs but cannot launch | Device lock, provisioning validity, profile trust, bundle/signing mismatch; keep OS error details |
| App launches but cannot load JS | Correct Metro project/port, current launch URL, reachable phone address and network permission |
| UI appears but interaction fails | Real state transitions, route history, input persistence, async errors and account ownership |
| “Save failed” after camera success | Shutter → returned file → normalization → verification → durable copy → metadata → success UI; identify the first failing stage |
| Preview succeeds but saved image fails | Compare exact captured bytes/geometry/orientation with preview; do not assume equivalent pixels |
| Frame recognition uncertain | Instrument observed evidence and gate reasons; missing data must remain unknown |
| Memory/swap high or build very slow | Concurrent jobs/processes, incremental-cache reuse, free disk and measured pressure before cleanup |

Keep a bounded retry rule: after the same failure recurs without new evidence,
stop repeating the same operation and add diagnostics or change the hypothesis.
Do not ask a person to repeat a physical action indefinitely while guessing.
UIKit/font-service messages alone are not proof of a failed bundle or capture.

## Native APIs, async storage and bundled assets

Inspect the installed SDK's types/source when API behavior matters. In DOOTAA,
assuming copy/move completion before awaiting the installed Expo FileSystem
implementation caused a real save failure. Another app/version may differ;
verify rather than imposing that API assumption universally.

For file-backed features, wait for persistence to complete before checking the
copy or acknowledging durable success. Preserve prior good records on failure,
and test delayed/rejected I/O when touching that boundary. Keep transient preview
state separate from stored truth. Only normalize/re-encode when required by the
consumer; if a decision concerns a particular file, retain that file's provenance
through persistence instead of quietly validating different bytes.

For local native modules/models/frameworks, check both device and Simulator
architecture slices, transitive linkage, deployment target and runtime resource
lookup. Confirm needed files exist in the **built app**, not just source folders.
Pin/checksum acquired binary assets where reproducibility requires it and retain
attribution. Code license, model weights and training-dataset rights are separate
questions; a repository license does not settle all of them.

Capability-check optional native functionality so an older binary fails clearly
instead of showing fabricated success. New native functionality needs a rebuild;
JS reload cannot link missing code or package native resources.

## Verify proportionally

| Evidence | What it proves / does not prove |
| --- | --- |
| Typecheck, lint, targeted unit tests | Source and modeled behavior; no actual sensor evidence |
| JS bundle/export | Bundling; no native linkage or installability claim |
| Simulator native build | Compilation/linkage for that destination; not the physical-device artifact |
| Simulator UI/flow run | Layout, navigation, inputs and supported platform behavior; not camera optics or real-world performance |
| Browser component preview | That renderer/component state only; explicitly distinguish it from native UI |
| Physical install/launch | Binary accepted and app opened; not completion of the requested feature |
| Physical feature test | Only the device, conditions and behavior actually exercised |

For device-dependent changes, prepare a short test with expected observations:
permission allow/deny, main action, saved result/reopen if relevant, background
and resume, and the specific failure being fixed. Select only impacted checks;
do not require a whole-app audit for a one-screen change. If hardware is absent,
complete independent work and retain an explicit pending list.

Camera/audio/haptics/brightness/biometrics/notifications can behave differently
on hardware. Verify the chosen API's actual limitations. Avoid multiple camera
owners or overlapping speech queues; stop/reconcile resource use on navigation,
background and permission loss. Build a visible success signal tied to the real
operation, not merely an animation or timeout.

For native UI, check at the actual small-phone size, with keyboard and relevant
font scaling: safe areas, fixed primary actions, sheets, back/gesture history and
long copy. Test navigation from more than one entry point when back behavior is
changed. Preserve the project's language/font/brand choices; DOOTAA's TH/EN and
Noto Sans are not a universal branding rule.

## Evidence closeout

Say exactly which build/configuration and checks passed, what failed, and what
still needs hardware. Do not turn user feedback into independently labeled
accuracy, or a procedural fixture into real data. For images and diagnostic logs,
use scoped local paths; copy only the needed artifacts, not whole account/device
containers. Do not publish private camera, account, signing or participant data.

Readiness for a local development build, TestFlight and App Store are different
outcomes. Only begin distribution when requested; verify current signing,
entitlements, privacy declarations and platform requirements for that release.
