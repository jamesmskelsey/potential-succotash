// exports.

function isSearchValue(element, val) {
  return element === val;
}

exports.linearSearch = function(valueToFind, arrayToSearchThrough) {
  // account for undefined not in array
    let output = undefined;
    for (let i = 0; i < arrayToSearchThrough.length; i++){
        if (isSearchValue(arrayToSearchThrough[i], valueToFind)) {
          // i'm going to do something
          output = i;
          break;
        }
    }
  // move through the array
  // compare value to index position
  return output;
};



// console.log(linearSearch(4, [1,2,3]))
// console.log(linearSearch("A", ["C", "A", "T"]))
// console.log(linearSearch("A", "CAT"))

exports.linearSearchGlobal = function(valueToFind, arrayToSearchThrough) {
  let output = [];
  for (let i = 0; i < arrayToSearchThrough.length; i++){
      if (isSearchValue(arrayToSearchThrough[i], valueToFind)){
          output.push(i);
      }
  }
  return output;
  // variable for an array for index position
  //if statement 
}

// console.log(linearSearchGlobal("S", "BANANAS"));