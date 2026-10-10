import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 1], [1, 0]])

print(A @ B)
print(B @ A)
print(A * B)
print(A @ np.array([1, 1]))

# A * B multiplies matching entries one by one (element-wise).
# A @ B takes each row of A times each column of B and adds the results.
# The order matters for @, because the rows and columns being combined change.


def matmul_manual(A, B):
    rows, inner, cols = len(A), len(B), len(B[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(inner):
                result[i][j] += A[i][k] * B[k][j]
    return result


assert np.allclose(matmul_manual([[1, 2], [3, 4]], [[0, 1], [1, 0]]), A @ B)
print("Manual version matches NumPy.")
