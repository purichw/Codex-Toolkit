---
name: frontend-copy-deterrence
description: Deter casual copying of public website text, photos and media via selection, copy, drag, context menus and touch interactions. Use to design, implement or test public-page copy controls while preserving CMS editing, accessible navigation and deliberate sharing actions.
---

# Frontend Copy Deterrence

Use public-page interaction controls to make casual copying less convenient.
Treat rendered text, images and video as observable, including through
screenshots and assistive tools. Deliver only the media derivatives intended
for public viewing. Use [frontend-source-protection](../frontend-source-protection/SKILL.md)
when the request concerns private originals, build exposure, or bulk API reads.

## Identify the protected surfaces

1. Find the shared public shell and independent entrypoints such as demos,
   embedded views and standalone errors that are in scope. Identify the
   editing and preview routes and existing copy/download actions before
   changing their common owner.
2. Apply a named CSS class or attribute to the intended content region. Use
   route-level coverage when the requested policy spans a public site.
   Keep the route or region predicate shared by styling and event handlers.
   Preserve server-rendered text, semantic structure, image alt text and the
   site's existing crawlable content.
3. Retain selection, editing and paste for native inputs, contenteditable and
   custom text editors. Provide a narrow, explicit opt-out for intentional
   copy regions such as contact details, booking references or code examples.
   Preserve both pointer and keyboard links, controls, focus, labels, media
   playback and user-facing copy or share buttons.

## Apply the appropriate deterrent

- For text, use scoped selection CSS and cancel relevant copy/cut events on
  protected content. Resolve the event target, focus and selection when a
  document-level event could affect a nested editable control or opt-out.
  Canceling a copy should leave the existing clipboard intact.
- For media, scope drag, image context-menu or browser-specific touch-callout
  behavior to the requested surface. Test linked images separately from text
  links. Keep normal navigation and media controls usable. Consider a preview
  derivative or watermark when the owner wants a visible attribution or a
  smaller publicly delivered file. Check delivered URLs in `src`, `srcset`,
  posters and downloads when keeping an original private.
- Keep the implementation quiet and event-driven. Limit any shortcut
  interception to the requested copying flow. Preserve ordinary shortcuts,
  browser controls, assistive navigation and diagnostics. Register shared
  listeners once per document, synchronize on the actual route transition
  mechanism and remove them when their owner unmounts or reloads.
- For DeepX, read [the project example](references/deepx.md) for its existing
  guard, route exclusions and editable exceptions. Extend that owner when
  changing the DeepX behavior.

## Verify everyday use

- Try the requested copy/selection, right-click or drag action on a rendered
  public route. Try a linked image, a normal text link, a form input and an
  intentional copy action in the same build.
- Open a representative CMS or preview, type and select text, use copy/paste,
  and verify keyboard navigation and focus. Exercise a public-to-exempt
  transition and back when both share a router.
- Verify the touch interaction on the relevant browser or device when touch
  behavior matters. A mobile-sized capture can show layout. Report long-press
  and native menu behavior based on the platform actually exercised. Describe
  the specific deterrence shown and the exceptions retained.
