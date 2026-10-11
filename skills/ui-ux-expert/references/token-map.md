# Token Roles, Not A Universal Theme

Use the project's own tokens first. [../tokens.css](../tokens.css) is a small,
optional light-theme starting point for genuinely unbranded work. It defines
custom properties only; it must not silently reset existing pages.
[../assets/gallery-base.css](../assets/gallery-base.css) styles the standalone
gallery and is not part of the token contract.

## Role Map

| Role | Fallback | Use / check |
| --- | --- | --- |
| Canvas / surface | `--bg` / `--surface` | Page versus objects/overlays. They may intentionally match in a flat design. |
| Primary / secondary text | `--ink` / `--muted` | Hierarchy without sacrificing readability. |
| Lower-emphasis text | `--faint` | Still meet text contrast when information is readable content, including placeholders. Not an exemption for timestamps. |
| Divider / control boundary | `--border` / `--control-border` | A decorative divider need not meet the same role as a boundary necessary to identify an input. |
| Action / on-action | `--accent` / `--accent-ink` | Verify the actual pair, including hover/active. |
| Selected surface | `--accent-soft` | Translucency depends on the surface underneath; verify composited colors. |
| Semantic feedback | `--success` / `--danger` | Pair with words/icons. Add named warning/info roles if needed. |
| Space | `--s1` to `--s9` | Reuse steps for rhythm; a real unmet role can justify an extension. |
| Type / leading | `--t-xs` to `--t-4xl`, `--lh-*` | Match hierarchy, container, script and viewing distance; do not force one ratio everywhere. |
| Shape / depth | `--radius*`, `--shadow-*` | Coherent role families; use the project's existing language. |
| Motion | `--dur-fast`, `--dur`, `--ease-out` | Starting durations, not correctness limits. Honor reduced motion. |

## Adaptation Contract

- Reuse by semantic role, not by coincidental visual resemblance. Do not use
  success green for arbitrary selected navigation just because it matches.
- Prefer an existing token when it fits. If it does not, identify the unmet role,
  define the smallest coherent extension at the owner, and check affected users.
  Tiny optical corrections and borders need not create a new global token.
- Retheming may change hue, luminance, chroma, density, scales and geometry.
  "Only change accent hue" is not a design system and may break contrast.
- Multiple accents, dark surfaces, pure black/white, different radii, or a border
  plus shadow are not failures by themselves. Judge hierarchy, brand coherence,
  and applicable instructions. Avoid gratuitous competing emphasis.
- Keep `tokens.css` declaration-only. Put optional reset/base rules in an explicit
  opt-in stylesheet with scoped selectors. Document migration impact when
  changing an existing token's role or value.
- Test tokens at use sites: light/dark or overlay surfaces as supported,
  text-on-accent, tinted status text, focus/control boundaries and disabled
  reasons. A token file passing syntax checks does not prove rendered contrast.

See [accessibility-checks.md](accessibility-checks.md) for contrast criteria,
[contextual-rules.md](contextual-rules.md) for applicability, and
`$design-system-guardian` for shared-owner changes.
