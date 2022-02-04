// Can you translate this driver code to unit tests?

var ana = require("./anagram2"),
listOfWords = ["threads", "trashed", "hardest", "hatreds", "hounds"];

// console.log(ana.anagramsFor("threads", listOfWords).length == 4);
// console.log(ana.anagramsFor("threads", listOfWords)[0] == "threads");
// console.log(ana.anagramsFor("threads", listOfWords)[1] == "trashed");
// console.log(ana.anagramsFor("threads", listOfWords)[2] == "hardest");
// console.log(ana.anagramsFor("threads", listOfWords)[3] == "hatreds");

// console.log(ana.anagramsFor("apple", listOfWords).length == 0);

test("should return an array", () => {
  expect(ana.anagramsFor("threads", listOfWords)).toBeInstanceOf(Array)
})

test("threads should return an array of length 4", () => {
  expect(ana.anagramsFor("threads", listOfWords)).toHaveLength(4)
})

test("threads should have matched threads, trashed, hardest, hatreds", () => {
  expect(ana.anagramsFor("threads", listOfWords)).toEqual(expect.arrayContaining(["threads", "trashed", "hardest", "hatreds"]))
})

test("apple should have no matches", () => {
  expect(ana.anagramsFor("apple", listOfWords)).toHaveLength(0)
})