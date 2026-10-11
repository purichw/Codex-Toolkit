# Accessibility Checks And Platform Claims

Use current primary sources for compliance claims. The following distinctions
were checked on 2026-10-12; this is a targeted checklist, not certification.

- **Text:** WCAG 2.2 AA generally requires 4.5:1, or 3:1 for large text (18pt
  regular / 14pt bold, with equivalent script considerations). Placeholder text
  is text, not automatically exempt. Inactive controls, incidental decoration and
  logos have specific exceptions. Measure specified/composited foreground and
  background, not antialiased glyph-edge pixels; do not round a failure up.
  [W3C contrast explanation](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- **Non-text UI:** 3:1 applies to visual information needed to identify active
  components/states and relevant graphics against adjacent colors, with
  exceptions. It does not mean every divider must pass or every button label
  only needs 3:1.
  [W3C non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
- **Targets:** AA SC 2.5.8 uses 24 by 24 CSS px or permitted exceptions, including
  sufficient spacing, inline targets, equivalent controls, user-agent controls
  and essential presentation. Inspect actual hit regions. Around 44px is a
  useful touch-comfort default, not a universal AA minimum or a reason to force
  44px line-height on inline links.
  [W3C target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).
- **Reflow:** test the relevant 320-CSS-pixel equivalent for vertically scrolling
  content; genuinely two-dimensional content has exceptions. Keep zoom enabled.
  Narrow-viewport screenshots alone do not establish text-resize, browser zoom,
  keyboard or assistive-technology behavior.
  [W3C reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).
- **Interaction:** exercise actual keyboard order, visible focus, accessible
  names, modal/background behavior, recovery and reduced motion for touched
  controls. Static ARIA attributes and screenshot simulations are not tests.
- **Platform:** record actual OS/browser/engine/version, not a device-preset
  name. Chromium at phone dimensions does not test Safari, a native picker or
  the software keyboard. Avoid "all iOS browsers use WebKit": Apple supports
  qualifying alternative engines under specific regional/platform conditions.
  [Apple engine support](https://developer.apple.com/support/alternative-browser-engines/).

Use available accessibility/interaction specialists for deeper work. Report
untested engines, assistive technologies and conditions explicitly.
