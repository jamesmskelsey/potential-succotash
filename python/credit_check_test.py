""" tests for credit check"""
from credit_check import credit_check, sum_digits


def test_returns_a_string():
    assert type(credit_check("4024007136512380")) == str


def test_returns_valid_for_valid_numbers():
    assert credit_check("5541808923795240") == "The number is valid!"
    assert credit_check("4024007136512380") == "The number is valid!"
    assert credit_check("6011797668867828") == "The number is valid!"


def test_returns_invalid_for_invalid_numbers():
    assert credit_check("5541801923795240") == "The number is invalid!"
    assert credit_check("4024007106512380") == "The number is invalid!"
    assert credit_check("6011797668868728") == "The number is invalid!"


def test_returns_4_for_13():
    assert sum_digits(13) == 4
