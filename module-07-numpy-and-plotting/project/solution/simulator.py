import numpy as np


def roll_dice(n, rng):
    """Roll a fair six-sided die n times. The upper bound of integers() is exclusive."""
    return rng.integers(1, 7, size=n)


def face_frequencies(rolls):
    """Return the fraction of rolls showing each face, for faces 1 to 6."""
    counts = np.bincount(rolls, minlength=7)[1:]
    return counts / len(rolls)


def running_heads(flips):
    """Return the fraction of heads after each flip (1 = heads, 0 = tails)."""
    return np.cumsum(flips) / np.arange(1, len(flips) + 1)


def two_dice_expected():
    """Return the exact probability of each sum from 2 to 12."""
    sums = np.add.outer(np.arange(1, 7), np.arange(1, 7)).ravel()
    return np.bincount(sums, minlength=13)[2:] / 36


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    rng = np.random.default_rng(42)
    n = 10_000

    # 1. Dice faces
    rolls = roll_dice(n, rng)
    freq = face_frequencies(rolls)
    print("Face  Simulated  Expected")
    for face, f in enumerate(freq, start=1):
        print(f"{face:>4}  {f:>9.4f}  {1/6:>8.4f}")

    # 2. Coin flips
    flips = rng.integers(0, 2, size=n)
    running = running_heads(flips)

    # 3. Sum of two dice
    sums = roll_dice(n, rng) + roll_dice(n, rng)
    sum_freq = np.bincount(sums, minlength=13)[2:] / n
    expected = two_dice_expected()

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    axes[0].bar(np.arange(1, 7), freq, label="Simulated")
    axes[0].axhline(1 / 6, color="red", linestyle="--", label="Expected (1/6)")
    axes[0].set_title("One die, 10,000 rolls")
    axes[0].set_xlabel("Face")
    axes[0].set_ylabel("Fraction of rolls")
    axes[0].legend()

    axes[1].plot(running)
    axes[1].axhline(0.5, color="red", linestyle="--")
    axes[1].set_title("Coin flips: running share of heads")
    axes[1].set_xlabel("Number of flips")
    axes[1].set_ylabel("Fraction heads")

    totals = np.arange(2, 13)
    axes[2].bar(totals, sum_freq, label="Simulated")
    axes[2].plot(totals, expected, "ro--", label="Exact")
    axes[2].set_title("Sum of two dice")
    axes[2].set_xlabel("Sum")
    axes[2].legend()

    fig.tight_layout()
    fig.savefig("simulation.png")
    plt.show()
