# Build, install and run

## Identify native ownership and installed CLI behavior

First distinguish:

- **Generated native projects (Expo CNG):** app config, plugins and local modules
  define native inputs. Make durable changes there.
- **Hand-maintained native source:** Xcode/Gradle project files are authoritative.
  Do not run prebuild to overwrite them just because Expo is installed.

For hand-maintained projects, identify the requested config/plugin effect and
apply its documented native changes directly. If generated output is needed to
understand the change, inspect it in an isolated copy, then port only the intended
diff. A non-clean flag does not make prebuild safe for arbitrary manual edits.

Read the installed `expo prebuild --help` before invoking it. Flag defaults have
changed across versions. In DOOTAA's installed CLI 57 on 2026-09-20, `--no-clean`
explicitly layers changes instead of recreating native directories. Some older
documentation describes different defaults. Do not generalize either behavior
to every project; the actual CLI determines the safe invocation.

For generated projects with that supported flag, an example incremental step
from the app root is `pnpm exec expo prebuild --platform ios --no-clean`.
Use the repository's package manager, inspect native edits and generated diffs,
and separate dependency installation when useful. Never regenerate/clean existing
folders destructively without the required authorization and preservation plan.
If a plugin is not idempotent, investigate or use a disposable checkout rather
than repeatedly layering it into the working tree.
[Expo CNG ownership and prebuild](https://docs.expo.dev/workflow/continuous-native-generation/)

For Pods, use `bundle exec pod install` when the repo pins Bundler, otherwise its
documented CocoaPods command. Use the workspace when Pods require it. Do not
run `pod update` or change framework versions as a routine rebuild step.

## Normal development loop

For Expo examples below, run from the confirmed app root and use locally
installed CLI tools; adapt pnpm to the repository's package manager:

```sh
pnpm exec expo run:ios --help
pnpm exec expo start --dev-client
```

`expo run:ios` builds/installs native code; `expo start` serves JS. Reuse the
existing matching Metro process. If building with the CLI, inspect supported
device and no-bundler options to avoid starting duplicate servers. Pure JS
changes usually need no native rebuild; native changes require a new binary.
[Expo local development](https://docs.expo.dev/guides/local-app-development/)

A binary compiled for Simulator cannot be installed on an iPhone, even when
both use ARM64. An archive/distribution build is a separate artifact from a
development `.app`. A development client normally needs its reachable JS server;
a correctly packaged standalone build should be checked without Metro.

## Simulator and explicit local builds

Read-only discovery:

```sh
xcode-select -p
xcodebuild -version
xcrun simctl list runtimes
xcrun simctl list devices available
```

Use the actual workspace/project, scheme and destination. Do not reuse a saved
UUID from another machine. If missing, add a suitable runtime/device via Xcode
within the requested setup scope. Use available computer-use tools for UI actions.

For a constrained Mac, an explicit build can control concurrency. The variables
below must already contain observed project paths/names and the chosen UUID;
`IOS_BUILD_DIR` should be a stable ignored project-owned output directory:

```sh
xcodebuild -workspace "$IOS_WORKSPACE" -scheme "$IOS_SCHEME" \
  -configuration Debug \
  -destination "platform=iOS Simulator,id=$IOS_SIMULATOR_ID" \
  -derivedDataPath "$IOS_BUILD_DIR" -jobs 2 build
```

For a project without a workspace, use `-project` appropriately. Keep build logs
in the project. Preserve the command's real exit status if piping through a
formatter. Do not suppress signing indiscriminately or trust a final log line
without checking the command result and expected artifact.

## Physical iPhone

1. Inspect `xcrun devicectl list devices` and the current Xcode Devices view.
   Obtain the actual device ID and availability; distinguish locked, unpaired,
   disconnected and developer-mode errors.
2. User actions may include unlocking, Trust This Computer, enabling Developer
   Mode, and trusting a developer app profile. Explain the specific prompt that
   was observed. These are separate from app camera/photo permissions.
   [Apple Developer Mode](https://developer.apple.com/documentation/xcode/enabling-developer-mode-on-a-device)
3. Use the project's chosen bundle identifier, capabilities and authorized team.
   Build for `platform=iOS,id=<actual-device-id>` or the appropriate device SDK.
   Do not guess a team, disable signature checks or strip entitlements to hide a
   trust/provisioning failure. A profile can expire separately from its certificate.
4. Inspect installed Xcode's `devicectl ... --help`, then install the **device**
   `.app` and launch its actual bundle ID. Preserve the app's existing data;
   uninstall/reinstall is not a default troubleshooting step.
5. Verify the launch result and actual app content. If OS trust/lock is the
   blocker, ask for that action once after the binary is ready.

Typical commands after substituting confirmed values:

```sh
xcrun devicectl device install app --device "$IOS_DEVICE_ID" "$IOS_DEVICE_APP"
xcrun devicectl device process launch --device "$IOS_DEVICE_ID" "$IOS_BUNDLE_ID"
```

For a development client, use the current CLI-generated launch URL when needed.
Do not copy DOOTAA's scheme, LAN address, team or identifier into another app.

## Metro and network checks

Confirm the matching project is served on the actual port before changing code.
Check `localhost` health on the Mac, then the address the **phone** uses; localhost
on a phone means that phone. USB install does not by itself prove Metro access.
For a LAN workflow, check the reachable interface, same reachable network,
local-network permission, VPN/firewall or Wi-Fi client isolation as indicated.
Do not disable security protections indiscriminately. Use an appropriate tunnel
only when supported and authorized; do not expose private diagnostic files.

## Android companion path

Do this only when local Android work is in scope. Verify SDK path, platform tools,
command-line tools, installed platforms/build tools and emulator architecture.
Read JDK/AGP/Gradle and NDK requirements from the current configuration. An AGP
fallback error is not authorization to replace the project's pinned NDK.
The user completes required licenses. Prefer one emulator at a time on a small
Mac. A diagnostic Gradle command may use `--max-workers=2 --no-parallel` when
pressure warrants it. An iOS build or JS Android export does not prove Android
native readiness.

## Record the successful path

In the project's existing README/build notes, keep: repo/app roots; stack and
runtime pins; native folder ownership; environment variable names; commands for
install, Metro, Simulator, device and relevant tests; rebuild triggers; build-log
location; last evidence by platform; and exact pending hardware checks. Use
placeholders for private team/device values. Do not create a second competing
manual when the project already has a maintained playbook.
