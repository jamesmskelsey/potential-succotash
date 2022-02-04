// Can you translate this driver code to unit tests?

var { findArmstrongNumbers, isArmstrongNumber } = require("./armstrongNumbers")
var shallowEqualArrays = require('shallow-equal/arrays')

function createArrayOfNum(maxValue) {
  return Array.apply(null, {length: maxValue}).map(Number.call, Number)
}

// console.log(shallowEqualArrays(arm.findArmstrongNumbers([0]),[0]));
// console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(8)), [0, 1, 2, 3, 4, 5, 6, 7]));
// console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(99)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]));
// console.log(shallowEqualArrays(arm.findArmstrongNumbers(createArrayOfNum(999)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]));

// Write our tests here

//test that function findArmstrongNumbers returns array
test('should return an array', () => {
  expect(findArmstrongNumbers([0])).toEqual([0])
})

//test that function isArmstrongNumber returns boolean value
test('should return a boolean value', () => {
  expect(isArmstrongNumber(8)).toBeTruthy()
})

test('153 should return true', () => {
  expect(isArmstrongNumber(153)).toBeTruthy()
})

test('100 should return false', () => {
  expect(isArmstrongNumber(100)).toBeFalsy()
})

//test return of proper values
test('armstrongNumbers(5) returns 5', () => {
  expect(findArmstrongNumbers([5])).toEqual([5])
})

test('armstrongNumbers(array of numbers 0 to 8) returns (numbers 0 to 7)', () => {
  expect(findArmstrongNumbers(createArrayOfNum(8))).toEqual([0, 1, 2, 3, 4, 5, 6, 7])
})

test('armstrongNumbers(array of numbers 0 to 99) returns (numbers 0 to 9)', () => {
  expect(findArmstrongNumbers(createArrayOfNum(99))).toEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
})

test('armstrongNumbers(array of numbers 0 to 999) returns [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]', () => {
  expect(findArmstrongNumbers(createArrayOfNum(999))).toEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
})