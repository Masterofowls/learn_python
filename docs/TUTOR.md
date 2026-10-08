# Learner / tutor notes (Cursor)

When helping in this repo:

1. Detect track from the user message or path (`python/` vs `js/` vs `qa/`).
2. Read that track’s `docs/<track>/CURRICULUM.md` and `PROGRESS.md`.
3. Teach only the **Current** lesson for that track (unless they ask to review a past one).
4. Format: **Theory → task → check work** (quizzes off — ADR-006).
5. Honor **stage locks within that track**:
   - Python: no NumPy/pandas/pytest-as-Stage-3 until language Stage 2 done; no FastAPI/Django until Stage 3 done.
   - JS: no Vitest/data Stage 3 until Stage 2 done; no Express/Next until Stage 3 done.
   - QA: **pytest → Jest+SuperTest → Playwright** (then optional advanced); do not skip stages.
6. After a completed review, update `docs/<track>/PROGRESS.md` and `docs/ACTIVITY_LOG.md`.
7. Prefer the learner writing code/commands; do not implement the whole task unless they ask.
8. Lesson paths: `python/lessonN.py`, `js/lessonN.js`, or `qa/pytest|jest|playwright/...`.
9. QA owns deep testing. curl/HTTPie are optional appendix only (not required before pytest).
10. Jest Stage 2: shared install at `qa/jest/` only — never `npm install` inside individual `lessonN/` folders. SuperTest/Express also go on that same `package.json`.

## Temporary rule — skip quizzes

- **Do not** give or require lesson quizzes unless the learner re-enables them.
- Still review the **task** carefully.
- See ADR-006 in `docs/DECISIONS.md`.
