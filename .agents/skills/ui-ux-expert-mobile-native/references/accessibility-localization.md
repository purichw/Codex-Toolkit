# Accessibility, language, and usable native text

Read when text or interaction changes. Sources [A1, A2, A4, D1, D2, R1, F3] are indexed in
[sources](sources.md). Platform guidance is a floor for testing, not a certificate of accessibility.

## Test people-facing output, not only semantics in source

Use VoiceOver on iOS and TalkBack on Android for the changed flow when making assistive-use claims.
Inspect useful names, roles, values, selected/disabled/expanded states, focus order, error feedback,
and focus restoration after dismissal. Avoid announcing the same decorative icon and label twice;
do not merge a row so aggressively that secondary actions disappear. A semantics tree helps locate
bugs but does not establish task completion with an assistive technology.

Native touch checks must use the platform's units and actual hit regions. Apple design guidance uses
44×44 pt for touch controls [A1]; Android guidance uses 48 dp minimum targets [D1]. These are not CSS
pixels and not rules to make every glyph that large. Check expanded hit areas do not overlap neighboring
actions. System-owned controls may have platform behavior that the app cannot restyle.

## Readability and scaling

Use semantic text styles and the platform/stack scaling mechanism. Check default and a meaningful
large/accessibility size on the target OS. Record the exact setting, not simply “200%.” Never use a
browser zoom or an image resize as proof of native text scaling. Bold text, display size, contrast,
reduced motion and relevant appearance settings deserve separate checks where the affected design
relies on them. Do not silently cap scaling or downsize all text to repair a crowded row.

For non-system styles, establish foreground/background contrast in actual states, including imagery,
translucency and disabled/selected/error states. Use the appropriate text and non-text criteria from
current guidance, not one universal ratio or a token name. Apple/Android sources discuss these [A2, D2].
Color is not the only status signal. Decorative texture must not be the text's readability mechanism.

## Thai, English, and real content pressure

Use a font with the required script/weight coverage and lawful project assets. Do not ship fonts from
the skill package. Test Thai marks above/below glyphs, punctuation, multi-line field names, long names,
addresses, email, currency, negative/large numbers, 0, unknowns, and mixed-language strings. Do not add
Latin-style tracking to Thai by default or split text by byte count. Required truncation needs an
accessible way to reach the full value; not every headline or error is safely truncatable.

Format dates, times, numbers and currencies with locale-aware facilities and the product's explicit
calendar/timezone rules. Do not assume every Thai product uses a Buddhist calendar, or convert stored
instants merely to match a screenshot. Keep labels outside a field readable while value editing remains
natural. Honor [owner preferences](user-preferences.md), not blanket centering.

If RTL is supported, test actual locale, directional icons, logical leading/trailing alignment and
mixed-direction numbers. Do not declare RTL support just because the layout library has such a flag.

## Input and recovery

Choose an appropriate keyboard/content type and return action; preserve paste/autofill/selection where
safe and relevant. Let the real keyboard, text selection menu, permission dialog or picker appear during
the test. Check that first-error focus and keyboard dismissal do not trap or erase user input. Screen
reader and larger text testing cannot be replaced by screenshot contrast tooling.

Report each unavailable assistive/device check as untested. Do not claim legal compliance from this guide.
