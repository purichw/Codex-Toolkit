# 04 · Interaction design

Everything here concerns what happens between the click and the result. It is the area where
screenshots are least sufficient and where engineers have the most authority — the interaction
model is usually decided in code, not in the design file.

## What designers notice that developers often miss

- **The action's blast radius sets the friction.** Friction should scale with how hard the action
  is to reverse — not with how hard it was to implement a dialog.
- **Undo beats confirm.** A confirm dialog interrupts every user to protect against a rare mistake;
  undo protects after the fact and costs nothing when things go right.
- **State survival is a feature.** Scroll position, selection, filters, drafts, and expanded rows
  are user work. Losing them on refresh or on back is data loss, just cheap data.
- **Disabled is a dead end.** A disabled control with no explanation makes the user guess. Designers
  never ship one; engineers ship them constantly because the disabled condition was easy to compute.
- **Partial failure is the normal case in bulk actions.** "17 of 20 updated" needs a designed
  screen; developers usually ship success-or-toast-error.
- **Latency is a design material.** 0–100ms feels instant, 100–300ms feels responsive, >1s needs
  progress, >10s needs a way to leave and come back.
- **Two spinners is a bug.** A global spinner plus a local one means nobody decided where feedback belongs.
- **Focus is state.** After a dialog closes, a row is deleted, or a step advances, focus has to land
  somewhere deliberate.

## 1. Multi-step flows

