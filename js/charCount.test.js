// Can you translate this driver code to unit tests?

var char = require("./charCount");

// console.log(char.charCount("aaabbc")['a'] === 3)
// console.log(char.charCount("aaabbc")['b'] === 2)
// console.log(char.charCount("aaabbc")['c'] === 1)

// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['a'] === 6)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['e'] === 4)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['l'] === 3)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['p'] === 3)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['w'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['d'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['o'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['t'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['y'] === 2)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['k'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['h'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['i'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['c'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['n'] === 1)
// console.log(char.charCount('rplyoacadawpettlleaodeeywapkniha')['r'] === 1)

test("aaabbc returns an object with correct keys/counts", () => {
  let result = char.charCount("aaabbc")
  expect(result).toHaveProperty('a', 3);
  expect(result).toHaveProperty('b', 2);
  expect(result).toHaveProperty('c', 1);
})

test("'' returns an empty object", () => {
  let result = char.charCount("")
  expect(result).toEqual({})
})