# Logical operators are  used to combine conditional statement
# and , or , not
a = int(input("enter your number a:"))
b = int(input("enter your number b:"))

# below code is conditional statement

if a == b:
    print("equal")
elif a > b:
    print('greater')
else:
    print("smaller")

x = 10
y = 20
print("x value: " + str(x) + "y value: " + str(y))
print("logical and : if all condition are true return true")
print(x > y and x < y)

print("logical or : if one condition is true return true")
print(x > y or x < y)

print("logical not : it return negation")
print("not(x > y and x < y) : it's return true because in barcket result false not is convert into true")
print(not(x > y and x < y))