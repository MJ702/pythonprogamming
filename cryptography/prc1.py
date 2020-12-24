import numpy as np
import pandas as pd
matrix_1 = np.arange(start=1, stop=10).reshape(3, 3)
print(matrix_1.T)
matrix_1[[0, 1]] = matrix_1[[1, 0]]
print(matrix_1)