**Bad patterns** `[FACT]`
- "Next" disabled with no indication of what's missing.
- Validation firing on every keystroke, so the user is told they're wrong while typing.
- Back button loses entered data, or exits the flow entirely.
- Progress indicator with a fake denominator (steps that don't exist, or a percentage).
- Flow with no exit; or an exit that discards without asking.
- Refresh mid-flow restarts from step 1.

```js
// ❌ Next disabled, reason invisible
<button disabled={!isValid}>Next</button>

// ✅ Always clickable; submitting surfaces the specific blockers and focuses the first one
<button onClick={submit} aria-describedby={errorId}>Next</button>
// on submit: mark invalid fields, render an inline summary listing them as links,
// move focus to the first invalid field, keep the button enabled.
```

**Rules**
- **IX-1** Never disable a forward action without a visible reason. Prefer enabled + on-submit validation that names and focuses the blocker. `[CRAFT]`
- **IX-2** Validate text on blur, cross-field rules on submit; only format-as-you-type for masks (card, phone). Never show an error for an incomplete field the user is still in. `[CRAFT]`
- **IX-3** Back preserves everything entered. Forward after back re-shows entered values, not defaults. `[FACT]`
- **IX-4** Step count is real and derived from the actual remaining path. `[FACT]`
- **IX-5** Flows are resumable: state persists across refresh and across devices if the flow spans sessions (persistence scope is `[PD]`). `[PD]`
- **IX-6** Exit is always available, states what happens to the work ("Save as draft" / "Discard"), and never discards silently. `[CRAFT]`

## 2. Autosave

**Bad patterns** `[FACT]`
- No save state at all — user can't tell if their work is safe.
- A spinner in the middle of the content while typing.
- "Saved" toast on every keystroke debounce.
- Save on every character (server load, and every intermediate state persisted).
- Silent failure: connection dropped, edits kept in memory, tab closed, work gone.
- Autosave plus a Save button, both present, meaning something different.

```
❌  [ Editing… ] (spinner, center of canvas)
✅  Status line, one place, low contrast, in the header:
    idle    →  "Saved 2 minutes ago"
    saving  →  "Saving…"           (only after 400ms of pending state)
    saved   →  "Saved just now"    (persists, doesn't animate away)
    error   →  "Couldn't save — retrying. Your changes are kept on this device." + Retry
    offline →  "Offline. Changes will save when you reconnect."
```

**Rules**
- **IX-7** One persistent save-status region per editing surface, never a toast, never centered over content. `[CRAFT]`
- **IX-8** Four states minimum: idle-with-timestamp, saving, saved, failed-with-retry. Offline is a fifth if the product works offline. `[CRAFT]`
- **IX-9** Debounce 500–1000ms after the last keystroke plus a forced save on blur, navigation, and every ~30s of continuous editing. `[CRAFT]`
- **IX-10** Never mix autosave and manual save on the same surface. Pick one per surface type and document it. `[PD]`
- **IX-11** Failed saves keep the user's text locally and say so. Conflict resolution strategy (last-write-wins, merge, lock) is `[PD]`. `[PD]`

## 3. Undo

**Bad patterns** `[FACT]`
- Confirm dialog for a reversible action (archive, hide, reorder).
- Undo toast that vanishes in 3 seconds, or that's covered by another toast.
- Undo that restores the record but not its position, selection, or scroll.
- Undo offered for something not actually undoable (email already sent).
- `⌘Z` doing nothing in an app full of editable state.

**Rules**
- **IX-12** Reversible actions get undo, not confirmation. Undo affordance visible ≥6s; ≥10s for bulk or destructive. `[CRAFT]`
- **IX-13** Undo restores the full prior state: value, order, selection, scroll, and open/expanded state. `[FACT]`
- **IX-14** Never label something Undo if it can't fully reverse — say what it does ("Recall message (may already be read)"). `[CRAFT]`
- **IX-15** In editing surfaces, support `⌘Z`/`Ctrl+Z` for the same operations the UI can undo, with a visible history if depth >1. Depth is `[PD]`. `[PD]`

## 4. Bulk actions

The single richest source of interaction bugs.

**Bad patterns** `[FACT]`
- "Select all" ambiguity: checkbox selects the visible page but the action applies to all matches (or vice versa) with no wording to distinguish.
- Selection count not shown, or shown only in a place that scrolls away.
- Actions applied to items the user filtered out after selecting.
- Selection lost on pagination, sort, filter change, or refresh — silently.
- All-or-nothing result reporting: 20 items, 3 failed, one generic error toast.
- Destructive bulk action with the same friction as a single one.

```
❌  [✓] header checkbox   "Delete"     → deletes 10,000 matching rows

✅  [✓] 25 on this page selected · Select all 1,043 matching this filter
    ┌ persistent bar ───────────────────────────────────────────────┐
    │ 25 selected   [Assign]  [Export]  [Archive]        [Delete]   │
    └───────────────────────────────────────────────────────────────┘
    Delete → type-to-confirm because irreversible + bulk:
      "This deletes 25 invoices. Type DELETE 25 to confirm."
    Result → "23 of 25 archived. 2 failed: INV-3021 (locked), INV-3044 (locked). Retry failed"
```

**Rules**
- **IX-16** Distinguish "all on this page" from "all matching" in words, always, with the count of each. `[FACT]`
- **IX-17** Selection count and available actions live in a bar that stays visible while any selection exists. `[CRAFT]`
- **IX-18** Changing filter/sort/page either preserves selection (and says so: "3 selected items are hidden by this filter") or clears it with an explicit notice. Never silently. `[FACT]`
- **IX-19** Bulk results report per-item outcomes with reasons and a retry-failed-only action. `[CRAFT]`
- **IX-20** Bulk friction ≥ single-item friction, scaled by count: a threshold above which extra confirmation applies is `[PD]`. `[PD]`

## 5. Permission states

Three legitimate treatments, one wrong one.

| Treatment | Use when | Requirement |
| --- | --- | --- |
| **Hide** | The user can never have this capability in this context; its existence is not useful information | Nothing hidden that the user could unlock — that creates support tickets |
| **Disable + reason** | The user could have it (wrong role, wrong plan, wrong object state) | Reason on hover **and** on focus, and in the accessible name |
| **Show + explain path** | The capability is purchasable/requestable | Explicit next step ("Ask an owner", "Upgrade to Team") |
| ❌ **Disable, no reason** | never | — |

**Bad patterns** `[FACT]`
- Buttons that 403 on click.
- Disabled controls with `pointer-events: none`, so the tooltip can never show and focus skips them.
- Permission errors surfaced as generic failures.
- Whole page blank for a role that has partial access, instead of showing what it can see.
- Read-only mode implemented as a form with disabled inputs (unreadable) rather than as rendered values.

```css
/* ❌ tooltip unreachable, invisible to keyboard */
button[disabled] { pointer-events: none; opacity: .4; }

/* ✅ focusable, explained, still legible */
button[aria-disabled="true"] { color: var(--color-text-muted);
  border-color: var(--color-border-subtle); cursor: not-allowed; }
/* keep it in the tab order, announce the reason via aria-describedby,
   and swallow the click in the handler rather than in CSS */
```

**Rules**
- **IX-21** No control is disabled without a reason reachable by pointer *and* keyboard, and included in its accessible description. `[FACT]`
- **IX-22** Never render an action the current user cannot perform without explaining the condition. No silent 403s. `[FACT]`
- **IX-23** Read-only is a different rendering, not a disabled form: show values as text with the same layout, and a single "why can't I edit this" affordance. `[CRAFT]`
- **IX-24** Partial access shows what's permitted plus an explicit count of what's withheld. Whether counts of hidden items leak information is `[PD]`. `[PD]`

## 6. Optimistic updates

| Safe to be optimistic | Never optimistic |
| --- | --- |
| Toggles with local effect (star, pin, read/unread) | Money movement, refunds, payouts |
| Reordering, renaming | Permission and role changes |
| Adding a comment, a tag, a like | Deletion of anything not soft-deleted |
| Local UI state (collapse, filter) | Anything that triggers an external side effect (send, publish, charge) |
| Fast (<500ms p95) and idempotent operations | Operations whose failure isn't detectable client-side |

**Bad patterns** `[FACT]`
- Optimistic write, failure surfaced as a global toast while the item still shows the new value.
- Item reverts with no explanation, user assumes they misclicked.
- Optimistic delete that removes the row, then restores it at the bottom of the list on failure.
- Two sources of truth: server response ignored, local state kept.
- No pending affordance at all, so a slow failure looks like success for 4 seconds.

```
❌  toggle → UI updates → request fails → toast "Error" → UI stays wrong

✅  toggle → UI updates immediately, item marked pending (subtle, in place)
          → success: pending mark clears
          → failure: value reverts in place, inline error at the item
                     ("Couldn't star — you don't have access. Retry"),
                     focus stays where the user left it
```

**Rules**
- **IX-25** Optimistic only when the operation is reversible, local in effect, and its failure is detectable. Otherwise show pending state and wait. `[CRAFT]`
- **IX-26** On failure, revert *at the item* with an inline, specific error; a global toast is not sufficient. `[FACT]`
- **IX-27** Reverting restores the original position and the user's focus/scroll. `[FACT]`
- **IX-28** Any operation slower than ~400ms shows a pending state on the affected element, not a page-level spinner. `[CRAFT]`

## 7. Interruption recovery

Assume every session ends abruptly: closed tab, dead battery, lost connection, expired token.

**Bad patterns** `[FACT]`
- Refresh loses filters, sort, page, selection, scroll, expanded rows, and open panel.
- Session expiry drops the user on a login screen and then to the dashboard, losing the deep link and the draft.
- Long-running job with no record of it — leaving the page loses the result.
- Draft text lost on accidental navigation, with no "you have unsaved changes" and no local copy.
- Back after submit re-submits, or shows a stale form.

**Rules**
- **IX-29** Everything the user configured on a screen is in the URL: filters, sort, page, tab, open item. `[FACT]`
- **IX-30** Everything the user typed is persisted locally within 1s of typing, and offered back on return ("Restore draft from 14:02?"). Retention period is `[PD]`. `[PD]`
- **IX-31** Auth interruption returns the user to the exact prior URL, with the draft intact. `[FACT]`
- **IX-32** Long jobs are addressable objects with their own status view; the user can navigate away and come back. Notification on completion is `[PD]`. `[PD]`
- **IX-33** Restore scroll position and expanded/collapsed state on back-navigation within the app. `[CRAFT]`

## 8. Destructive actions

Friction ladder — match the rung to the blast radius. `[PD]` for where each of the product's
actions sits; the ladder itself is `[CRAFT]`.

| Rung | Mechanism | Use for |
| --- | --- | --- |
| 0 | Immediate + undo (≥6s) | Reversible, single, low value: archive, hide, remove a tag |
| 1 | Immediate + undo (≥10s) + trash/soft-delete with retention | Reversible-by-recovery single deletes |
| 2 | Confirm dialog naming the object and the effect | Irreversible single action, or multi-item reversible |
| 3 | Type-to-confirm the object's name or count | Irreversible + bulk, or irreversible + high value |
| 4 | Delay window + notification to other stakeholders + cancel | Catastrophic/organizational: delete workspace, revoke all access, cancel plan |

**Bad patterns** `[FACT]`
- `confirm("Are you sure?")` — no object named, no consequence stated, browser-styled.
- Destructive button as the primary/default-focused action in a dialog.
- Delete placed adjacent to a frequent action (Edit, Duplicate) with identical treatment and <16px separation.
- Filled red buttons used for every destructive action, including reversible ones — red fatigue.
- Confirm dialog for a reversible action *and* no undo for an irreversible one (backwards).
- Dialog that doesn't say what will *also* be deleted (children, references, history).

```html
<!-- ❌ -->
<button class="btn-danger" onclick="if(confirm('Are you sure?')) del()">Delete</button>

<!-- ✅ rung 2: object named, consequences enumerated, cancel is the default focus -->
<div role="dialog" aria-modal="true" aria-labelledby="t" aria-describedby="d">
  <h2 id="t">Delete “Q3 revenue model”?</h2>
  <p id="d">This permanently deletes the file and its 42 revisions.
     3 dashboards reference it and will show an error.</p>
  <div class="actions">
    <button autofocus>Cancel</button>
    <button class="btn-danger-outline">Delete file</button>
  </div>
</div>
```

**Rules**
- **IX-34** Confirmations name the object, enumerate what else is affected, and label the confirm button with the verb ("Delete file"), never "OK"/"Yes". `[FACT]`
- **IX-35** Cancel holds initial focus in any rung-2+ dialog; `Esc` cancels; the destructive control is never the default action. `[FACT]`
- **IX-36** Destructive controls are visually separated (≥16px, or an overflow menu with a divider) and never share treatment with the primary action. `[CRAFT]`
- **IX-37** Reserve filled-danger treatment for rung 3–4. Rungs 0–2 use an outlined/text danger treatment. `[CRAFT]`
- **IX-38** Prefer soft-delete with a stated retention period over hard delete. Retention length and hard-delete availability are `[PD]`. `[PD]`

## Screenshot QA

Some of these need two or three captures — capture them, don't just click through.

1. Capture every control's disabled state. Does each show a reason on hover **and** focus? (IX-21)
2. Capture a form mid-error. Are blockers named, linked, and is focus on the first one? (IX-1, IX-2)
3. Capture the editing surface in all save states side by side. Distinguishable? Same location? (IX-7, IX-8)
4. Capture a selection of 2 items. Is the count visible? Is "all on page" vs "all matching" worded? (IX-16, IX-17)
5. Change the filter with a selection active. Screenshot the result — silent loss? (IX-18)
6. Force a bulk partial failure (kill one request). Is the result per-item with reasons? (IX-19)
7. Force an optimistic failure. Is the error at the item, is the value reverted, did focus move? (IX-26, IX-27)
8. Refresh a configured screen (filters + sort + open row + scrolled). Diff the before/after screenshots. (IX-29, IX-33)
9. Type a draft, navigate away, come back. Is it offered? (IX-30)
10. Open every destructive confirm. Is the object named, the cascade listed, cancel focused, the verb on the button? (IX-34, IX-35)
11. Measure the pixel distance between the destructive control and its nearest neighbor. ≥16px? (IX-36)
12. Throttle to 3G and capture at 400ms after a click. Is there exactly one feedback indicator, on the right element? (IX-28)

## Adapt or override

- **High-frequency expert workflows can drop friction a rung.** A moderator archiving 400 items an
  hour should not confirm anything — undo + trash is correct. Requires knowing the frequency: `[PD]`.
- **Regulated or irreversible domains raise every rung.** Payments, medical records, and legal
  filings may require confirm even for reversible actions, plus an audit entry. `[PD]`
- **Offline-first products invert IX-25**: optimistic is the default and conflict resolution becomes
  a first-class designed surface, not an error path. `[PD]`
- **IX-29 (state in URL)** has a privacy caveat: don't put PII or secrets in query strings; use
  opaque view IDs for sensitive filters.
- **IX-1 (never disable)** — a genuinely uninitialized form (nothing typed yet) may start with a
  disabled submit; the rule targets forms where the user has entered *something* and can't tell
  what's missing.
- **Native mobile** replaces several of these with platform mechanics: system back, swipe-to-delete
  with undo bar, sheet dismissal semantics. See [05](05-mobile-native-feel.md); don't reimplement.
