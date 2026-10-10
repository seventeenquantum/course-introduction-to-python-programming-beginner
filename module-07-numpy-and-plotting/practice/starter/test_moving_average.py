import numpy as np
import pytest

from exercise_02_moving_average import moving_average


def test_known_values():
    assert np.allclose(moving_average([1, 2, 3, 4, 5, 6], 3), [2, 3, 4, 5])


def test_window_of_one_returns_same_values():
    assert np.allclose(moving_average([4, 8, 9], 1), [4, 8, 9])


def test_bad_window_raises():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], 0)
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], 4)
