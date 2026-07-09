#!/usr/bin/env python3
"""Verify the Codex Toolkit skill archive.

The verifier intentionally uses only the Python standard library so future
Codex sessions can run it on a fresh machine without setup.
"""

from __future__ import annotations

import argparse
import re
import stat
import sys
from pathlib import Path
from urllib.parse import unquote


MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
FENCED_CODE = re.compile(r"```.*?```", re.DOTALL)
HIGH_CONFIDENCE_SECRET = re.compile(
    r"("
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----|"
    r"\bsk-[A-Za-z0-9_-]{20,}|"
    r"\bgh[pousr]_[A-Za-z0-9_]{20,}|"
    r"\bAIza[0-9A-Za-z_-]{35}\b"
    r")"
)


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def print_summary(self) -> None:
        for warning in self.warnings:
            print(f"WARN: {warning}")
        for error in self.errors:
            print(f"ERROR: {error}")

        if self.errors:
            print(f"\nFAILED: {len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        else:
            print(f"OK: 0 errors, {len(self.warnings)} warning(s)")


def parse_frontmatter(skill_md: Path, reporter: Reporter) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        reporter.error(f"{skill_md}: missing opening frontmatter delimiter")
        return {}

    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break

    if end_index is None:
        reporter.error(f"{skill_md}: missing closing frontmatter delimiter")
        return {}

    data: dict[str, str] = {}
    for raw_line in lines[1:end_index]:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            reporter.error(f"{skill_md}: invalid frontmatter line: {raw_line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")

    return data


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.relative_to(root).parts
    )


def strip_fenced_code(text: str) -> str:
    return FENCED_CODE.sub("", text)


def verify_markdown_links(root: Path, reporter: Reporter) -> None:
    for md_file in iter_markdown_files(root):
        text = strip_fenced_code(md_file.read_text(encoding="utf-8"))
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip()
            if (
                "://" in target
                or target.startswith("#")
                or target.startswith("mailto:")
                or target.startswith("tel:")
            ):
                continue

            clean_target = unquote(target.split("#", 1)[0]).strip()
            if not clean_target:
                continue

            linked_path = (md_file.parent / clean_target).resolve()
            try:
                linked_path.relative_to(root.resolve())
            except ValueError:
                reporter.warning(f"{md_file}: link points outside repo: {target}")
                continue

            if not linked_path.exists():
                reporter.error(f"{md_file}: broken local link: {target}")


def verify_skill_directories(root: Path, expected_count: int | None, reporter: Reporter) -> None:
    skills_dir = root / "skills"
    if not skills_dir.is_dir():
        reporter.error("skills/: directory is missing")
        return

    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    names: set[str] = set()

    if expected_count is not None and len(skill_dirs) != expected_count:
        reporter.error(
            f"skills/: expected {expected_count} skill directories, found {len(skill_dirs)}"
        )

    for skill_dir in skill_dirs:
        if skill_dir.name.startswith("."):
            reporter.error(f"{skill_dir}: hidden skill directories should not be archived")
            continue

        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            reporter.error(f"{skill_dir}: missing SKILL.md")
            continue

        frontmatter = parse_frontmatter(skill_md, reporter)
        name = frontmatter.get("name")
        description = frontmatter.get("description")

        if not name:
            reporter.error(f"{skill_md}: frontmatter missing name")
        elif name != skill_dir.name:
            reporter.error(f"{skill_md}: name {name!r} does not match folder {skill_dir.name!r}")

        if name in names:
            reporter.error(f"{skill_md}: duplicate skill name {name!r}")
        elif name:
            names.add(name)

        if not description:
            reporter.error(f"{skill_md}: frontmatter missing description")
        elif len(description) < 20:
            reporter.warning(f"{skill_md}: description is unusually short")


def verify_python_scripts(root: Path, reporter: Reporter) -> None:
    for script in sorted(root.glob("skills/*/scripts/*.py")):
        try:
            source = script.read_text(encoding="utf-8")
            compile(source, str(script), "exec")
        except SyntaxError as exc:
            reporter.error(f"{script}: Python syntax check failed: {exc.msg}")

        if not script.stat().st_mode & stat.S_IXUSR:
            reporter.warning(f"{script}: helper script is not executable")


def verify_no_bundled_skill_paths(root: Path, reporter: Reporter) -> None:
    forbidden = (
        ".codex/skills/.system",
        ".codex/plugins/cache",
        "plugins/cache",
    )
    for path in root.rglob("*"):
        rel = path.relative_to(root).as_posix()
        if any(part in rel for part in forbidden):
            reporter.error(f"{path}: bundled/system skill path should not be archived")


def verify_high_confidence_secrets(root: Path, reporter: Reporter) -> None:
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        if ".git" in path.relative_to(root).parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if HIGH_CONFIDENCE_SECRET.search(text):
            reporter.error(f"{path}: high-confidence secret pattern detected")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Verify Codex Toolkit skills")
    parser.add_argument(
        "--root",
        default=".",
        help="repository root to verify; defaults to current directory",
    )
    parser.add_argument(
        "--expected-count",
        type=int,
        default=None,
        help="expected number of skill directories",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    reporter = Reporter()

    verify_skill_directories(root, args.expected_count, reporter)
    verify_markdown_links(root, reporter)
    verify_python_scripts(root, reporter)
    verify_no_bundled_skill_paths(root, reporter)
    verify_high_confidence_secrets(root, reporter)

    reporter.print_summary()
    return 1 if reporter.errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
