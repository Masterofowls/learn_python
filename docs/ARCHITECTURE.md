# Architecture

Personal **multi-track** learning workspace (Python + JavaScript + QA), not a product monorepo.

## Layout

```
learn_python/
  python/                 # Python lessons
  js/                     # JavaScript lessons
  qa/                     # Testing labs (curl, httpie, pytest, jest, playwright)
  docs/
    HOW_TO_LEARN.md
    TUTOR.md
    ACTIVITY_LOG.md
    ARCHITECTURE.md
    DECISIONS.md
    python/
    js/
    qa/
  README.md
```

## Design choices

- **Separate code roots** per track; shared tutoring method.
- **Lesson-sized artifacts** for reviewable feedback.
- **Per-track stage locks** so tools/frameworks wait on foundations.
- **QA is its own track** so testing can go deep without blocking language study.

## Runtime

- Python: CPython / pyenv; venv as needed for pytest (`qa/pytest`).
- JavaScript: Node.js LTS; local installs for Jest, SuperTest, Playwright under `qa/jest` and `qa/playwright`.

## Growth

```
qa/pytest/       # Stage 1
qa/jest/         # Stage 2 (+ SuperTest)
qa/playwright/   # Stage 3
```
