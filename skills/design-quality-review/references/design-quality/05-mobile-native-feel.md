# 05 · Mobile-native feel

Why a technically responsive screen still feels like a website in a phone frame. Applies to
native apps, React Native, and mobile web — the perceptual rules are the same; only the APIs differ.

## What designers notice that developers often miss

- **Reachability, not just fit.** A layout that fits 390×844 can still put every action in the top
  20% of the screen, where a thumb can't go.
- **Scroll physics and overscroll.** iOS rubber-bands, Android glows. A custom scroll container
  that does neither reads as foreign in under a second.
- **Sheet vs. dialog is semantic.** Sheets are for choosing and doing; dialogs interrupt. Using a
  centered dialog for a picker is the most common "this is a website" tell.
- **Keyboard behavior is 40% of form quality.** Wrong keyboard type, wrong return key label, field
  hidden behind the keyboard, no scroll-to-field — each costs more than any visual detail.
- **The gesture edges are reserved.** Horizontal scrollers and drawers that start at x=0 fight the
  system back gesture.
- **Safe areas are not padding.** They are variable per device and per orientation, and they must
  come from the platform, not from a magic number.
- **Density is not a scale factor.** Mobile gets *bigger* text and *taller* rows than desktop, with
  fewer columns — not the same layout shrunk.
- **Transitions communicate depth.** Push-from-right = deeper; sheet-from-bottom = temporary;
  fade = replace. Getting this wrong makes navigation feel arbitrary.

## Bad patterns

| Pattern | Tell `[FACT]` | Fix |
| --- | --- | --- |
| Desktop layout scaled | Two columns at 390px; 13px body; 32px controls | Single column, 16–17px body, 44pt targets |
| Hover-dependent affordance | Action only appears on hover; sticky hover after tap | Always-visible or long-press with a visible alternative |
| `100vh` layout | Content clipped by the URL bar; bottom bar jumps on scroll | `100dvh`, or `svh`/`lvh` where a fixed bound is needed |
| Fixed bottom bar with static padding | Bar sits under the home indicator | `padding-bottom: max(12px, env(safe-area-inset-bottom))` |
| Web `<select>` for a long list | 60-item native dropdown | Sheet with search, or platform picker |
| Centered dialog for a picker | Scrim + 280px box mid-screen | Bottom sheet with detents |
| Custom back chevron only | Swipe-back does nothing; Android system back exits the app | Wire the platform gesture and system back to the same stack |
| Carousel at the screen edge | Edge-swipe triggers back instead of scrolling | Keep ≥24px inset from both edges, or disable edge gesture in that region deliberately |
| Field under the keyboard | User types blind | Keyboard-avoiding container + scroll the focused field into the visible area |
| 14px inputs on iOS Safari | Page zooms on focus | Inputs ≥16px |
| Tab bar that hides on scroll | Destination lost; re-appears unpredictably | Persistent tab bar; hide only in immersive/media modes |
| Per-tab state reset | Switching tabs and back loses scroll and stack | Keep an independent nav stack + scroll per tab |

## Before / after

### Safe areas and viewport (mobile web)

```html
<!-- ❌ -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>.app { height: 100vh } .tabbar { position: fixed; bottom: 0; padding: 12px }</style>

<!-- ✅ -->
<meta name="viewport"
      content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
<style>
  .app     { min-height: 100dvh; }
  .header  { padding-top: max(12px, env(safe-area-inset-top)); }
  .tabbar  { position: fixed; inset-inline: 0; bottom: 0;
             padding-block: 10px;
             padding-bottom: max(10px, env(safe-area-inset-bottom));
             padding-inline: max(16px, env(safe-area-inset-left)); }
  .sheet   { max-height: 90dvh; overscroll-behavior: contain; }
</style>
```

### Inputs

