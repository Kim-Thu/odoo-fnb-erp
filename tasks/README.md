# Task workflow

Task states:

- `backlog/`: ready or waiting for dependencies.
- `in-progress/`: exactly one active task per worker.
- `review/`: code complete, waiting for CI/review.
- `blocked/`: cannot proceed; reason must be recorded.
- `done/`: merged and verified.

Execution order is defined in `MASTER_TASK_PLAN.md`.

Each task must use one branch:

`<type>/<task-id>-<short-name>-<YYYYMMDD-HHmm>`

Before implementation:

1. Read the task file.
2. Verify dependencies are `done`.
3. Create the branch from the latest approved base.
4. Move the task to `in-progress/`.

Before completion:

1. Run all required tests.
2. Check security and multi-company rules.
3. Update the task evidence section.
4. Move the task to `review/`.
5. Move to `done/` only after CI passes and the change is merged.
