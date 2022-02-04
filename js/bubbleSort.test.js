const { bubbleSort } = require('./bubbleSort.js')

test('do you even sort, bro?', () => {
  let res = bubbleSort([1, 0, 2, 3, 4, 5])
  expected = [0, 1, 2, 3, 4, 5]
  expect(res).toEqual(expected)
})