---
name: mobile-web-qa
description: Audit and verify responsive web UI across iPhone, Android, tablet, and desktop. Use when the user mentions mobile web, Safari, Chrome on iPhone, iPhone SE/Pro/Pro Max, Android secondary support, tablet render, responsive bugs, keyboard behavior, safe areas, touch targets, horizontal overflow, or pre-deploy frontend QA.
---

# Mobile Web QA

Verify the interface where people actually touch it. Treat mobile QA as layout,
interaction, browser behavior, and content stress testing together.

Use `$snapshot` when visual evidence will help the user judge the result. Use
`$release-gate` before commit, push, deploy, PR, or handoff after UI changes.

## Viewport Matrix

Use project-defined breakpoints first. For general mobile work, cover:

| Target | Viewport |
| --- | --- |
| iPhone SE class | `375 x 667` |
| common iPhone | `390 x 844` or `393 x 852` |
| iPhone Pro class | `402 x 874` or `414 x 896` |
| iPhone Pro Max class | `430 x 932` |
| Android secondary | `412 x 915` |
| tablet | `820 x 1180` |
| desktop sanity | `1280 x 800` |

Use WebKit or real Safari for Safari-specific claims when available. Treat
Chrome on iOS as WebKit behavior, not desktop Chromium behavior.

## Risk-Based Coverage

Use `$efficient-execution` when choosing a reduced matrix. Start with the
changed viewport class, one adjacent mobile size, and desktop sanity for narrow
layout fixes. Run the full matrix when touching navigation, sticky/fixed
regions, forms/keyboard behavior, global layout primitives, typography scale,
responsive media, launch-critical pages, or pre-deploy QA.

Reuse screenshots only when route, build, viewport, auth/data state, scroll
position, and relevant source files match. A stale screenshot is not mobile QA.

## Audit Checklist

- first viewport, scrolled content, sticky/fixed regions, bottom bars, modals;
- safe-area spacing, notch/home-indicator areas, address bar height changes;
- virtual keyboard behavior for forms, focus rings, scroll-to-input, submit;
- tap targets, disabled/pressed/loading states, hover alternatives;
- no page-level horizontal overflow, clipped text, overlapping controls, or
  layout shift from dynamic labels/loading states;
- images, icons, fonts, shadows, borders, radii, and asset crops;
- localization, long names, empty states, error states, and slow loading;
- console errors, failed assets, and network failures.

Exercise states that commonly fail only on mobile:

- open and close nav menus, drawers, sheets, popovers, and modals;
- focus each changed form input and verify keyboard scroll/focus recovery;
- tap primary buttons twice when loading/disabled states matter;
- rotate or compare tall/short viewport behavior when sticky elements exist;
- scroll to the bottom of long pages and inside internal scroll containers.

## Browser Workflow

1. Start the local app or open the target URL.
2. Use a browser automation skill when available to capture screenshots and
   interact with the page at each viewport.
3. Capture at least one context screenshot for each risky viewport; add tight
   crops only for pixel-level details.
4. Exercise primary flows, not just static screenshots.
5. Compare against design references or existing production behavior when a
   regression is suspected.
6. Check console errors, page errors, failed network/assets, and page-level
   horizontal overflow after hydration.
7. Fix, then re-run the affected viewport and interaction checks.

Evidence is invalid if it came from the wrong route, stale build, unauthenticated
shell, hidden overlay, pre-hydration content, or a viewport different from the
one being claimed.

## Report Template

```text
Viewports:
Browsers/tools:
Routes/components:
Interactions exercised:
Screenshots:
Bugs fixed:
Skipped/unverified:
Safari/WebKit caveats:
Residual risk:
```

## Report

Summarize viewports tested, browsers/tools used, flows exercised, bugs fixed,
remaining unverified devices, and any Safari/WebKit caveats.
