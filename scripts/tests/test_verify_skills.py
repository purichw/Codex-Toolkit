"""Keep local recovery copies separate from maintained Markdown validation."""

from pathlib import Path
import runpy
import tempfile
import unittest


VERIFIER = runpy.run_path(str(Path(__file__).resolve().parents[1] / "verify_skills.py"))


class MarkdownScopeTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="skill-verifier-test-")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)

    def add(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def test_only_root_exports_are_excluded_from_link_scan(self):
        paths = ["README.md", "docs/guide.md", "skills/example/SKILL.md",
                 ".agents/skills/native/SKILL.md", "skills/example/exports/notes.md"]
        for path in paths + ["exports/checkpoint/skills/example/SKILL.md", ".git/notes.md"]:
            self.add(path, "[missing](missing.md)\n")
        reporter = VERIFIER["Reporter"]()
        VERIFIER["verify_markdown_links"](self.root, reporter)
        self.assertEqual(len(reporter.errors), len(paths))
        scanned = {p.relative_to(self.root).as_posix() for p in VERIFIER["iter_markdown_files"](self.root)}
        self.assertEqual(scanned, set(paths))

    def test_links_from_maintained_docs_into_exports_are_still_checked(self):
        self.add("README.md", "[missing](exports/missing.md)\n")
        reporter = VERIFIER["Reporter"]()
        VERIFIER["verify_markdown_links"](self.root, reporter)
        self.assertEqual(len(reporter.errors), 1)

    def test_exports_remain_in_secret_and_bundled_path_scans(self):
        self.add("exports/example.txt", "-----BEGIN " + "PRIVATE KEY-----\n")
        self.add("exports/plugins/cache/example.txt", "fixture\n")
        reporter = VERIFIER["Reporter"]()
        VERIFIER["verify_high_confidence_secrets"](self.root, reporter)
        VERIFIER["verify_no_bundled_skill_paths"](self.root, reporter)
        self.assertTrue(any("secret pattern" in error for error in reporter.errors))
        self.assertTrue(any("bundled/system" in error for error in reporter.errors))


if __name__ == "__main__":
    unittest.main()
