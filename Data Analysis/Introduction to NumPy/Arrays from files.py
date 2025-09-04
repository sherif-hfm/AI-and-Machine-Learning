import numpy as np
data = np.loadtxt("D:\\AI-and-Machine-Learning\\Data Analysis\\Introduction to NumPy\\array.csv", delimiter=",")
print(f"Data loaded from CSV:\n{data}")

random_array = np.random.random((3, 4))
np.savetxt("D:\\AI-and-Machine-Learning\\Data Analysis\\Introduction to NumPy\\random_array.csv", random_array, delimiter=",")
