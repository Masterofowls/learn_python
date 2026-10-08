import double from "./math.js";

test("double of 4 is 8", () => {
  expect(double(4)).toBe(8);
});

test("double of 0 is 0", () => {
  expect(double(0)).toBe(0);
});
