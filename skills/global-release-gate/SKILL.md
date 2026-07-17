---
name: global-release-gate
description: Global reusable alias for the canonical release-gate skill. Use when the user asks for $global-release-gate, says this should be global or non-project-specific, or wants the reusable version of release gate. This alias routes to release-gate/SKILL.md; keep release-gate as the source of truth.
---

# Global Release Gate

This is a global alias for the canonical `release-gate` skill.

Before acting, read and follow the canonical skill:

```text
../release-gate/SKILL.md
```

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `release-gate` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
