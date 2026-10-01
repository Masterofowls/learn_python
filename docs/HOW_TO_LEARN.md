# How to learn in this repo

Interactive tutoring for **Python**, **JavaScript**, and **QA / testing**. Same loop; separate folders and progress files.

## Loop (all tracks)

1. **Theory** — tutor explains the topic.
2. **Task** — you write the lesson artifact.
3. **Review** — tutor checks work (ideas, not only “it runs”).
4. **Next** — only after the lesson is complete.

### Temporary rule — skip quizzes

**Quizzes / written tests are OFF for now.**  
Do not require quiz answers before the task. Resume quizzes only when the learner asks to turn them back on.

## Which track?

| Track | Folder | Typical run | Progress |
|-------|--------|-------------|----------|
| Python | `python/` | `python python/lessonN.py` | [docs/python/PROGRESS.md](python/PROGRESS.md) |
| JavaScript | `js/` | `node js/lessonN.js` | [docs/js/PROGRESS.md](js/PROGRESS.md) |
| QA | `qa/` | `pytest` / `npx jest` / `npx playwright test` | [docs/qa/PROGRESS.md](qa/PROGRESS.md) |

Say which track you want (e.g. “continue JS”, “start QA Lesson 1”, “continue Python L21”).

## Your job

- Create/edit the lesson artifact yourself.
- Run it locally.
- `@`-mention the file when ready for review.
- Fix issues the tutor flags before moving on.

## Tutor job

- Teach one **current** lesson per track (see that track’s `PROGRESS.md`).
- Honor **stage locks** inside that track.
- **Skip quizzes** until re-enabled.
- Prefer the learner writing code / commands.
- Update the track’s `PROGRESS.md` and `docs/ACTIVITY_LOG.md` when a lesson is done.

## File conventions

| Track | Lesson artifact |
|-------|-----------------|
| Python | `python/lessonN.py` |
| JS | `js/lessonN.js` |
| QA | `qa/lessonN.md`, `qa/lessonN.sh`, or `qa/<tool>/lessonN/` |

## Environment

- **Python:** one interpreter for run + pip; venv from Python L22 / QA pytest stage.
- **JS:** Node.js LTS; local `package.json` for Jest/Playwright.
- **QA Stage 1:** `curl` + [HTTPie](https://httpie.io/) on PATH.

## Docs map

- Shared: this file, [TUTOR.md](TUTOR.md), [ARCHITECTURE.md](ARCHITECTURE.md), [DECISIONS.md](DECISIONS.md), [ACTIVITY_LOG.md](ACTIVITY_LOG.md)
- [python/](python/) · [js/](js/) · [qa/](qa/)
