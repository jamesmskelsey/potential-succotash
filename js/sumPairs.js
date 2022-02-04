exports.sumPairs = function(arr, num) {
  let output = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i; j < arr.length; j++) {
      if (j === i) {
        continue;
      }
      if (arr[i] + arr[j] == num) {
        output.push([arr[i], arr[j]])
      } 
    }
  }

  return output.length === 0 ? 'unable to find pairs' : output;
};
