"""
    List data type in python
        1. List
        2. Nested list
        3. List comprehension
"""

# ------------------------- List -------------------------
print()
print("-------------------- List -------------------------")
# List is denoted by squre bracket [] in list store any thing like float integer string complex etc.
# index  [00, 01, 02 , 03]
list_1 = [10, 20, 30, "Insane programer"]
# negative index [-04, -03, -02, -01]
print("\nWhole list with bracket :")
print(list_1)

print("\nprint list using nagative index -3 :")
print(list_1[-3])

# In list update element in existing index number
print("\nUpdate element in lis_1 using index number 1 : add element is Python ")
print("\n\tBefore update list :")
"""
    Here a str is function of python to convert type 
    syntax convert_type_naem(float, int)(variable name to convert type)
    for example a="Insane programer" this string and convert into int following syntax is
    int(a)
"""
print("\t" + str(list_1))
print("\n\tAfter update list :")
list_1[1] = "Python"
print("\t" + str(list_1))

# Add element in list and this element add on at the and of list
print('\nAdd element in list_1 using append function : Add element is Python_turtle ')
print("\n\tBefore update list :")
print("\t" + str(list_1))
print("\n\tAfter update list :")
list_1.append("python_turtle")
print("\t" + str(list_1))

# Return the length of list
print("\nFunction name len: ")
print(len(list_1))

# Insert element in list using index number this function
# add element in list not over right in existing element
print('\nAdd element in list_1 using insert function : Add element is 40 at index 4')
print("\n\tBefore update list :")
print("\t" + str(list_1))
print("\n\tAfter update list :")
# syntax list_name.insert(index_number, values_you_want_to_insert)
list_1.insert(4, 40)
print("\t" + str(list_1))

# Remove function is used to remove particular element or item
print('\nremove element in list_1 using remove function : remove element is Python_turtle ')
print("\n\tBefore update list :")
print("\t" + str(list_1))
print("\n\tAfter update list :")
list_1.remove("python_turtle")
print("\t" + str(list_1))

# Pop function is used to remove element it automatically remove last element
print('\nremove element in list_1 using pop function : pop element is 40 ')
print("\n\tBefore update list :")
print("\t" + str(list_1))
print("\n\tAfter update list :")
list_1.pop()
print("\t" + str(list_1))

# Del function is used to delete element using index values
print('\nremove element in list_1 using del function : remove element is 30 ')
print("\n\tBefore update list :")
print("\t" + str(list_1))
print("\n\tAfter update list :")
# syntax del space variable_name[index_number]
# you right del list_1 not specify it del whole list
del list_1[2]
print("\t" + str(list_1))

# Copy function is used to copy list to another list
list_2 = list_1.copy()
print('\nfunction name copy :')
print("Copy list:" + str(list_2))
print("Copy list using list function:")
list_2 = list(list_1)
print("Copy list:" + str(list_2))

# Join to list list using + operator
print("\nAdd list = original list + copy list")
# In this method list_1 is first  so list_1 element copy first after copy list_2 element
list_3 = list_1 + list_2
print(list_3)

# Join to list using extend function
print("\nFunction name extend : ")
# In this case list_2 copy in list_1
list_1.extend(list_2)
print(list_1)

# Clear is function in list to clear a list an make empty list like list_1 = [] , syntax list_1.clear()

# Count function in list to count the values given in barcket
print("\nFunction name count : apply in copy list name is list_3 count is Insane programer")
print(list_3.count("Insane programer"))

# Reverse function in list to reverse whole list
print("\nFunction name reverse ")
print("\toriginal list :")
print('\t' + str(list_3))
print("\treverse list : ")
list_3.reverse()
print('\t' + str(list_3))

# short function in list to short list if list have a same  type of element
list_4 = ['z', 'x', 'y']
print("\nFunction name short")
print("\toriginal list :")
print('\t' + str(list_4))
print("\treverse list : ")
list_4.sort()
print('\t' + str(list_4))
print("\n")

# -------------------- Nested list ---------------
print("-------------------- Nested list --------------------")
# Here we over right list
# Nested list is list in another list
list_1 = [
    'Human Language', ['Gujrati', 'Hindi', 'English'],
    'Computer Language', ['Python', 'R', 'Csharp']
]

print(list_1)

# ------------------------- List comprehension -------------------------
print()
print("-------------------- List comprehension -------------------------")

# In this section create a list using different wave

print("List using rang function:")
# Last digit not include in range for this example 11
list_1 = list(range(0, 10))
print(list_1)

print('\nCreate a list using for loop:')

"""
    number = range(0,11) 11 is not include 
    
    new_list = [] make a empty list
    
    for i in number:
        if i % 2 == 0 :
            new_list.append(n**2)
    
    print(new_list)
    
    now above code is output like [[0, 4, 16, 36, 64, 100] 
    but this program can right in one line like below
    new_list = [x for x in range(0,11) if x % 2 ==0 ]
"""
print("\nThis list is a square number of 1 to 10:")
square = [x ** 2 for x in range(0, 11)]
print(square)

print("\nThis list is a base 2 and power 11:")
power = [2 ** i for i in range(0, 11)]
print(power)

print("\nThis is derived list from square number 1 to 10 : this list element is only even of square list")
square_even = [x for x in square if x % 2 == 0]
print(square_even)

print("\nThis is also derived list from square number 1 to 10 : this list element is only odd of square list")
square_odd = [x for x in square if x % 2 != 0]
print(square_odd)

# print list using for loop without bracket
list_1 = [10, 20, 30, "Insane programer"]
print("\nwithout for loop" + str(list_1))
print("\nusing for loop ")
print([i for i in list_1])
