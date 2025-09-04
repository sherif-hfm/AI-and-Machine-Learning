import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

print(f"Addition:\n{array1 + array2}")
print(f"Subtraction:\n{array1 - array2}")
print(f"Element-wise multiplication:\n{array1 * array2}")
print(f"Element-wise division:\n{array1 / array2}")


print("Scalar addition:\n",array1 + 1)
print("Scalar multiplication:\n",array1 * 2)

#broadcasting
array7 = np.array([[1], [2], [3]])
array8 = np.array([4, 5, 6])
print(f"Broadcasting:\n{array7 + array8}")
