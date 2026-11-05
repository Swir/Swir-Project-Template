# SWIR repository maintenance review

Use this checklist when reviewing or updating repositories and releases. A narrower request can explicitly exclude areas; record those exclusions.

## Required review areas

Record each area as VERIFIED, FIXED, BLOCKED, NOT CHECKED or NOT APPLICABLE, with dated evidence and a reason for omissions.

1. **Application and source:** identify the maintained branch, shipped version, actual runtime consumer and unfinished fixes. Compare documentation with source and release state.
2. **Dependencies and upstream sources:** inspect supported dependency versions and advisories relevant to the project. For filters, blocklists, models, catalogs and remote data, identify upstream URLs, licenses, update cadence, supported schemas and the exact data used by the shipped application.
3. **Freshness:** fetch the real production endpoints, not only a manifest or cached screenshot. Check payload timestamps, expiry, age limits, version, checksum and provenance against the current date. A matching hash can describe stale data.
4. **Update behavior:** trace the update button/background job through fetch, validation, application and failure reporting. Distinguish live data refresh, bundled data rebuilt with the application, and store/application updates. Verify stale/offline/rejected-data fallback without weakening protection.
5. **Functional validation:** run relevant builds and regressions. For protection rules, test both intended blocking and normal login, checkout, media and other representative flows. State which runtime/platform checks were actually performed.
6. **Release integrity:** inspect push-triggered workflows before mutation. Ordinary docs/image commits must not silently overwrite a published binary. Tie artifacts to the exact tested commit/tag, verify downloaded hashes and preserve release channel/prerelease status.
7. **Presentation:** update truthful installation instructions, known limitations and release notes; review screenshots and portfolio/release copies at native size for pointers and glow.

## Completion rule

Prioritize stale protection data, broken update paths and release integrity. Complete authorized fixes with appropriate verification. If a remaining item requires user input or cannot be safely completed, identify the concrete blocker and affected product behavior. Do not report an overall maintenance review as complete based only on README, screenshot or checksum changes.

Never advance timestamps/expiry, increase age limits or bypass validators merely to make a stale-data check pass. A data refresh needs source review, compatibility and false-positive evidence. Failed detection of an existing stale feed is evidence of an open product issue, not a reason to weaken the check.

## Deliverable

For each reviewed repository, record: reviewed commit and product version; source/feed URLs and freshness; dependency findings; changes; tests; release artifact verification; unresolved issues and next actions. Include a check date. A missing release or a development branch is not itself a defect.

## Automated coverage

Use a read-only freshness CI check for time-sensitive published data, run it regularly and on relevant changes, and retain diagnostics on failure. Distinguish early warnings, expired/stale data and network failures. An automated age/integrity check does not establish the quality or completeness of filtering rules.

This shared document is linked by community contribution guidance. GitHub does not automatically apply a shared AGENTS.md to unrelated repositories; use repository-local instructions or the project template to make the review entry point explicit.

