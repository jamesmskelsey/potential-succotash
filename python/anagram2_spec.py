# Can you translate this driver code to unit tests?

from anagram2 import anagrams_for 
from unittest import TestCase, main

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

# print(anagrams_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
# print(anagrams_for("apple", list_of_words) == [])

class AnagramsTwoUnitTest(TestCase):
    def test_anagrams_for_returns_list(self):
        self.assertEqual(type(anagrams_for("threads", list_of_words)), list)
        self.assertEqual(len(anagrams_for("threads", list_of_words)), 4)

    def test_af_matches_threads_correctly(self):
        self.assertEqual(anagrams_for("threads", list_of_words), ["threads", "trashed", "hardest", "hatreds"])

    def test_af_returns_no_matches_for_apple(self):
        self.assertEqual(anagrams_for("apple", list_of_words), [])

    def test_af_returns_empty_list_given_blanks(self):
        self.assertEqual(anagrams_for("", []), [])

if __name__ == "__main__":
    main()
