// Write unit tests!
const { pad } = require('./padArray.js')

test('returns an array', () => {
  expect(pad([1,2,3], 0)).toEqual([1,2,3])
})

test('adds null to the array as appropriate', () => {
  expect(pad([1,2,3,], 5)).toEqual([1,2,3,null,null])
  expect(pad([1,2,3,], 5).length).toBe(5)
})

test('does not add if minsize is less than the length', () => {
  expect(pad([1,2,3], 1).length).toBe(3)
  expect(pad([1,2,3], 1)).toEqual([1,2,3])
})

test('adds the correct value if passed', () => {
  expect(pad([1,2,3], 5, "donuts")).toEqual([1,2,3,"donuts","donuts"])
})