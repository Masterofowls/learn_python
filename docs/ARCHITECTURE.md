# Architecture

This repo is a **personal Python learning workspace**, not a multi-app product monorepo.

## Layout

```
learn_python/
  lessonN.py          # one file per lesson task (N = lesson number)
  helpers.py          # shared module when a lesson needs imports
  docs/
    CURRICULUM.md     # full stage/lesson map + locks
    HOW_TO_LEARN.md   # tutoring workflow
    PROGRESS.md       # checklist
    ACTIVITY_LOG.md   # dated history
    ARCHITECTURE.md   # this file
    DECISIONS.md      # ADRs / choices
  README.md           # setup + how to start
```

## Design choices

- **Lesson-per-file** keeps feedback small and reviewable.
- **Stages** prevent jumping to pandas/web before language depth.
- **Docs as source of truth** for order; chat follows `CURRICULUM.md`.

## Runtime

- Local CPython via pyenv (Windows). Target one version per project phase (see Lesson 22 / venv).
- Third-party packages installed into that same environment (`python -m pip …`).

## Future (Stage 3–4)

When libraries and web apps appear, prefer:

```
apps/          # e.g. api experiments
packages/      # shared helpers if needed
tests/         # pytest
```

Until then, flat `lessonN.py` at repo root is intentional.
