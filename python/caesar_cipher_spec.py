# Rewrite this in Unit Test

from caesar_cipher import caesar_cipher
from unittest import TestCase, main
# print(caesar_cipher("Boy! What a string!", -5) == "Wjt! Rcvo v nomdib!")
# print(caesar_cipher("Hello zach168! Yes here.", 5) == "Mjqqt efhm168! Djx mjwj.")
# print(caesar_cipher("Hello Zach168! Yes here.", -5) == "Czggj Uvxc168! Tzn czmz.")

class CaesarCipherUnitTest(TestCase):
    """ tests for the amazing caeser cipher """
    def test_returns_correctly_shifted_string(self):
        self.assertEqual(caesar_cipher("Boy! What a string!", -5), "Wjt! Rcvo v nomdib!")
        self.assertEqual(caesar_cipher("Hello zach168! Yes here.", 5), "Mjqqt efhm168! Djx mjwj.")
        self.assertEqual(caesar_cipher("Hello Zach168! Yes here.", -5), "Czggj Uvxc168! Tzn czmz.")

if __name__ == "__main__":
    main()
