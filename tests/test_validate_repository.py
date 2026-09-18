"""Behavioral regressions for current release and README asset consistency."""

import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_repository", ROOT / "scripts/validate_repository.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReadmeValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name).resolve()
        self.versions = {"Codex": "0.2.0", "Claude": "0.2.0"}
        self.readme = """# Synthetic package
Release **v0.2.0** · [MIT license](LICENSE) · Codex + Claude Code
<picture>
  <source media="(max-width: 1000px)" srcset="art/compact.4a2b.svg">
  <img src="art/wide.8c9d.svg" alt="Original synthetic artwork">
</picture>
"""
        self.write("README.md", self.readme)
        self.write_svg("art/compact.4a2b.svg", "Version-free compact artwork")
        self.write_svg("art/wide.8c9d.svg", "Version-free wide artwork")

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def write_svg(self, relative, text):
        self.write(relative, '<svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
                   'viewBox="0 0 100 50"><!-- Release v0.1.0: historical comment -->'
                   '<text x="0.1" y="0.2">' + text + '</text></svg>')

    def validate(self):
        return MODULE.validate_readme(self.root, self.versions)

    def test_versionless_art_and_historical_versions_pass(self):
        self.write("README.md", self.readme + """
## History
Version 0.1.0 was evaluated earlier; v0.1 is not the current release.
```text
Release **v0.1.0** is a historical metadata example.
<img src="missing-example.svg">
```
""")
        self.write("docs/history.md", "Release **v0.1.0**\n")
        self.write_svg("art/wide.8c9d.svg", "Scale 0.1 / 0.2; 01 / EVIDENCE")
        errors, count = self.validate()
        self.assertEqual(errors, [])
        self.assertEqual(count, 2)

    def test_readme_current_release_must_match_both_plugins(self):
        self.write("README.md", self.readme.replace("v0.2.0", "v0.1.0"))
        errors, _ = self.validate()
        self.assertEqual(len(errors), 2)
        self.assertTrue(all("current release 0.1.0 differs" in error for error in errors))

    def test_missing_or_duplicate_current_release_is_not_guessed(self):
        for text in (self.readme.replace("Release **v0.2.0**", "Historical v0.2.0"),
                     self.readme + "\nRelease **v0.2.0**\n"):
            with self.subTest(text=text):
                self.write("README.md", text)
                errors, _ = self.validate()
                self.assertTrue(any("expected one current-release declaration" in e for e in errors))

    def test_stale_explicit_svg_version_fails_including_split_text(self):
        for label in ("v0.1", "Version 0.1.0", "Release: v0.1.0",
                      "Version <tspan>0.1.0</tspan>", "DESIGN SKILL / 0.1",
                      "STN Ultradesign / 0.1.0"):
            with self.subTest(label=label):
                self.write_svg("art/wide.8c9d.svg", label)
                errors, _ = self.validate()
                self.assertTrue(any("labelled SVG version 0.1" in e for e in errors), errors)

    def test_matching_explicit_svg_versions_pass(self):
        for label in ("v0.2.0", "Version 0.2", "Release <tspan>v0.2.0</tspan>",
                      "DESIGN SKILL / 0.2", "STN Ultradesign / v0.2.0"):
            with self.subTest(label=label):
                self.write_svg("art/wide.8c9d.svg", label)
                self.assertEqual(self.validate()[0], [])

    def test_missing_compact_srcset_fails_even_when_fallback_exists(self):
        (self.root / "art/compact.4a2b.svg").unlink()
        errors, _ = self.validate()
        self.assertTrue(any("source[srcset]: art/compact.4a2b.svg" in e for e in errors), errors)

    def test_every_srcset_candidate_and_img_src_are_checked(self):
        self.write("README.md", self.readme.replace(
            'srcset="art/compact.4a2b.svg"',
            'srcset="art/compact.4a2b.svg 1x, art/retina.missing.svg 2x"').replace(
            'src="art/wide.8c9d.svg"', 'src="art/fallback.missing.svg"'))
        errors, count = self.validate()
        self.assertEqual(count, 3)
        self.assertTrue(any("source[srcset]: art/retina.missing.svg" in e for e in errors), errors)
        self.assertTrue(any("img[src]: art/fallback.missing.svg" in e for e in errors), errors)

    def test_encoded_local_paths_and_remote_candidates(self):
        self.write_svg("art/compact name.svg", "Original")
        self.write("README.md", self.readme.replace(
            "art/compact.4a2b.svg", "art/compact%20name.svg?cache=a&amp;size=1#preview") + """
<img src="https://example.invalid/badge.svg" alt="External">
<source srcset="data:image/svg+xml,%3Csvg%3E 1x, art/wide.8c9d.svg 2x">
""")
        errors, count = self.validate()
        self.assertEqual(errors, [])
        self.assertEqual(count, 3)

    def test_invalid_svg_and_package_escape_are_reported(self):
        self.write("art/wide.8c9d.svg", "<svg><text>broken")
        self.write("README.md", self.readme + '<img src="../outside.svg" alt="Outside">')
        errors, _ = self.validate()
        self.assertTrue(any("cannot parse README SVG" in e for e in errors), errors)
        self.assertTrue(any("escapes package" in e for e in errors), errors)

    def test_cli_integration_preserves_scope_disclaimer(self):
        for relative in MODULE.REQUIRED:
            if relative != "README.md":
                self.write(relative, "{}" if relative.endswith(".json") else "")
        manifest = {"name": MODULE.NAME, "version": "0.2.0", "license": "MIT"}
        self.write(".codex-plugin/plugin.json", json.dumps(dict(manifest, skills="./skills/")))
        self.write(".claude-plugin/plugin.json", json.dumps(manifest))
        self.write(".claude-plugin/marketplace.json", json.dumps({
            "name": MODULE.NAME, "plugins": [{"name": MODULE.NAME, "source": "./"}]}))
        skill = self.root / "skills" / MODULE.NAME
        self.write(f"skills/{MODULE.NAME}/SKILL.md",
                   f"---\nname: {MODULE.NAME}\ndescription: Synthetic test skill\n---\n")
        self.write(f"skills/{MODULE.NAME}/agents/openai.yaml", f"prompt: ${MODULE.NAME}\n")
        for current, expected in (("0.2.0", 0), ("0.1.0", 1)):
            with self.subTest(current=current):
                self.write("README.md", self.readme.replace("v0.2.0", "v" + current))
                output, errors = io.StringIO(), io.StringIO()
                with patch.multiple(MODULE, ROOT=self.root, SKILL=skill), \
                        redirect_stdout(output), redirect_stderr(errors):
                    result = MODULE.main()
                self.assertEqual(result, expected, errors.getvalue())
                if expected == 0:
                    self.assertIn("not client installation or design quality", output.getvalue())
                else:
                    self.assertIn("current release 0.1.0 differs", errors.getvalue())

    def test_cli_rejects_inconsistent_distribution_metadata(self):
        # Use the package layout to verify both distribution formats together.
        import shutil
        package = self.root / "package"
        shutil.copytree(ROOT, package, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        target = package / ".claude-plugin/plugin.json"
        manifest = json.loads(target.read_text())
        cases = (
            ({"version": "9.9.9"}, "Plugin versions differ"),
            ({"version": "unstable"}, "expected a release version"),
            ({"name": "another-skill"}, "unexpected plugin name"),
            ({"license": "Proprietary"}, "license differs from package"),
            ({"hooks": {}}, "no external integrations or hooks"),
        )
        for change, message in cases:
            with self.subTest(change=change):
                target.write_text(json.dumps(dict(manifest, **change)))
                output, errors = io.StringIO(), io.StringIO()
                with patch.multiple(MODULE, ROOT=package, SKILL=package / "skills" / MODULE.NAME), \
                        redirect_stdout(output), redirect_stderr(errors):
                    self.assertEqual(MODULE.main(), 1, errors.getvalue())
                self.assertIn(message, errors.getvalue())


if __name__ == "__main__":
    unittest.main()
