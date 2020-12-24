import numpy as np

matrix_1 = np.arange(start=1, stop=10, step=1).reshape(3, 3)
matrix_2 = np.arange(9, 0, -1).reshape(3, 3)

print("matrix 1: \n" + str(matrix_1))
print("matrix 1: \n" + str(matrix_2))

print("matrix addition: \n" + str(matrix_1 + matrix_2))
