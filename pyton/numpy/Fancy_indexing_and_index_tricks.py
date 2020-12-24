import numpy as np

# Fancy indexing adn index tricks

a = np.arange(12) ** 2
i = np.array([1, 1, 3, 8, 5])
print(a[i])
j = np.array([[3, 4], [9, 7]])
print(a[j])

palette = np.array([[0, 0, 0],
                    [255, 0, 0],
                    [0, 255, 0],
                    [0, 0, 255],
                    [255, 255, 255]])

image = np.array([[0, 1, 2, 0],
                  [0, 3, 4, 0]])

print(palette[image])

a = np.arange(12).reshape(3, 4)
print(a)
i = np.array([[0, 1],  # indices for the first dim of a
              [1, 2]])
j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])

print(a[i, j])

"""
    a[i, j] = a[i(0), j(2)]  = 2
    a[i, j] = a[i(1), j(1)]  = 5
    a[i, j] = a[i(1), j(2)]  = 7
    a[i, j] = a[i(2), j(3)]  = 11

"""
print(a[i, 2])



print(a.argmin(axis=0))
print(a.argmin(axis=1))
print(a.argmax(axis=0))
print(a.argmax(axis=1))
print()
"""
    [[ 0  3  8 13] 
     [12 11  2 11]  this for max number
     [ 5 13  8  3] 
     [12 15  3  4]]
      ^  ^   ^  ^ 
     12  15  8  13  - element 
     1   3   0  0   - indices 

"""

# apply in index number
a = np.arange(5)
print(a)
a[[2, 3, 4]] = 5
print(a)
a[[2, 3, 4]] += 3
print(a)

b = a >3
print(b)
print(a[b])
a[b] = 0
print(a)