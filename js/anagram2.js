const cm = require('./characterMatch');

exports.anagramsFor = function(word, listOfWords) {
  return listOfWords.filter(el => cm.isCharacterMatch(el, word))
};
