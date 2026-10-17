# Native flows and behavior contracts

Load for affected flows, not as an instruction to add every feature. This is an original workflow
synthesis; consult platform sources [A3, D2, D3, D4] in [sources](sources.md) for supported APIs.

## Navigation is state, not just chrome

Describe the actual route, entry point, parent/destination, dismiss behavior, and state ownership.
Separate top-level destinations, hierarchical drill-down, temporary tasks, and contextual actions.
Use tabs for actual destinations, not a forced count of shortcuts; retain state when switching where
promised. A full-screen task can be right when a sheet becomes a cramped multi-step form.

Check iOS interactive back/dismiss and Android system Back/predictive Back on the supported stack.
Verify cancellation partway through a gesture as well as completion. Do not intercept system behavior
merely to force an animation. Protect unsaved work by the product's autosave/draft/confirm contract;
do not force a discard dialog after every change or let a decorative close silently lose data.

## For each affected screen, identify the necessary state path

| State family | Contract to preserve | Useful observation |
| --- | --- | --- |
| Loading/refresh | Show progress without blanking usable existing data unnecessarily | The same selection and scroll remain meaningful after refresh |
| Empty/no results | Distinguish no data, a filter result, no access, and unavailable data | Recovery action matches the actual reason |
| Editing/keyboard | Labels, field, validation, and next action remain reachable | Focus a low field; open the real software keyboard; scroll to error and CTA |
| Saving/retrying | No double submission; no premature success; draft retained on failure | Delay then fail; retry; reopen once saved |
| Offline/stale | Tell pending/local/synced states apart when the product supports them | Return online without duplicate work or silently overwritten changes |
| Permission denied/restricted | Contextual request and a usable fallback; no repeated coercive prompts | Deny, return from Settings, and revoke between uses |
| Background/recreation | Restore what the product promises; revalidate sensitive stale state | Resume, recreate/relaunch where supported; inspect data, not just appearance |
| External authentication/deep link | Correct return route, cancellation, denied/expired response, no duplicate navigation | Cold/warm entry and return to the unfinished task |

OAuth/LINE/Apple/Google and other provider UI is conditional on the product. Do not add providers
unasked, fake authentication success, collect a provider password in a custom form, or invent SDK
integration. Preserve provider branding requirements and use its official current integration docs.
This skill covers UX and integration contracts, not security certification or backend auth design.

## Ergonomics and system boundaries

Insets: identify the one owner for system bars, keyboard, sheet, and content padding. Do not stack
multiple safe-area wrappers blindly. A fixed bottom action needs scrolling clearance and correct
IME behavior, not a magic bottom offset. Check both gesture/button navigation where in scope.

Selection/pickers: use platform-supported editing, paste, autofill and input types where suitable.
Native controls need not have identical pixels on both OSes. Preserve accessibility names/states,
focus order, and cancel behavior in custom components. Gesture-only essential actions need a discoverable
alternative appropriate to the product.

Data and shared components: find all affected consumers, including errors and overlays. Keep identifiers,
permissions, full values, calculations and persistence semantics. Null/unknown is not zero; a retry is
not a new transaction by default. Avoid visual redesigns that hide critical status behind decoration.

For tablets/foldables/window resizing, adapt by available space and task, not device-name checks alone.
Define selection/detail persistence across pane changes. Do not stretch a phone layout edge to edge.
