---
name: global-visual-diagnosis
description: Global reusable alias for the canonical visual-diagnosis skill. Use when the user asks for $global-visual-diagnosis, says this should be global or non-project-specific, or wants the reusable version of visual diagnosis. This alias routes to visual-diagnosis/SKILL.md; keep visual-diagnosis as the source of truth.
---

# Global Visual Diagnosis

This is a global alias for the canonical `visual-diagnosis` skill.

Before acting, read and follow the canonical skill:

```text
../visual-diagnosis/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements whenever they apply. Do not treat this global alias as a way to bypass the canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `visual-diagnosis` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