```html
<!-- ❌ one keyboard for everything, no autofill, iOS zooms -->
<input type="text" placeholder="Email" style="font-size:14px">
<input type="text" placeholder="Card number">
<input type="text" placeholder="Amount">

<!-- ✅ right keyboard, right return key, autofill, no zoom, label not placeholder -->
<label for="email">Email</label>
<input id="email" type="email" inputmode="email" autocomplete="email"
       enterkeyhint="next" autocapitalize="off" spellcheck="false" style="font-size:16px">

<label for="card">Card number</label>
<input id="card" inputmode="numeric" autocomplete="cc-number" enterkeyhint="next"
       pattern="[0-9\s]{13,19}" maxlength="19" style="font-size:16px">

<label for="amt">Amount</label>
<input id="amt" inputmode="decimal" enterkeyhint="done" style="font-size:16px;
       font-variant-numeric: tabular-nums; text-align: right">
```

### Sheet vs. dialog

```
❌  "Choose a category"  → centered dialog, 280px wide, list of 12, page scroll locked, X to close

✅  Bottom sheet:
    ── grabber ──────────────────────────
    Choose a category                 ✕
    [search field, focused on open]
    12 rows, 48pt each, scrollable within the sheet
    detents: 50% → 92%; drag-down dismisses; scrim taps dismiss;
    scroll inside content, drag only from the grabber/header when not at scroll-top
```

### Density

```
❌ 390px wide:  2 columns · 13px body · 32px rows · 8px margins · labels beside fields
✅ 390px wide:  1 column  · 16px body · 48px rows · 16–20px margins · labels above fields
                primary action pinned in the bottom third
```

## Rules

### Layout and safe areas
- **MB-1** Never `100vh` for a full-height layout; use `100dvh` (or `svh`/`lvh` when a stable bound matters). `[FACT]`
- **MB-2** All edge padding uses `max(<design value>, env(safe-area-inset-*))`; `viewport-fit=cover` is set. Native equivalents: `safeAreaInsets` / `WindowInsets`, never hard-coded. `[FACT]`
- **MB-3** Fixed bottom elements clear the home indicator / gesture bar; nothing interactive within 8pt of the very bottom edge. `[FACT]`
- **MB-4** Single column below 600px. Side-by-side controls only for genuinely paired items (from/to, min/max). `[CRAFT]`

### Targets and reach
- **MB-5** Minimum target 44×44pt (iOS) / 48×48dp (Android), including icon-only buttons; ≥8pt between adjacent targets. `[FACT]`
- **MB-6** The screen's primary action sits in the bottom third; destructive actions are not adjacent to it. `[CRAFT]`
- **MB-7** No functionality is hover-only or long-press-only without a visible alternative. `[FACT]`

### Gestures
- **MB-8** The platform back gesture works everywhere and maps to the same stack as the on-screen back control. `[FACT]`
- **MB-9** Horizontally scrolling regions keep ≥24px clear of both screen edges, or explicitly opt out of the edge gesture in that region. `[CRAFT]`
- **MB-10** Swipe actions on rows expose the same actions available elsewhere, are labeled once revealed, and destructive swipes are undoable. `[CRAFT]`
- **MB-11** Pull-to-refresh only where the list is the screen's content, and only in addition to an explicit refresh path. `[CRAFT]`

### Sheets, dialogs, navigation
- **MB-12** Sheets for choosing, filtering, quick create, and detail peeks. Dialogs only for blocking, consequential decisions ([IX-34](04-interaction-design.md)). `[CRAFT]`
- **MB-13** Sheets have: a grabber or explicit close, a scrim, `overscroll-behavior: contain`, at most 2–3 detents, keyboard avoidance, and drag-to-dismiss that doesn't fight inner scroll. `[FACT]`
- **MB-14** ≤5 tab-bar destinations; tabs persist across the app; each tab keeps its own nav stack and scroll position. `[CRAFT]`
- **MB-15** Transition direction encodes relationship: push-from-edge = deeper, sheet-from-bottom = temporary, crossfade = sibling replace. Use one mapping app-wide. `[CRAFT]`

