import numpy as np

# A 2-dimensional array of size 2 x 3, composed of 4-byte(32bits) integer elements

x = np.array([(1, 2, 3), (4, 5, 6)])
print("\nType of x variable:", end=" ")
print(type(x))

print("\nShape of array:", end=" ")
print(x.shape)

print("\nData type of array", end=" ")
print(x.dtype)

# The element of x in the *second* row, *third* column, namely, 6.
print("\nSecond raw and third column element as shown in below output", end=" ")
print(x[1, 2])
print(x)

# slicing can produce views of the array:
print("\nPrint first and second  raw 1 index element:", end=" ")
y = x[:, 1]
print(y)
print(x)


y[0] = 9  # This also changes the corresponding element in x
print("\nChange the 0 index values as 9:", end=" ")
# Here y 0 index indicate a x of first raw second element so directly change in x first raw second element 9
print(y)
print(x)

