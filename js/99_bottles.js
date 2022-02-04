// Run this file with node
// node 99_bottles.js [number of bottles] (defaults to 9)

function bottleSong(numBottles = 9) {
  singLine(numBottles);
  console.log(
    `No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, ${numBottles} bottles of beer on the wall.`
  );
}

function singLine(numBottles) {
  if (numBottles > 0) {
    console.log(
      `${pluralBottles(numBottles)} of beer on the wall, ${pluralBottles(
        numBottles
      )} of beer.
Take one down and pass it around, ${pluralBottles(
        numBottles - 1
      ).toLowerCase()} of beer on the wall.`
    );
    singLine(numBottles - 1);
  }
}

function pluralBottles(num) {
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

bottleSong(process.argv[2]);
