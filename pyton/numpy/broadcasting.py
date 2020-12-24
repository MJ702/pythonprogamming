import numpy as np

"""
    The term broadcasting describes how numpy treats arrays with
    different shapes during arithmetic operations. subject to certain
    constraints, the smaller array is "Broadcast" across the larger array
    so that they have compatible shapes.

"""

a = np.array([1, 2, 3])
b = np.array([2, 2, 2])
print(a * b)

b = 2
print(a * b)

""" 
    GENERAL BROADCASTING RULES
    -> When operating on two, Numpy compares their  shapes
    element-wise. It start with the  trailing dimensions and
    works its way forward. Two dimension are compatible when
        1. they are equal
        2. one of them is 1
    
    SOME EXAMPLE
    A   (4d array): 8 * 1 * 6 * 1
    B   (3d array):     7 * 1 * 5
    result        : 8 * 7 * 6 * 5
    
"""

"""
    A      (1d array):  3
    B      (1d array):  4 
    trailing dimensions do not match

    A      (2d array):      2 x 1
    B      (3d array):  8 x 4 x 3  
    second from last dimensions mismatched

"""
x = np.arange(4)
xx = x.reshape(4, 1)
y = np.ones(5)
z = np.ones((3, 4))

print(x.shape)
print(y.shape)

# print(x + y)
"""
    ValueError: operands could not be broadcast together with shapes (4,) (5,)
"""

print(xx.shape)
print(y.shape)

print((xx + y).shape)
print(xx + y)

a = np.array([1, 2, 3, 4, 5])

b = np.array([1, 2])
print(a[:, np.newaxis] + b)
