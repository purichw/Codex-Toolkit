# Stack adapter: SwiftUI / UIKit

This is workflow guidance, not a compiled component library. Read only for this stack. Verify exact
API availability in the installed SDK; use [Apple sources](sources.md) A2–A6 as starting points.

Inspect project/workspace, schemes, deployment targets, resources, navigation coordinators, shared
components, test targets and CI before editing. Preserve UIKit/SwiftUI boundaries already in use; a UI
repair is not authorization to migrate one to the other. Retain state owners and accessibility IDs.

In SwiftUI, distinguish view identity/state from persisted product state. Use semantic text styles and
scaling-aware custom styles; prefer content-driven layout and correct safe-area ownership over geometry
readers and offsets everywhere. Navigation, focus and presentation bindings must describe the same flow.
In UIKit, inspect constraints, intrinsic sizes, hugging/compression and preferred text-style scaling;
fix the constraint/owner instead of translating the view after layout. Test reused cells with long text.

Do not introduce duplicate screen titles, duplicated navigation bars, or inconsistent padding at hosted
UIKit/SwiftUI boundaries. Avoid erasing useful accessibility semantics with broad container overrides.
Use accessibility labels/values/actions appropriate to the platform, with focus and group behavior tested.

Discover actual schemes and test destinations first; execute the project's documented build and
XCUIAutomation/XCTest tests on the named simulator/device. Use previews for iteration, then installed
native runs for behavior. A screenshot attached to a unit test is not automatically an end-to-end check.
For CLI captures, see [tooling](tooling.md); the helper supports iOS Simulator, not arbitrary iPhones.

If Xcode/Apple runtime is absent, make scoped code/spec changes only and report the exact missing check.
Do not replace the target with a browser, claim a build passed, or fabricate a simulator identifier.
