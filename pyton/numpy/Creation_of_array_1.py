import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(14, size=10)
print(a)

# different upper bounds
a = np.random.randint(1, [12, 54, 89])
print(a)

# different lower bounds
a = np.random.randint([7, 8, 9], 15)
print(a)

a = np.random.random_integers(1, 6, 1000)
b = np.random.random_integers(1, 6, 1000)
d = a + b

count, bin_1, ignored = plt.hist(d, 11, density=True)
plt.show()
