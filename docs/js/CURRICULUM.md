# JavaScript Curriculum

Same tutoring style as Python: Theory → Quiz → `js/lessonN.js` → review.  
Do **not** skip stages. Tracks are independent — you can study JS and Python in parallel.

## Stages overview

| Stage | Name | Lessons | Status |
|-------|------|---------|--------|
| 1 | Core language + first tools | L1–L13 | Not started |
| 2 | Master data types + structure | L14–L26 | Locked until Stage 1 done |
| 3 | Tooling & testing | L27–L29 | Locked until Stage 2 done |
| 4 | Web frameworks | L30+ | Locked until Stage 3 done |

---

## Stage 1 — Core

| Lesson | Topic | File |
|--------|--------|------|
| 1 | `console.log`, variables (`let`/`const`), types | `js/lesson1.js` |
| 2 | operators, template literals, `prompt` / input patterns | `js/lesson2.js` |
| 3 | if / else / else if | `js/lesson3.js` |
| 4 | for / while loops | `js/lesson4.js` |
| 5 | Arrays (intro) | `js/lesson5.js` |
| 6 | Objects (intro) | `js/lesson6.js` |
| 7 | Functions | `js/lesson7.js` |
| 8 | Files with `fs` (Node) | `js/lesson8.js` |
| 9 | Errors / try-catch | `js/lesson9.js` |
| 10 | Modules (`import`/`export`) | `js/lesson10.js`, helpers |
| 11 | Classes (intro) | `js/lesson11.js` |
| 12 | `Date` / timers + `fetch` | `js/lesson12.js` |
| 13 | `async` / `await` + `Promise` | `js/lesson13.js` |

---

## Stage 2 — Depth

| Lesson | Topic | File |
|--------|--------|------|
| 14 | `Set` | `js/lesson14.js` |
| 15 | Tuples-like patterns / destructuring pairs | `js/lesson15.js` |
| 16 | Arrays (master) | `js/lesson16.js` |
| 17 | Objects (master) | `js/lesson17.js` |
| 18 | String methods | `js/lesson18.js` |
| 19 | Array methods / map-filter (comprehension analogs) | `js/lesson19.js` |
| 20 | rest / spread (`...args`) | `js/lesson20.js` |
| 21 | OOP: extends, getters, `toString` | `js/lesson21.js` |
| 22 | npm + package discipline | practice |
| 23 | `JSON` | `js/lesson23.js` |
| 24 | JSDoc / basic TypeScript intro | `js/lesson24.js` or `.ts` |
| 25 | `path` / `node:fs` paths | `js/lesson25.js` |
| 26 | Debugging / `console` levels | `js/lesson26.js` |

---

## Stage 3 — Tooling & testing (after Stage 2)

| Lesson | Topic | Python analog |
|--------|--------|----------------|
| 27 | Modern JS data patterns (typed arrays / utilities) | NumPy-ish mindset |
| 28 | Working with tabular CSV/JSON data in JS | pandas-ish |
| 29 | Vitest (or Jest) | pytest |

## Stage 4 — Web (after Stage 3)

| Lesson | Topic | Python analog |
|--------|--------|----------------|
| 30+ | Express or Fastify | FastAPI |
| later | Next.js (or NestJS) | Django-scale apps |

## Rules

1. Theory → Quiz → `js/lessonN.js` → tutor review.
2. No skipping stages within the JS track.
3. Prefer **Node.js** LTS for running lessons: `node js/lessonN.js`.
4. After L22, use a project `package.json` and local `node_modules` (never mix global installs casually).
