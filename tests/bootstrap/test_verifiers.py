import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]

def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"scripts/{name}.py")
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result

safety = module("verify-public-safety")
bootstrap = module("verify-bootstrap")

class PublicSafetyTest(unittest.TestCase):
    def test_git_failure_is_inspection_failure(self):
        with patch.object(safety.subprocess, "run", side_effect=subprocess.CalledProcessError(128, "git")):
            self.assertEqual(safety.main(), 2)

    def test_untracked_source_is_inspected_and_secret_value_not_reported(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "tmp") as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "--quiet", str(root)], check=True)
            secret = "ghp_" + "z" * 36
            (root / "untracked.txt").write_text(secret)
            findings = safety.scan(root)
            self.assertIn(("untracked.txt", "GitHub token"), findings)
            self.assertNotIn(secret, repr(findings))

    def test_missing_indexed_source_fails(self):
        with patch.object(safety, "source_files", return_value=["missing.txt"]):
            with self.assertRaises(ValueError):
                safety.scan(ROOT)

    def test_tracked_secret_filename_rejected(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "tmp") as directory:
            root = Path(directory)
            (root / ".env").write_text("SYNTHETIC=1")
            with patch.object(safety, "source_files", return_value=[".env"]):
                self.assertIn((".env", "secret-bearing filename"), safety.scan(root))

    def test_live_token_remains_blocked_pending_separate_review(self):
        with tempfile.TemporaryDirectory(dir=ROOT / "tmp") as directory:
            root = Path(directory)
            (root / "unsafe.txt").write_text("REAL_" + "LIVE")
            with patch.object(safety, "source_files", return_value=["unsafe.txt"]):
                self.assertIn(("unsafe.txt", "build-track live-route token"), safety.scan(root))

class BootstrapTest(unittest.TestCase):
    def test_current_approved_sources_and_windows_manifest(self):
        bootstrap.verify(ROOT)

    def test_policy_failure_is_explicit_even_with_python_optimized(self):
        with self.assertRaises(ValueError):
            bootstrap.require(False, "unsafe")

if __name__ == "__main__":
    (ROOT / "tmp").mkdir(exist_ok=True)
    unittest.main()
