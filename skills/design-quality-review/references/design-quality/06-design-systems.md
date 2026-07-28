# 06 · Design systems: taxonomy, variants, tokens, drift

A design system is a contract about where decisions live. Most decay isn't caused by bad
components — it's caused by decisions being re-made locally, one PR at a time.

## What designers notice that developers often miss

- **The count of primitives in the built product.** Designers can spot the 5th shadow and the 9th
  type size on sight. Nobody notices adding one; everyone notices the result.
- **Variant vs. new component.** Designers think in anatomy: same parts in the same arrangement =
  variant. Developers think in props, so a `Card` grows a `variant="pricing"` that shares no anatomy.
- **Tokens have layers.** A component referencing a raw palette value can't be themed. Developers
  reach for `--blue-500` because it exists.
- **Names encode intent.** `--color-danger` survives a rebrand; `--color-red` doesn't survive a
  brand whose danger color is amber.
- **Overrides are the leak.** One `style={{marginTop: 13}}` doesn't matter; 400 of them are the
  system's actual spacing scale.
- **The gallery is the source of truth.** If there's no page showing every component in every state,
  drift is undetectable and reviews are guesswork.

## Bad patterns

| Pattern | Tell `[FACT]` | Cost |
| --- | --- | --- |
| **Boolean explosion** | `<Button primary secondary large small danger loading icon compact>` | Invalid combinations are representable; every new state multiplies test surface |
| **Appearance names** | `--color-blue-600`, `.card-gray`, `<Badge color="green">` | Rebrand and theming require touching every call site |
| **Skipped semantic layer** | Components reference palette primitives directly | Dark mode requires per-component patches |
| **One-off props** | `<Table stickyFirstColWithShadowOnMobile>` | System becomes a union of page requirements |
| **Copy-forked components** | `Button2`, `CardNew`, `ModalV3`, `TableLegacy` all in use | Fixes land in one fork; states diverge |
| **Wrapper drift** | Every page wraps the component to patch spacing | The system's spacing is fiction |
| **Undocumented escape hatches** | `className`/`style` passthrough used on 60% of instances | The component defines nothing |
| **No gallery** | No page renders every variant × state | Drift found by customers |
| **Token aliasing loops** | `--surface: var(--card-bg); --card-bg: var(--surface)` | Silent fallback to invalid values |
| **Component owns layout** | `Card` has `margin-bottom: 24px` | Reuse impossible without override |

## 1. Component taxonomy

Four tiers. Every element belongs to exactly one.

| Tier | Definition | Examples | Rule of thumb |
| --- | --- | --- | --- |
| **Primitive** | No product semantics; pure rendering | `Text`, `Box`, `Icon`, `VisuallyHidden` | Never contains business logic or copy |
| **Component** | One interactive/semantic unit | `Button`, `Field`, `Select`, `Table`, `Sheet` | Owns its states; owns no layout margin |
| **Pattern** | A named arrangement of components solving a recurring task | `EmptyState`, `BulkActionBar`, `FilterSet`, `PageHeader` | Owns internal layout; may hold copy props |
| **Screen** | A route; assembles patterns; owns data | `OrdersList`, `Checkout` | Not in the system; may not export parts |

**Variant vs. new component test:**

1. Same anatomy (same parts, same arrangement, same slots)? →
2. Same semantics (a user would call both "the same kind of thing")? →
3. Same states (hover/focus/disabled/loading behave identically)?

All three yes → **variant**. Any no → **new component**, possibly sharing primitives.

```
Same anatomy, same semantics → variant
  Button: intent=neutral|accent|danger  ×  emphasis=filled|outline|ghost  ×  size=sm|md|lg

Different anatomy → separate components
  Button  vs.  IconButton (square, no label, needs accessible name, different min size)
  Card    vs.  StatTile   (single metric + delta + sparkline: different parts entirely)
```

**Rules**
- **DS-1** Every exported UI element is tagged with its tier; components never set outer margin, and patterns never fetch data. `[CRAFT]`
- **DS-2** Apply the three-question test before adding a variant. Record the answer in the PR. `[CRAFT]`
- **DS-3** The 3rd occurrence of a local pattern promotes it into the system; the 1st and 2nd stay local. `[CRAFT]`

## 2. Variants

Model variants as **enumerated axes**, never as booleans.

