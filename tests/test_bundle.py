import importlib.util
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('validator', ROOT/'scripts/validate_bundle.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class BundleTests(unittest.TestCase):
    def test_canonical_bundle_validates(self):
        self.assertEqual([], module.validate())

    def test_missing_reference_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp)/'bundle'
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('.git','__pycache__'))
            (copy/'skills/omarchy-package-test/references/validation.md').unlink()
            self.assertTrue(any('missing or escaping' in e for e in module.validate(copy)))

    def test_adapter_and_version_drift_are_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp)/'bundle'
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('.git','__pycache__'))
            (copy/'plugins/build-omarchy-packages/skills/omarchy-package-test/SKILL.md').write_text('changed')
            (copy/'VERSION').write_text('0.2.0\n')
            errors = module.validate(copy)
            self.assertTrue(any('content drift' in e for e in errors))
            self.assertTrue(any('version drift' in e for e in errors))
