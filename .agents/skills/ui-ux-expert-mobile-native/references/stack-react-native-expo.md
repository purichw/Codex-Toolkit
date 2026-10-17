# Stack adapter: React Native / Expo

Workflow guidance, not a shipped component library. Read package/lock files, app config, native folders,
navigation/safe-area dependencies, scripts and build mode before choosing APIs. Preserve the project's
package manager, navigation stack and styling system. Sources [R1–R3, E1] in [sources](sources.md).

A React Native app can share product logic without making iOS and Android look or behave identically.
Use native primitives and platform-aware shared boundaries. Do not import web CSS, DOM-only libraries,
or assume React Native Web screenshots prove native layout. For embedded web content, name its scope
and test the native/web boundary separately; a wrapped website is not fully native validation.

Inspect text scaling, Android font padding, multiline labels, measured view bounds, keyboard avoidance,
safe-area/navigation insets and modal focus. Do not disable `allowFontScaling` across the app to force
fit. Use the project's current safe-area integration, not a blindly copied deprecated API. A
KeyboardAvoidingView configuration can differ by platform; inspect the actual keyboard state. [R1, R2]

Preserve screen and store state across tabs, auth returns and backgrounding under the product contract.
Test platform Back/dismiss with the installed navigation version. Validate accessibility names, roles,
values, actions and modal focus on both OSes; shared JS does not prove shared behavior.

For Expo, distinguish web preview, Expo Go, development client and release artifact. When native SDKs,
configuration or external provider callbacks matter, use the project-appropriate native development
build, not Expo Go as blanket proof. Inspect generated/manual native configuration boundaries; do not
run destructive prebuild regeneration or replace native folders without authorization. Local native
build workflows exist; no paid service is required by this skill. [E1]

JS/component tests do not exercise all backing platform code. Use the project's device-level tooling
and actual native captures for affected critical flows; do not add a new E2E framework reflexively.
Separate JS snapshot/regression tests from visual quality and full native behavior. [R3]

For proof, capture native runtime plus the JS bundle/update identity and native build identity. An
unchanged native build number does not prove screenshots use the final JavaScript edits. Missing native
runtime is an explicit limitation, not a reason to claim the web variant passed for both platforms.
