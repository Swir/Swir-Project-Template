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

The template includes a manual **Create Release** GitHub Actions workflow.

Open:

`Actions → Create Release → Run workflow`

Provide:

- a version tag such as `v1.0.0`,
- a release title,
- whether it is a pre-release.

Attach platform-specific binaries or installers when the project produces them.

## After publishing

- Download and test the published assets.
- Check the README download instructions.
- Verify screenshots and version references.
- Open issues for any known post-release work.
