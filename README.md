<div align="center">

<img width="100%" src="assets/readme-hero.svg" alt="SWIR Project Template — a consistent starting point for your next software project" />

<br>

**Build your next SWIR project on a consistent foundation.**

Project structure &nbsp;·&nbsp; CI &nbsp;·&nbsp; Dependabot &nbsp;·&nbsp; Release workflow

[![CI](https://github.com/Swir/Swir-Project-Template/actions/workflows/ci.yml/badge.svg)](https://github.com/Swir/Swir-Project-Template/actions/workflows/ci.yml)

### [Use this template →](https://github.com/new?template_name=Swir-Project-Template&template_owner=Swir)

[**Setup checklist**](TEMPLATE_SETUP.md) · [**Release guide**](docs/RELEASE_GUIDE.md)

[Highlights](#highlights) · [Quick Start](#quick-start) · [Automation](#automation) · [Roadmap](#roadmap) · [Releases](#releases)

</div>

<img width="100%" src="assets/readme-divider.svg" alt="" />

## What is SWIR Project Template?

[SWIR Project Template](https://github.com/Swir/Swir-Project-Template) brings the structure, documentation and maintenance tooling for a new repository into one reusable starting point. Create a project, give it an identity and adapt the baseline to your technology.

The repository is enabled as a **GitHub template**. Its automation provides initial repository and Python syntax checks; add the build steps and tests your product needs as it develops.

## Highlights

| Included | What it provides |
|---|---|
| **Project structure** | Dedicated `src/`, `tests/`, `docs/`, icon and screenshot directories. |
| **Continuous integration** | [GitHub Actions CI](.github/workflows/ci.yml) for baseline files and Python syntax validation when sources are present. |
| **Dependency maintenance** | [Dependabot](.github/dependabot.yml) with weekly GitHub Actions and pip updates. |
| **Roadmap** | [Milestone planning](ROADMAP.md) with a visible project completion bar. |
| **Changelog** | [User-facing change history](CHANGELOG.md) to keep releases understandable. |
| **Quality checklist** | [Product and repository review](PROJECT_CHECKLIST.md) before publishing. |
| **Release workflow** | [Manual GitHub Release creation](.github/workflows/release.yml) with a tag, title and pre-release option. |
| **Release guide** | A [repeatable publishing process](docs/RELEASE_GUIDE.md), from build checks to verification of published assets. |
| **README standard** | [Presentation guidance](docs/README_STYLE_GUIDE.md) for project identity, useful documentation and Search Keywords. |
| **Community standards** | [SWIR guidance](https://github.com/Swir/.github) for issues, pull requests, contributing, security and support. |

## Quick Start

### 1. Create your repository

Select **[Use this template](https://github.com/new?template_name=Swir-Project-Template&template_owner=Swir)** and create a repository for the new project. Open **[TEMPLATE_SETUP.md](TEMPLATE_SETUP.md)** to work through the initialization checklist.

### 2. Give it an identity

Replace the template name, description and README with the real product. Add its application icon and current screenshots, set the repository description and topics, and write project-specific Search Keywords. Update repository links and the CI badge to point to the new project.

### 3. Configure the foundation

Review CI, dependency manifests and Dependabot for the chosen stack. For a non-Python project, remove or replace Python-specific configuration and `requirements.txt` as part of that project's setup.

### 4. Build and verify

Put application code in `src/` and tests in `tests/`, unless the technology has a more suitable standard layout. Add checks for the main behavior, confirm CI passes and keep the roadmap and changelog current.

Before the first public release, complete the [project checklist](PROJECT_CHECKLIST.md) and follow the [release guide](docs/RELEASE_GUIDE.md).

## Automation

### Continuous integration

The [CI workflow](.github/workflows/ci.yml) runs on pushes and pull requests. It uses Python **3.12**, compiles Python sources when present and skips compilation cleanly when there are no Python files. It also checks that `README.md`, `CHANGELOG.md` and `ROADMAP.md` exist.

Extend these initial checks with the project's own build, tests and packaging validation.

### Dependency maintenance

[Dependabot](.github/dependabot.yml) checks **GitHub Actions** and **pip / Python dependencies** weekly. Keep its ecosystem configuration aligned with the dependencies the project actually uses.

## Roadmap

[ROADMAP.md](ROADMAP.md) tracks four stages: **Foundation → Usability → Quality → Release**. The included completion bar starts at **0%** for a new project's milestones.

Update it as meaningful milestones are completed. Progress should represent finished project work; template availability or activity alone does not establish product readiness.

## Releases

The [Create Release workflow](.github/workflows/release.yml) publishes a GitHub Release from the Actions tab:

1. Review [PROJECT_CHECKLIST.md](PROJECT_CHECKLIST.md) and [docs/RELEASE_GUIDE.md](docs/RELEASE_GUIDE.md).
2. Test the build and update [CHANGELOG.md](CHANGELOG.md) and [ROADMAP.md](ROADMAP.md).
3. Open **Actions → Create Release → Run workflow**.
4. Provide a version tag such as `v1.0.0`, a release title and the pre-release flag when needed.
5. Review the generated release notes, attach any project binaries or installers, then download and verify the published assets.

The workflow creates the release and generates notes. Product builds, tests and asset uploads must be handled by the project's own release process.

## SWIR project standard

| Product | Repository | Release |
|---|---|---|
| Working main flow | Clear README | Tested build |
| Useful errors | Accurate screenshots | Consistent version |
| Own icon and identity | Search Keywords | Updated changelog |
| Stable behavior | No committed secrets | Useful release notes |
| Documented limitations | Passing CI | Verified release assets |

### README quality

A finished README should quickly explain **what the product is**, **why to use it**, **how to install and use it**, and **whether it is maintained and safe to try**.

Follow the [README style guide](docs/README_STYLE_GUIDE.md) for the full SWIR presentation standard. Keep the opening clear, screenshots current and claims grounded in working behavior.

### Shared governance

Repositories owned by Swir can use the supported defaults from **[Swir/.github](https://github.com/Swir/.github)**: bug, feature and documentation reports; the pull request checklist; contribution guidelines; security policy; support guidance; and code of conduct.

A project can override shared defaults with local files. If the new repository belongs to another account, configure its community files for that owner. See the [inheritance and override rules](https://github.com/Swir/.github#override-model).

## Project structure

```text
Swir-Project-Template/
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       ├── ci.yml
│       └── release.yml
├── assets/
│   ├── icons/
│   ├── screenshots/
│   ├── readme-divider.svg
│   └── readme-hero.svg
├── docs/
│   ├── README_STYLE_GUIDE.md
│   └── RELEASE_GUIDE.md
├── src/
├── tests/
├── .editorconfig
├── .gitignore
├── CHANGELOG.md
├── PROJECT_CHECKLIST.md
├── README.md
├── ROADMAP.md
├── TEMPLATE_SETUP.md
└── requirements.txt
```

## Search Keywords

`github project template` · `software project template` · `python project template` · `github actions template` · `dependabot template` · `release workflow` · `open source project structure` · `repository boilerplate` · `SWIR project template`

<img width="100%" src="assets/readme-divider.svg" alt="" />

<div align="center">

**SWIR · BUILD · RELEASE · EVOLVE**

A clear foundation. Room for your product.

[**Use this template →**](https://github.com/new?template_name=Swir-Project-Template&template_owner=Swir)

[**← SWIR Profile**](https://github.com/Swir) · [**Shared Standards →**](https://github.com/Swir/.github)

</div>
