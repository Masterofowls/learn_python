# Learner / tutor notes (Cursor)

When helping in this repo:

1. Detect track from the user message or path (`python/` vs `js/`).
2. Read that track’s `docs/<track>/CURRICULUM.md` and `PROGRESS.md`.
3. Teach only the **Current** lesson for that track (unless they ask to review a past one).
4. Format: **Theory → task file → check code** (see temporary rule below).
5. Honor **stage locks within that track**:
   - Python: no NumPy/pandas/pytest until Stage 2 done; no FastAPI/Django until Stage 3 done.
   - JS: no Vitest/data Stage 3 until Stage 2 done; no Express/Next until Stage 3 done.
6. After a completed review, update `docs/<track>/PROGRESS.md` and `docs/ACTIVITY_LOG.md`.
7. Prefer the learner writing code; do not implement the whole task for them unless they ask.
8. Lesson paths: `python/lessonN.py` or `js/lessonN.js` (not repo root).

## Temporary rule — skip quizzes

- **Do not** give or require lesson quizzes / written tests unless the learner re-enables them.
- Still review the **task code** carefully.
- Documented in `docs/HOW_TO_LEARN.md` and `docs/DECISIONS.md` (ADR-006).
