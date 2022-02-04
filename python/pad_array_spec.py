# Write unit tests!
from pad_array import pad
from unittest import TestCase, main

class PadArrayUnitTest(TestCase):

    def test_returns_list(self):
        self.assertEqual(type(pad([1,2,3],5)), list)

    def test_returns_list_if_already_min_size(self):
        self.assertEqual(pad([1,2,3], 2), [1,2,3])

    def test_returns_list_correct_length_and_contents(self):
        result = pad([1,2,3], 5)
        self.assertEqual(result, [1,2,3,None, None])
        self.assertEqual(len(result), 5)

    def test_returns_array_with_value_added(self):
        result = pad(["donuts", "are"], 3, "yummy")
        self.assertEqual(result, ["donuts", "are", "yummy"])
        self.assertEqual(len(result), 3)

if __name__ == "__main__":
    main()