exports.charCount = function(str) {
  const output = {};
  // Split the string, do something for each item.
  str.split('').forEach(key => {
    // If the key is undefined, assign an initial count of one, otherwise add 1 to it
    output[key] = output[key] != undefined ? output[key] + 1 : 1
  })
  // ?? magic
  return output;
};
