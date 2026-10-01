# QA Lesson 1 - Why we test

Manual: Good: UX, exploratory, small checks Bad: slow, inconsistent, large tasks
Automated: Good: Repeatable checks after every change, complex testing, big tasks Bad: Cost time, can go stale, sometimes complex tests need sub-tests

Pyramid: E2E/UI: check is button is clickable Integration: test API, Database Unit: test isolated small function (2+3 ===5)

Unit - pytest/jest
curl/httpie - http checks
Playwright - E2E, browser

## Still manual on purpose
I would still test manually when exploring a new UI flow or judging whether the experience *feels* right.