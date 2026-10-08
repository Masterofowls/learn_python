# QA track — how to learn

Same loop as other tracks. See [../HOW_TO_LEARN.md](../HOW_TO_LEARN.md).

**Path:** Stage 1 pytest → Stage 2 Jest + SuperTest → Stage 3 Playwright.  
**Quizzes skipped** for now.

## Run examples

```bash
# Stage 1 — each pytest lesson has its own folder
cd qa/pytest/lesson1 && pytest -v

# Stage 2 — ONE shared Jest install at qa/jest/
cd qa/jest
npm install                 # once
npm run test:lesson10       # or: npx jest lesson10
# SuperTest/Express also install into qa/jest/ (not per lesson)

# Stage 3
cd qa/playwright/lesson17 && npx playwright test
```

## Progress

- [PROGRESS.md](PROGRESS.md)
- [CURRICULUM.md](CURRICULUM.md)
