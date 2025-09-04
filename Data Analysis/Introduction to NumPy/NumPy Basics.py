import numpy as np
#print("NumPy version:", np.__version__)

list1 = [1, 2, 3, 4, 5]
array1 = np.array(list1)
print("NumPy array:", array1)
print("dimensions:", array1.ndim)
print("shape:", array1.shape)
print("size:", array1.size)
print("data type:", array1.dtype)

list2 = [[1,2,3],[4,5,6]]
array2 = np.array(list2)
print("NumPy array:", array2)
print("dimensions:", array2.ndim)
print("shape:", array2.shape)
print("size:", array2.size)
print("data type:", array2.dtype)
