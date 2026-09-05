#!/usr/bin/env python3
"""Compatibility CLI for the canonical HTML reference extractor."""

from pathlib import Path
import runpy
import sys


def main() -> int:
    target = Path(__file__).resolve().parents[2] / "reference-to-a-tee" / "scripts" / "extract_reference.py"
    if not target.is_file():
        print("Install reference-to-a-tee beside claude-to-a-tee to use this legacy command.", file=sys.stderr)
        return 2
    namespace = runpy.run_path(str(target))
    return namespace["main"](legacy=True)


if __name__ == "__main__":
    raise SystemExit(main())
