// Rewrite this in Unit Test

var {caesarCipher: cs} = require("./caesarCipher");

// console.log(cs.caesarCipher("Boy! What a string!", -5) === "Wjt! Rcvo v nomdib!")
// console.log(cs.caesarCipher("Hello zach168! Yes here.", 5) === "Mjqqt efhm168! Djx mjwj.")
// console.log(cs.caesarCipher("Hello Zach168! Yes here.", -5) === "Czggj Uvxc168! Tzn czmz.")

test("returns correct values", () => {
  expect(cs("Boy! What a string!", -5)).toBe("Wjt! Rcvo v nomdib!")
  expect(cs("Hello zach168! Yes here.", 5)).toBe("Mjqqt efhm168! Djx mjwj.")
  expect(cs("Hello Zach168! Yes here.", -5)).toBe("Czggj Uvxc168! Tzn czmz.")
})