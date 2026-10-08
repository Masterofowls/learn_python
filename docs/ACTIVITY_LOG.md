# Activity log

Running history of tutoring and repo changes.

## 2026-10-09

- QA Stage 1 (pytest L1–L9) complete; unlocked Stage 2 Jest + SuperTest at L10.
- QA pytest L9 complete (`pytest.ini` + 100% cov on `math_utils`, 3 passed).

## 2026-10-02

- QA pytest L8 complete (httpbin GET/POST with timeout, 2 passed); current = pytest L9 (config/coverage).
- QA pytest L7 complete (`monkeypatch.setenv` + default banner, 2 passed); current = pytest L8 (API + requests).
- QA pytest L6 complete (skip/xfail/slow + `-m slow`, 2 passed / 1 skipped / 1 xfailed); current = pytest L7 (mocking).
- QA pytest L5 complete (parametrize 4 rows + raises, 5 passed); current = pytest L6 (markers).
- QA pytest L4 complete (custom fixture + `tmp_path` file test, 2 passed); current = pytest L5 (parametrize).
- QA pytest L3 complete (`pytest.raises` + `match=`, 2 passed); current = pytest L4 (fixtures).
- QA pytest L2 complete (`qa/pytest/lesson2`, 3 passed, separate `math_utils`); current = pytest L3 (`pytest.raises`).
- QA pytest L1 complete (`qa/pytest/lesson1`, 2 passed); current = pytest L2.
- QA curriculum reordered (ADR-008): Stage 1 pytest → Stage 2 Jest+SuperTest → Stage 3 Playwright; curl/HTTPie demoted to optional appendix.
- QA orientation L1 notes kept; current = pytest Lesson 1.

## 2026-10-01

- Added QA/testing track (`qa/`, `docs/qa/*`): curl → HTTPie → pytest → Jest → Playwright → advanced; ADR-007.
- JS Lesson 5 reviewed complete (`js/lesson5.js`, `for...of` fix); current = JS L6.
- JS Lesson 4 reviewed complete (`js/lesson4.js`); current = JS L5.
- JS Lesson 3 reviewed complete (`js/lesson3.js`); current = JS L4.
- JS Lesson 2 reviewed complete (`js/lesson2.js`); current = JS L3.
- JS Lesson 1 reviewed complete (`js/lesson1.js`); current = JS L2.
- ADR-006: lesson quizzes/tests skipped temporarily (Theory → task → review). Updated `HOW_TO_LEARN.md` + `TUTOR.md`.
- Started JS track at Lesson 1 (theory + task assigned).
- Reorganized repo into dual tracks: moved all `lesson*.py` + `helpers.py` → `python/`; created `js/` for JavaScript lessons.
- Split curricula: `docs/python/*`, `docs/js/*`; shared process docs updated (`HOW_TO_LEARN`, `TUTOR`, `ARCHITECTURE`, `DECISIONS`).
- Python progress unchanged: Stage 2 current = L21. JS progress: Stage 1 current = L1.
- Lesson 20 (`*args` / `**kwargs`) reviewed complete; Lesson 19 comprehensions complete earlier same day.

## 2026-09-26

- Created local learning docs: `CURRICULUM.md`, `HOW_TO_LEARN.md`, `PROGRESS.md`, `ARCHITECTURE.md`, `DECISIONS.md`, root `README.md`.
- Locked curriculum into 4 stages: Stage 1 done (L1–L13); Stage 2 next (L14 Sets → L26 logging); Stage 3 = NumPy → pandas → pytest; Stage 4 = FastAPI → Django.
- Expanded `.gitignore` for Python artifacts, venv, env files, and logs.

## 2026-09-24 … 2026-09-26 (tutoring, pre-docs)

- Stage 1 completed interactively: lessons 1–13 (`lesson1.py` … `lesson13.py`, plus `helpers.py`).
- Topics covered: basics → control flow → collections intro → functions → files → errors → modules → classes → `time`/`requests` → `asyncio`.
- Agreed to insert Stage 2 depth before libraries and web frameworks.
