"""
test cases for bubble sort
"""
from unittest import TestCase, main
from bubble_sort import bubble_sort

class BubbleSortTestCases(TestCase):
    """
    Test to ensure our bubble sort works.
    """
    def test_sorts_an_array(self):
        """
        Just one thing: Do you SORT?
        """
        res = bubble_sort([1, 0, 2, 3, 4, 5])
        expected = [0, 1, 2, 3, 4, 5]
        self.assertEqual(res, expected)

if __name__ == "__main__":
    main()
