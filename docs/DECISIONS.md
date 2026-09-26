# Decisions (ADR log)

## ADR-001: Four-stage curriculum with hard locks

- **Date:** 2026-09-26
- **Status:** Accepted
- **Context:** Learner wants zero → advanced, including numpy/pandas/pytest and later FastAPI/Django, but Stage 1 skimmed sets, list/dict/tuple depth, strings, comprehensions, typing, etc.
- **Decision:** Insert **Stage 2** (L14–L26) for language/tooling depth. **Stage 3** = NumPy → pandas → pytest. **Stage 4** = FastAPI → Django. No skipping stages.
- **Consequences:** Libraries and web frameworks wait until Stage 2 is complete; stronger foundation for pandas and APIs.

## ADR-002: Tutoring loop = Theory → Test → task file → review

- **Date:** 2026-09-24
- **Status:** Accepted
- **Context:** Learner wants interactive teaching with checked homework, not only “run the script.”
- **Decision:** Each lesson has theory, a short quiz, a `lessonN.py` task, then tutor review of answers and code.
- **Consequences:** Progress is gated on understanding, not only output.

## ADR-003: Flat lesson files until Stage 3

- **Date:** 2026-09-26
- **Status:** Accepted
- **Context:** Early lessons are tiny scripts; a full `apps/` monorepo would add noise.
- **Decision:** Keep `lessonN.py` at repo root through Stage 2; introduce `apps/`, `tests/` when pytest and web work begin.
- **Consequences:** Simple git status and reviews; structure grows when needed.

## ADR-004: Stage 3 order is NumPy → pandas → pytest

- **Date:** 2026-09-26
- **Status:** Accepted
- **Context:** Learner listed pandas/pytest/numpy; pandas conceptually builds on array thinking; pytest should test real code after data libs are introduced.
- **Decision:** Teach NumPy first, then pandas, then pytest.
- **Consequences:** Clear dependency order for Stage 3 lessons.
