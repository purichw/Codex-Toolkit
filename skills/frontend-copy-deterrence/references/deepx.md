# DeepX public copy controls

Use the active DeepX checkout. See `docs/CONTENT_PROTECTION.md` for the owner's
public copy policy and dated evidence. The direction is to make casual copying
harder while keeping discovery, normal editing and public navigation usable.

| Responsibility | Source |
| --- | --- |
| Route predicate, scoped event guards, listener disposal | `src/security/content-protection.ts` |
| Selection, media drag and touch-callout styling | `src/security/content-protection.css` |
| Application and error entrypoints | `src/main.tsx`, `src/errors/error-entry.tsx` |

The shared module applies the `deepx-protected` HTML class for published
surfaces. Its class and event predicate exempt `/admin` and descendants and
`/studio/ideas/:category/cms` and descendants, including preview routes in
those families. The class synchronizes on history navigation. When adding
another client-side navigation path or entrypoint, verify its real transition
and the resulting class and event behavior.

On protected pages the module handles copy, cut, selection, drag, context menu
and the document selection/copy/cut shortcuts. It permits normal context
menus on links and controls, with a media exception for a linked image.
The supported editing escape hatches are native text fields, editable regions
and `data-allow-copy`. Review both CSS inheritance and event handling if
expanding an exception, particularly for nested images or custom widgets.
The existing implementation cancels events without inspecting or replacing
clipboard data and uses silence as the feedback behavior.

Use a published DeepX page and representative demo for the interaction check,
and a Content Studio or category CMS route for the exception. Verify a form,
a deliberate copy action, a normal navigation menu and the route transition.
Test long press on the actual browser in scope. Keep semantic markup and
crawlable HTML intact. Use the build and exposure skill for source packages,
public API reads or private media.
