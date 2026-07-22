---
name: global-export-html
description: Global reusable alias for the canonical export-html skill. Use when the user asks for $global-export-html, says this should be global or non-project-specific, or wants the reusable version of export html. This alias routes to export-html/SKILL.md; keep export-html as the source of truth.
---

# Global Export Html

This is a global alias for the canonical `export-html` skill.

Before acting, read and follow the canonical skill:

```text
../export-html/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `export-html` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
