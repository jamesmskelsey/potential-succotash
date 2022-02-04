exports.isCharacterMatch = function(string1, string2) {
  return mangle(string1) === mangle(string2)
};

function mangle(str) {
  return str.toLowerCase().split('').sort().join('').trim();
}