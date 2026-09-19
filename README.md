<div align="center">

<img width="100%" src="assets/readme-hero.svg" alt="SWIR Project Blueprint" />

<br>

[![CI](https://github.com/Swir/Swir-Project-Template/actions/workflows/ci.yml/badge.svg)](https://github.com/Swir/Swir-Project-Template/actions/workflows/ci.yml)
[![Template](https://img.shields.io/badge/GITHUB-TEMPLATE_ENABLED-02050A?style=flat-square&logo=github&logoColor=62E5FF)](https://github.com/Swir/Swir-Project-Template)
[![Maintained by Swir](https://img.shields.io/badge/MAINTAINER-SWIR-02050A?style=flat-square&logo=github&logoColor=62E5FF)](https://github.com/Swir)

### [**USE THIS TEMPLATE →**](https://github.com/new?template_name=Swir-Project-Template&template_owner=Swir)

**Reusable foundation for new SWIR software repositories.**

</div>

<img width="100%" src="assets/readme-divider.svg" alt="" />

## 🚀 Release-ready foundation

**SWIR Project Template** provides the repository structure and maintenance tooling that new projects usually need before real product work can begin.

Instead of rebuilding CI, documentation, release housekeeping and project layout every time, start from a consistent baseline and customize only what the project actually requires.

```text
IDEA  →  PROJECT  →  BUILD  →  TEST  →  RELEASE  →  EVOLVE
          ▲
          │
      THIS TEMPLATE
```

> After creating a repository, open **[TEMPLATE_SETUP.md](TEMPLATE_SETUP.md)** and complete the initialization checklist before the first public release.

---

## ✨ Included by default

| Module | Status | Purpose |
|---|:---:|---|
| 🧱 **Project structure** | ✅ | `src/`, `tests/`, `docs/`, icons and screenshots |
| ⚙️ **GitHub Actions CI** | ✅ | Repository checks and Python syntax validation when applicable |
| 🤖 **Dependabot** | ✅ | Weekly GitHub Actions and pip dependency updates |
| 🗺️ **Roadmap** | ✅ | Milestones and visible project progress |
| 📝 **Changelog** | ✅ | User-facing release history |
| ✅ **Quality checklist** | ✅ | Pre-release QA and repository review |
| 🚀 **Release workflow** | ✅ | Manual GitHub Release creation from Actions |
| 📚 **Release guide** | ✅ | Repeatable publishing process |
| 🎨 **README standard** | ✅ | SWIR presentation and Search Keywords guidance |
| 🛡️ **Community baseline** | ✅ | Shared issues, PRs, security and contribution rules |

---

## 📦 Repository structure

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

---

## ⚡ From template to project

### 01 · Create

Use **[Use this template](https://github.com/new?template_name=Swir-Project-Template&template_owner=Swir)** to create a clean repository from this blueprint.

### 02 · Brand

Replace the template identity with the real project:

- project name and description,
- application icon,
- screenshots,
- repository description and topics,
- project-specific Search Keywords.

### 03 · Configure

Keep only the automation and dependencies the project actually uses.

For a non-Python project, remove or replace Python-specific dependency and CI configuration rather than carrying unused tooling.

### 04 · Build

Keep application code in `src/` and tests in `tests/`, unless the chosen technology has a stronger standard layout.

### 05 · Release

Before publishing, review:

- **[PROJECT_CHECKLIST.md](PROJECT_CHECKLIST.md)**
- **[docs/RELEASE_GUIDE.md](docs/RELEASE_GUIDE.md)**
- **[CHANGELOG.md](CHANGELOG.md)**
- **[ROADMAP.md](ROADMAP.md)**

---

## 🧪 Automation

### Continuous integration

The included CI workflow:

- verifies the expected repository baseline,
- sets up Python 3.12,
- compiles Python sources when present,
- skips Python compilation cleanly for non-Python repositories.

### Dependency maintenance

Dependabot performs weekly checks for:

- **GitHub Actions**
- **pip / Python dependencies**

### Releases

The **Create Release** workflow can create a GitHub Release directly from the Actions tab using a tag, title and optional pre-release flag.

See **[docs/RELEASE_GUIDE.md](docs/RELEASE_GUIDE.md)** before publishing.

---

## 🎯 SWIR project standard

| Product | Repository | Release |
|---|---|---|
| Working main flow | Clear README | Tested build |
| Useful errors | Accurate screenshots | Consistent version |
| Own icon / identity | Search Keywords | Updated changelog |
| Stable behavior | No secrets committed | Useful release notes |
| Documented limitations | Passing CI | Verified release assets |

---

## 📈 Roadmap system

The included **[ROADMAP.md](ROADMAP.md)** starts with milestone-based planning and a visible completion bar.

```text
░░░░░░░░░░ 0%  →  ██████████ 100%
```

Progress should reflect completed project milestones rather than activity alone.

---

## 🎨 README quality standard

A finished README should answer quickly:

```text
WHAT IS IT?
WHY USE IT?
HOW DO I INSTALL IT?
HOW DO I USE IT?
IS IT MAINTAINED AND SAFE TO TRY?
```

See **[docs/README_STYLE_GUIDE.md](docs/README_STYLE_GUIDE.md)** for the full SWIR presentation standard.

---

## 🛡️ Shared governance

Repositories can inherit community standards from **[Swir/.github](https://github.com/Swir/.github)**:

- bug reports,
- feature requests,
- documentation reports,
- pull request checklist,
- contribution guidelines,
- security policy,
- support guidance,
- code of conduct.

Any project can override a default with its own local file.

---

## 🔎 Search Keywords

`github project template` • `software project template` • `python project template` • `github actions template` • `dependabot template` • `release workflow` • `open source project structure` • `repository boilerplate` • `SWIR project template`

<img width="100%" src="assets/readme-divider.svg" alt="" />

<div align="center">

### `SWIR // PROJECT BLUEPRINT`

## START CLEAN. SHIP BETTER.

**Build the product — not the repository boilerplate.**

[**← SWIR Profile**](https://github.com/Swir) · [**Shared Standards →**](https://github.com/Swir/.github)

</div>
