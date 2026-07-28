---
name: global-domain-taste
description: Global reusable alias for the canonical domain-taste skill. Use when the user asks for $global-domain-taste, says this should be global or non-project-specific, or wants the reusable version of domain taste. This alias routes to domain-taste/SKILL.md; keep domain-taste as the source of truth.
---

# Global Domain Taste

This is a global alias for the canonical `domain-taste` skill.

Before acting, read and follow the canonical skill:

```text
../domain-taste/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements whenever they apply. Do not treat this global alias as a way to bypass the canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `domain-taste` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
