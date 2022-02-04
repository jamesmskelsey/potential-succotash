creditCheck = function(str) {
  return (
    str.split("").map((el,idx) => {
      return (idx === 0 || idx % 2 === 0) ? (el * 2) : Number(el)
    }).map(el => {
      return el > 9 ? sumDigits(el) : el
    }).reduce((prev, curr) => prev + curr) % 10) == 0 ? "The number is valid!" : "The number is invalid!"
} 

function sumDigits(element)
{
  element = element.toString().split("")
  // ["1", "2"]
  return Number(element[0]) + Number(element[1])
}

module.exports = {
  creditCheck,
  sumDigits
}

// console.log(creditCheckTwo("5541808923795240"))
// console.log(creditCheck("5541808923795240"))