bubbleSort = (arr) => {
  let prev = 0;
  let curr = 1;
  let swapMade = false;
  // Loop over the array while it's not sorted
  while (!swapMade) {
    // if no swap was made, we'll keep this as false.
    swapMade = swapMade ? false : true;
    if (arr[prev] > arr[curr]) {
      // swap the values if prev > curr
      [arr[prev], arr[curr]] = [arr[curr], arr[prev]];
      swapMade = true
    } else {
      // otherwise increment our indices
      prev++;
      curr++;
    }
    // if we're at the end of the array, reset
    if (curr > arr.length) {
      prev = 0;
      curr = 1;
    }
  }
  return arr
}

module.exports = {
  bubbleSort
}