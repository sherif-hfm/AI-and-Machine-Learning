import numpy as np
array1 = np.arange(10)
indices=[2,5,3]
index_elements = array1[indices]
print("Indexed Elements:\n", index_elements)

bool_indices = array1 % 2 == 0
even_elements = array1[bool_indices]
print("Even Elements:\n", even_elements)