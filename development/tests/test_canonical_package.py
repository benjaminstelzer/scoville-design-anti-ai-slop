"""Exercise the maintained generators against the single published source."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

DEVELOPMENT = Path(__file__).resolve().parents[1]
REPOSITORY = DEVELOPMENT.parent
PACKAGE = REPOSITORY / 'scoville-design-anti-ai-slop'


def snapshot(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


class CanonicalPackageTests(unittest.TestCase):
    def command(self, script, *args, expected=0):
        result = subprocess.run([sys.executable, '-B', str(DEVELOPMENT/'scripts'/script), *map(str, args)],
                                capture_output=True, text=True, cwd=REPOSITORY)
        self.assertEqual(expected, result.returncode, result.stdout + result.stderr)
        return result

    def test_default_index_and_export_use_single_source_without_modifying_it(self):
        before = snapshot(PACKAGE)
        self.command('generate_module_index.py')
        self.command('generate_module_index.py', '--check')
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            manifest = temporary/'manifest.json'
            self.command('build_package_manifest.py', '--output', manifest)
            self.command('build_package_manifest.py', '--output', manifest, '--check')
            self.command('build_runtime_package.py', '--destination', temporary/'export',
                         '--receipt', temporary/'receipt.json')
            self.assertEqual(before, snapshot(temporary/'export'))
            receipt = json.loads((temporary/'receipt.json').read_text())
            self.assertEqual(receipt['source'], receipt['runtime'])
            rejected = REPOSITORY/'forbidden-second-package'
            self.command('build_runtime_package.py', '--destination', rejected,
                         '--receipt', temporary/'rejected.json', expected=1)
            self.assertFalse(rejected.exists())
        self.assertEqual(before, snapshot(PACKAGE))
        self.assertFalse((REPOSITORY/'SKILL.md').exists())

    def test_index_drift_fails_then_generator_repairs_only_the_index(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory)/'package'
            shutil.copytree(PACKAGE, package)
            before = snapshot(package)
            skill = package/'SKILL.md'
            text = skill.read_text(encoding='utf-8')
            changed = text.replace('→', 'BROKEN', 1)
            self.assertNotEqual(text, changed)
            skill.write_text(changed, encoding='utf-8', newline='\n')
            self.command('generate_module_index.py', '--root', package, '--check', expected=1)
            self.command('generate_module_index.py', '--root', package)
            self.assertEqual(before, snapshot(package))
            manifest = Path(directory)/'manifest.json'
            self.command('build_package_manifest.py', '--root', package, '--output', manifest)
            skill.write_text(text+'\nDrift.\n', encoding='utf-8', newline='\n')
            self.command('build_package_manifest.py', '--root', package, '--output', manifest, '--check', expected=1)


if __name__ == '__main__':
    unittest.main()
