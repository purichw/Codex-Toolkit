---
name: ios-app-development
description: Set up, build, run and troubleshoot iOS apps on Mac, especially Expo/React Native with TypeScript and optional Android support. Use for starting a mobile project, checking Xcode and SDK readiness, choosing Simulator versus iPhone, development builds, signing, Metro connectivity, native-module rebuilds, or transferring a repeatable build workflow to a new project. Preserve existing Swift, Flutter or native projects; do not migrate their stack by default. Not needed for an isolated copy/style edit with no build or device issue.
---

# iOS App Development

Turn a new or existing repository into a repeatable edit → build → install →
launch → verify workflow. Teach in the user's language and at their experience
level. This skill carries engineering lessons from DOOTAA, not its eye-detection
criteria, brand, accounts, device identifiers or dependency pins.

## First decision: what is needed now?

- **New project / machine readiness / stack choice:** read
  [setup-and-stack.md](references/setup-and-stack.md).
- **First build / native change / Simulator / physical iPhone:** read
  [build-and-device.md](references/build-and-device.md).
- **Failure / slow builds / storage / feature verification:** read
  [debug-and-verification.md](references/debug-and-verification.md).

Read only the applicable references. A working project's small JS edit does not
need another toolchain audit. A request to teach means small steps with an
expected result; a request to do the work means perform authorized steps and
reserve user actions for things that actually require them.

## Establish the project contract

Before edits, locate the repository and app roots, read its instructions and
build notes, and inspect Git status. Identify the actual package manager,
lockfile, runtime pins, native project ownership, app identity and existing
running dev server. Native folders can be generated outputs or hand-maintained
source: that distinction controls whether prebuild is appropriate.

Preserve the selected stack and product behavior. For a **new** iOS + Android
app without contrary requirements, Expo + React Native + TypeScript is a useful
starting recommendation. Explain alternatives when native SDK needs or an
existing codebase justify them; do not scaffold or migrate merely because this
skill was invoked.

Use installed package source, CLI help and project pins first. Verify changing
requirements with official Apple, Expo, React Native, Android or tool-provider
documentation. A version that worked in DOOTAA is not a universal default.

Optional read-only inventory, using Python 3 and absolute paths:

```sh
python3 /path/to/ios-app-development/scripts/check-environment.py --project /absolute/repository --app apps/mobile
```

Omit `--app` for an app at the repository root. Add `--android` only when local
Android tooling is relevant. The script reports observations and missing tools;
it does not install packages, accept licenses, edit shell configuration, build
an app or certify readiness. A missing PATH entry is not proof of no installation.

## Choose the smallest correct next operation

| Change or request | Next operation |
| --- | --- |
| JS/TS, copy, layout, logic using modules already in the installed binary | Existing Metro + refresh/reload; targeted logic/UI checks |
| JS environment configuration | Check how it is loaded; restart the relevant bundler and reload if needed |
| Native package, native source, config plugin, native permission, launcher icon, compiled splash, entitlements or SDK change | Sync the relevant native inputs and rebuild/install that platform |
| Missing native module in a running app | Compare installed binary with JS dependencies before reinstalling packages |
| Device cannot reach Metro | Check server, client, address, network and permissions before rebuilding |
| TestFlight / App Store / distributable package | Separate signing/distribution workflow, only within the user's requested scope |

Starting Metro does not install a development client. A JS export is not a
native binary. Simulator and device binaries are different. Launching an app
does not prove its camera, storage, audio or real backend works.

## Work without unnecessary interruption

- Continue independent code, typecheck, tests and available UI checks when an
  iPhone is absent or locked. Record the exact physical checks still pending.
- When the phone is needed, prepare the build and a short concrete test first.
  Ask for one bounded action, such as unlock, OS trust, or a specific interaction.
  Do not keep asking the user to repeat a failure without collecting new evidence.
- Obtain current device IDs, scheme, team, bundle ID, port and network address
  from the current project/tools. Never inherit them from another project.
- Use current authorization. Explain any genuinely required user-only step and
  its source; do not add a confirmation to every build. Do not accept legal
  agreements, erase app data, regenerate native directories destructively or
  change signing/security settings as an unexamined troubleshooting step.
- On a constrained Mac, run one native build at a time; two compiler/Metro
  workers are a reasonable starting point to adjust from measured pressure.
  Preserve useful caches and other running tasks.

## Verification and handoff

Match checks to the changed risk. Use project scripts rather than inventing a
test suite. For UI work, use the existing design system, safe areas, keyboard
behavior and real back-stack navigation; keep the immediate task and primary
action visible on the target phone. Consult available UI/mobile skills only
when changing that surface. `native-parity` is the companion for product/data
parity with another platform, not a prerequisite for every build.

Report separately: source checks, bundle/export, native build, install, launch,
and actual feature verification. Mark untested platforms and hardware checks
explicitly. Preserve simulated fixture versus physical observation provenance.

When the setup/build path or remaining verification changes, update the
project's existing build notes with working commands, tool versions,
target/configuration, native ownership, rebuild triggers, environment variable
**names only**, diagnostic-log location and remaining checks. Keep secrets,
personal device identifiers and private user data out of reusable skills.
Do not edit build documentation after an unrelated copy/layout fix.

Close out with what is ready, what was actually checked, and the next smallest
step. Do not call a product ready merely because compilation succeeded.
