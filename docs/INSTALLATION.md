# Installation And Usage

This repository is a backup and distribution point for custom Codex skills. The
runtime location for personal skills is:

```sh
~/.codex/skills
```

## Install One Skill

From the repository root:

```sh
mkdir -p ~/.codex/skills
cp -R skills/project-onboarding ~/.codex/skills/project-onboarding
```

Replace `project-onboarding` with the skill folder you want to install.

Aliases and compatibility routers require their canonical skill alongside them.
For `claude-to-a-tee`, `global-claude-to-a-tee`, or
`global-mockup-to-product`, also install `mockup-to-product`. See
[reference parity migration](REFERENCE_PARITY_MIGRATION.md).

Install `mockup-fidelity-repair` alongside `mockup-to-product`: the latter now
loads it automatically for material in-scope visual mismatches. The repair
workflow also uses `snapshot` for visual proof and `responsive-design` when
reflow needs it. Its `global-mockup-fidelity-repair` alias requires the canonical
repair skill; it is not a standalone copy of those instructions.

Install `frontend-copy-deterrence` and `frontend-source-protection` together:
they link to each other for interaction deterrents versus build/data exposure.
Their `global-*` aliases require the respective canonical folders. The source
protection workflow also routes authorized publishing through `release-gate`.

`reference-to-a-tee` and `global-reference-to-a-tee` are retired and removed. Update old
prompts to the corresponding mockup name. A copy-only sync does not remove old
installed folders; inspect local differences and get approval before retiring
those copies. Do not restore them automatically from an older backup.

## Install All Skills

From the repository root:

```sh
mkdir -p ~/.codex/skills
rsync -a --exclude '/README.md' skills/ ~/.codex/skills/
```

This copies every skill folder into the local Codex skills directory.

## Use Symlinks For Active Editing

When you want edits in the repository to be picked up directly by Codex, use a
symlink instead of copying:

```sh
mkdir -p ~/.codex/skills
ln -sfn "$(pwd)/skills/project-onboarding" ~/.codex/skills/project-onboarding
```

Use symlinks only when the repository checkout should be the live editable copy.
For stable use, copying is simpler.

## Confirm A Skill Is Available

Start a new Codex session or refresh the environment, then ask for the skill by
name or trigger it with a matching task. Each skill's trigger context is listed
in [SKILL_CATALOG.md](SKILL_CATALOG.md).

## Keep Local And Repo Copies In Sync

If `~/.codex/skills` is the active source of truth, refresh this repository with:

```sh
rsync -ani --delete --exclude '.system' --exclude '/README.md' --exclude '__pycache__/' --exclude '*.orig' ~/.codex/skills/ skills/
```

Review the dry-run diff before applying it. If the dry run would delete
repo-only `global-*` aliases, sync changed canonical folders selectively instead
of running a broad delete sync.
