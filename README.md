# learn_python

Personal interactive courses for **Python**, **JavaScript**, and **QA / testing** — same tutoring style.

## Tracks

| Track | Code folder | Curriculum | Progress | Current |
|-------|-------------|------------|----------|---------|
| Python | [`python/`](python/) | [docs/python/CURRICULUM.md](docs/python/CURRICULUM.md) | [docs/python/PROGRESS.md](docs/python/PROGRESS.md) | Stage 2 — L21 |
| JavaScript | [`js/`](js/) | [docs/js/CURRICULUM.md](docs/js/CURRICULUM.md) | [docs/js/PROGRESS.md](docs/js/PROGRESS.md) | Stage 1 — L6 |
| QA / Testing | [`qa/`](qa/) | [docs/qa/CURRICULUM.md](docs/qa/CURRICULUM.md) | [docs/qa/PROGRESS.md](docs/qa/PROGRESS.md) | Stage 2 — Jest L13 |

Tracks are **independent**. You can run them in parallel (QA Stage 1 needs almost no coding).

## How learning works

1. Theory → 2. You write the lesson artifact → 3. Tutor reviews → 4. Next lesson  

*(Quizzes temporarily off — see [docs/HOW_TO_LEARN.md](docs/HOW_TO_LEARN.md).)*

## Quick start

**Python:**

```bash
cd python
python lesson21.py
```

**JavaScript:**

```bash
cd js
node lesson5.js
```

**QA:**

```bash
# Stage 1: pytest labs under qa/pytest/
# Stage 2: Jest + SuperTest under qa/jest/
# Stage 3: Playwright under qa/playwright/
```

QA path skips curl/HTTPie as required stages (optional appendix only).

## Layout

```
python/           # Python lessons
js/               # JavaScript lessons
qa/               # Testing labs (curl, httpie, pytest, jest, playwright)
docs/
  HOW_TO_LEARN.md
  TUTOR.md
  python/  js/  qa/
```

## Stage locks

Do not skip stages **within** a track.  
QA owns deep testing; Python/JS Stage 3 unit-test lessons stay short intros.
