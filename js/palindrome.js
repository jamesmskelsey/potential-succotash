
exports.palindrome = function(word) {
  const re = /[^A-Za-z0-9]/g
  word = word.toString().toLowerCase().replace(re, "")
  return word.split('').reverse().join('') === word
};

console.log(exports.palindrome("race car"))
