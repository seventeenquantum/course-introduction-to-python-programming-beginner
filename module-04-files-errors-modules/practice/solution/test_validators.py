import pytest

from validators import is_valid_email, is_whole_number_in_range


def test_number_in_range():
    assert is_whole_number_in_range("5", 1, 10) is True
    assert is_whole_number_in_range("11", 1, 10) is False
    assert is_whole_number_in_range("abc", 1, 10) is False
    assert is_whole_number_in_range("-3", -5, 5) is True


def test_bad_range_raises():
    with pytest.raises(ValueError):
        is_whole_number_in_range("5", 10, 1)


def test_email():
    assert is_valid_email("ada@example.com") is True
    assert is_valid_email("ada@example") is False
    assert is_valid_email("@example.com") is False
    assert is_valid_email("a b@example.com") is False
