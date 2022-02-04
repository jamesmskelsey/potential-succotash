translate = (sentence) => {
  return sentence.split(" ").map(word => translateWord(word)).join(" ");
};

translateWord = (word) => {
  let output = "";
  let punctuation = "";
  const reVowelWords = /^[aeiou]/
  const reTranslateQuWords = /^.*qu/
  const reConsonantWords = /^[^aeiou]*/
  const rePunctuation = /[^\w][A-Za-z]*$/
  // remember if the word is upper case
  let wasUpper = isUpper(word)
  // Set word to lower case
  word = word.toLowerCase()
  // set aside punctuation, remove it from the string
  if (rePunctuation.test(word)) {
    punctuation = word.match(rePunctuation)[0]
  }
  word = word.replace(rePunctuation, "")
  // translate the words now...
  if (reVowelWords.test(word)) {
    output = `${word}ay`
  } else if (reTranslateQuWords.test(word)) {
    output = rearrange(word, reTranslateQuWords)
  } else if (reConsonantWords.test(word)) {
    output = rearrange(word, reConsonantWords)
  }
  // re apply any punctuation from earlier
  output += punctuation;
  // return a correctly cased word
  return wasUpper ? capitalize(output) : output;
}

rearrange = (word, re) => {
  let match = word.match(re)
  return word.slice(match[0].length) + match[0] + "ay"
}

isUpper = (word) => {
  let firstCharCode = word.charCodeAt(0);
  return firstCharCode > 65 && firstCharCode < 90;
}

capitalize = (word) => {
  return word[0].toUpperCase() + word.slice(1)
}

module.exports = {
  translate
}

console.log(translate("Completed the challenge!"))