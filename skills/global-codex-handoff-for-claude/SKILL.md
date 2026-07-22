---
name: global-codex-handoff-for-claude
description: Global reusable alias for the canonical codex-handoff-for-claude skill. Use when the user asks for $global-codex-handoff-for-claude, says this should be global or non-project-specific, or wants the reusable version of codex handoff for claude. This alias routes to codex-handoff-for-claude/SKILL.md; keep codex-handoff-for-claude as the source of truth.
---

# Global Codex Handoff For Claude

This is a global alias for the canonical `codex-handoff-for-claude` skill.

Before acting, read and follow the canonical skill:

```text
../codex-handoff-for-claude/SKILL.md
```

Follow the canonical skill's `$snapshot` and visual-evidence requirements
whenever they apply. Do not treat this global alias as a way to bypass the
canonical snapshot gate.

Use this alias when the user explicitly wants the global, reusable, or non-project-specific variant. Keep `codex-handoff-for-claude` as the source of truth; update the canonical skill first, then regenerate this alias if the routing language needs to change.
