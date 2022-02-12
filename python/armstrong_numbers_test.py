from armstrong_numbers import find_armstrong_numbers, is_armstrong_number

def test_returns_correct_array_0():
    assert find_armstrong_numbers([0]) == [0]

def test_returns_correct_array_0to8():
    assert find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7]

def test_returns_correct_array_0to999():
    assert find_armstrong_numbers(list(range(0, 999))) == [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

def test_is_armstrong_number_returns_boolean():
    assert type(is_armstrong_number(1)) == bool

def test_is_armstrong_number_1():
    assert is_armstrong_number(1) == True