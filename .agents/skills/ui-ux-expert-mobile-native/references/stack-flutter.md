# Stack adapter: Flutter

Workflow guidance, not a compiled widget library. Inspect pubspec/lock, SDK constraints, themes, router,
state management, assets/fonts and integration tests. Preserve the project's architecture; do not
convert it to Flutter because this reference exists. Sources [F1–F4] in [sources](sources.md).

Keep product semantics shared while adapting platform conventions deliberately. Material on Android,
Cupertino-style behavior on iOS, or a brand-led shared system should be a conscious product decision,
not a global platform toggle used to excuse wrong navigation. Flutter mobile renders are native-target
app evidence; Flutter web and desktop runs are not substitutes for mobile OS behavior.

Inspect constraints and composition before adding fixed sizes. Use LayoutBuilder/MediaQuery context
where appropriate, one coherent SafeArea/inset owner, and content-driven rows. Understand how Scaffold,
viewInsets and scroll padding cooperate when the real keyboard opens. Do not add keyboard height twice,
scale an entire phone design as an image, or use fit-to-box text everywhere. [F1, F2]

Preserve system text scaling with the SDK's supported mechanism; do not globally force a linear scale
or shrink essential labels. Keep semantics useful and actions discoverable. Verify Thai font coverage,
marks and mixed text on the actual target. Use current navigation/back integration for the pinned
SDK; don't paste an obsolete interception API from memory. [F3]

Keep widget identity, controllers, focus and route state stable. A widget held in memory is not proof
of state restoration after app termination. Asset decoding, image crop and animation behavior should
be checked on the target; golden images are useful regressions, not a taste certificate.

Use `flutter analyze`, the project's widget/unit tests, and native-device `integration_test` or the
existing equivalent as appropriate. Discover a real `flutter devices` target and pass its ID; do not
let an automated prompt silently choose Chrome/Linux. Integration testing requires an app to run. [F4]

If the product embeds Flame or another game surface, preserve approved sprite atlas, manifests,
coordinates, hit regions and timing. Treat overlays/forms/navigation as app UI; pause/resume and touch
conflicts need game-specific tests. This skill does not replace game-engine or character-art tooling.

Capture the native build and Dart/source identity. Hot reload alone is not a clean-build/lifecycle test.
If the SDK/device is unavailable, state that code and adapters have not been compiled or run here.
