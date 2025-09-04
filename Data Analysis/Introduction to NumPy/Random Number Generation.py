import numpy as np
#np.random.seed(42)
random_array = np.random.rand(3, 4)
print("Random Array:\n", random_array)

random_array2 = np.random.randn(3, 4)
print("Random Array:\n", random_array2)

random_array3 = np.random.randint(1, 100, size=10)
print("Random Array:\n", random_array3)
