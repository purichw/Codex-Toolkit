import contextlib
import copy
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path


EVALS = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("evaluation_validate", EVALS / "validate.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class EvaluationPackTests(unittest.TestCase):
    def setUp(self):
        self.pack = json.loads((EVALS / "cases.json").read_text(encoding="utf-8"))

    def test_shipped_pack_is_valid(self):
        self.assertEqual(VALIDATOR.validate_pack(self.pack), [])

    def test_invalid_top_level_and_empty_cases(self):
        for value in (None, [], {}, {"schema_version": 1, "cases": []}):
            with self.subTest(value=value):
                self.assertTrue(VALIDATOR.validate_pack(value))

    def test_boolean_is_not_a_version(self):
        self.pack["schema_version"] = True
        self.assertTrue(VALIDATOR.validate_pack(self.pack))

    def test_duplicate_ids_rejected(self):
        self.pack["cases"].append(copy.deepcopy(self.pack["cases"][0]))
        self.assertTrue(VALIDATOR.validate_pack(self.pack))

    def test_missing_rubric_and_malformed_focus_rejected(self):
        for field, value in (("review_criteria", []), ("focus", [{}]), ("prompt", " ")):
            with self.subTest(field=field):
                pack = copy.deepcopy(self.pack)
                pack["cases"][0][field] = value
                self.assertTrue(VALIDATOR.validate_pack(pack))

    def test_missing_focus_area_rejected(self):
        for case in self.pack["cases"]:
            case["focus"] = [x for x in case["focus"] if x != "alternatives"]
        self.assertTrue(VALIDATOR.validate_pack(self.pack))

    def test_real_case_needs_source_and_permission_notes(self):
        case = self.pack["cases"][0]
        case["provenance"] = "sanitized-real"
        self.assertTrue(VALIDATOR.validate_pack(self.pack))
        case["source_note"] = "Synthetic test of the metadata contract, not a real case."
        case["permission_note"] = "Test-only value; no project data imported."
        self.assertEqual(VALIDATOR.validate_pack(self.pack), [])

    def test_solver_brief_does_not_leak_reviewer_fields(self):
        case = copy.deepcopy(self.pack["cases"][0])
        case["review_criteria"] = ["REVIEW_ONLY_SENTINEL"]
        case["failure_modes"] = ["FAILURE_ONLY_SENTINEL"]
        brief = VALIDATOR.format_case(case)
        self.assertIn(case["prompt"], brief)
        self.assertNotIn("REVIEW_ONLY_SENTINEL", brief)
        self.assertNotIn("FAILURE_ONLY_SENTINEL", brief)
        review = VALIDATOR.format_case(case, review=True)
        self.assertIn("REVIEW_ONLY_SENTINEL", review)
        self.assertIn("FAILURE_ONLY_SENTINEL", review)

    def test_missing_or_malformed_pack_returns_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "pack.json"
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(VALIDATOR.main(["--pack", str(path)]), 1)
                path.write_text("{invalid", encoding="utf-8")
                self.assertEqual(VALIDATOR.main(["--pack", str(path)]), 1)

    def test_unknown_case_returns_failure(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(VALIDATOR.main(["--case", "missing-case"]), 1)

    def test_cli_can_emit_task_or_review(self):
        case = self.pack["cases"][0]
        for flag in ("--case", "--review-case"):
            with self.subTest(flag=flag), contextlib.redirect_stdout(io.StringIO()) as out:
                self.assertEqual(VALIDATOR.main([flag, case["id"]]), 0)
                self.assertIn(case["id"], out.getvalue())


if __name__ == "__main__":
    unittest.main()
