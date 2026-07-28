---
name: global-design-quality-review
description: Global reusable alias for the canonical design-quality-review skill. Use when the user asks for $global-design-quality-review, says this should be global or non-project-specific, or wants the reusable version of design quality review. This alias routes to design-quality-review/SKILL.md; keep design-quality-review as the source of truth.
---

# Global Design Quality Review

This is a global alias for the canonical `design-quality-review` skill.

Before acting, read and follow the canonical skill:

```text
../design-quality-review/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements whenever they apply. Do not treat this global alias as a way to bypass the canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `design-quality-review` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