```tsx
// ❌ 8 booleans = 256 representable states, most invalid
<Button primary danger large loading iconOnly block compact rounded />

// ✅ 3 axes, 27 valid combinations, invalid ones unrepresentable
type ButtonProps = {
  intent?: 'neutral' | 'accent' | 'danger';
  emphasis?: 'filled' | 'outline' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;          // state, not variant
  disabledReason?: string;    // disabled requires a reason (IX-21)
};
```

- **DS-4** Variants are enums on named axes (intent × emphasis × size). Booleans are reserved for *states* (loading, selected, invalid). `[CRAFT]`
- **DS-5** ≤3 variant axes per component. A 4th axis means you have two components. `[CRAFT]`
- **DS-6** Every axis combination either renders correctly or fails at the type level. No silently-wrong combinations. `[FACT]`
- **DS-7** New variants require a second real use case. One page's need is a local override, not a variant. `[CRAFT]`

## 3. Token layering

Three layers, strict direction of reference.

```css
/* Layer 1 — primitives. Raw values. Referenced ONLY by layer 2. */
:root {
  --palette-neutral-100: #f3f2f2;
  --palette-neutral-900: #201f1d;
  --palette-accent-500:  #b68235;
  --palette-accent-700:  #7d5a24;
  --size-1: 4px; --size-2: 8px; --size-3: 12px; --size-4: 16px;
}

/* Layer 2 — semantic. Roles. This is the theming surface. */
:root {
  --color-bg:            var(--palette-neutral-100);
  --color-text:          var(--palette-neutral-900);
  --color-text-muted:    color-mix(in oklch, var(--color-text) 62%, var(--color-bg));
  --color-border:        color-mix(in oklch, var(--color-text) 18%, var(--color-bg));
  --color-accent:        var(--palette-accent-500);
  --color-accent-strong: var(--palette-accent-700);
  --space-inset:         var(--size-4);
  --space-stack:         var(--size-3);
}

/* Layer 3 — component. Optional; only when a component needs its own knob. */
:root {
  --button-height-md:   36px;
  --button-bg-hover:    color-mix(in oklch, var(--color-accent) 8%, transparent);
  --button-border:      var(--color-accent);
}

/* Components consume layer 2 or 3. NEVER layer 1. */
.btn { height: var(--button-height-md); border: 1px solid var(--button-border);
       color: var(--color-accent-strong); padding-inline: var(--space-inset); }
.btn:hover { background: var(--button-bg-hover); }
```

**Theming happens at layer 2 only:**

```css
[data-theme="dark"] {
  --color-bg:   var(--palette-neutral-900);
  --color-text: var(--palette-neutral-100);
  --color-accent: var(--palette-accent-400);   /* accents shift on dark grounds */
}
```

- **DS-8** Components reference semantic or component tokens only. A palette token in component code is S2. `[FACT]`
- **DS-9** Theming is achieved by redefining layer 2. If a theme needs component-level patches, the semantic layer is incomplete. `[CRAFT]`
- **DS-10** Every semantic token has a documented role sentence ("border of a resting, non-interactive surface"). Undocumented tokens get misused. `[CRAFT]`
- **DS-11** Contrast pairs are tokenized together (`--color-accent` / `--color-on-accent`) and verified per theme, not per instance. `[FACT]`
- **DS-12** No token references a token in the same layer more than one hop deep; no cycles. `[FACT]`

## 4. Naming

| Do | Don't | Why |
| --- | --- | --- |
| `--color-danger` | `--color-red` | Survives brand change |
| `--color-surface-raised` | `--color-white-2` | Describes role and elevation |
| `--space-stack-sm` | `--gap-8` | Value can change; role can't |
| `--color-text-muted` | `--color-gray-600` | Contrast obligation is in the name |
| `intent="danger"` | `color="red"` | Enum reads as meaning |
| `emphasis="ghost"` | `transparent={true}` | Nameable third option |
| `StatTile` | `Card2` | Anatomy in the name |

**Pattern:** `--<category>-<role>-<modifier>-<state>` — `--color-border-subtle-hover`,
`--space-inset-lg`. Order is fixed so tokens sort usefully.

- **DS-13** Names describe role, not appearance; state is a suffix, not a separate token family. `[CRAFT]`
- **DS-14** No numeric suffixes to disambiguate two things with the same name (`accent-2`, `Card2`). If two exist, one of them needs a real name — or shouldn't exist. `[CRAFT]`
- **DS-15** One vocabulary across code, tokens, and design-tool layer names. Renames land in all three in the same change. `[CRAFT]`

## 5. Drift detection

Run these as CI checks, not as review vibes.

