import numpy as np
matrix = np.array([[2, 1], [1,  2]])

#determinant
determinant = np.linalg.det(matrix)
print("Determinant:", determinant)

#inverse
inverse = np.linalg.inv(matrix)
print("Inverse:\n", inverse)

#eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)