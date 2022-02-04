# Can you translate this driver code to unit tests?

import unittest
from credit_check import credit_check, sum_digits
from unittest import TestCase, main
# print(credit_check('5541808923795240') == "The number is valid!")
# print(credit_check("4024007136512380") == "The number is valid!")
# print(credit_check("6011797668867828") == "The number is valid!")

# print(credit_check("5541801923795240") == "The number is invalid!")
# print(credit_check("4024007106512380") == "The number is invalid!")
# print(credit_check("6011797668868728") == "The number is invalid!")

class CreditCheckTestCase(TestCase):
    """ tests for credit check"""
    def test_returns_a_string(self):
        self.assertEqual(type(credit_check("4024007136512380")), str)
    
    def test_returns_valid_for_valid_numbers(self):
        self.assertEqual(credit_check("5541808923795240"), "The number is valid!")
        self.assertEqual(credit_check("4024007136512380"), "The number is valid!")
        self.assertEqual(credit_check("6011797668867828"), "The number is valid!")

    def test_returns_invalid_for_invalid_numbers(self):
        self.assertEqual(credit_check("5541801923795240"), "The number is invalid!")
        self.assertEqual(credit_check("4024007106512380"), "The number is invalid!")
        self.assertEqual(credit_check("6011797668868728"), "The number is invalid!")

    def test_returns_4_for_13(self):
        self.assertEqual(sum_digits(13), 4)

if __name__ == '__main__':
    main()