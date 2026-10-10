import pytest

from converter import convert


def test_length():
    assert round(convert(10, "km", "miles"), 2) == 6.21


def test_mass():
    assert round(convert(1, "kg", "pounds"), 2) == 2.2


def test_temperature():
    assert convert(100, "c", "f") == 212.0
    assert convert(32, "f", "c") == 0.0


def test_incompatible_units():
    with pytest.raises(ValueError):
        convert(5, "km", "kg")
