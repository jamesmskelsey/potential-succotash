// Can you translate this driver code to unit tests?

var {creditCheck, sumDigits} = require("./creditCheck");

test('returns a string', () => {
  expect(typeof creditCheck("5541808923795240")).toBe('string')
})

test('valid numbers return "The number is valid!', () => {
  expect(creditCheck("5541808923795240")).toBe("The number is valid!")
  expect(creditCheck("4024007136512380")).toBe("The number is valid!")
  expect(creditCheck("6011797668867828")).toBe("The number is valid!")
})

test('invalid numbers return "The number is invalid!', () => {
  expect(creditCheck("5541801923795240")).toBe("The number is invalid!")
  expect(creditCheck("4024007106512380")).toBe("The number is invalid!")
  expect(creditCheck("6011797668868728")).toBe("The number is invalid!")
})

test('sum digits returns 4 for 13', () => {
  expect(sumDigits(13)).toBe(4)
})
