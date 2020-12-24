import numpy as np

matrix_1 = np.arange(start=1, stop=10).reshape(3, 3)

print("matrix 1: \n" + str(matrix_1))

matrix_1[[0, 1]] = matrix_1[[1, 0]]
print("swap row matrix: \n" + str(matrix_1))