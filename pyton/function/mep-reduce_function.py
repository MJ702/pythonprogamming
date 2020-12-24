def new(a):
    return a * a


x = list(map(new, [1, 2, 3, 4, 5]))
print(x)


def new(a, b):
    return a * b


x = list(map(new, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]))
print(x)

# filter


def new(i):
    if i >= 3:
        return i


number_list = [1, 2, 3, 4, 5]
x = list(filter(new, number_list))
print(x)

x = list(filter(lambda x: (x >= 2), number_list))
print(x)

# reduce

from functools import reduce


def new1(i, j):
    return i + j


number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(reduce(new1, number_list))

print(reduce(lambda x, y: x * y, number_list))

# Filter with map
print(tuple(map(lambda x: x + x, filter(lambda x: (x >= 30), number_list))))

# Map with filter

print(tuple(filter(lambda x: (x >= 30), map(lambda x: x + x, number_list))))

# Map and filter with reduce

print(reduce(lambda x, y: x + y, map(lambda x: x + x, filter(lambda x: (x <= 50), number_list))))
