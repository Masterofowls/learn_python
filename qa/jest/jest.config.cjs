/** Shared Jest config (CJS so Jest can load it while package.json is "type": "module") */
module.exports = {
  testEnvironment: "node",
  testMatch: ["**/lesson*/**/*.test.js"],
  clearMocks: true,
  transform: {},
};
