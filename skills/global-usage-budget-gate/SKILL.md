---
name: global-usage-budget-gate
description: Global reusable alias for the usage-budget-gate compatibility router. Use when the user asks for $global-usage-budget-gate, says this should be global or non-project-specific, or wants the reusable version of usage budget gating. This alias routes through usage-budget-gate/SKILL.md to efficient-execution/SKILL.md, where proportional effort now lives.
---

# Global Usage Budget Gate

This is a global alias for the `usage-budget-gate` compatibility router. The
proportional-effort workflow now lives in `efficient-execution`.

Before acting, read and follow:

```text
../usage-budget-gate/SKILL.md
../efficient-execution/SKILL.md
```

Use this alias when the user explicitly wants the global, reusable, or
non-project-specific variant. Keep `efficient-execution` as the source of truth
for depth modes and stop rules; keep `usage-budget-gate` only as the stable
trigger name.
