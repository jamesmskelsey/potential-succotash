exports.factorial = function(num) {
  return num === 0 ? 1 : zeroFree(num);
};

function zeroFree(num) {
  let output = 1;
  for (let i = 1; i <= num; i++) {
    output *= i;
  }
  return output;
}
