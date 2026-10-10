"""Exercise 3: Random walk plot.

Simulate 5 random walks of 1,000 steps each. Each step is +1 or -1 with equal
probability. Plot all five on one chart, and print each walk's final position
and its furthest distance from zero.

Expected: final positions are typically a few tens of steps from zero
(the spread after n steps is about the square root of n, about 32 here).

Hints: rng.choice([-1, 1], size=(5, 1000)) makes a 5 by 1,000 grid of steps;
np.cumsum(steps, axis=1) adds them up along each row.
"""

import matplotlib.pyplot as plt
import numpy as np

# TODO
