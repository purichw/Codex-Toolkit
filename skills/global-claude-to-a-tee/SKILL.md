---
name: global-claude-to-a-tee
description: Global reusable alias for the canonical claude-to-a-tee skill. Use when the user asks for $global-claude-to-a-tee, says this should be global or non-project-specific, or wants the reusable version of claude to a tee. This alias routes to claude-to-a-tee/SKILL.md; keep claude-to-a-tee as the source of truth.
---

# Global Claude To A Tee

This is a global alias for the canonical `claude-to-a-tee` skill.

Before acting, read and follow the canonical skill:

```text
../claude-to-a-tee/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `claude-to-a-tee` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
