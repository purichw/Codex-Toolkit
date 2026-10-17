---
name: ui-ux-expert-mobile-native
description: Design, implement, critique, and refine native iOS/iPadOS and Android app UI/UX in SwiftUI/UIKit, Jetpack Compose/Views, React Native/Expo, or Flutter. Use for native screens, flows, components, visual defects, accessibility, and platform behavior. Inspect real native renders and repair causes before delivery. Not for responsive websites, PWAs, backend-only work, or browser screenshots presented as native proof. No other skill is required.
---

# UI/UX Expert Mobile Native

Produce a context-appropriate native experience, not a small website or a universal app theme.
Judge the rendered result and actual task behavior, not the confidence of the explanation.
This is a first-release workflow, not a guarantee of design quality.

## 1. Establish the real target

Read the current request, project instructions, actual app code, dependency locks, shared UI,
approved references, assets, and product behavior. Identify supported OS versions, device/window
classes, language, native stack, navigation owner, and build/test commands. Keep the existing
stack; do not migrate frameworks just to match an example. For a new app, decide from stated
constraints; disclose a provisional choice. Do not assume every target is a phone in portrait.

Classify the deliverable: design proposal, implementation, audit, or targeted repair.
For design-only requests, deliver the requested visuals/specs without claiming native validation.
For implementation, check build/device/capture/image-inspection access early. Missing access means
scoped work plus explicit verification gaps, never substitution of a web mock as native evidence.

## 2. Resolve constraints, then load selectively

Visual direction: current explicit request and approved references → product brand/system →
platform-appropriate conventions → contextual fallback. This order never authorizes broken
accessibility, data integrity, security, or product behavior. When constraints genuinely conflict,
name the conflict and preserve the safe behavior; do not silently discard an explicit preference.

Always read [user preferences](references/user-preferences.md) for this owner's defaults.
Use the current project profile to keep product-specific fonts, artwork, provider choices, and
styling local; do not export one project's personality into every app.

| Present need | Load |
| --- | --- |
| New composition, density, hierarchy, reference translation, or ambiguous visual defect | [Design craft](references/design-craft.md); relevant section of [works/fails](examples/works-fails.md) |
| Screen/flow/control change | [Native interactions](references/native-interactions.md) |
| Text, input, scaling, assistive access, localization | [Accessibility and localization](references/accessibility-localization.md) |
| iOS/iPadOS target | [iOS](references/ios-ipados.md) |
| Android target | [Android](references/android.md) |
| Current implementation stack only | [SwiftUI/UIKit](references/stack-swiftui-uikit.md), [Compose/Views](references/stack-compose-views.md), [React Native/Expo](references/stack-react-native-expo.md), or [Flutter](references/stack-flutter.md) |
| Artwork, animation, game-adjacent native UI | [Assets and motion](references/assets-motion.md) |
| Rendered review or a delivery claim | [Visual review](references/visual-review.md) |
| Need evidence commands or current source verification | [Tooling](references/tooling.md); [sources](references/sources.md) |

Do not load all references or evaluation materials for every task. A small edit needs the owner,
local constraints, relevant state, and neighbor check, not a new design system or a full report.

## 3. Translate the reference into decisions

For the few decisions that shape the screen, connect:
**observed reference feature → purpose for this task → adaptation for real content/platform →
component/token/layout owner → rendered check**. Distinguish observed facts, hypotheses, and unknowns.
When no reference exists, select a coherent direction appropriate to the task and assets; compare
alternatives only for consequential uncertainty. Do not invent a carousel of concepts for a tiny fix.

Use meaningful real or clearly synthetic content immediately: long Thai/English labels, large
values, missing values, errors, and relevant imagery. Preserve full underlying data and its meaning.
Choose information structure before decoration. Native does not mean visually anonymous: brand can
shape type, imagery, surfaces, and motion while navigation and controls remain understandable.

## 4. Implement a small complete slice

Establish navigation, content, actions, feedback, and recovery together. Use the project's shared
components and semantic roles. Change shared owners deliberately and check their affected consumers.
Do not hardcode text heights, turn every surface into a card, shrink all text, disable system scaling,
hide overflow, remove actions, or replace a system control merely to make a screenshot fit.

Make platform decisions explicit at their boundary; shared product semantics do not require identical
pixels on both OSes. Preserve drafts, selection, scroll position, permissions, and transaction state
according to the app's actual contract. Keep fixture modes out of production paths and test auth.

## 5. Render → diagnose → repair → re-check

Before editing, choose a small evidence matrix: target build, representative devices/window sizes,
screens, states, language/text size, and affected neighbors. Fix this coverage before judging the result;
add newly discovered risks transparently. Use [design contract](templates/design-contract.md) only when useful.

Inspect an early native build, not just the final screen. Look at the whole screen, the complete flow,
and normal-scale details. For scrollable content capture the initial viewport and relevant below-fold
states with overlap; a stitched or cropped image is supplemental, never a substitute for viewport context.
Keep system bars, keyboard, sheets, and overlays in context when they matter.

For each material issue record briefly:
**image/state/region → observable problem → likely cause and distinguishing check → correct owner →
small repair → same-state comparison → regression check**.
First fix task/composition/hierarchy, then typography/grouping/density, then control optics.
A tint change is not a repair for a broken reading order. A static image cannot prove gestures,
keyboard handling, accessibility focus, persistence, animation feel, or native-provider integration.

Re-render after a meaningful visual change and inspect the final build. If the result contradicts the
hypothesis, revise the diagnosis. Do not fabricate defects or force a fixed iteration count; do not
redesign a clean surface just to demonstrate effort. Stop when no material in-scope defect remains,
or report the precise unresolved issue and constraint. Use human/blind comparison for uncertain taste
or release evaluation instead of letting the author self-certify quality.

## 6. Deliver with bounded claims

Return the implementation/diff or requested design artifact, decisions that matter, tested screens/states,
actual images and behavior checks, remaining risks, and next executable checks where blocked.
Separate structural integrity, behavior/accessibility, visual judgment, and repair evidence.
Use VERIFIED only for a specifically observed claim on a named build/runtime; PARTIAL for missing scope;
BLOCKED for a check that could not run. Never label the whole product verified from one screen.
The bundled checker reports evidence integrity/coverage, never beauty or runtime authenticity.

No hidden external skills, paid services, or native SDKs are bundled. Use available project tooling;
verify version-specific APIs in official docs as needed. Source pointers live in [sources](references/sources.md).
Do not claim an unavailable device, unopened image, generated illustration, unit test, or browser preview
establishes native UI quality. Protect secrets and user data in captures and logs.
