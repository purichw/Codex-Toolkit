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

## Install All Skills

From the repository root:

```sh
mkdir -p ~/.codex/skills
rsync -a skills/ ~/.codex/skills/
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
rsync -a --delete --exclude '.system' ~/.codex/skills/ skills/
```

Review the diff before committing.
