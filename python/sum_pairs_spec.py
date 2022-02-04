from unittest import TestCase, main
import unittest
from sum_pairs import sum_pairs

# write your specs here!
class SumPairsTestCase(TestCase):
    """ tests for sum pairs"""

    def test_returns_a_string_if_passed_nothing(self):
        """should return a string if passed nothing"""
        self.assertEqual(sum_pairs([],0), 'unable to find pairs')

    def test_returns_an_array(self):
        """should return an array"""
        self.assertEqual(type(sum_pairs([1,2], 3)), list)

    def test_returns_a_pair_of_values(self):
        """should return [[1,2]]"""
        self.assertEqual(sum_pairs([1,2], 3), [[1,2]])
