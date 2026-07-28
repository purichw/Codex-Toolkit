# 09 · Motion

Motion has one job: explain what happened and where things came from. Any movement that doesn't do
that job is cost — in attention, in perceived speed, and in accessibility.

## What designers notice that developers often miss

- **Direction encodes relationship.** A panel that slides in from the right must exit to the right.
  Reversing it makes the spatial model incoherent.
- **Duration scales with distance and size.** A 24px chip and a full-screen sheet cannot share a
  250ms duration; the big one looks fast and the small one looks sluggish.
- **Exit is faster than enter.** Roughly 70% of the enter duration. Symmetric timing feels sticky.
- **Easing communicates physics.** Things entering decelerate; things leaving accelerate. Linear is
  for opacity and progress only.
- **Layout animation is the expensive kind.** Animating `height`, `width`, `top`, or `margin` costs
  frames and jitters text; `transform` and `opacity` don't.
- **Stagger has a ceiling.** Past ~4 items or ~200ms total, a staggered list feels slow rather than crafted.
- **A spinner under 400ms is a flash.** Delaying the spinner makes fast responses feel instant.
- **Reduced motion is not "no feedback".** Remove translation, keep confirmation.

## Timing reference `[CRAFT]`

| What moves | Duration | Easing | Property |
| --- | --- | --- | --- |
| Hover/press feedback | 80–120ms | `ease-out` | `background`, `border-color`, `transform: translateY(.5px)` |
| Small state change (checkbox, toggle, chip) | 120–180ms | `cubic-bezier(.2,.8,.2,1)` | `transform`, `opacity` |
| Popover / menu / tooltip enter | 140–200ms | decelerate | `opacity` + `translateY(4–8px)` + `scale(.98→1)` |
| Popover exit | 100–140ms | accelerate | `opacity` (+ small translate) |
| Drawer / sheet enter | 240–320ms | `cubic-bezier(.2,.8,.2,1)` | `transform: translateX/Y` |
| Drawer / sheet exit | 180–240ms | `cubic-bezier(.4,0,1,1)` | same |
| Scrim fade | 120–160ms in, 100–140ms out | linear/ease | `opacity` |
| Tab content swap | 100–140ms | ease-out | `opacity` + 8px directional `translateX` |
| Route/page transition | 260–360ms | decelerate | `transform` + `opacity` |
| Shared-element (list→detail) | 300–400ms | `cubic-bezier(.2,.8,.2,1)` | `transform` on the shared element |
| List stagger | 20–40ms per item, ≤4 items, ≤200ms total | ease-out | `opacity` + `translateY(6px)` |
| Skeleton shimmer | 1.2–1.6s loop | linear | `background-position` |

Anything over 400ms on a routine interaction should be justified in the PR.

## Bad patterns

| Pattern | Tell `[FACT]` | Fix |
| --- | --- | --- |
| One duration constant | Chips and full-screen sheets both 300ms | Duration tiers by distance/size |
| Symmetric enter/exit | Dismiss feels sticky | Exit ≈ 0.7 × enter |
| `transition: all` | Unintended properties animate; jank on layout | Enumerate properties |
| Animating `height`/`width`/`top` | Text reflow jitter, dropped frames | `transform`, `clip-path`, or `grid-template-rows` with `interpolate-size` |
| Bounce/overshoot on utility UI | A settings drawer springs past its edge | Overshoot only for playful/consumer moments, ≤4% |
| Spinner at 0ms | Flash on fast responses | Delay 300–400ms before showing |
| Skeleton of the wrong shape | Layout shifts when real content lands | Skeleton matches final geometry within 2px |
| Reveal-on-scroll for every section | Whole page fades up; content invisible until scrolled | Reserve for ≤2 key moments; never hide content behind it |
| Scroll hijacking | Wheel/scroll velocity overridden; trackpad feels broken | Native scroll; pin with a clear exit |
| Toast as the only success signal | Nothing on the page changes | Change the state in place, toast optional |
| Animation on every render | Element re-animates when unrelated state changes | Key the animation to the state change, not the render |
| `prefers-reduced-motion` ignored | Parallax and slide persist | Media query with opacity-only equivalents |

