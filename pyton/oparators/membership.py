# Membership operators are used to check sequence is present in object
# 1.in return true if a sequence with the specified values is present in the object
# 2.not in return true if a sequence with the specified values are is not present in the object

list_1 = [10, 20, 30]
list_2 = list(range(10, 31, 10))
print(10 in list_1)

print(list_1 in list_2)

print(35 not in list_1)