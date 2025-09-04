import numpy as np
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# vertical Stacking
stacked_array = np.vstack((array1, array2))
print("Stacked Array:\n", stacked_array)

# horizontal Stacking
h_stacked_array = np.hstack((array1, array2))
print("Horizontally Stacked Array:\n", h_stacked_array)

#depth Stacking
d_stacked_array = np.dstack((array1, array2))
print("Depth Stacked Array:\n", d_stacked_array)

# horizontal Splitting
h_split_arrays = np.hsplit(h_stacked_array, 2)
for i, arr in enumerate(h_split_arrays):
    print(f"Horizontal Split Array {i}:\n", arr)

# vertical Splitting
v_split_arrays = np.vsplit(array1, 2)
for i, arr in enumerate(v_split_arrays):
    print(f"Vertical Split Array {i}:\n", arr)
