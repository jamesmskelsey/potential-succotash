binarySearch = (target, array, startIndex = 0, endIndex = 0) => {
  // This means we just started
  if (endIndex == 0) {
    endIndex = array.length - 1;
  }
  let checkIndex = endIndex - Math.ceil((endIndex - startIndex) / 2);
  // short circuits
  if (
    array[startIndex] != target &&
    array[endIndex] != target &&
    endIndex - startIndex < 2
  ) {
    // we have a super short array and it's not either of them
    return -1;
  } else if (array[startIndex] == target) {
    // it's at the beginning
    return startIndex;
  } else if (array[endIndex] == target) {
    // it's at the end
    return endIndex;
  }
  if (array.length == 1 && array[0] != target) {
    // there's only one item and it's not target
    return -1;
  }
  if (target > array[endIndex]) {
    // it's a sorted array and this is outside our target
    return -1;
  }
  if (array[checkIndex] > target) {
    // middle is greater than the target. binary search the bottom half.
    return binarySearch(
      target,
      array,
      (startIndex = 0),
      (endIndex = checkIndex)
    );
  } else if (array[checkIndex] < target) {
    // middle is less than the target, binary serach the top half
    return this.binarySearch(
      target,
      array,
      (startIndex = checkIndex),
      (endIndex = endIndex)
    );
  } else if (array[checkIndex] == target) {
    // we found it!
    return checkIndex;
  }
  // after all that, we didn't find it
  return -1;
};

module.exports = {
  binarySearch,
};
