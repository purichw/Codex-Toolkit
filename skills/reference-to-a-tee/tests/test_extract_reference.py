"""Behavior checks for HTML extraction, image rejection, and legacy invocation."""

from contextlib import redirect_stderr, redirect_stdout
import io
import json
import os
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SKILL = Path(__file__).resolve().parents[1]
SCRIPT = SKILL / "scripts" / "extract_reference.py"
LEGACY = SKILL.parent / "claude-to-a-tee" / "scripts" / "extract_reference.py"
HTML = """<!doctype html><html><head><title>Reference fixture</title>
<style>.card { color: #123456; font-family: Arial; }
@media (max-width: 600px) { .card { display: block; } }</style></head>
<body><main><h1>Overview</h1><button id="save">Save</button>
<a href="#settings">Settings</a><img src="hero.png" alt="Hero"></main>
<script>function openSettings() { setScreen('settings'); }</script></body></html>
"""


class ExtractReferenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="reference-to-a-tee-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "reference.html"
        self.source.write_text(HTML, encoding="utf-8")

    def cli(self, *args, script=SCRIPT):
        return subprocess.run(
            [sys.executable, str(script), *map(str, args)],
            cwd=self.root,
            capture_output=True,
            text=True,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            timeout=20,
        )

    def manifest(self, folder):
        return json.loads((folder / "reference-manifest.json").read_text(encoding="utf-8"))

    def test_static_html_inventory_and_canonical_outputs(self):
        result = self.cli(self.source)
        self.assertEqual(result.returncode, 0, result.stderr)
        out = self.root / ".design-reference"
        manifest = self.manifest(out)
        self.assertEqual(manifest["mode"], "html")
        item = manifest["files"][0]
        self.assertEqual(item["title"], "Reference fixture")
        self.assertIn("settings", item["state_value_candidates"])
        self.assertIn("max-width:600px", item["breakpoints"])
        self.assertTrue(any(c["attrs"].get("id") == "save" for c in item["controls"]))
        self.assertTrue(any(a["value"] == "hero.png" for a in item["assets"]))
        self.assertTrue((out / "reference-manifest.md").is_file())
        self.assertTrue((out / "REFERENCE_TO_A_TEE_WORKLOG.md").is_file())
        self.assertFalse((out / "CLAUDE_TO_A_TEE_WORKLOG.md").exists())

    def test_multiple_html_files_keep_separate_identities(self):
        second = self.root / "second.HTM"
        second.write_text("<title>Second screen</title><button>Next</button>", encoding="utf-8")
        out = self.root / "bundle"
        result = self.cli(self.source, second, "--out", out)
        self.assertEqual(result.returncode, 0, result.stderr)
        items = self.manifest(out)["files"]
        self.assertEqual([i["title"] for i in items], ["Reference fixture", "Second screen"])
        self.assertNotEqual(items[0]["sha256"], items[1]["sha256"])

    def test_image_input_is_not_silently_parsed_as_html(self):
        image = self.root / "screen.png"
        image.write_bytes(b"\x89PNG\r\n\x1a\n")
        out = self.root / "rejected"
        result = self.cli(image, "--out", out)
        self.assertEqual(result.returncode, 2)
        self.assertIn("image workflow", result.stderr)
        self.assertFalse(out.exists())

    def test_missing_input_and_directory_fail_without_outputs(self):
        for source in (self.root / "missing.html", self.root):
            with self.subTest(source=source):
                result = self.cli(source)
                self.assertEqual(result.returncode, 2)
                self.assertIn("Missing HTML", result.stderr)
        self.assertFalse((self.root / ".design-reference").exists())

    def test_screenshot_request_cannot_silently_skip_rendering(self):
        result = self.cli(self.source, "--screenshots")
        self.assertEqual(result.returncode, 2)
        self.assertIn("requires --render", result.stderr)

    def test_legacy_cli_preserves_default_directory_and_worklog(self):
        result = self.cli(self.source, script=LEGACY)
        self.assertEqual(result.returncode, 0, result.stderr)
        out = self.root / ".claude-reference"
        self.assertEqual(self.manifest(out)["mode"], "html")
        self.assertEqual(
            (out / "CLAUDE_TO_A_TEE_WORKLOG.md").read_bytes(),
            (out / "REFERENCE_TO_A_TEE_WORKLOG.md").read_bytes(),
        )

    def run_with_probe(self, probe):
        main = runpy.run_path(str(SCRIPT))["main"]
        out = self.root / "new-render-output"
        with patch.dict(main.__globals__, {"rendered_probe": probe}):
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                code = main([str(self.source), "--out", str(out), "--render", "--screenshots", "--viewport", "390x844"])
        return code, self.manifest(out)

    def test_render_probe_receives_existing_output_directory(self):
        def probe(paths, viewports, out, screenshots):
            self.assertEqual(paths, [self.source.resolve()])
            self.assertEqual(viewports, [(390, 844)])
            self.assertTrue(out.is_dir())
            self.assertTrue(screenshots)
            return {"available": True, "captures": []}

        code, manifest = self.run_with_probe(probe)
        self.assertEqual(code, 0)
        self.assertTrue(manifest["rendered"]["available"])

    def test_unavailable_render_probe_is_failure_with_static_inventory(self):
        code, manifest = self.run_with_probe(
            lambda *args: {"available": False, "error": "Playwright unavailable"}
        )
        self.assertEqual(code, 1)
        self.assertFalse(manifest["rendered"]["available"])
        self.assertEqual(manifest["files"][0]["title"], "Reference fixture")

    def test_browser_launch_failure_does_not_claim_render_success(self):
        def probe(*args):
            raise RuntimeError("Browser missing")

        code, manifest = self.run_with_probe(probe)
        self.assertEqual(code, 1)
        self.assertIn("Browser missing", manifest["rendered"]["error"])


if __name__ == "__main__":
    unittest.main()
