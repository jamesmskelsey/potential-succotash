// How can you make this more scalable and reusable later?
// I'll write the code here to pass your tests
findArmstrongNumbers = (input) => {
  let output = []
  for (let i = 0; i < input.length; i++) {
    if (isArmstrongNumber(input[i])) {
      output.push(input[i])
    }
  }
  return output;
};

isArmstrongNumber = (n) => {
  // exponent 3
  let exponent = n.toString().length;
  let sum = n.toString().split('').reduce((prev, curr) => {
    prev += Math.pow(Number(curr), exponent) 
    return prev
  }, 0)
  return sum == n;
}

module.exports = {
  findArmstrongNumbers,
  isArmstrongNumber
}
