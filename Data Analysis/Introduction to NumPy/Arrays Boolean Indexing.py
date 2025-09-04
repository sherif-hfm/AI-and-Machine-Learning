import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])

mask = array1 > 2
filtered_array1 = array1[mask]
print("Mask:",mask)
print(f"Original array1:\n{array1}")
print(f"Filtered array1:\n{filtered_array1}")

array2[array2 > 8]=11
print(f"Modified array2:\n{array2}")
