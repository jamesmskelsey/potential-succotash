factorial = function() {
  return x == 0 ? 1 : x * factorial(x-1)
};

palindrome = function(string, reversed="") {
 // look at reversed, if it's no the ssame length as string
  if (string.length > reversed.length) {
    // we haven't reversed it yet. call palindrom again with the next letter appended
    curr = string.length - reversed.length - 1
    reversed += string[curr]
    return palindrome(string, reversed)
  }
  if (string.length == reversed.length) {
    return string == reversed
  }
};

const ROMAN_TO_ARABIC_MAP = [
  ["M", 1000],
  ["CM", 900],
  ["D", 500],
  ["CD", 400],
  ["C", 100],
  ["L", 50],
  ["XL", 40],
  ["X", 10],
  ["IX", 9],
  ["V", 5],
  ["IV", 4],
  ["I", 1],
]

romanNum = function(num, rtaMapItem=0) {
  [letter, value] = ROMAN_TO_ARABIC_MAP[rtaMapItem];
  if (num - value > 0) {
    return letter + romanNum(num - value, rtaMapItem);
  } else if (num - value < 0) {
    return romanNum(num, rtaMapItem + 1);
  } else {
    return letter;
  }
};

romanNum(1000)

// node 99_bottles.js [number of bottles] (defaults to 9)
// I originally solved this with recursion because I thought that's what you wanted 
// us to do.
bottles = (numBottles = 9) => {
  singLine(numBottles);
  console.log(
    `No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, ${numBottles} bottles of beer on the wall.`);
};

singLine = (numBottles) => {
  if (numBottles > 0) {
    console.log(
      `${pluralBottles(numBottles)} of beer on the wall, ${pluralBottles(numBottles)} of beer.
Take one down and pass it around, ${pluralBottles(numBottles - 1).toLowerCase()} of beer on the wall.`);
    singLine(numBottles - 1);
  }
}

pluralBottles = (num) => {
  // Most common occurence
  if (num > 1) {
    return `${num} bottles`;
  }
  // Least common
  if (num === 1) {
    return "1 bottle";
  }
  // Last but not least...
  return "No more bottles";
}

module.exports = {
  palindrome,
  factorial,
  bottles,
  romanNum
}