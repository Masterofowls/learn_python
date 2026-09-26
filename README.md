# learn_python

Personal interactive Python course: zero → advanced, with staged locks.

## Quick start

1. Use one Python version (example: 3.12.10 via pyenv).
2. Open this folder in Cursor.
3. Read:
   - [docs/HOW_TO_LEARN.md](docs/HOW_TO_LEARN.md) — how each lesson works
   - [docs/CURRICULUM.md](docs/CURRICULUM.md) — full map
   - [docs/PROGRESS.md](docs/PROGRESS.md) — what is done / next
4. Do the **Current** lesson in `PROGRESS.md` (right now: **Lesson 14 — Sets**).
5. Write `lessonN.py`, answer the quiz in chat, ask the tutor to review.

## Stages (short)

| Stage | What | When |
|-------|------|------|
| 1 | Core language + first tools | Done (L1–L13) |
| 2 | Sets, collections master, strings, comps, OOP, venv, json, typing, pathlib, logging | Now (L14–L26) |
| 3 | NumPy → pandas → pytest | After Stage 2 |
| 4 | FastAPI → Django | After Stage 3 |

## Run a lesson

```bash
python lesson14.py
```

Install packages into the **same** interpreter you use to run:

```bash
python -m pip install requests
```

## Repo layout

- `lessonN.py` — lesson tasks
- `helpers.py` — shared module (Lesson 10+)
- `docs/` — curriculum, progress, architecture, decisions, activity log

## Contributing / study rules

- One lesson at a time; do not skip stages.
- Prefer `if __name__ == "__main__": main()` from Lesson 10 onward.
- Keep secrets out of git; use `.env` locally only (gitignored).
