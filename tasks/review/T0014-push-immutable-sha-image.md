# T0014 — Push immutable SHA image to GHCR

## Business goal

Publish a reproducible container artifact for every accepted commit on approved branches so deployments can reference an exact source revision.

## Technical scope

- Extend the existing container workflow.
- Authenticate to GHCR only for trusted non-pull-request events.
- Publish `ghcr.io/<owner>/<repo>:<commit-sha>`.
- Keep pull-request execution build-only.

## Security impact

- Use the short-lived `GITHUB_TOKEN`; no static registry credential.
- Grant `packages: write` only to this workflow.
- Never authenticate or publish from pull-request events.
- No application ACL, record rule, `sudo()`, raw SQL, personal data, or production configuration changes.

## Files changed

- `.github/workflows/container-build.yml`
- `tasks/review/T0014-push-immutable-sha-image.md`
- `MASTER_TASK_PLAN.md` when backlog synchronization is committed.

## Test cases

1. Pull request: image builds successfully and is not pushed.
2. Push to `master`: workflow logs in to GHCR and pushes a SHA-only tag.
3. Push to `release/**`: workflow pushes the same immutable tag format.
4. No mutable `latest` tag is generated.

## Definition of done

- Workflow syntax passes.
- Pull-request container build passes without registry write.
- Approved-branch run publishes the SHA-tagged image.
- CI passes.
- Pull request documents security and rollback impact.
