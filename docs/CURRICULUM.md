# Python Curriculum

Personal path from zero to web frameworks. Do **not** skip stages.

## Stages overview

| Stage | Name | Lessons | Status |
|-------|------|---------|--------|
| 1 | Core language + first tools | L1–L13 | Complete |
| 2 | Master data types + structure | L14–L26 | Current |
| 3 | Data & testing | L27–L29 | Locked until Stage 2 done |
| 4 | Web frameworks | L30+ | Locked until Stage 3 done |

---

## Stage 1 — Core (done)

| Lesson | Topic | File |
|--------|--------|------|
| 1 | print, variables, types | `lesson1.py` |
| 2 | input, operators, f-strings | `lesson2.py` |
| 3 | if / elif / else | `lesson3.py` |
| 4 | for / while loops | `lesson4.py` |
| 5 | Lists (intro) | `lesson5.py` |
| 6 | Dicts + tuples (intro) | `lesson6.py` |
| 7 | Functions | `lesson7.py` |
| 8 | Files | `lesson8.py` |
| 9 | Errors / try-except | `lesson9.py` |
| 10 | Modules & `__main__` | `lesson10.py`, `helpers.py` |
| 11 | Classes (intro) | `lesson11.py` |
| 12 | `time` + `requests` | `lesson12.py` |
| 13 | `asyncio` basics | `lesson13.py` |

---

## Stage 2 — Depth (now)

Order is fixed. Finish each lesson before the next.

| Lesson | Topic | File |
|--------|--------|------|
| 14 | Sets | `lesson14.py` |
| 15 | Tuples (master) | `lesson15.py` |
| 16 | Lists (master) | `lesson16.py` |
| 17 | Dicts (master) | `lesson17.py` |
| 18 | String methods | `lesson18.py` |
| 19 | Comprehensions | `lesson19.py` |
| 20 | `*args` / `**kwargs` | `lesson20.py` |
| 21 | OOP: inheritance, `@property`, `__str__` | `lesson21.py` |
| 22 | Virtualenv + pip discipline | `lesson22` notes / practice |
| 23 | `json` stdlib | `lesson23.py` |
| 24 | Type hints | `lesson24.py` |
| 25 | `pathlib` | `lesson25.py` |
| 26 | Debugging / logging | `lesson26.py` |

### Stage 2 topic notes

- **14 Sets** — uniqueness, `| & - ^`, membership, hashable items
- **15 Tuples** — immutability, unpacking, multi-return, when to use vs list
- **16 Lists** — `extend`, `insert`, `pop`, `remove`, `sort`/`sorted`, slicing, copy
- **17 Dicts** — `keys`/`values`/`pop`/`update`/`setdefault`, nesting
- **18 Strings** — `split`, `join`, `replace`, `strip`, `find`, `startswith`
- **19 Comprehensions** — list/dict/set comps, basic filtering
- **20 args/kwargs** — flexible function signatures
- **21 OOP** — inheritance, `@property`, `__str__` / `__repr__` intro
- **22 venv/pip** — one interpreter, `requirements.txt`, no mixed 3.12/3.14 installs
- **23 JSON** — `json.load` / `dump` / `loads` / `dumps`
- **24 Type hints** — `def f(x: int) -> str`, `list[int]`, optional
- **25 Pathlib** — `Path`, join, read/write text, exists
- **26 Logging** — `logging` module vs print; levels; basic debug workflow

---

## Stage 3 — Data & testing (after Stage 2)

| Lesson | Topic | Why this order |
|--------|--------|----------------|
| 27 | NumPy | Arrays before tables |
| 28 | pandas | Tables / CSV / analysis |
| 29 | pytest | Test real code you write |

Do **not** start Stage 3 until L26 is reviewed complete.

---

## Stage 4 — Web (after Stage 3)

| Lesson | Topic | Notes |
|--------|--------|--------|
| 30+ | FastAPI | First API framework (modern, typed) |
| later | Django | Full stack / batteries-included |

Do **not** start Stage 4 until NumPy, pandas, and pytest lessons are complete.

---

## Rules

1. One lesson at a time: Theory → Quiz → `lessonN.py` → tutor review.
2. No skipping stages.
3. Prefer the same Python interpreter for run and `pip` (see Lesson 22).
4. Keep lesson files in the repo root as `lessonN.py` unless a lesson says otherwise.
