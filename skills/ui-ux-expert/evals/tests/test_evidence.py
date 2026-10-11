import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("evidence", Path(__file__).resolve().parents[1] / "evidence.py")
E = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(E)


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "screen.html").write_text("original", encoding="utf-8")
        (self.root / "view.png").write_bytes(b"\x89PNG\r\n\x1a\nunit-test-not-real-pixels")
        self.matrix = {"schema_version": 1, "source_files": ["screen.html"], "required": [
            {"id": "narrow-error", "route": "/form", "viewport": [320, 800], "state": "error", "checks": ["recovery"]}]}
        self.capture = {**self.matrix["required"][0], "file": "view.png", "sha256": E.digest(self.root / "view.png"),
                        "source_hashes": {"screen.html": E.digest(self.root / "screen.html")},
                        "review": {"reviewer": "unit-test", "note": "Synthetic metadata, not a visual claim"},
                        "checks": {"recovery": "passed"}}
        self.manifest = {"schema_version": 1, "captures": [self.capture]}

    def errors(self):
        return E.validate(self.matrix, self.manifest, self.root, self.root)

    def test_valid_metadata_only(self):
        self.assertEqual(self.errors(), [])

    def test_stale_source(self):
        (self.root / "screen.html").write_text("late edit", encoding="utf-8")
        self.assertTrue(self.errors())

    def test_missing_image(self):
        self.capture["file"] = "absent.png"
        self.assertTrue(self.errors())

    def test_changed_image(self):
        (self.root / "view.png").write_bytes(b"different")
        self.assertTrue(self.errors())

    def test_missing_state(self):
        self.manifest["captures"] = []
        self.assertTrue(self.errors())

    def test_wrong_state_route_or_viewport(self):
        for field, value in (("state", "ready"), ("route", "/login"), ("viewport", [1280, 800])):
            with self.subTest(field=field):
                old = self.capture[field]
                self.capture[field] = value
                self.assertTrue(self.errors())
                self.capture[field] = old

    def test_unreviewed(self):
        self.capture["review"] = {"reviewer": "", "note": ""}
        self.assertTrue(self.errors())

    def test_failed_blocked_or_missing_check(self):
        for value in ("failed", "blocked", "not_run", True, None):
            with self.subTest(value=value):
                self.capture["checks"]["recovery"] = value
                self.assertTrue(self.errors())

    def test_paths_cannot_escape(self):
        for path in ("../outside.png", "/tmp/view.png", ""):
            self.capture["file"] = path
            self.assertTrue(self.errors())

    def test_symlink_cannot_escape(self):
        with tempfile.TemporaryDirectory() as outside:
            target = Path(outside) / "outside.png"
            target.write_bytes(b"test")
            (self.root / "escape.png").symlink_to(target)
            self.capture["file"] = "escape.png"
            self.assertTrue(self.errors())

    def test_incomplete_source_set(self):
        self.capture["source_hashes"] = {}
        self.assertTrue(self.errors())

    def test_duplicate_or_extra_capture(self):
        self.manifest["captures"].append(copy.deepcopy(self.capture))
        self.assertTrue(self.errors())
        self.manifest["captures"][-1]["id"] = "extra"
        self.assertTrue(self.errors())

    def test_empty_or_malformed_contract(self):
        for value in (None, {}, {"schema_version": True}, {"schema_version": 1, "source_files": []}):
            self.assertTrue(E.validate(value, self.manifest, self.root, self.root))
        self.matrix["required"] = []
        self.assertTrue(self.errors())


if __name__ == "__main__":
    unittest.main()
