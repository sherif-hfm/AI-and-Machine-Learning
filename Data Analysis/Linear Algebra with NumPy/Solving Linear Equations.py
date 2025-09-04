import numpy as np
matrix_a = np.array([[3, 1], [1,  2]])
matrix_b=np.array([9,8])

solution = np.linalg.solve(matrix_a, matrix_b)
print("Solution:", solution)

#verify the solution
verification = matrix_a @ solution
print("Verification (Ax = b):", verification)
print("Original b:", matrix_b)