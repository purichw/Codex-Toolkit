import importlib.util
import tempfile
import unittest
from pathlib import Path

EVALS = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("prepare", EVALS / "prepare.py")
P = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(P)


class PrepareTests(unittest.TestCase):
    def test_all_cases_exclude_rubrics_solutions_and_previous_results(self):
        with tempfile.TemporaryDirectory() as folder:
            for case in P.CASES:
                out = Path(folder) / case
                manifest = P.prepare(EVALS.parent, case, out)
                self.assertTrue((out / "app/index.html").is_file())
                self.assertTrue((out / "skills/ui-ux-expert/SKILL.md").is_file())
                names = [str(p.relative_to(out)) for p in out.rglob("*")]
                self.assertFalse(any("calibration.css" in n or "cases.json" in n or "/evals/" in n for n in names))
                self.assertTrue(manifest["sha256"])
                self.assertTrue(manifest["omitted_evaluation_links"])
                for doc in (out / "skills").rglob("*.md"):
                    self.assertNotRegex(doc.read_text(), r"\]\((?:\.\./)*evals/")
                self.assertIn(case, (out / "TASK.md").read_text())

    def test_existing_output_and_unknown_case_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            with self.assertRaises(ValueError):
                P.prepare(EVALS.parent, "dashboard", Path(folder))
            with self.assertRaises(ValueError):
                P.prepare(EVALS.parent, "unknown", Path(folder) / "new")


if __name__ == "__main__":
    unittest.main()
