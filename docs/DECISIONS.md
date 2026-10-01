# Decisions (ADR log)

## ADR-001: Four-stage curriculum with hard locks (Python)

- **Date:** 2026-09-26
- **Status:** Accepted
- **Decision:** Stage 2 depth (L14–L26) before NumPy → pandas → pytest; then FastAPI → Django.
- **Consequences:** Libraries/web wait until language depth is done.

## ADR-002: Tutoring loop = Theory → Test → task file → review

- **Date:** 2026-09-24
- **Status:** Accepted
- **Decision:** Each lesson has theory, quiz, task file, tutor review.
- **Consequences:** Progress gated on understanding.

## ADR-003: Language folders instead of repo-root lessons

- **Date:** 2026-10-01
- **Status:** Accepted (supersedes flat root lessons from ADR-003 old form)
- **Context:** Learner wants the same interactive system for JavaScript alongside Python.
- **Decision:** Move all Python lessons to `python/`; add `js/` with parallel curriculum/docs. Shared process docs stay under `docs/`; per-track maps under `docs/python/` and `docs/js/`.
- **Consequences:** Clear separation; run paths change (`python python/lessonN.py`, `node js/lessonN.js`).

## ADR-004: Stage 3 order is NumPy → pandas → pytest (Python)

- **Date:** 2026-09-26
- **Status:** Accepted
- **Decision:** NumPy first, then pandas, then pytest.

## ADR-005: Parallel JS four-stage track

- **Date:** 2026-10-01
- **Status:** Accepted
- **Decision:** JS mirrors Python stages with Node/JS analogs (arrays/objects, fetch/async, Vitest, Express/Fastify → Next/Nest). Tracks progress independently.
- **Consequences:** Tutor must scope to the active track’s `PROGRESS.md`.

## ADR-006: Skip lesson quizzes temporarily

- **Date:** 2026-10-01
- **Status:** Accepted (temporary)
- **Context:** Learner asked to skip tests/quizzes for now while starting the JS track.
- **Decision:** Tutoring loop is Theory → task → code review. No quiz required until the learner turns quizzes back on.
- **Consequences:** Faster lesson flow; less formal concept checks until re-enabled.
