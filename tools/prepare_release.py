"""Build a verifiable source-only release from an existing tag at HEAD."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


def prepare(tag, repository, output):
    if not re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+(?:-[0-9A-Za-z.-]+)?', tag):
        raise ValueError('Use a version tag such as v1.2.3 or v1.2.3-beta.1')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('Repository must be owner/name')
    head = git('rev-parse', 'HEAD')
    tagged = git('rev-parse', '--verify', f'refs/tags/{tag}^{{commit}}')
    if tagged != head:
        raise ValueError('The existing release tag must point to the selected workflow commit')
    if git('status', '--porcelain', '--untracked-files=no'):
        raise ValueError('Tracked files changed after checkout; refusing to package untested source')
    output = Path(output)
    if output.exists() and any(output.iterdir()):
        raise ValueError('Output directory must be empty; stale assets cannot join a release')
    output.mkdir(parents=True, exist_ok=True)
    name = repository.split('/')[1]
    archive = output / f'{name}-{tag}-source.zip'
    subprocess.run(['git', 'archive', '--format=zip', f'--prefix={name}-{tag}/',
                    f'--output={archive.resolve()}', tagged], check=True)
    manifest = output / 'BUILD_INFO.json'
    manifest.write_text(json.dumps({
        'schema_version': 1, 'repository': repository, 'tag': tag,
        'source_commit': tagged, 'package_kind': 'source-only',
        'workflow_run': os.environ.get('GITHUB_RUN_ID'),
        'platform_binaries_built': False,
    }, indent=2) + '\n', encoding='utf-8')
    checksums = []
    for file in (archive, manifest):
        digest = hashlib.sha256(file.read_bytes()).hexdigest()
        checksums.append(f'{digest}  {file.name}\n')
    (output / 'SHA256SUMS.txt').write_text(''.join(checksums), encoding='utf-8')
    return tagged


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tag', required=True)
    parser.add_argument('--repository', required=True)
    parser.add_argument('--output', default='release-assets')
    args = parser.parse_args()
    try:
        print(prepare(args.tag, args.repository, args.output))
    except (ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'Release preparation failed: {exc}\n')
