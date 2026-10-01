# How to learn in this repo

Interactive tutoring for **Python** and **JavaScript**. Same loop; separate folders and progress files.

## Loop (both tracks)

1. **Theory** — tutor explains the topic.
2. **Task** — you write the lesson file.
3. **Review** — tutor checks code (ideas, not only “it runs”).
4. **Next** — only after the lesson is complete.

### Temporary rule — skip quizzes

**Quizzes / written tests are OFF for now.**  
Do not require quiz answers before the task. Resume quizzes only when the learner asks to turn them back on.

## Which track?

| Track | Folder | Run | Progress |
|-------|--------|-----|----------|
| Python | `python/` | `python python/lessonN.py` | [docs/python/PROGRESS.md](python/PROGRESS.md) |
| JavaScript | `js/` | `node js/lessonN.js` | [docs/js/PROGRESS.md](js/PROGRESS.md) |

Say which track you want in chat (e.g. “continue Python” or “start JS Lesson 1”).

## Your job

- Create/edit the lesson file yourself.
- Run it locally.
- `@`-mention the file when ready for review.
- Fix bugs the tutor flags before moving on.

## Tutor job

- Teach one **current** lesson per track (see that track’s `PROGRESS.md`).
- Honor **stage locks** inside that track.
- **Skip quizzes** until re-enabled.
- Prefer the learner writing code.
- Update the track’s `PROGRESS.md` and `docs/ACTIVITY_LOG.md` when a lesson is done.

## File conventions

| Track | Lesson file | Helpers |
|-------|-------------|---------|
| Python | `python/lessonN.py` | `python/helpers.py` |
| JS | `js/lessonN.js` | `js/helpers.js` |

### Python entry style (from L10+)

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

### JS entry style

```js
function main() {
  // ...
}

main();
```

## Environment

- **Python:** one interpreter for run + pip (pyenv); venv from Python L22.
- **JS:** Node.js LTS; npm/`package.json` from JS L22.

## Docs map

- Shared: this file, [TUTOR.md](TUTOR.md), [ARCHITECTURE.md](ARCHITECTURE.md), [DECISIONS.md](DECISIONS.md), [ACTIVITY_LOG.md](ACTIVITY_LOG.md)
- Python: [python/CURRICULUM.md](python/CURRICULUM.md)
- JS: [js/CURRICULUM.md](js/CURRICULUM.md), [js/HOW_TO_LEARN.md](js/HOW_TO_LEARN.md)
