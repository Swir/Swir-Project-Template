# New Project Setup

Use this checklist immediately after creating a repository from **Swir-Project-Template**.

## 1. Project identity

- [ ] Rename every `PROJECT_NAME` placeholder.
- [ ] Write a one-sentence project description.
- [ ] Set an accurate GitHub repository description.
- [ ] Add relevant repository topics.
- [ ] Add the real application/project icon to `assets/icons/`.
- [ ] Add screenshots to `assets/screenshots/`.

## 2. README

- [ ] Replace the template overview with the real project purpose.
- [ ] Document the actual installation method.
- [ ] Document the actual launch command or entry point.
- [ ] Remove sections that do not apply.
- [ ] Replace generic Search Keywords with project-specific phrases.
- [ ] Add known limitations when important.

## 3. Code and dependencies

- [ ] Put application code in `src/` or document a different layout.
- [ ] Keep dependencies in the appropriate manifest.
- [ ] Remove `requirements.txt` if the project is not Python-based.
- [ ] Add tests for important behavior.
- [ ] Confirm CI succeeds.

## 4. Roadmap and releases

- [ ] Update `ROADMAP.md` and its progress bar.
- [ ] Update `CHANGELOG.md`.
- [ ] Review `PROJECT_CHECKLIST.md`.
- [ ] Test the distributable build on a clean environment.
- [ ] Create a GitHub Release only after the release checklist passes.

## 5. Security and privacy

- [ ] Remove API keys, tokens, passwords and local secrets.
- [ ] Keep secrets in environment variables or secret storage.
- [ ] Review logs/screenshots for private information.
- [ ] Use the inherited SWIR security policy or add a project-specific policy.

## 6. Final cleanup

Delete this file when the project is fully initialized, or keep it as a maintainer checklist.
