const {sumPairs} = require("./sumPairs");

// Don't forget to add your tests :)

// return a array of arrays
// return a string that says 'unable to find pairs'

test('empty arrays returns no pairs', () => {
  expect(sumPairs([], 0)).toBe('unable to find pairs')
})

test('[1,2,3,4,5], 9 returns [[4,5]]', () => {
  expect(sumPairs([1,2,3,4,5], 9)).toEqual([[4,5]])
})

test('([1,2,3,4,5], 7) returns [[4,5]]', () => {
  expect(sumPairs([1,2,3,4,5], 7)).toEqual([[2,5],[3,4]])
})

test('([1,2,3,4,5], 7) returns [[4,5]]', () => {
  expect(sumPairs([3, 1, 5, 8, 2], 27)).toBe('unable to find pairs')
})