### Input ergonomics
- **MB-16** Every input declares `type`/`inputmode`, `autocomplete`, `enterkeyhint`, and appropriate `autocapitalize`/`spellcheck`. `[FACT]`
- **MB-17** Input font-size ≥16px on mobile web (prevents iOS zoom-on-focus). `[FACT]`
- **MB-18** The focused field and its error are visible above the keyboard; the form scrolls to keep them so. `[FACT]`
- **MB-19** Visible labels above fields; placeholders are examples, never the label. `[FACT]`
- **MB-20** One-thumb submission: the submit control is reachable without moving the focused field out of view. `[CRAFT]`

### Platform fidelity
- **MB-21** Use the platform's own controls for pickers, dates, share, and permissions prompts. `[CRAFT]`
- **MB-22** Respect platform text-size settings (Dynamic Type / `sp` units); layouts must survive 200% text without clipping. `[FACT]`
- **MB-23** Native scroll containers only; no JS-driven scroll emulation, no scroll hijacking. `[FACT]`
- **MB-24** Haptics only on meaningful state change (success, commit, threshold), never on every tap. Whether to use haptics at all is `[PD]`. `[PD]`

## Screenshot QA

Capture at 390×844 (small iPhone) **and** 360×800 (common Android) **and** 430×932, plus one with
the keyboard open and one at 200% system text size.

1. Overlay a thumb-reach arc from the bottom-right corner (~75% of screen height radius). Is the primary action inside it? (MB-6)
2. Measure the smallest interactive element. ≥44pt? Measure gaps between adjacent targets. ≥8pt? (MB-5)
3. Screenshot on a device with a home indicator: is anything interactive inside the bottom inset? Is content clipped at the top notch? (MB-2, MB-3)
4. Scroll to the bottom, then screenshot: does the bottom bar overlap the last row? Is there bottom padding equal to the bar height + inset?
5. Open the keyboard on the last field of the longest form. Is the field visible? Is the submit reachable? (MB-18, MB-20)
6. Tap each input and screenshot the keyboard: correct type, correct return key label? (MB-16)
7. Screenshot at 200% text size: any clipped text, overlapping rows, or truncated buttons? (MB-22)
8. Count tab-bar items. ≤5? Switch tabs and return — is scroll position preserved? (MB-14)
9. Capture every sheet: grabber present, scrim present, content scrolls without dismissing the sheet? (MB-13)
10. Swipe from the left edge on every screen: does back work? Does any carousel intercept it? (MB-8, MB-9)
11. Tap a row, then screenshot after the transition ends: does the direction match the relationship? (MB-15)
12. Tap a button and screenshot immediately after releasing: is there any lingering hover styling? (MB-7)

## Adapt or override

- **Tablet and foldables break MB-4**: two-pane layouts are correct at ≥600dp width. Treat them as
  a separate breakpoint with their own reachability model (thumbs at the sides, not the bottom).
- **MB-14 (≤5 tabs)** doesn't apply to apps whose navigation is genuinely a drawer or a search-first
  model. If a drawer is chosen, the top 3 destinations still need a persistent path.
- **Games, cameras, media players, and maps** override MB-3, MB-11, MB-23 — immersive surfaces have
  their own gesture vocabulary. Document the deliberate deviation.
- **MB-21 (platform controls)** yields when the platform control cannot express the data (a custom
  date range with availability, a multi-select with search). Then match the platform's *behavior*
  (sheet presentation, momentum, dismissal) even with custom rendering.
- **Cross-platform consistency vs. platform fidelity** is `[PD]`: some brands deliberately ship one
  identical UI on both platforms. If that's the choice, still honor safe areas, system back, text
  scaling, and target sizes — those are correctness, not style.
- **Mobile web installed as PWA** needs MB-1..3 even more (no browser chrome to absorb insets), and
  must handle the missing system back on iOS with an in-app back that never dead-ends.
