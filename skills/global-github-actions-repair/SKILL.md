---
name: global-github-actions-repair
description: Global alias for github-actions-repair. Use for reusable diagnosis and repair of failed GitHub Actions runs, recurring failure notifications, setup problems, and deployment-smoke failures; ordinary release readiness belongs to release-gate.
---

# Global GitHub Actions Repair

Read and follow [github-actions-repair](../github-actions-repair/SKILL.md).
The canonical skill owns failure diagnosis, credential handling, authorized
reruns, target verification, and terminal evidence. This alias does not grant
permission to deploy, mutate production, weaken checks, or inspect other chats.
Preserve the canonical workflow's scoped visual-evidence requirements when they
apply. Keep repository-specific details and secrets out of this global alias.
