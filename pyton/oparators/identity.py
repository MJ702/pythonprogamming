# Identity operator is used to compare object
# 1.is  return true if both variable are same
# 2.is not return true if both variable not same

list_1 = [10, 20, 30]
list_2 = list(range(10, 31, 10))

x = list_1  # assign list_1 to x
print("x is list_1 : true")
print(x is list_1)

print(list_1  is not list_2)