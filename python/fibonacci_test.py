from fibonacci import fibonacci


def test_returns_correct_20th():
    assert fibonacci(20) == 6765


def test_handles_negative_numbers():
    assert fibonacci(-1) == 0


def test_handles_zero():
    assert fibonacci(0) == 0
