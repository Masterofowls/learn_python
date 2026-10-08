# QA / Testing Curriculum

Automated testing path (revised). Same tutoring loop: Theory → task → review (quizzes off).  
Do **not** skip stages within this track.

**Code:** `qa/`  
**Path:** **pytest → Jest + SuperTest → Playwright**

> curl / HTTPie and “why test” notes are **optional appendix** — not required before Stage 1.

---

## Stages overview

| Stage | Name | Focus | Status |
|-------|------|--------|--------|
| 1 | pytest | Python unit → API-style tests | Complete |
| 2 | Jest + SuperTest | JS unit + HTTP API tests | **Current** |
| 3 | Playwright | Browser E2E | Locked until Stage 2 |
| 4 | Advanced (optional) | CI, strategy, flaky tests | Locked until Stage 3 |

**Jest install:** shared at `qa/jest/` (one `package.json` / `node_modules`). Lessons are subfolders only — no per-lesson npm install.

---

## Stage 1 — pytest

| Lesson | Topic | Artifact |
|--------|--------|----------|
| 1 | Install pytest; first `test_*.py`; `assert` | `qa/pytest/lesson1/` |
| 2 | Multiple tests; AAA in code; `pytest -v` | `qa/pytest/lesson2/` |
| 3 | `pytest.raises` | `qa/pytest/lesson3/` |
| 4 | Fixtures (`@pytest.fixture`) | `qa/pytest/lesson4/` |
| 5 | Parametrize | `qa/pytest/lesson5/` |
| 6 | Markers, skip, xfail; selecting tests | `qa/pytest/lesson6/` |
| 7 | Mocking / monkeypatch | `qa/pytest/lesson7/` |
| 8 | API-style tests with `requests` (or httpx) | `qa/pytest/lesson8/` |
| 9 | `pytest.ini` / layout; coverage mindset | `qa/pytest/lesson9/` |

---

## Stage 2 — Jest + SuperTest

| Lesson | Topic | Artifact |
|--------|--------|----------|
| 10 | First `*.test.js`; `expect` (Jest already at `qa/jest/`) | `qa/jest/lesson10/` |
| 11 | `describe` / matchers; AAA | `qa/jest/lesson11/` |
| 12 | Async tests; `jest.fn` mocks | `qa/jest/lesson12/` |
| 13 | Hooks (`beforeEach`); testing modules | `qa/jest/lesson13/` |
| 14 | SuperTest setup; first HTTP assert on an Express (or similar) app | `qa/jest/lesson14/` |
| 15 | SuperTest: POST/JSON, status codes, headers | `qa/jest/lesson15/` |
| 16 | SuperTest + auth / errors; Jest config & coverage | `qa/jest/lesson16/` |

---

## Stage 3 — Playwright

| Lesson | Topic | Artifact |
|--------|--------|----------|
| 17 | Install Playwright; first browser test | `qa/playwright/lesson17/` |
| 18 | Locators, clicks, fills, assertions | `qa/playwright/lesson18/` |
| 19 | Navigation, waits, auto-waiting | `qa/playwright/lesson19/` |
| 20 | Page Object Model intro | `qa/playwright/lesson20/` |
| 21 | `APIRequestContext` + UI hybrid | `qa/playwright/lesson21/` |
| 22 | Trace, screenshots, debug failures | `qa/playwright/lesson22/` |
| 23 | Projects / multi-browser config | `qa/playwright/lesson23/` |

---

## Stage 4 — Advanced (optional)

| Lesson | Topic |
|--------|--------|
| 24 | Mini test strategy (what to automate where) |
| 25 | Capstone: pytest API + Jest/SuperTest + Playwright smoke |
| 26 | CI (GitHub Actions) |
| 27 | Flaky tests / isolation |
| 28 | Reporting / quality gates |

---

## Appendix (optional, not staged)

- Why test / test pyramid (`qa/lesson1.md` — already done as orientation)
- AAA notes (`qa/lesson2.md` — optional)
- `curl` / HTTPie labs — revisit anytime for manual API exploration

---

## Rules

1. One lesson at a time; stage locks: pytest → Jest/SuperTest → Playwright.
2. Prefer small runnable projects under `qa/pytest`, `qa/jest`, `qa/playwright`.
3. No secrets in repo — use `.env` (gitignored).
4. Language tracks may still have a short unit-test intro; **this track owns depth**.
