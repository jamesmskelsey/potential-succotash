# Can you translate this driver code to unit tests?

from anagram2 import anagrams_for

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

def test_anagrams_for_returns_list():
    assert type(anagrams_for("threads", list_of_words)) == list


def test_af_matches_threads_correctly():
    assert anagrams_for("threads", list_of_words) == [
        "threads", "trashed", "hardest", "hatreds"]


def test_af_returns_no_matches_for_apple():
    assert anagrams_for("apple", list_of_words) == []


def test_af_returns_empty_list_given_blanks():
    assert anagrams_for("", []) == []
