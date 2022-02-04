// Program returns the value of the nth value of the fibonacci sequence
// User may provide value based on command line input.
//let n = process.argv[2] ? process.argv[2] : 5;

fibonacci = (num) => {
  // using Binet's Formula to find the nth value of the sequence
  // I'm not a math wiz, but it's easy to find this info on wikipedia

  // (1 + sqrt(5) / 2) power of n
  let onePlusSqrt5 = (1 + Math.sqrt(5)) / 2;
  let first = Math.pow(onePlusSqrt5, num);
  // minus

  // (1 - sqrt(5) / 2) power of n
  let oneMinusSqrt5 = (1 - Math.sqrt(5)) / 2;
  let second = Math.pow(oneMinusSqrt5, num);
  // and that divided by sqrt(5)
  return Math.trunc((first - second) / Math.sqrt(5));
};

module.exports = { fibonacci };
