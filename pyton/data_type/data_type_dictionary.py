"""
    Dictionary data type in python
        1.Dictionary
        2.Nested dictionary
"""

# -------------------- Dictionary -------------------
print("\n --------------------- Dictionary --------------------")
# Dictionary in python data type unordered,can be change (mutable) , noduplicate entry are present
# In dictionary one element has two part one part is key that is first and second part is values
# In dictionary key and values separated by : and two element separated by ,
# In all comment dictionary = dict
dict_1 = {
    # Key : values
    'fruit': 'apple, orange , banana',
    'odd number': 2,
    1: 'even number'
}

print(dict_1)

# Copy function in dict to copy dict to another dict
print('\nFunction name copy : ')
dict_2 = dict_1.copy()
print(dict_2)

# Fromkey is function in Python to create a dict
x = ('key1', 'key2', 'key3')  # Here tuple() is another data type
y = 0
print('\nFunction name fromkey :')
dict_3 = dict.fromkeys(x, y)
print(dict_3)
print(type(dict_3))

# Get function in dict to print the values of given key
print('\nFunction name get : fruit')
print(dict_1.get('fruit'))

# Returns a list containing a tuple for each key value pair
print('\nFunction name item : ')
print(dict_1.items())

# Key function in dict to print the key
print('\nFunction name keys : ')
print(dict_1.keys())

# values function in dict to print values
print('\nFunction name values : ')
print(dict_1.values())

# Pop function in dict to remove element in dict using a key
print('\nFunction name pop : ')
print(dict_1.pop(1))

# Popitem function in python to remove last element of dict
print('\nFunction name pop : ')
print(dict_1)
print(dict_1.popitem())

# Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print('\nFunction name setdefault : ')
dict_1.setdefault("PI", '3.14')
print(dict_1)

# Updates the dictionary with the specified key-value pairs
print('\nFunction name setdefault : ')
dict_1.update({"E": '2.818'})
print(dict_1)
print('\n')


# -------------------- Nested dictionary -------------------
print("--------------------- Nested dictionary --------------------")
# In dict duplicate item print once time
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          1: {'name': 'John', 'age': '27', 'sex': 'Male'}}

print(people)

# -------------------- Hash table and hash map -------------------------
print('\n-------------------- Hash table and hash map -------------------------\n')

# hash table and hash map is type of data sturcture that maps key to its values pairs.
# In other words Hash table stores key-value pairs but the key is generated through a hashing function.

# creat dictionary using dict function

my_dict = {} # make a empty dict
print(my_dict)
print(type(my_dict))

# add element in my_dict using dict function

my_dict = dict(python = '3.8.1', c = '2.0.5')
print(my_dict)

print()
emp_details = {'employee':{'deva':{'Id':'001', 'salary':'2000', 'Designation':'team lead'},
'Ava':{'Id':'002', 'salary':'5000', 'Designation':'Associate'}}}

print(emp_details)

# -------------------- Operations on hash table --------------------
"""
    Operations 
        1.Acessing item
        2.
"""
# -------------------- Acessing item --------------------

print('\nAcessing item: python')
print('\tDict is :' + str(my_dict))
print('\t'+ str(my_dict['python']))

print('\t using key:')
print('\tDict is :' + str(my_dict))
print('\t'+ str(my_dict.keys()))

print('\n\t using values:')
print('\tDict is :' + str(my_dict))
print('\t' + str(my_dict.values()))

print()
for x in my_dict:
    print(x)

print()
for x in my_dict.values():
    print(x)

print()
for x, y in my_dict.items():
    print(x, y)

# Updating

print("\nupdate items:'python'= '3.8.1','csharp' ='6.34")
my_dict['python'] = '3.8.1'
my_dict['csharp'] = '6.34'
print(my_dict)

# Deleting

print("\ndeleting element: csharp")
print(my_dict.pop('csharp'))
print(my_dict.popitem())

del my_dict['python']
print(my_dict)

# convert dictionary into data frame
# Now data frame is two dimension data structure that consists of columns of various type. """

import pandas
emp_details = {'employee':{'deva':{'Id':'001', 'salary':'2000', 'Designation':'team lead'},
                            'Ava':{'Id':'002', 'salary':'5000', 'Designation':'Associate'}}}

data_frame = pandas.DataFrame(emp_details['employee'])
print(data_frame)