# Architecture

Personal **dual-track** learning workspace (Python + JavaScript), not a product monorepo.

## Layout

```
learn_python/
  python/                 # Python lessons (lessonN.py, helpers.py)
  js/                     # JavaScript lessons (lessonN.js)
  docs/
    HOW_TO_LEARN.md       # shared tutoring loop
    TUTOR.md
    ACTIVITY_LOG.md
    ARCHITECTURE.md       # this file
    DECISIONS.md
    python/
      CURRICULUM.md
      PROGRESS.md
    js/
      CURRICULUM.md
      PROGRESS.md
      HOW_TO_LEARN.md
  README.md
```

## Design choices

- **Two code roots** keep languages separate while sharing the same study method.
- **Lesson-per-file** keeps feedback small and reviewable.
- **Per-track stage locks** prevent jumping to frameworks before depth.
- **Docs per track** for curriculum/progress; shared docs for process.

## Runtime

- Python: CPython via pyenv; later `python/.venv` + `requirements.txt`.
- JavaScript: Node.js LTS; later `js/package.json` + local `node_modules`.

## Future (each track Stage 3–4)

```
python/apps/   or  js/apps/
python/tests/  or  js/tests/
```

Until then, flat `lessonN` files inside `python/` and `js/` are intentional.
