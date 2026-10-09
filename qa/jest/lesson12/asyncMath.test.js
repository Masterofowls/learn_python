import doubleAsync from "./asyncMath.js";
import { jest } from "@jest/globals";

describe("asyncMath", () => {
  test("doubleAsync resolves to 8", async () => {
    await expect(doubleAsync(4)).resolves.toBe(8);
  });

  test("mock greets Dan", () => {
    const mockFn = jest.fn((name) => `Hi, ${name}`);

    expect(mockFn("Dan")).toBe("Hi, Dan");
    expect(mockFn).toHaveBeenCalledWith("Dan");
  });
});