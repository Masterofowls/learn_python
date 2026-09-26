# How to learn in this repo

Interactive tutoring format used for every lesson.

## Loop

1. **Theory** — tutor explains the topic (gradually, in detail).
2. **Test** — short quiz (answer in chat).
3. **Task** — you write code in `lessonN.py` (or files named in the lesson).
4. **Review** — tutor checks quiz + code (correctness and ideas, not only “it runs”).
5. **Next** — only after the lesson is marked complete.

## Your job

- Create/edit the lesson file yourself.
- Run it locally when useful: `python lessonN.py` (use your chosen pyenv version consistently).
- Send quiz answers and point at the file (e.g. `@lesson14.py`).
- Fix bugs the tutor flags before moving on.

## Tutor job

- Teach one lesson at a time.
- Grade quiz and code against the lesson requirements.
- Explain mistakes with a short correction (especially Python vs JS differences).
- Unlock the next lesson only when the current one is done.
- Follow `docs/CURRICULUM.md` stage locks (Stage 2 → 3 → 4).

## File conventions

| Kind | Pattern |
|------|---------|
| Lesson script | `lessonN.py` |
| Shared helpers | e.g. `helpers.py` when a lesson needs a second module |
| Generated/local data | e.g. `learner.txt` (gitignored when appropriate) |
| Docs | `docs/*.md` |

Prefer:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

for lessons from Stage 1 L10 onward (unless the lesson says otherwise).

## Environment tips

- Stick to **one** Python version per session (example: 3.12.10 via pyenv).
- Install packages into that same interpreter:

  ```bash
  py -3.12 -m pip install requests
  ```

- After Lesson 22, use a project venv and `requirements.txt`.

## Progress tracking

- Checklist: `docs/PROGRESS.md`
- Full map: `docs/CURRICULUM.md`
- What changed when: `docs/ACTIVITY_LOG.md`

## Current focus

See **Current** in `docs/PROGRESS.md`. As of Stage 2 start: **Lesson 14 — Sets**.
