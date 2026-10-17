# Stack adapter: Jetpack Compose / Android Views

Workflow guidance, not a compiled UI library. Use the existing project and SDK/Gradle versions. Sources
[D1–D5] in [sources](sources.md). Do not migrate Views to Compose just to use this skill.

Inspect modules/build variants, navigation graph, theme roles, state holders, previews and test tasks.
Use stable identifiers and shared components. In Compose, inspect parent constraints, modifier order,
Scaffold/inset ownership, semantics and list keys before adding offsets. A remembered view state is not
a claim of persistence after process recreation. In Views, inspect constraints, measured sizes, adapters,
text appearances and focus behavior rather than masking a layout bug with translations.

Text must participate in system scaling; rows and groups should adapt where essential text wraps.
Keep touch expansion from colliding with adjacent controls. Prefer one coherent semantic interactive
row to duplicate inaccessible click targets, while leaving truly separate actions reachable. [D1]

For meaningful UI changes, use the project's Compose UI/Espresso/instrumentation setup and render the
installed build. Verify TalkBack and system Back in their actual contexts. Previews and local JVM tests
are useful, but do not prove real keyboard, permission, gesture, or lifecycle behavior.

Discover tasks/variant names rather than assume a module called app or a universal debug variant.
Use the existing Gradle wrapper and lock/version policy. Build failures should retain logs. Match the
artifact installed on the selected emulator/device to the source under review.

Use [tooling](tooling.md) for optional `adb` screenshots. The helper does not build/install/navigate or
validate a transaction; it captures the currently visible native runtime declared by the operator.
