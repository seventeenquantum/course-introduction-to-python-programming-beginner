"""Exercise 2: Moving average.

Write moving_average(values, window) returning the average of every run of
`window` consecutive values. Raise ValueError if the window is smaller than 1
or longer than the data.
Example: moving_average([1, 2, 3, 4, 5, 6], 3) -> [2, 3, 4, 5]

Then smooth a noisy sine wave and plot both lines.
Hints: np.convolve(values, np.ones(window) / window, mode="valid").
The result is shorter by window - 1 items, so trim the x values when plotting.
"""

import matplotlib.pyplot as plt
import numpy as np


def moving_average(values, window):
    # TODO
    pass


# TODO: the noisy sine wave and the plot