## Before / after

### Drawer

```css
/* ❌ animates layout, symmetric, bounces, transitions everything */
.drawer { width: 0; transition: all .3s cubic-bezier(.34,1.56,.64,1); }
.drawer.open { width: 380px; }

/* ✅ transform only, asymmetric, scrim on its own faster curve */
.scrim { opacity: 0; transition: opacity 140ms linear; }
.scrim[data-open] { opacity: 1; }

.drawer {
  width: 380px; transform: translateX(100%);
  transition: transform 200ms cubic-bezier(.4,0,1,1);           /* exit */
  will-change: transform;
}
.drawer[data-open] {
  transform: translateX(0);
  transition: transform 280ms cubic-bezier(.2,.8,.2,1);          /* enter */
}
```

### Tabs

```css
/* ❌ animates container height → content jumps and reflows */
.panel { transition: height .3s; overflow: hidden; }

/* ✅ crossfade + directional hint; indicator animates position and width */
.panel { min-height: var(--panel-min); }         /* measured from the tallest panel */
.panel[data-enter] { animation: tab-in 130ms ease-out both; }
@keyframes tab-in { from { opacity: 0; transform: translateX(var(--dir, 8px)); } }

.tabs__indicator {
  transition: transform 200ms cubic-bezier(.2,.8,.2,1), width 200ms cubic-bezier(.2,.8,.2,1);
}
```

### Feedback on an async action

```
❌  click → (nothing for 900ms) → page-level spinner → toast "Saved"

✅  0ms     button enters pending state in place (label → "Saving…", control disabled-with-reason)
    300ms   if still pending, show the inline spinner (not before)
    on done  the affected row updates visibly; button returns to rest;
             optional low-priority toast; focus unchanged
    on fail  inline error at the element, focus moved to it, retry available
```

### Reduced motion

```css
.card { animation: rise 260ms cubic-bezier(.2,.8,.2,1) both; }
@keyframes rise { from { opacity: 0; transform: translateY(12px) scale(.98); } }

@media (prefers-reduced-motion: reduce) {
  /* keep the state change, drop the movement */
  .card { animation: fade 120ms ease-out both; }
  @keyframes fade { from { opacity: 0; } }

  .drawer, .drawer[data-open] { transition-duration: 1ms; }
  .scrim { transition-duration: 80ms; }         /* opacity is fine to keep */
  .parallax { transform: none !important; }
  [data-autoplay] { animation-play-state: paused; }
}
```

## Rules

### Choreography
- **MO-1** One hero transition per interaction. If two things animate, one is subordinate (shorter, smaller, later). `[CRAFT]`
- **MO-2** Direction is consistent: an element exits the way it entered; deeper navigation always moves the same way. `[FACT]`
- **MO-3** Duration tiers by distance/size (see table). No single global duration constant. `[CRAFT]`
- **MO-4** Exit ≈ 0.7 × enter duration. `[CRAFT]`
- **MO-5** Enter decelerates, exit accelerates; linear only for opacity, progress, and shimmer. `[CRAFT]`
- **MO-6** Stagger ≤40ms per item, ≤4 items, ≤200ms total. `[FACT]`
- **MO-7** Animate `transform`/`opacity`/`clip-path` only. Layout properties require an explicit performance note. `[FACT]`
- **MO-8** Never `transition: all`. `[FACT]`

### Surfaces
- **MO-9** Drawers/sheets translate from the edge they belong to; the scrim fades faster than the panel moves. `[CRAFT]`
- **MO-10** Tab and accordion content never animates container height; reserve `min-height` or use a crossfade. `[CRAFT]`
- **MO-11** Overshoot/spring is reserved for consumer/playful moments and capped at 4% of the travel distance. Whether the brand uses springs is `[PD]`. `[PD]`
- **MO-12** A shared element between two views animates continuously (list thumbnail → detail hero) or not at all — never a crossfade between two positions. `[CRAFT]`

