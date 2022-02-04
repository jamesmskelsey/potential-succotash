// Write your unit tests here
const { romanNum } = require("./recursionChallenge")

test("should convert to the correct values", () => {
  expect(romanNum(1)).toBe('I')
  expect(romanNum(3)).toBe('III')
  expect(romanNum(4)).toBe('IV')
  expect(romanNum(444)).toBe('CDXLIV')
  expect(romanNum(500)).toBe('D')
  expect(romanNum(944)).toBe('CMXLIV')
})