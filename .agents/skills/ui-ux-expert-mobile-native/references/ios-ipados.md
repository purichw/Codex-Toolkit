# iOS / iPadOS adapter

Load for an Apple mobile target. Preserve deployment targets and the project's framework. Sources
[A1–A5, A6] in [sources](sources.md) guide current verification; UI style and APIs depend on OS/SDK.

## Design decisions

Use system-supported navigation, tabs, toolbars, sheets, menus and editing where they match the task.
Do not clone a remembered iOS version's chrome or add a material effect everywhere simply because it
is new. A brand-led illustrated surface can coexist with predictable navigation and readable controls.
Do not use Android visual conventions blindly on iOS, but don't remove a deliberate cross-platform
product convention without a reason.

For a temporary task, choose a sheet when context and content fit; use a full-screen flow when depth,
keyboard needs or information density make a sheet awkward. Show how to finish/cancel, preserve state,
and test interactive dismissal with unfinished work. A presented editor must not save merely because
it disappeared. On iPad, reassess sheet/popover size and split views; don't assume a phone modal stretched
wider is the right solution. [A3]

Use semantic typography/Dynamic Type and inspect long translated strings at accessibility sizes.
Avoid fixed content heights and magic status-bar/home-indicator offsets. Give useful content a safe
layout while backgrounds may extend where appropriate; read actual insets rather than device model names.
Preserve text selection, edit menus, keyboard return behavior, autofill and native picker semantics. [A2, A4]

## Actual runtime checks

Capture a native build on a named simulator/device and OS version. Exercise navigation from root to
child and back, canceled/completed interactive gestures, sheet dismissal, keyboard covering the lower
fields, tab return state, and external links/auth return where affected. Use exact screen and state IDs.
A preview is an early visual check; it is not installed-app lifecycle or system-integration evidence.

For iPad targets, test supported narrow/wide windows, orientation, hardware keyboard/focus and pane
selection. Keep equivalent tasks possible across window states. Scope unsupported orientations/window
modes explicitly rather than claiming universal adaptation.

Use VoiceOver, larger text and relevant appearance settings for actual accessibility claims. Hardware
camera, haptics, biometric/auth-provider behavior and performance need device-appropriate evidence.
Simulator screenshots alone do not prove all these behaviors. UI automation can use the project's
XCUIAutomation/XCTest tooling; verify APIs against its installed Xcode. [A5]

## Failure-driven repairs

- A lower save button is hidden: inspect keyboard/inset ownership and scrolling; don't raise it by a
  fixed number copied from one phone.
- A large title consumes the entire short window: adapt title/content hierarchy to the task and
  available space; don't disable larger text for the whole screen.
- A branded field is not centered: correct app-owned field geometry; report OS-owned picker limits
  instead of replacing a wheel/calendar only to force typography.

All numeric geometry needs pt vs screenshot-pixel distinction. Record device scale separately.
