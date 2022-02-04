import unittest

from armstrong_numbers import find_armstrong_numbers, is_armstrong_number

class ArmstrongNumbersTestCase(unittest.TestCase):
    """Tests for armstrong_numbers.py"""

    def test_returns_the_correct_array(self):
        self.assertEqual(find_armstrong_numbers([0]), [0])
        self.assertEqual(find_armstrong_numbers(list(range(0, 8))), [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(find_armstrong_numbers(list(range(0, 100))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(find_armstrong_numbers(list(range(0, 999))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

    def test_is_armstrong_number_returns_boolean(self):
        self.assertEqual(type(is_armstrong_number(1)), bool)


if __name__ == '__main__':
    unittest.main()