```bash
# Hex literals outside the token file
rg -n '#[0-9a-fA-F]{3,8}\b' src --glob '!**/tokens.css'

# Off-scale spacing / sizing (allow only the scale + 0/1px/100%/auto)
rg -n '(margin|padding|gap|top|left|right|bottom)\s*:\s*(?!0|1px|auto)\d+px' src

# Raw palette tokens used inside components
rg -n 'var\(--palette-' src/components

# Inline style escape hatches
rg -c 'style=\{\{' src | sort -t: -k2 -rn | head -20

# Forked components
rg -n 'export (const|function|class) (\w+)(2|New|V\d|Legacy|Copy)\b' src
```

**Metric baseline** — record these numbers per release and treat increases as review triggers `[FACT]`:

| Metric | Healthy | Investigate |
| --- | --- | --- |
| Distinct `border-radius` values in the build | ≤4 | ≥6 |
| Distinct `box-shadow` definitions | ≤4 | ≥6 |
| Distinct `font-size` values | ≤8 | ≥12 |
| Distinct `font-weight` values | ≤3 | ≥5 |
| Distinct color literals outside tokens | 0 | ≥1 |
| Off-scale spacing occurrences | 0 | ≥1 per 1k lines |
| Instances using `style`/`className` passthrough | <10% of instances | >25% |

- **DS-16** A gallery route renders every component × variant × state, including empty/error/long-content, and is the target of visual regression tests. `[CRAFT]`
- **DS-17** The drift metrics above are computed in CI; regressions require an explicit exemption comment naming the reason. `[CRAFT]`
- **DS-18** Escape hatches are allowed but counted. When one component's passthrough rate exceeds 25%, the component is wrong, not the pages. `[CRAFT]`
- **DS-19** Deprecation is a two-step with a codemod and a date; forks are never left in parallel use. `[CRAFT]`

## Before / after

```tsx
// ❌ page patches the system
<Card className="mt-[13px] rounded-xl shadow-lg">
  <div style={{ padding: 18, color: '#6b7280' }}>
    <h3 style={{ fontSize: 17, fontWeight: 700 }}>Usage</h3>
    <p style={{ fontSize: 13 }}>4,201 requests</p>
  </div>
</Card>

// ✅ layout outside, tokens inside, one new pattern promoted after its 3rd use
<Stack gap="stack-md">
  <StatTile label="Usage" value={4201} unit="requests" period="last 30 days" />
</Stack>
```

The `StatTile` is a new **component** (different anatomy from `Card`), consumes semantic tokens,
sets no outer margin, and renders its own empty/loading/error states.

## Screenshot QA

1. Open the gallery route. Screenshot it. Any variant missing a state cell? (DS-16)
2. In the gallery screenshot, count distinct radii, shadows, type sizes, weights. Compare to the baseline table. (DS-17)
3. Toggle every theme in the gallery and screenshot each. Anything unreadable, any element that didn't change? (DS-9, DS-11)
4. Screenshot the same component on 3 different pages side by side. Any difference in padding, radius, or height? That's wrapper drift. (DS-18)
5. Set the longest realistic label on every variant in the gallery. Any clipping, wrap, or height change that breaks alignment? (DS-6)
6. Grayscale the gallery: do `intent` variants remain distinguishable by more than hue? (DS-13, [AX-19](10-accessibility.md))
7. Zoom the gallery to 200%: does every component reflow without clipping? (DS-16)
8. Diff this release's gallery screenshot against the last one. Every pixel change intentional and named in the PR? (DS-17)

## Adapt or override

- **Early-stage products should not build layer 3.** Two layers (palette → semantic) is enough
  until a component genuinely needs a knob. Premature component tokens are their own kind of drift.
- **A single-brand product may skip theming** but still needs the semantic layer for dark mode,
  high-contrast, and print. Whether to support those is `[PD]`.
- **DS-5 (≤3 axes)** stretches for genuinely multi-dimensional primitives (`Text`: size × weight ×
  tone × align). Judge by whether combinations are independently meaningful.
- **DS-3 (rule of three)** is a floor, not a ceiling: promote earlier when the pattern encodes a
  correctness rule (money formatting, destructive confirmation) that must not vary.
- **Third-party or platform components** (payment fields, map controls, native pickers) can't be
  token-styled. Wrap them, match the nearest tokens available, and document the deviation instead of
  fighting the vendor.
- **When the design file and the code disagree**, the design file wins for *visual* values and the
  code wins for *state completeness* — designers routinely omit states the code must have.
