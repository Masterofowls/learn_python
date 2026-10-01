# Contributing

Personal dual-track learning repo (Python + JavaScript).

## Rules

1. Follow the active track’s curriculum — no skipping stages within that track.
2. One lesson per change set when possible.
3. Mark lessons done only after tutor review; update `docs/<track>/PROGRESS.md`.
4. Append milestones to `docs/ACTIVITY_LOG.md`.
5. Conventional commits if you commit: `feat:`, `fix:`, `docs:`, `chore:`.
6. Never commit secrets, venv, `node_modules`, or `__pycache__`.
7. Put new lessons in `python/`, `js/`, or `qa/` — not the repo root.

## Review checklist

- [ ] Task requirements met
- [ ] Runs with the intended runtime (CPython / Node)
- [ ] No stage lock violated for that track
- [ ] Quiz concepts correct *(only when quizzes are re-enabled)*
