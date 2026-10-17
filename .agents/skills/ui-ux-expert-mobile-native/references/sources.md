# Source registry and evidence boundaries

Retrieved/checked: **2026-10-17**. These are source pointers and brief paraphrases, not bundled copies of official documentation.
Verify exact APIs and changed platform policies against the project's pinned versions before implementation.
The design diagnosis/repair workflow is an authored synthesis, not a claim that official docs certify its taste.

| ID | Primary source | What was actually accessible |
| --- | --- | --- |
| C1 | [Codex skill format, discovery, invocation and optional metadata](https://learn.chatgpt.com/docs/build-skills) | Read current official documentation; use installed-version behavior if it differs. |
| A1 | [Apple UI Design Dos and Don’ts](https://developer.apple.com/design/tips/) | Read; includes 44 pt hit-target guidance. Do not turn its lowest text-size example into a body-text default. |
| A2 | [Apple HIG: Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) | HTML shell; content read via official JSON endpoint https://developer.apple.com/tutorials/data/design/human-interface-guidelines/accessibility.json |
| A3 | [Apple HIG: Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets) | Content read via official JSON endpoint https://developer.apple.com/tutorials/data/design/human-interface-guidelines/sheets.json |
| A4 | [Apple HIG: Typography](https://developer.apple.com/design/human-interface-guidelines/typography) | Content read via official JSON endpoint https://developer.apple.com/tutorials/data/design/human-interface-guidelines/typography.json |
| A5 | [Apple XCUIAutomation](https://developer.apple.com/documentation/xcuiautomation) | HTML shell available; exact API content not retrieved. Verify against installed Xcode before code changes. |
| A6 | [Apple: Capturing screenshots and videos from devices](https://developer.apple.com/documentation/xcode/capturing-screenshots-and-videos-from-devices) | HTML shell available; command details require local simctl help. Helper path is unit-tested with mocks, not on an Apple runtime. |
| D1 | [Android Compose accessibility API defaults](https://developer.android.com/develop/ui/compose/accessibility/api-defaults) | Read; touch targets, expanded hit regions, semantics and decoration. |
| D2 | [Android core app quality guidelines](https://developer.android.com/docs/quality-guidelines/core-app-quality) | Read; use relevant task/state/target-device checks, not an unbounded checklist. |
| D3 | [Android predictive Back support](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture) | Read; verify implementation against actual OS/target SDK/navigation library. |
| D4 | [Android window insets](https://developer.android.com/develop/ui/compose/system/insets) | Read; actual toolkit/inset ownership must be inspected in the app. |
| D5 | [Android Debug Bridge](https://developer.android.com/tools/adb) | Read; supports explicit device selection and exec-out screencap -p. No device was available here. |
| R1 | [React Native accessibility](https://reactnative.dev/docs/accessibility) | Read; match docs to the project version, not the moving default docs. |
| R2 | [React Native KeyboardAvoidingView](https://reactnative.dev/docs/keyboardavoidingview) | Read; verify platform-specific behavior rather than copy one universal configuration. |
| R3 | [React Native testing overview](https://reactnative.dev/docs/testing-overview) | Read; JavaScript/component tests are distinct from native end-to-end behavior. |
| E1 | [Expo development builds](https://docs.expo.dev/develop/development-builds/introduction/) | Read; development builds, native configuration, and local toolchains. No Expo account or service is required by this package. |
| F1 | [Flutter adaptive and responsive design](https://docs.flutter.dev/ui/adaptive-responsive) | Read; adaptation is not simply shrinking a layout. |
| F2 | [Flutter SafeArea and MediaQuery](https://docs.flutter.dev/ui/adaptive-responsive/safearea-mediaquery) | Read; verify constraints/insets with the actual app. |
| F3 | [Flutter testing overview](https://docs.flutter.dev/testing/overview) | Read; testing levels differ in scope. Pair native accessibility checks with platform sources. |
| F4 | [Flutter integration tests](https://docs.flutter.dev/testing/integration-tests) | Read; native integration tests need an app/device. Not compiled or exercised here. |

## What was not verified

- No native SDK/device, Codex execution, native screenshots, accessibility session, or A/B human judgment was available in this authoring environment.
- A5/A6 were accessible only as documentation shells. Current command/API details must be checked locally; no inference that their full text was read.
- Source excerpts and mock-based script tests do not establish compatibility with every installed framework version.
- User-specific preferences came from the supplied web skill section `SKILL.md` (original lines 189–225), not platform standards. No source archive or original web skill is required at runtime.
- No external skill is a hidden dependency. Platform SDKs/tools remain external prerequisites and are not installed automatically.
