# Release Guide

## Before building

1. Confirm the version number is final.
2. Update `CHANGELOG.md`.
3. Update the progress/status in `ROADMAP.md`.
4. Run the project's tests and CI checks.
5. Test the main user flow from a clean environment.
6. Verify that no secrets or private files are included.

## Build quality

For desktop applications, verify at minimum:

- the application starts without a development environment,
- the icon is embedded correctly,
- required runtime files are included,
- paths do not depend on the developer's machine,
- first-run behavior is understandable,
- errors are visible and useful,
- the build survives a restart and second launch.

## Release notes

A useful release description should contain:

- version and release date,
- main additions,
- important fixes,
- compatibility notes,
- known limitations,
- upgrade notes when relevant.

## Publishing

The template includes a manual **Create Release** GitHub Actions workflow. It creates a **draft source-only release** with a source ZIP, `BUILD_INFO.json` and `SHA256SUMS.txt`. It does not claim that a desktop executable has been built or tested.

Open:

`Actions → Create Release → Run workflow`

Provide:

- an existing version tag such as `v1.0.0`, pointing to the commit selected in the workflow's branch/tag picker,
- a release title,
- whether it is a pre-release.

Create and push the version tag after testing the candidate. The workflow rejects a missing tag, a tag for a different commit, dirty tracked files and a non-empty package directory. It runs the baseline tests, packages tracked files from the exact tag, uploads the draft assets, downloads them again and verifies their SHA-256 checksums. Re-running an existing release fails instead of overwriting its assets.

Review the draft notes, add platform-specific binaries or installers built from the same tested commit, and include checksums for those additional files. The template's checksum file covers only the source ZIP and build manifest; regenerate it when adding product assets. Perform the product's clean-environment runtime checks before publishing the draft. A passing source-packaging test is not a runtime qualification.

For local source-package verification:

```sh
python -m unittest discover -s tests -v
python tools/prepare_release.py --tag v1.0.0 --repository OWNER/REPOSITORY
cd release-assets
sha256sum --check SHA256SUMS.txt
```

On Windows, compare `Get-FileHash -Algorithm SHA256 <asset>` with the corresponding entry in `SHA256SUMS.txt`. SHA-256 detects changed files; it is not a digital signature.

## Screenshot quality

Use a native window or browser capture with pointer inclusion disabled. Move the pointer away from the capture, remove text-input focus, and disable click highlights or capture overlays. Inspect the saved image at its original size for mouse arrows, I-beams, carets and halos. Repeat this check for portfolio copies. Preserve real UI text and warnings; recapture when an overlay prevents a faithful repair.

## After publishing

- Download and test the published assets.
- Check the README download instructions.
- Verify screenshots and version references.
- Open issues for any known post-release work.

