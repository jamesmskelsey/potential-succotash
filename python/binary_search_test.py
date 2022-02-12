# Write your unit tests here

from binary_search import binary_search

test_array = [1, 2, 3, 4, 5]
super_big_array = [1, 5, 7, 2, 3, 8, 4, 9]


def test_search_can_find_an_item_in_any_index():
    assert binary_search(1, test_array) == 0
    assert binary_search(2, test_array) == 1
    assert binary_search(3, test_array) == 2
    assert binary_search(4, test_array) == 3
    assert binary_search(5, test_array) == 4


def test_search_find_an_item():
    assert binary_search(7, super_big_array) == 2
    assert binary_search(9, super_big_array) == 7


def test_search_can_identify_no_item():
    assert binary_search(6, super_big_array) == -1
