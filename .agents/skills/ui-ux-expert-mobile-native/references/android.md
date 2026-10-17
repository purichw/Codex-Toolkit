# Android adapter

Load for an Android target. Verify target/min SDK, UI toolkit, navigation library and actual device
configuration. Sources [D1–D5] in [sources](sources.md). Avoid universal API-level claims from memory.

## Platform behavior before decoration

Respect system Back, including predictive Back where supported/configured. Check both completion and
cancellation, root/child/sheet states, and unsaved work. Do not intercept Back solely to achieve a custom
transition or exit confirmation on every screen. Use current supported navigation integration rather
than resurrecting an obsolete callback pattern. [D3]

Make system bar/window/IME inset ownership explicit. Edge-to-edge appearance is not permission to put
controls under the navigation region or keyboard. Avoid double padding from Scaffold, wrappers and
screen code. Record gesture/button navigation mode and keyboard state for affected captures. [D4]

Use platform-appropriate components and semantic theming where useful; brand does not require overriding
every system gesture. Dynamic color should be a product decision, not silently overwrite an approved
brand. Test readability in the appearances the product supports; a palette change is not dark-mode QA.

## Density and adaptation

Use dp for geometry and scale-aware text units/mechanisms as appropriate to the toolkit. Check actual
font/display scale and touch areas, not a screenshot's pixel width. Standard target guidance is 48 dp;
expanded hit areas must not overlap adjacent actions. [D1]

Adapt to available window space, content and capabilities: compact list, wider list/detail or other
appropriate grouping. Keep destination and selection state across window changes. Do not stretch phone
rows across a large display or lock an app to portrait as an unrequested workaround. For tablet/foldable
support, include relevant fold/window transitions rather than claiming support from one emulator. [D2]

## Runtime and restoration

Test draft/selection/scroll restoration for the app's agreed lifecycle contract: background/resume,
configuration change, and activity/process recreation where needed. `remember` or a JavaScript local
state variable is not a persistence claim. Returning to a sensitive or stale transaction may require
revalidation; don't blindly restore an unsafe confirmation state. [D2]

Exercise TalkBack, keyboard, permission denial/Settings return, loading/retry and deep-link entry where
affected. A mocked repository test does not establish the OS dialog or external provider works. Measure
performance using the project's relevant build and target device; a debug desktop/emulator impression
is not a release frame-time result.

## Repair examples

- Text clips after font scaling: fix constrained height/role layout, not a global font-scale cap.
- Screen jumps above the keyboard: inspect which container resizes and which adds IME padding.
- Back loses a draft: fix route/state ownership before adjusting the toolbar icon.
- All rows compete: change task hierarchy and action footprint while preserving 48 dp hit regions.
