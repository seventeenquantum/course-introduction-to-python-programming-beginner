"""Dice and coin simulator (starter).

pip install numpy matplotlib pytest

Step 0: write down your predictions BEFORE you simulate:
  - each face of a fair die: ?
  - heads on a fair coin: ?
  - the most common sum of two dice, and its probability: ?

Each function below does one job and returns an array. None of them print or plot.
Run `pytest` to check them.
"""

import numpy as np


def roll_dice(n, rng):
    """Roll a fair six-sided die n times and return an array.

    Hint: rng.integers(low, high, size=n). The upper bound is EXCLUSIVE.
    """
    # TODO
    pass


def face_frequencies(rolls):
    """Return the fraction of rolls showing each face, for faces 1 to 6.

    Hint: np.bincount(rolls, minlength=7) counts each whole number; drop index 0.
    """
    # TODO
    pass


def running_heads(flips):
    """Return the fraction of heads after each flip (1 = heads, 0 = tails).

    Hint: np.cumsum(flips) divided by np.arange(1, len(flips) + 1).
    """
    # TODO
    pass


def two_dice_expected():
    """Return the exact probability of each sum from 2 to 12 (11 numbers).

    Hint: np.add.outer(np.arange(1, 7), np.arange(1, 7)) builds a 6x6 grid of sums.
    """
    # TODO
    pass


if __name__ == "__main__":
    rng = np.random.default_rng(42)
    # TODO Step 2: print a table of simulated vs expected face frequencies.
    # TODO Step 3: plot all three charts on one figure with matplotlib and save simulation.png.
    # TODO Step 4: change n to 100, 1,000 and 1,000,000 and write two sentences on what you see.
