# Write your unit tests here
from unittest import TestCase, main
from recursion_challenge import roman_num

class RomanNumUnitTest(TestCase):
    def test_converts_correctly(self):
        self.assertEqual(roman_num(1), 'I')
        self.assertEqual(roman_num(3), 'III')
        self.assertEqual(roman_num(4), 'IV')
        self.assertEqual(roman_num(444), 'CDXLIV')
        self.assertEqual(roman_num(500), 'D')
        self.assertEqual(roman_num(944), 'CMXLIV')

if __name__ == "__main__":
    main()