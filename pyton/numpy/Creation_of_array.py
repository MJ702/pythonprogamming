import numpy as np

# creation of array
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=np.int32)
print(a)
print()

b = np.array([[34, 54, 73, 78], [78, 90, 91, 67]], dtype=complex)
print(b)
print()

# The function zeros creates an array full of zeros
c = np.zeros((3, 4))
print(c)
print()

d = np.ones((2, 3))
print(d)
print()

e = np.empty((2, 4))
print(e)
print()

# Using range function

f = np.arange(10)
print(f)
print()

f = np.arange(0, 30, 2)
print(f)
print()

f = np.arange(0, 5, 0.3)
print(f)
print()

"""
    When arange is used with floating point arguments, it is generally not possible to predict the number of elements 
    obtained, due to the finite floating point precision. For this reason,
    it is usually better to use the function linspace that receives as an argument the number of elements that we want,
    instead of the step:

"""

# Create a array with n floating point
g = np.linspace(0, 3, 9)  # In this 9 is floating point number
print(g)
print()

# Return an array of zeros with the same shape and type as a given array.
h = np.zeros_like(a)
print(h)
print()

# Using random function
i = np.random.rand(5, 5)
print(i)
print()

# Form function
j = np.fromfunction(lambda i_1, j_1: i_1 + j_1, (3, 2), dtype=int)
print(j)
print()

