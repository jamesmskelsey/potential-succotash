ROMAN_TO_ARABIC_MAP = {
  "M": 1000,
  "D": 500,
  "C": 100,
  "L": 50,
  "X": 10,
  "V": 5,
  "I": 1,
}

const toRoman = function(num) {
  let output = "";
  
  // divide input by 1000, no rounding
  for (let letter in ROMAN_TO_ARABIC_MAP) {
    let arabic = ROMAN_TO_ARABIC_MAP[letter]
    times = Math.trunc(num / arabic);
    // append m as many units as there are
    for (let i = 0; i < times; i++) {
      output += letter
      num -= arabic;
    }
      
  }
  output = condenseMultiples(output);
  return output;
};

condenseMultiples = function(roman) {
  roman = roman.replace(/VIIII/g, "IX");
  roman = roman.replace(/IIII/g, "IV");
  roman = roman.replace(/DCCCC/g, "CM");
  roman = roman.replace(/XXXX/g, "XL");
  roman = roman.replace(/MMMM/g, "ĪV") // I couldn't find the ascii for a 'V' with macron.
  
  return roman;
}

module.exports = { toRoman }




