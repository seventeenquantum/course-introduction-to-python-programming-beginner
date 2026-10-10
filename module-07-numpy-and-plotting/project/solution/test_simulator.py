import numpy as np

from simulator import face_frequencies, roll_dice, running_heads, two_dice_expected


def test_roll_dice_range_and_size():
    rolls = roll_dice(1000, np.random.default_rng(1))
    assert len(rolls) == 1000
    assert rolls.min() >= 1 and rolls.max() <= 6


def test_same_seed_gives_same_rolls():
    a = roll_dice(50, np.random.default_rng(7))
    b = roll_dice(50, np.random.default_rng(7))
    assert (a == b).all()


def test_frequencies_sum_to_one_and_are_close_to_a_sixth():
    freq = face_frequencies(roll_dice(10_000, np.random.default_rng(42)))
    assert abs(freq.sum() - 1) < 1e-9
    assert np.allclose(freq, 1 / 6, atol=0.02)


def test_running_heads_known_values():
    result = running_heads(np.array([1, 0, 1, 1]))
    assert np.allclose(result, [1.0, 0.5, 2 / 3, 0.75])


def test_two_dice_expected():
    probs = two_dice_expected()
    assert len(probs) == 11
    assert abs(probs.sum() - 1) < 1e-9
    assert abs(probs[5] - 6 / 36) < 1e-9  # a sum of 7 is at index 5
