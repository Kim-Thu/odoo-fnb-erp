# T0013 — Build container image on approved branches

## Status

`review`

## Scope

Add a dedicated GitHub Actions workflow that verifies the repository Docker image can be built on approved branches without publishing it.

## Changes

- Build on pushes to `master` and `release/**`.
- Build on pull requests to `master` only when container-relevant files change.
- Support manual workflow dispatch.
- Use Docker Buildx and GitHub Actions cache.
- Tag the temporary build with the immutable commit SHA.
- Do not push images or request package-write permissions.

## Validation

- GitHub validates workflow syntax when the pull request opens.
- The `build-container` job must complete successfully before merge.
- Existing CI remains unchanged.

## Security

- Workflow has read-only repository permissions.
- No registry credentials are used.
- No image is published.
- No production configuration or secrets are introduced.
