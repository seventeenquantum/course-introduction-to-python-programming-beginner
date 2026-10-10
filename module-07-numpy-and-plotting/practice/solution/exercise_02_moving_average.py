import matplotlib.pyplot as plt
import numpy as np


def moving_average(values, window):
    values = np.asarray(values, dtype=float)
    if window < 1 or window > len(values):
        raise ValueError("window must be between 1 and len(values)")
    return np.convolve(values, np.ones(window) / window, mode="valid")


if __name__ == "__main__":
    assert np.allclose(moving_average([1, 2, 3, 4, 5, 6], 3), [2, 3, 4, 5])

    rng = np.random.default_rng(0)
    x = np.linspace(0, 4 * np.pi, 200)
    noisy = np.sin(x) + rng.normal(0, 0.3, size=200)
    smooth = moving_average(noisy, 15)

    plt.plot(x, noisy, alpha=0.4, label="Noisy")
    plt.plot(x[7:-7], smooth, label="Moving average (15)")
    plt.legend()
    plt.show()
