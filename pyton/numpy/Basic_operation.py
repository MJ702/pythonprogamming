import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
print()
b = np.array([1, 2, 3, 4])
print(b)
print()

print(a - b)
print()
print(a + b)
print()
print(a * b)
print()
print(a / b)
print()

print(a ** 2)
print()

print(a < 3)
print()

# matrix product(cross product)
print(a @ b)
print()

# another matrix product(dot product)
print(a.dot(b))
print()

a = np.ones((2, 3), dtype=int)
b = np.random.random((2, 3))
a *= 3
print(a)
print()

print(a + b)

print(a.sum())
print(a.max())
print(a.min())

print(a)
print()

print(a.sum(axis=1))  # sum of each raw
print(a.sum(axis=0))  # sum of each column

print(a.min(axis=0))
print(a.max(axis=1))

a = np.ones((3, 3))
print(a)
print(a.cumsum(axis=1))
print()

# Universal function

a = np.arange(3)
print(a)
print()
print(np.exp(a))
print()
print(np.sqrt(a))
print(np.add(a, b))
print()
print(np.subtract(a, b))
print()
print(np.multiply(a, b))
print()
print(np.divide(a, b))


# slicing array can be possible

# multidimensional array

def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)
print(b)

print(b[2, 3])  # second raw fourth element

print(b[0:5, 1])  # each row in the second column of b
