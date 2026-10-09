import double from "../lesson10/math";

describe("double", () => {
    test("doubles positives", () => {
      expect(double(3)).toBe(6);
    });
    test("result is a number", () => {
      expect(typeof double(1)).toBe("number");
    });
    test("negative result", () => {
        expect(double(2)).not.toBe(3);
      });
  });