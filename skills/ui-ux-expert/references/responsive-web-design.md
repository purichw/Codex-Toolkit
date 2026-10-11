# Full Website Responsiveness

Use this reference when designing, implementing, or QAing responsive web UI across
viewport sizes, operating systems, browser engines, input models, media, zoom,
and mobile performance. It complements the main `ui-ux-expert` craft rules and
the `mobile-web-qa` viewport workflow.

## Table of Contents

- [Mental Model](#mental-model)
- [Foundation](#foundation)
- [Layout Strategy](#layout-strategy)
- [Mobile Viewport Height](#mobile-viewport-height)
- [iOS and Android](#ios-and-android)
- [Platform Details](#platform-details)
- [Input Model](#input-model)
- [Browser Engines](#browser-engines)
- [Responsive Media](#responsive-media)
- [Accessibility and Preferences](#accessibility-and-preferences)
- [Performance](#performance)
- [Testing Workflow](#testing-workflow)
- [Pre-Ship Checklist](#pre-ship-checklist)

## Mental Model

Responsiveness is three interacting axes:

| Axis | What varies | Common failure |
| --- | --- | --- |
| Viewport/layout | width, height, orientation, density | overflow, cramped/empty layouts, tiny targets |
| Platform/OS | fonts, controls, safe areas, keyboard, scroll physics | clipped notches, janky scroll, ugly widgets |
| Browser/engine | CSS support, JS APIs, default styles | layout drift, missing features, silent failures |

Design for capabilities and layout pressure, not a fixed list of devices.

## Foundation

Start every web project with:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

Do not use `maximum-scale=1` or `user-scalable=no`; blocking zoom fails
accessibility. Use `viewport-fit=cover` so iOS safe-area variables work.

```css
*, *::before, *::after { box-sizing: border-box; }
html, body { margin: 0; }
body { text-rendering: optimizeLegibility; }
img, picture, video, canvas, svg { display: block; max-width: 100%; height: auto; }
html { -webkit-text-size-adjust: 100%; }
```

## Layout Strategy

- Author mobile-first base styles, then add `min-width` breakpoints upward.
- Place breakpoints where content breaks, not at device brand names.
- Resize continuously from about `320px` upward and fix the first breakage.
- Prefer intrinsic CSS before media queries:
  - `repeat(auto-fill, minmax(260px, 1fr))` for card grids.
  - Bounded spacing with `min()`/`clamp()`; use role-based text sizes, not
    viewport-width font scaling. Let text wrap and containers grow.
  - `min()`, `max()`, and `minmax()` for widths/gutters.
  - Container queries for reusable components inside sidebars, drawers, or
    narrow columns.
- Use Flexbox for one-dimensional wrapping rows/columns and Grid for
  two-dimensional layout.
- Use `gap` for sibling spacing. Avoid per-item margins that break on wrap.
- Avoid fixed heights around text. Use `min-height` and let content grow.
- Diagnose overflowing children, minimum sizes and grid tracks. Do not use
  page-level `overflow-x:hidden` to conceal clipped content or focus rings.
- Test short landscape phones and split-screen tablets; height is a constraint.

## Mobile Viewport Height

`100vh` is often taller than the visible mobile viewport because browser chrome
appears and disappears. For full-height sections:

```css
.hero {
  min-height: 100vh;  /* fallback */
  min-height: 100svh; /* safe visible height */
}
```

Use `svh` for always-visible layouts and `dvh` when the section should track
dynamic browser bars.

## iOS and Android

iOS Safari needs explicit care:

- Pad fixed top/bottom UI with `env(safe-area-inset-*)`.
- Keep form-control text at `16px` or larger to prevent input-focus zoom.
- Test sticky/fixed bars with the keyboard; use `visualViewport` when needed.
- Use `overscroll-behavior: contain` for internal scroll containers when page
  rubber-banding is disruptive.
- Verify the actual browser engine and supported OS/region. Safari is WebKit;
  do not infer every installed iOS browser's engine from its platform alone.
  Apple documents [alternative engines](https://developer.apple.com/support/alternative-browser-engines/)
  under specific conditions (checked 2026-10-12).

Android needs breadth:

- Rely on fluid layout and responsive media, not hardcoded dimensions.
- Test Chrome address-bar resize and software-keyboard resizing.
- Check important flows in relevant Android WebViews/in-app browsers.
- Respect system back gestures and horizontal edge swipes.

## Platform Details

- Use a robust stack such as
  `system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`.
- Self-host brand fonts when visual consistency matters.
- Native controls and scrollbars vary by OS/browser. Either accept them or
  restyle deliberately with the affordance rebuilt.
- Use `scrollbar-gutter: stable` when scrollbar appearance would shift layout.
- Do not rely on emoji or system glyph rendering for meaning.

## Input Model

Screen size is not the same as input mode. Touch laptops and iPads with trackpads
can have both coarse and fine pointers.

```css
@media (hover: hover) and (pointer: fine) {
  .button:hover { background: var(--accent); }
}

@media (pointer: coarse) {
  .button { min-height: 44px; min-width: 44px; }
}
```

- Never hide essential content or actions behind hover.
- Around `44 x 44` CSS px is a touch-comfort default, not a universal AA
  threshold or a native-unit conversion. See
  [accessibility-checks.md](accessibility-checks.md) for targets and exceptions.
- Use Pointer Events for shared mouse/touch/pen interactions where appropriate.
- Correct viewport meta prevents old tap-delay problems.

## Browser Engines

Test engines, not browser logos:

- Blink: Chrome, Edge, Opera, most Android, Android WebView.
- WebKit: Safari and browsers that actually use WebKit on the tested platform.
- Gecko: Firefox.

Use progressive enhancement:

```css
@supports (display: grid) { /* enhanced layout */ }
@supports not (aspect-ratio: 1) { /* fallback */ }
```

```js
if ("IntersectionObserver" in window) {
  // enhanced behavior
} else {
  // fallback
}
```

Detect features, not user agents. Check current support before shipping recent
CSS/JS features, and provide a usable fallback below the support baseline.

## Responsive Media

```html
<img
  src="hero-800.jpg"
  srcset="hero-400.jpg 400w, hero-800.jpg 800w, hero-1600.jpg 1600w"
  sizes="(min-width: 768px) 50vw, 100vw"
  width="1600"
  height="900"
  alt=""
  loading="lazy"
  decoding="async">
```

- Use `srcset`/`sizes` for density and viewport-appropriate images.
- Use `<picture>` for format fallback or art direction.
- Always reserve space with `width`/`height` or `aspect-ratio` to prevent CLS.
- Use `object-fit: cover` only when cropping is acceptable and intentional.

## Accessibility and Preferences

- Use relative units (`rem`, `em`, `%`, `ch`) where user zoom/settings should scale.
- Check text enlargement and browser zoom separately from viewport emulation.
  Reflow should preserve content/operation at the relevant 320-CSS-pixel
  equivalent; genuinely two-dimensional regions have exceptions. See the
  accessibility reference rather than treating all horizontal scroll as failure.
- Honor `prefers-reduced-motion` and any supported color-scheme choices.
- Keep focus states visible and keyboard paths usable at every viewport.
- Maintain readable measure, usually `60-75ch`, on wide screens.

## Performance

Responsive also means fast on a mid-range phone:

- Ship less JS/CSS; code-split where helpful.
- Lazy-load below-the-fold images and iframes.
- Avoid layout thrash; batch DOM reads/writes.
- Animate `transform` and `opacity`, not layout properties.
- Use `content-visibility: auto` for long offscreen sections when suitable.
- Test with throttled CPU/network and, when possible, a low-end Android device.
- Watch LCP, INP, and CLS.

## Testing Workflow

1. Resize continuously from about `320px` to desktop widths.
2. Use device presets for fast checks, but treat them as approximations.
3. Test real devices for iOS safe areas, keyboard behavior, scroll physics,
   font rendering, touch accuracy, WebViews, and performance.
4. Cover at least one WebKit device, one Blink/Android device, and Firefox/Gecko
   when making cross-browser claims.
5. Rotate devices and test short landscape viewports.
6. Zoom to `200%` and `400%`; navigate by keyboard.
7. Automate cross-browser regressions when the support matrix is large.

## Pre-Ship Checklist

- [ ] Correct viewport meta with `viewport-fit=cover`; no zoom blocking.
- [ ] Global box sizing; no page-level horizontal overflow at any width.
- [ ] Mobile-first layout with breakpoints where content actually breaks.
- [ ] Intrinsic grids, bounded spacing, role-based type and content-driven reflow.
- [ ] `svh`/`dvh` used instead of raw `100vh` for full-height mobile sections.
- [ ] iOS safe areas and form input zoom behavior handled.
- [ ] Android keyboard resize and relevant WebViews checked.
- [ ] Targets meet applicable size/spacing criteria and are comfortable for the
  intended input; essential actions are not hover-only.
- [ ] Robust font stack and deliberate native-control/scrollbar handling.
- [ ] Feature detection used; no brittle user-agent sniffing.
- [ ] WebKit, Blink, Gecko, and key WebViews tested as required.
- [ ] Responsive images reserve space and use `srcset`/`sizes`/fallbacks.
- [ ] Motion/user preferences and `200%`/`400%` zoom reflow verified.
- [ ] LCP, INP, and CLS checked on throttled mobile conditions.
