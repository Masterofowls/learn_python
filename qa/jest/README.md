# QA Stage 2 — Jest (+ SuperTest later)

**One shared install** for all lessons. Do **not** run `npm install` inside each `lessonN/` folder.

**Module system:** ESM (`"type": "module"`) — use `export` / `import`, not `module.exports` / `require`.

## Setup (once)

```bash
cd qa/jest
npm install
```

## Layout

```
qa/jest/
  package.json
  jest.config.cjs
  node_modules/
  lesson10/
    math.js
    math.test.js
```

## ESM style (Lesson 10+)

```js
// math.js
export default function double(n) {
  return n * 2;
}

// math.test.js
import double from "./math.js";
```

Named exports also work: `export function double` → `import { double } from "./math.js"`.

### `jest.fn` / mocks under ESM

`jest` is **not** a free global with `--experimental-vm-modules`. Import it:

```js
import { jest } from "@jest/globals";

const mockFn = jest.fn();
```

Same for `expect` if you ever see `expect is not defined` (usually `expect` still works; `jest` is the common missing one).

## Run tests

```bash
cd qa/jest
npm run test:lesson10
npm test
```

Scripts use `node --experimental-vm-modules` so Jest can run native ESM.

## SuperTest (from Lesson 14)

```bash
cd qa/jest
npm install --save-dev supertest
npm install express
```
