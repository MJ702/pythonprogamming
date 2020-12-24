"""
    Tuple data type in python
        1. Tuple
        2. Nested Tuple
"""

# -------------------- Tuple --------------------
print("\n -------------------- Tuple --------------------")

# Tuple is ordered, cannot be change (immutable) ,duplicate item are present
# denoted with ()

tuple_1 = (1, 2, 1, 7, 1, 3, 4, 5, 'Tiger', 'Elephant', 'Lion', 'monkey', 'Tiger')
print(tuple_1)

# Element print using index number
print("print index values 2 :")
print(tuple_1[2])

# Count in tuple to count the values in tuple
print('\ncount the number 1 and tiger :')
print(tuple_1.count(1))
print(tuple_1.count('Tiger'))
