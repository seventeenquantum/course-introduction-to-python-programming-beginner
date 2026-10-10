import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(3)
steps = rng.choice([-1, 1], size=(5, 1000))
walks = np.cumsum(steps, axis=1)

for i, walk in enumerate(walks, start=1):
    plt.plot(walk, label=f"Walk {i}")
    print(f"Walk {i}: final {walk[-1]}, farthest from zero {np.abs(walk).max()}")

plt.axhline(0, color="black", linewidth=0.5)
plt.xlabel("Step")
plt.ylabel("Position")
plt.title("Five random walks")
plt.legend()
plt.show()
