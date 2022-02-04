const pad = (array, minSize, value=null) => {
  return [...array, ...Array(minSize - array.length < 0 ? 0 : minSize - array.length).fill(value)]
}

module.exports = {
  pad
}

console.log(pad([], 1))