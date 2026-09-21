# Setup and stack selection

## Inspect before installing

For an existing repository, inspect instructions, package manifests/lockfile,
`.nvmrc` or equivalent, Expo config, native workspace/project, Podfile/Gemfile,
Gradle wrapper and existing build notes. Do not execute arbitrary app config
just to discover facts when static files suffice. Preserve local changes.

For a new project, resolve only consequential unknowns: target platforms,
required device APIs, existing backend/design, distribution needs, and whether
the user wants guided steps or execution. Start with a small running vertical
slice before adding packages for hypothetical features.

| Context | Starting recommendation |
| --- | --- |
| New iOS + Android app with shared UI/domain logic | Expo + React Native + TypeScript; development build when native capability is required |
| Existing Swift/SwiftUI app | Keep Xcode/native architecture; no Node/Expo requirement unless its own tooling needs them |
| Existing Flutter or bare React Native app | Follow its current build system; do not run Expo prebuild over native source |
| iOS-only, deeply Apple-specific product | Consider Swift/SwiftUI alongside team experience and future Android requirements |
| No suitable Mac for local iOS compilation | Explain a supported cloud-build path and its account/network requirements; do not claim local Simulator support |

Expo Go can help an initial experiment within its included capabilities. A
development build is the app's own native runtime and supports custom native
modules; installing its JS package alone does not put it on a phone.
[Expo development builds](https://docs.expo.dev/develop/development-builds/introduction/)

## Readiness checklist: required versus optional

| Component | Check and implication |
| --- | --- |
| Mac / macOS / architecture | Detect architecture and available disk/RAM; choose Apple Silicon or Intel downloads accordingly. Check Rosetta if a tool reports a different architecture |
| Xcode | Full Xcode is needed for local iOS native builds; Command Line Tools alone are insufficient. Inspect selected developer directory and Xcode version |
| First launch and license | User completes any required Xcode agreement/setup. Do not silently run a license-accept command |
| iOS SDK and Simulator runtime | SDK/toolchain comes through Xcode; an appropriate Simulator runtime may need installation in Xcode Settings. Check what's already present before downloading |
| Node / package manager | Required for Expo/RN, not inherently for Swift. Match repo engines/runtime pin and `packageManager`/lockfile; for a new app verify a supported LTS |
| TypeScript | Project dependency for a TS app; no global TypeScript installation is required |
| CocoaPods / Ruby | Use project Gemfile/Bundler if present. Use the selected stack's supported version; do not start with `sudo gem install` or replace system Ruby |
| Android Studio / SDK / JDK | Needed for local Android builds, not an iOS-only check. Read AGP/Gradle/Expo requirements before choosing JDK, SDK, build tools or NDK |
| Apple account / signing | Required as appropriate for physical device provisioning and distribution; Simulator success does not demonstrate signing readiness |

Current setup sources: [Expo environment](https://docs.expo.dev/get-started/set-up-your-environment/),
[React Native environment](https://reactnative.dev/docs/set-up-your-environment/),
[Expo iOS Simulator](https://docs.expo.dev/workflow/ios-simulator/).
Follow links for the chosen platform and currently installed versions rather
than copying old SDK numbers into a new project.

## Minimal project bootstrap

For an authorized new app, choose an unused destination and a current official
template that supports the selected SDK/TypeScript workflow. Record the chosen
SDK and dependency pins after creation. Never use a template reset on an existing
product. Do not mix npm/yarn/pnpm lockfiles.

For a clone, use the existing lockfile's frozen/immutable installation mode.
If it fails, inspect package-manager version, branch and manifest consistency;
do not delete the lockfile to force success. In an Expo app, use its installed
CLI's `expo install` for compatible native package versions, and inspect diffs.
Do not install every available app library at setup time.

Prefer a project script or current-shell toolchain activation. Do not modify
the user's shell dotfiles or global SDK selection without applicable authority.
When two Xcode installations exist, a command-scoped `DEVELOPER_DIR` can isolate
a build without changing all other projects.

Before feature development, establish the app ID/scheme for the new project,
one launchable screen, navigation, fonts/assets, permission behavior for actual
features, and a reproducible run command. Android support means a real Android
build/test path eventually, not only shared TypeScript.

## Keep Xcode and the machine manageable

Use one required iOS runtime and a small set of useful Simulator devices first;
watchOS/tvOS/visionOS are unnecessary unless targeted. Reuse project build caches.
Measure disk usage before proposing cleanup; identify exact paths and preserve
archives, signing assets and app data. Never use broad cache deletion, Simulator
erase or app uninstall as routine setup.

DOOTAA's Node 24 / JDK 17 and two-worker limit were local project choices, not
requirements of this skill. In particular, missing Java must not block an
iOS-only or JS-only task.
