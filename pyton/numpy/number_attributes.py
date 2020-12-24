import numpy as np

# --------------- Attributes ---------------
# Tuple of bytes to step in each dimension when traversing an array.
x = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]], dtype=np.int32)
print(x.strides)
"""
    This array is stored in memory as 40 bytes, one after the other (known as a contiguous block of memory). 
    The strides of an array tell us how many bytes we have to skip in memory to move to the next position along a 
    certain axis. For example, we have to skip 4 bytes (1 value) to move to the next column, but 20 bytes 
    (5 values) to get to the same position in the next row. As such, the strides for the array x will be (20, 4).
"""

# Information about the memory layout of the array.
print(x.flags)

# Number of array dimensions.
print("\nDimension of array:", end=" ")
print(x.ndim)

# Python buffer object pointing to the start of the array’s data.
# print(x.data)

# Number of elements in the array.
print("\nNumber of element present in array:", end=" ")
print(x.size)

# Length of one array element in bytes.
print("\nLength of one array element in bytes:", end=" ")
print(x.itemsize)

# Total bytes consumed by the elements of the array.
print("\nTotal bytes consumed by the elements of the array:", end=" ")
print(x.nbytes)

# Base object if memory is from some other object.
print("\nIf x is a derived array it print false:", end=' ')
print(x.base is None, end=" ")
print("That means x is crate by np.array of etc")

# Type of variable
print("\nType of x variable:", end=" ")
print(type(x))

# Shape of array
print("\nShape of array:", end=" ")
print(x.shape)

# Data type type of array
print("\nData type of array", end=" ")
print(x.dtype)

# The element of x in the *second* row, *third* column, namely, 7.
print("\nSecond raw and third column element as shown in below output", end=" ")
print(x[1, 2])
print(x)

# slicing can produce views of the array:
print("\nPrint first and second  raw 1 index element:", end=" ")
y = x[:, 1]
print(y)
print(x)

# Reshape can change the shape of array
print("\nReshape of x array and store  in y:")
y = x.reshape(5, 2)
print(y)


# The transposed array.
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int32)
print("\nTransport of x:")
print(x.T)

# The real part of the array.
print("\nThe real part of the array:")
print(x.real)

# The imaginary part of the array.
print("\nThe imaginary part of the array:")
print(x.imag)

# A 1-D iterator over the array.
print(x.flat[3])
print(x.T.flat[3])
x.flat = 3
print(x)
