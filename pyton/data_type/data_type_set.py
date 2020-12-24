"""
    Set data type in python
        1.Set
"""

# -------------------- Set ----------------------
# Unordered , No duplicate entry are present
print("\n-------------------- Set --------------------\n")

set_1 = {'Insane programer', 14, 702, 35, 'Python'}
set_2 = {14, 'Python', 702, 35, 56}
print(set_1)

# Add function is used to add new item in set
# The new values add in set it can any index values
print('\nFunction name add : Python_turtle')
print("\n\tset_1 =" + str(set_1))
set_1.add("Python_turtle")
print("\t" + str(set_1))

# Clear to used clear whole set
# Syntax is set_name.clear()

# Copy function is used in set to copy set
print("\nFunction name copy : ")
print("\n\tset_1 =" + str(set_1))
x = set_1.copy()
print("\t" + str(x))

# Return a set that contains the items that only exist in set set_1, and not in set set_2:
# print different values of both set
print("\nFunction name difference : ")
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
z = set_1.difference(set_2)
print('\n\t' + str(z))

# Remove "14" from the set:
print('\nFunction name discard : 14 ')
print("\n\tset_1 =" + str(set_1))
set_1.discard(14)
print("\t" + str(set_1))

# Return a set that contains the items that exist in both set x, and set y:
print('\nFunction name intersection : ')
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
z = set_1.intersection(set_2)
print("\n\t" + str(z))

# Remove the items that is not present in both set_1 and set_2
print('\nFunction name intersection_update : ')
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
set_1.intersection_update(set_2)
print("\n\t" + str(set_1))
print("\n\t after Function apply : ")
print("\n\tset_1 =" + str(set_1))


# Remove the items that exist in both sets:
print("\nFunction name difference_update : ")
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
set_1.difference_update(set_2)
print('\n\t' + str(set_1))
print("\n\t after Function apply : ")
print("\n\tset_1 =" + str(set_1))

# Over right set
set_1 = {"apple", "banana", "cherry"}
set_2 = {"google", "microsoft", "facebook"}
# Return True if no items in set set_1 is present in set set_2
# If both set are different it return true
print('\nFunction name isdisjoint :')
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
z = set_1.isdisjoint(set_2)
print('\n\t' + str(z))
print("\n\t Because set_1 and set_2 have some no same element ")

# Return True if all items set set_1 are present in set set_2:
print('\nFunction name issubset :')
set_1 = {"a", "b", "c"}
set_2 = {"f", "e", "d", "c", "b", "a"}
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
z = set_1.issubset(set_2)
print('\n\t' + str(z))
print("\n\t  set_1 is subset of set_2")


# Return True if all items set set_2 are present in set set_1:
set_1 = {"f", "e", "d", "c", "b", "a"}
set_2 = {"a", "b", "c"}
print('\nFunction name issuperset :')
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
z = set_1.issuperset(set_2)
print('\n\t' + str(z))

# Remove a random item from the set
set_1 = {'Insane programer', 14, 702, 35, 'Python'}
print('\nFunction name pop :')
print("\n\tset_1 =" + str(set_1))
set_1.pop()
print('\n\t' + str(set_1))

# Remove "35" from the set
set_1 = {'Insane programer', 14, 702, 35, 'Python'}
print('\nFunction name remove : 35')
print("\n\tset_1 =" + str(set_1))
set_1.remove(35)
print('\n\t' + str(set_1))

# Return a set that contains all items from both sets, except items that are present in both sets
# Not return same values in both set
set_1 = {"f", "e", "d", "c", "b", "a"}
set_2 = {"a", "b", "c"}
print('\nFunction name symmetric_difference :')
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
z = set_1.symmetric_difference(set_2)
print('\n\t' + str(z))


# Remove parement the items that are present in both sets
set_1 = {"f", "e", "d", "c", "b", "a"}
set_2 = {"a", "b", "c"}
print('\nFunction name symmetric_difference_update :')
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
set_1.symmetric_difference_update(set_2)
print('\n\t' + str(set_1))
print("\n\t after Function apply : ")
print("\n\tset_1 =" + str(set_1))

# Return a set that contains all items from both sets, duplicates are excluded
set_1 = {"f", "e", "d"}
set_2 = {"a", "b", "c"}
print('\nFunction name union :')
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
z = set_1.union(set_2)
print('\n\t' + str(z))

# Insert the items from set_2 into set_1
set_1 = {"f", "e", "d"}
set_2 = {"a", "b", "c"}
print('\nFunction name update :')
print("\n\tset_1 =" + str(set_1))
print("\n\tset_2 =" + str(set_2))
set_1.update(set_2)
print('\n\t' + str(z))
print("\n\t after Function apply : ")
print("\n\tset_1 =" + str(set_1))
