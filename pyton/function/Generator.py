import random


def lottery():
    for i in range(6):
        yield random.randint(1, 40)

    yield random.randint(1, 15)


for random_number in lottery():
    print("Winner number is....%d" % random_number)

# Fibonacci series

print("\n")


def fib():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f + s


for i in fib():
    if i > 50:
        break
    print(i, end=" ")

# Number stream
print("\n")
b = (x for x in range(2, 35, 2))
for i in b:
    print(i, end=" ")

