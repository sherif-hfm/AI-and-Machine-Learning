import numpy as np
matrix_a = np.array([[1, 2], [3,  4]])
matrix_b = np.array([[5, 6], [7, 8]])

#print(matrix_a[1, 0])


matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)
print("Matrix Product:\n", matrix_product)
exit()

matrix_product2 = matrix_a @ matrix_b
print("Matrix Product 2:\n", matrix_product2)

#transpose
matrix_a_transposed = matrix_a.T
print("Matrix A Transposed:\n", matrix_a_transposed)
