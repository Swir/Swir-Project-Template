# SWIR Project Quality Checklist

Use this before a public release.

## Product

- [ ] Core feature works from a clean install
- [ ] Main user flow is understandable without source-code knowledge
- [ ] Errors produce useful messages
- [ ] Existing features were regression-tested

## UI / Branding

- [ ] Application has its own icon
- [ ] UI has no clipped or overlapping controls
- [ ] Text remains readable at common scaling levels
- [ ] Screenshots match the current release
- [ ] Screenshots contain no mouse pointer, text caret, click highlight or capture-tool glow
- [ ] Full-resolution screenshots and portfolio copies were visually reviewed

## Repository

- [ ] README describes installation and usage
- [ ] Search Keywords are accurate and project-specific
- [ ] Roadmap progress is current
- [ ] Changelog is updated
- [ ] No tokens, passwords or private data are committed
- [ ] Releases contain clear notes

## Engineering

- [ ] Source layout is understandable
- [ ] Temporary/generated files are ignored
- [ ] CI passes
- [ ] Dependencies are justified and documented
- [ ] Known limitations are documented

## Release

- [ ] Version number is consistent
- [ ] Build was tested on a clean machine or environment
- [ ] Release assets launch correctly
- [ ] Existing tag resolves to the exact tested source commit
- [ ] Downloaded assets match the published SHA-256 checksums
- [ ] Source-only packages are clearly distinguished from runnable binaries
- [ ] Rollback or recovery path is known for risky changes

