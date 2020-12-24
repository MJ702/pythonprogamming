import numpy as np

a = np.arange(10)
b = a  # a and b are two names for the same ndarray object not copy
print(b)
b.shape = (5, 2)  # Also change the shape of a
print(a.shape)


# id is a unique identifier of an obj

def f(x):
    print(id(x))


f(a)
f(b)

# View or shallow copy

c = a.view()  # The view method creates a new array object that looks at the same data.
print(c is a)
print(c.base is a)
print(c.flags.owndata)
c.shape = 2, 5
print(c.shape)
print(a.shape)

c[0, 4] = 15  # a's data changes
print(a)

# Deep copy

b = a.copy()  # a new array object with new data is created
print(b is a)

# d doesn't share anything with
print(b.base is a)
b[2, 0] = 78  # dosen't change in a array
print(b)
print(a)

