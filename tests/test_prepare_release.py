import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

spec = importlib.util.spec_from_file_location('prepare_release', Path(__file__).parents[1] / 'tools' / 'prepare_release.py')
release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.original = Path.cwd()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.addCleanup(os.chdir, self.original)
        os.chdir(self.temp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Release Test')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'core.autocrlf', 'false')
        Path('hello.txt').write_bytes(b'source at release\n')
        self.git('add', 'hello.txt')
        self.git('commit', '-qm', 'initial')
        self.git('tag', 'v1.2.3')

    def git(self, *args):
        return subprocess.check_output(['git', *args], text=True, stderr=subprocess.PIPE).strip()

    def test_archive_and_manifest_have_valid_checksums(self):
        Path('untracked-secret.txt').write_text('must not enter archive')
        sha = release.prepare('v1.2.3', 'Swir/example', 'out')
        self.assertEqual(sha, self.git('rev-parse', 'HEAD'))
        with zipfile.ZipFile('out/example-v1.2.3-source.zip') as archive:
            self.assertEqual(archive.namelist(), ['example-v1.2.3/', 'example-v1.2.3/hello.txt'])
            self.assertEqual(archive.read('example-v1.2.3/hello.txt'), b'source at release\n')
        manifest = json.loads(Path('out/BUILD_INFO.json').read_text())
        self.assertEqual(manifest['source_commit'], sha)
        self.assertFalse(manifest['platform_binaries_built'])
        for line in Path('out/SHA256SUMS.txt').read_text().splitlines():
            digest, filename = line.split('  ', 1)
            self.assertEqual(digest, hashlib.sha256((Path('out') / filename).read_bytes()).hexdigest())

    def test_rejects_tag_that_does_not_match_checkout(self):
        Path('hello.txt').write_text('next version\n')
        self.git('commit', '-qam', 'next')
        with self.assertRaisesRegex(ValueError, 'selected workflow commit'):
            release.prepare('v1.2.3', 'Swir/example', 'out')
        self.assertFalse(Path('out').exists())

    def test_rejects_dirty_tracked_source(self):
        Path('hello.txt').write_text('not tested\n')
        with self.assertRaisesRegex(ValueError, 'Tracked files changed'):
            release.prepare('v1.2.3', 'Swir/example', 'out')

    def test_rejects_stale_assets(self):
        Path('out').mkdir()
        Path('out/old.exe').write_bytes(b'old')
        with self.assertRaisesRegex(ValueError, 'stale assets'):
            release.prepare('v1.2.3', 'Swir/example', 'out')

    def test_rejects_invalid_tag_and_repository(self):
        for tag in ['--help', '../../v1.2.3', 'v1.0.0\nmalicious']:
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                release.prepare(tag, 'Swir/example', 'out')
        with self.assertRaises(ValueError):
            release.prepare('v1.2.3', '../bad/name', 'out')

    def test_missing_tag_cannot_create_output(self):
        with self.assertRaises(subprocess.CalledProcessError):
            release.prepare('v9.9.9', 'Swir/example', 'out')
        self.assertFalse(Path('out').exists())


if __name__ == '__main__':
    unittest.main()
