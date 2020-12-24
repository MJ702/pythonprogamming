"""
    Collation data type in python
        1.namedtuple
        2.ChainMap
        3.deque
        4.counter
        5.orderedDict
        6.defaultDict
        7.userList # wrapper around dictionary objects for easier dict subclassing
        8.userDict # wrapper around list objects for easier list subclassing
        9.userString # wrapper around string objects for easier string subclassing

        There are four data type in python
         which are used to store collation of data is know as collation data type

        Specialised collation data structure
"""

# -------------------- Namedtuple --------------------
print('\n-------------------- namedtuple -------------------------\n')
from collections import namedtuple
# namedtuple() is return a tuple with a name values for each element in the  tuple

#  namedtuple factory function for creating tuple subclasses with named fields


# above syntax collection is library of python and import namedtuple function in our program

a = namedtuple('Language', 'human, computer ,alien')
s = a('Hindi', 'Python', 'xyz')
print(s)
# make function is used to list connect tuple
b = namedtuple('Language', 'human, computer ,alien')
d = a._make(['Hindi', 'Python', 'xyz'])
print(d)

"""
    In namedtuple must remember this note
    1.after namedtuple() in bracket name is tuple of name (language)
    2.tuple name not used after name declared ('Language', 'human language, computer language ,alien language')
    3.in a tuple you declared you declared element same as namedtuple()
        for example in a = namedtuple have 3 element and 
                       s = a have 3 element so give out put other wish give error
"""

# -------------------- deque -------------------------
print('\n-------------------- deque -------------------------\n')

# List-like container with fast appends and pops on either end
from  collections import deque
list_1 = list(range(0,11))
d = deque(list_1)

print('Append')
d.append(12)
print(d)

print('Append left')
d.appendleft(13)
print(d)

print('pop')
d.pop()
print(d)

print('pop left')
d.popleft()
print(d)


# -------------------- ChainMap ------------------------

print('\n-------------------- ChinMap -------------------------\n')

# Dict-like class for creating a single view of multiple mappings

from collections import ChainMap

dict_1 = {1: 'python', 2: 'c++', 3: 'c'}
dict_2 = {4: 'python turtle', 5: 'python pygame'}

a = ChainMap(dict_1,dict_2)
print(a)

# -------------------- Counter -------------------------

print('\n-------------------- Counter -------------------------\n')

# Dict subclass for counting hashable objects
from collections import Counter
list_1 = [1, 2, 3, 6, 5, 4, 3, 2, 3, 4, 2, 1, 3, 4, 9, 7, 5, 8, 9, 9]

c = Counter(list_1)
print(c)

print(list(c.elements()))

# shorted list of each count element
print(list(c.most_common()))

# sub dict is substract values from main dict
sub = {3: 1, 2: 2}
c.subtract(sub)
print(c.most_common())

# -------------------- OrderedDict -------------------------

print('\n-------------------- OrderedDict -------------------------\n')

# Dict subclass that remembers the order entries were added
from collections import OrderedDict

d = OrderedDict()

d[1] = 'H'
d[2] = 'e'
d[3] = 'l'
d[4] = 'l'
d[5] = 'o'
d[6] = 'w'
print(d)

print(d.keys())
print(d.items())

# -------------------- DefaultDict -------------------------

print('\n-------------------- DefaultDict -------------------------\n')

# Dict subclass that calls a factory function to supply missing values

from collections import defaultdict

d = defaultdict()
d[1] = 'python turtle'
d[2] = 'python pygame'

print(3)

# a = {4: 'python turtle', 5: 'python pygame'}
# print(a[3]) # this two line give a error but defaultdict not gives a error
