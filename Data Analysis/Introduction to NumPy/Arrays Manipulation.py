import numpy as np
array1 = np.array([1, 2, 3, 4, 5, 6])
print(f"Original array:\n{array1}")

#indexing
print(f"Element at index 1:{array1[1]}")
#slicing
print(f"Elements from index 1 to 4:{array1[1:4]}")

#modifiing slicing
array2 = array1[1:4]
array2[0]=11 #modifying array2 also modifies array1
print(f"Modified array:\n{array2}")
print(f"Original array:\n{array1}")

#concatenation
array3 = np.concatenate((array1, array2))
print(f"Concatenated array:\n{array3}")
