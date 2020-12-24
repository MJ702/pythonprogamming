import numpy as np


"""
a = np.floor(10 *np.random.random((3, 4)))
print(a)
print(a.shape)
print(a.ravel())
print(a.reshape(6, 2))  # not change parmetaly
print(a.T)
print(a.T.shape)
print(a.shape)
print(a)
a.resize(6, 2) # change parmetaly
print(a)

# If a dimension is given as -1 in a reshaping operation, the other dimensions are automatically calculated:
print(a.reshape(3, -1))
"""

""""
# Stacking together different arrays

a = np.floor(10*np.random.random((2, 2)))
print(a)
b = np.floor(10*np.random.random((2, 2)))
print(b)

print(np.vstack((a, b)))
print(np.hstack((a, b)))

print(np.column_stack((a,b)))  # same as hstack
"""
