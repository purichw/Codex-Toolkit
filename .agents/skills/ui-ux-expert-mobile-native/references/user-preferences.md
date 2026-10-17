# Owner-specific preferences — read for this user's tasks

These are preserved from the owner's supplied web skill and prior audit; they are not universal
UX guidance. The owner requested this standalone native counterpart. A newer explicit request can
override them. Do not infer new brand, authentication provider, font, or framework defaults from them.

| Role | Default to preserve | Boundary and proof |
| --- | --- | --- |
| Stat/KPI card | Center icon, value, label, and support text as one balanced group in both axes | Let real content determine height; keep peer sizing intentional. Not a rule for every card or list. |
| Above-field name | Center over the actual field, including text input, select, and date/time | Required marker belongs to the label. Adjacent buttons/counters must not shift the center. |
| Select/dropdown | Center the app-owned selected value and option text, and its above-field name | Verify closed/open/error states; balance indicator space. OS-owned picker/menu internals may limit styling. |
| Date/time value | Center the app-owned displayed value in empty and populated states | Preserve native editing, locale/calendar behavior and accessibility. Never rebuild a system picker just to center it. |
| Table/grid column name, when a real table is appropriate | Center the heading together with sort/filter affordances | Body cells follow content: amounts can align trailing. Do not create a table just to apply this preference. |
| Free text, helper/error prose, body, checkbox/radio/switch captions | Readable leading alignment | For Thai/English leading is left. Support the project's RTL policy without blanket centering. |

## Native adaptation contract

A preference about an **above-field name** does not force every platform's inline settings row into
a new form. Preserve the requested form organization. Where the UI has an above-field name, apply it;
where a system-owned label/value layout cannot be changed, state that boundary. Do not silently claim
full preference compliance. Show the actual app-owned surface and system overlay separately.

If a custom selector is already part of the approved product, implement its full interaction and
assistive semantics, not just the centered text. A custom menu is not inherently prohibited; creating
one solely to bypass OS alignment is not a sound tradeoff.

Use component ownership to fix alignment, not arbitrary per-screen translations. Compare the whole
control, actual hit region, optical glyph weight, chevron clearance, and the parent column.

Brand details belong in the project's design contract: a tavern game can stay illustrated and warm;
a business form need not inherit its parchment; neither is a global skin. An approved asset stays
approved until the user asks to change it. Do not re-create character art in code as a convenience.