### Scroll
- **MO-13** Never override scroll velocity, direction, or momentum. `[FACT]`
- **MO-14** Scroll-linked effects are idempotent and reversible: scrolling up returns the exact prior state. `[FACT]`
- **MO-15** Reveal-on-scroll: ≤2 per page, ≤300ms, and content is present in the DOM and visible to search/AT regardless of scroll position. `[FACT]`
- **MO-16** Pinned/sticky sections state their length and have a visible exit; nothing is pinned for more than ~2 viewport heights. `[CRAFT]`
- **MO-17** Prefer `animation-timeline: view()`/`scroll()` or a one-shot `IntersectionObserver`; never a scroll listener that writes styles every frame. `[CRAFT]`

### Feedback
- **MO-18** Acknowledge input within 100ms with a visible change on the element touched. `[FACT]`
- **MO-19** Show a spinner only after 300–400ms of pending; below that, use the pressed/pending state. `[CRAFT]`
- **MO-20** Skeletons match the final layout within 2px and only appear when the shape is known; otherwise a delayed spinner. `[CRAFT]`
- **MO-21** Success is a visible state change on the affected object. A toast is supplementary, never the only signal. `[FACT]`
- **MO-22** Progress over 1s shows determinate progress if the total is known; over 10s the operation becomes a resumable object ([IX-32](04-interaction-design.md)). `[CRAFT]`

### Reduced motion
- **MO-23** Honor `prefers-reduced-motion: reduce` globally: remove translate/scale/parallax/auto-advance; keep opacity, color, and all state changes. `[FACT]`
- **MO-24** The reduced-motion path conveys the same information — position, direction, and change must still be readable (labels, indicators, instant state). `[FACT]`
- **MO-25** Auto-playing motion longer than 5s has a pause control regardless of the media query. `[FACT]`
- **MO-26** No motion is required to understand or complete any task. `[FACT]`

## Screenshot QA

Motion needs frame captures. Use a screen recording at 60fps and step through it, or capture at
fixed delays after the trigger.

1. Capture at 0ms, 100ms, and the end of every interaction. Is there a visible change by 100ms? (MO-18)
2. Capture the enter and exit of every overlay. Is the direction reversed correctly? Is exit shorter? (MO-2, MO-4)
3. Record a drawer open/close; check for a bounce past the edge and for scrim/panel timing. (MO-9, MO-11)
4. Record a tab switch; watch the container's bottom edge for a height jump. (MO-10)
5. Record a list appearing; count staggered items and total time. ≤4, ≤200ms? (MO-6)
6. Trigger an action on a fast connection: does a spinner flash? On 3G: does one appear by ~400ms? (MO-19)
7. Screenshot the skeleton and the loaded state; overlay them. Do the boxes land within 2px? (MO-20)
8. Complete an action and screenshot with the toast removed. Is the success still visible? (MO-21)
9. Scroll down through the page, then back up. Diff the top screenshot against the original. Identical? (MO-14)
10. Disable JS (or scroll instantly to bottom): is all content visible? (MO-15)
11. Enable reduced motion at the OS level and repeat checks 2–5. Any translation, parallax, or auto-advance left? Is every state change still visible? (MO-23, MO-24)
12. Profile one interaction in DevTools: any layout/paint spikes from animated `height`/`top`? (MO-7)

## Adapt or override

- **Consumer, games, and brand moments** legitimately exceed the timing table — a celebratory
  animation may run 800ms. It must still be skippable, non-blocking, and reduced-motion-safe. `[PD]`
- **MO-19 (delayed spinner)** flips for operations the user knows are slow (export, import, build):
  show determinate progress immediately, since absence of feedback reads as failure.
- **MO-15 (reveal-on-scroll)** — an editorial long-read can use more reveals as pacing, provided
  content is in the DOM and legible without JS.
- **MO-11 (springs)** — platform-native motion on iOS/Android *is* spring-based; matching the
  platform is correct there. Use the platform's own spring constants, not hand-tuned cubic-béziers.
- **Data visualization transitions** may run longer (400–600ms) when the animation itself carries
  meaning (a value morphing between periods). Provide the static comparison too.
- **When a reference prototype shows motion you can't reproduce cheaply**, ship the reduced version
  and log it. A janky approximation is worse than a crisp simpler transition.
