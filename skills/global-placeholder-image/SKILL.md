---
name: global-placeholder-image
description: Global reusable alias for the canonical placeholder-image skill. Use when the user asks for $global-placeholder-image, says this should be global or non-project-specific, or wants the reusable version of placeholder image. This alias routes to placeholder-image/SKILL.md; keep placeholder-image as the source of truth.
---

# Global Placeholder Image

This is a global alias for the canonical `placeholder-image` skill.

Before acting, read and follow the canonical skill:

```text
../placeholder-image/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `placeholder-image` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
