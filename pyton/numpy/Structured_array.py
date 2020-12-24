import numpy as np

"""
    Structured arrays ar'e ndarrays whose datatype
    is a composition of of simpler datatypes
    organized as a sequence of nemed fields.
"""

x = np.array([('Rex', 9, 56), ('Jimi', 5, 78.9)],
             dtype=[('name', 'U10'), ('age', '<i4'), ('weight', '<f4')]
             )

print(x)
print()

print(x[1])
print()
print(x['age'])

x['age'] = 4
print(x['age'])
print()
print(x)

# Structured datatype creation

# 1. A list of tuples, one tuple per field

a = np.dtype([('x', 'f4'), ('y', np.float32), ('z', 'f4', (2, 2))])
print(a)

a = np.dtype([('x', 'f4'), ('', 'i4'), ('z', 'i8')])
print(a)

# 2. A string of comma-separated dtype specifications

x = np.dtype('i8, f4, S3')
print(x)

# 3. A dictionary of field parameter arrays

b = np.dtype({'names': ['col1', 'col2'], 'formats': ['i4', 'f4']})
c = np.dtype({'names': ['col1', 'col2'],
              'formats': ['i4', 'f4'],
              'offsets': [0, 4],
              'itemsize': 12})
print(c)

# 4. A dictionary of field names

c = np.dtype({'col1': ('i1', 0), 'col2': ('f4', 1)})
print(c)

# Minpulating and Displaying Structured Datatypes

d = np.dtype([('x', 'i8'), ('y', 'f4')])
print(d.names)
print(d.fields)


def print_offsets(d):
    print('offsets:', [d.fields[name][1] for name in d.names])
    print("itamsize:", d.itemsize)


print_offsets(np.dtype('u1, u1, i4, u1, i8, u2'))
print_offsets(np.dtype('u1, u1, i4, u1, i8, u2', align=True))
