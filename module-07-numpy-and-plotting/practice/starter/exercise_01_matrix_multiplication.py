"""Exercise 1: Matrix multiplication by hand and in NumPy.

A = [[1, 2], [3, 4]]    B = [[0, 1], [1, 0]]

Part A: work out A @ B and B @ A BY HAND on paper (row times column).
Part B: check both in NumPy.
Part C: explain in a comment why A * B differs from A @ B,
        and why A @ B is not equal to B @ A.
Part D: multiply A by the vector [1, 1].
Part E (challenge): write matmul_manual(A, B) with loops on plain lists
        and check it against NumPy with np.allclose.

Expected: A @ B = [[2, 1], [4, 3]]    B @ A = [[3, 4], [1, 2]]
          A * B = [[0, 2], [3, 0]]    A @ [1, 1] = [3, 7]
Note: B is the X (NOT) gate you will meet in Course 2.
"""

import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])

# TODO
