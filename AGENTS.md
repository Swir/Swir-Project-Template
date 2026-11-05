# Repository maintenance

For repository reviews, updates and release preparation, follow [docs/REPOSITORY_REVIEW.md](docs/REPOSITORY_REVIEW.md) and [PROJECT_CHECKLIST.md](PROJECT_CHECKLIST.md).

Include application/source state, dependencies, upstream data freshness, the actual update path, functional validation and release integrity. Report the evidence and unresolved issues before calling maintenance complete. Preserve the user's explicit scope and repository-specific constraints.

Inspect workflows before pushing: documentation and screenshots must not overwrite published binaries. For remote data, use the current date and the real production endpoints. Do not make old data appear fresh by only changing metadata or relaxing validation.

