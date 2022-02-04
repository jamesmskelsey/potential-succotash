// Rewrite this in Unit Test

var {translate: pig} = require("./pigLatin");

// write a test asserting that capitalized words are still capitalized
// (but with a different initial capital letter, of course) retain the
// punctuation from the original phrase

test("translate a word beginning with a vowel", () => {
  expect(pig("kevin's")).toBe("evinkay's")
});

test("translate a word beginning with a vowel", () => {
  expect(pig("apple")).toBe("appleay")
});

test("translates a word beginning with a consonant:", () => {
  expect(pig("banana")).toBe("ananabay")
});

test("translates a word beginning with two consonants", () => {
  expect(pig("cherry")).toBe("errychay")
});

test("translates two words", () => {
  expect(pig("eat pie")).toBe("eatay iepay")
});

test("translates a word beginning with three consonants", () => {
  expect(pig("three")).toBe("eethray")
});

test("counts 'sch' as a single phoneme", () => {
  expect(pig("school")).toBe("oolschay")
});

test("counts 'qu' as a single phoneme", () => {
  expect(pig("quiet")).toBe("ietquay")
});

test("counts 'qu' as a consonant even when it's preceded by a consonant", () => {
  expect(pig("square")).toBe("aresquay")
});

test("translates many words", () => {
  expect(pig("the quick brown fox")).toBe("ethay ickquay ownbray oxfay")
});

test("translates words and retains punctuation", () => {
  expect(pig("the quick, brown, fox")).toBe("ethay ickquay, ownbray, oxfay")
});

test("translates words and retains punctuation and capitalization", () => {
  expect(pig("The quick, brown, fox.")).toBe("Ethay ickquay, ownbray, oxfay.")
});