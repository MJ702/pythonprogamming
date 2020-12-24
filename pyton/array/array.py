# -------------------- Array --------------------
import array as arr
print('-------------------- Array --------------------')

# What is array?
# array is basically a data structure which can hold more then one values at a time. it is a collation of ordered of same element at a same Timeout.

a = arr.array('i',[1,2,3,4,5,6,7,8,9])
# here i is type of array
print(a)

# Accessing elements
print('\nArray first element')
print(a[0])

# Find length of array
print('\nArray lenght:')
print(len(a))

# -------------------- Add --------------------
print('\n-------------------- Add --------------------')

""" 
    Adding element to the array 
    1.append function is used to add a single element at the end of array.
    2.extend function is used to add a more then one element at the and of array.
    3.insert function is used to add element at particular index value. 
"""

# append
print('\nappend 10')
a.append(10)
print(a)

# extend
print('\nextend 11,12')
a.extend([11, 12])
print(a)

# insert
print('\ninsert at 0 index value is 0')
a.insert(0, 0)
print(a)

# -------------------- Pop --------------------
print('\n-------------------- Pop --------------------')
"""
    remove element to the Array
    1.pop function is used to remove last element of Array with return.
    2.remove fuction is used to remove a specific value without return it.
"""

# pop
print('\npop')
a.pop()
print(a)

# remove
print("\nremove 6 index which value is 6")
a.remove(6)
print(a)

# -------------------- Conctenation --------------------
print('\n-------------------- Conctenation --------------------')
# array concatenation  done with + operator
a = arr.array('i',[0,1,2,3,4,5])
print('\nfirst array')
print(a)

b = arr.array('i',[10,12,12,13,14,15])
print('\nsecond array')
print(b)

print('\nadd or conctenation array')
c = arr.array('i') # declare empty array to store the result
c = a + b
print(c)

# you can not add two different type of array

# -------------------- Slicing an array --------------------
print("\n-------------------- Slicing an array --------------------")

# an array can be sliced using the : symbol this is return a range of element that we have specified by index numbers


print('\nslicing of array : index values start with 0 to 3')
a = arr.array('i',[0,1,2,3,4,5])
print('\n array')
print(a)
print(a[0:3]) # 3 is not include
# you can also used nagative index number