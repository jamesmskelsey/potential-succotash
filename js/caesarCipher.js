caesarCipher = function(input, shift) {
  // split str, iterate array, convert as necessary
  return input.split('').map((l) => {
    return moveLetter(l, shift);
  }).join('')
};

moveLetter = (l, shift) => {
  //a = 97
  //z = 122
  //A = 65
  //Z = 90
  let code = l.charCodeAt(0);
  if (code >= 97 && code <= 122) {
    // move letter
    code += shift;
    if (code > 122) {
      code -= 26
    }
    if (code < 97) {
      code += 26
    }
  } else if (code >= 65 && code <= 90) {
    // move letter
    code += shift;
    if (code > 90) {
      code -= 26
    }
    if (code < 65) {
      code += 26
    }
  } else {
    return l;
  }
  return String.fromCharCode(code)
}

module.exports = {
  caesarCipher
}
