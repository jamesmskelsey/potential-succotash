"""
test cases for bubble sort
"""
from bubble_sort import bubble_sort

def test_do_you_even_sort():
    response = bubble_sort([1, 0, 2, 3, 4, 5])
    expected = [0, 1, 2, 3, 4, 5]
    assert response == expected
