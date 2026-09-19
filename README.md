<div align="center">

# ⚡ SWIR Project Template

### Professional repository blueprint for new SWIR software

**STRUCTURE • CI • DEPENDABOT • ROADMAP • RELEASES • DOCUMENTATION • QA**

[![CI](https://github.com/Swir/Swir-Project-Template/actions/workflows/ci.yml/badge.svg)](https://github.com/Swir/Swir-Project-Template/actions/workflows/ci.yml)
![Dependabot](https://img.shields.io/badge/DEPENDABOT-ENABLED-02050A?style=for-the-badge&logo=dependabot&logoColor=62E5FF)
![Release](https://img.shields.io/badge/RELEASE-WORKFLOW-02050A?style=for-the-badge&logo=githubactions&logoColor=62E5FF)
![Standard](https://img.shields.io/badge/SWIR-STANDARD-02050A?style=for-the-badge&logo=github&logoColor=62E5FF)

[![Author](https://img.shields.io/badge/Author-Swir-0088FF?style=flat-square&logo=github)](https://github.com/Swir)
[![Stars](https://img.shields.io/github/stars/Swir/Swir-Project-Template?style=flat-square&color=0088FF)](https://github.com/Swir/Swir-Project-Template/stargazers)

</div>

<img width="100%" src="https://raw.githubusercontent.com/Swir/Swir/main/assets/power-divider-v4.svg" alt="SWIR electric divider" />

## 🚀 Start new projects at release quality

**SWIR Project Template** is the reusable foundation for new repositories.

Instead of rebuilding repository structure, automation, documentation and release housekeeping every time, start with a clean baseline and focus on the actual product.

```text
IDEA  →  PROJECT  →  BUILD  →  TEST  →  RELEASE  →  EVOLVE
          ▲
          │
     THIS TEMPLATE
```

> After creating a new repository from this blueprint, open **[TEMPLATE_SETUP.md](TEMPLATE_SETUP.md)** and complete the initialization checklist.

---

## ✨ Batteries included

| Module | Included | What it gives you |
|---|:---:|---|
| 🧱 **Project structure** | ✅ | `src/`, `tests/`, `docs/`, icons and screenshots |
| ⚙️ **GitHub Actions CI** | ✅ | Automatic repository and Python syntax checks |
| 🤖 **Dependabot** | ✅ | Weekly GitHub Actions and pip dependency updates |
| 🗺️ **Roadmap** | ✅ | Milestones + visible project progress |
| 📝 **Changelog** | ✅ | A clean place for user-facing release history |
| ✅ **Quality checklist** | ✅ | Pre-release QA and repository review |
| 🚀 **Release workflow** | ✅ | Manual GitHub Release creation from Actions |
| 📚 **Release guide** | ✅ | Repeatable release process |
| 🎨 **README standard** | ✅ | SWIR presentation + Search Keywords guidance |
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
│   └── screenshots/
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

## ⚡ New project setup

### 01 · Create

Create a new repository from this blueprint.

### 02 · Brand

Replace the template identity with the real project:

- project name,
- one-line description,
- application icon,
- screenshots,
- repository description,
- GitHub topics,
- project-specific Search Keywords.

### 03 · Configure

Keep only the tooling the project actually uses.

For a non-Python project, remove or replace Python-specific dependency and CI sections instead of carrying unused configuration.

### 04 · Build

Put application code in `src/` and tests in `tests/`, unless the technology stack has a stronger convention.

### 05 · Release

Before publishing, review:

- **[PROJECT_CHECKLIST.md](PROJECT_CHECKLIST.md)**
- **[docs/RELEASE_GUIDE.md](docs/RELEASE_GUIDE.md)**
- **[CHANGELOG.md](CHANGELOG.md)**
- **[ROADMAP.md](ROADMAP.md)**

---

## 🧪 Automation

### GitHub Actions CI

The included CI workflow:

- checks required repository files,
- sets up Python 3.12,
- compiles Python source when Python files are present,
- skips Python compilation cleanly for non-Python repositories.

### Dependabot

Weekly checks are configured for:

- **GitHub Actions**
- **pip / Python dependencies**

### Release workflow

The **Create Release** workflow can generate a GitHub Release from the Actions tab using:

- release tag,
- release title,
- pre-release toggle.

See **[docs/RELEASE_GUIDE.md](docs/RELEASE_GUIDE.md)** for the full release process.

---

## 🎯 SWIR project standard

Every finished public project should aim to have:

| Product | Repository | Release |
|---|---|---|
| Working main flow | Clear README | Tested build |
| Useful errors | Accurate screenshots | Version number |
| Own icon / identity | Search Keywords | Changelog |
| Stable behavior | No secrets committed | Useful release notes |
| Documented limitations | Passing CI | Verified release asset |

---

## 📈 Roadmap system

The included **[ROADMAP.md](ROADMAP.md)** starts with milestone-based planning and a visible completion bar.

```text
░░░░░░░░░░ 0%  →  ██████████ 100%
```

Update the percentage only when real milestones move forward.

---

## 🎨 README quality

A SWIR README should answer quickly:

```text
WHAT IS IT?
WHY USE IT?
HOW DO I INSTALL IT?
HOW DO I USE IT?
IS IT ACTIVE / SAFE TO TRY?
```

The full repository presentation standard is in **[docs/README_STYLE_GUIDE.md](docs/README_STYLE_GUIDE.md)**.

---

## 🛡️ Shared project governance

New repositories can inherit community standards from **[Swir/.github](https://github.com/Swir/.github)**:

- bug reports,
- feature requests,
- documentation reports,
- pull request checklist,
- contributing guidelines,
- security policy,
- support guidance,
- code of conduct.

A project can override any default with its own local file.

---

## 🔎 Search Keywords

`github project template` • `software project template` • `python project template` • `github actions template` • `dependabot template` • `release workflow` • `open source project structure` • `repository boilerplate` • `SWIR project template`

---

<img width="100%" src="https://raw.githubusercontent.com/Swir/Swir/main/assets/power-divider-v4.svg" alt="SWIR electric divider" />

<div align="center">

### `SWIR // PROJECT BLUEPRINT`

## START CLEAN. SHIP BETTER.

**Build the product — not the repository boilerplate.**

[**← SWIR Profile**](https://github.com/Swir) · [**Shared Standards →**](https://github.com/Swir/.github)

</div>
