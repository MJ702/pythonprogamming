# Lambda argument: expression
"""
    Lambda function is anonymous or nameless function
    Lambda is used for reduce the number of code lien

"""
x = lambda a: a * a
print(x(3))

# Lambda with user-defined function


def add(x):
    return lambda y: x + y


t = add(5)
print(t(8))

# Using lambda function with filter, map , reduce

"""
    Filter the given iterables(list , dict, etc ) with the help of 
    another function passed an argument to test all the element to be true of false
    
    in lambda if values is true that return the function 
"""

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = list(filter(lambda a: (a/3 == 2), number_list))

print(new_list)


# Map function is applies give function all the iterable and return a new list

new_list = list(map(lambda a: (a/2 == 0), number_list))

print(new_list)

"""
    Reduce applied to some other function to a list of element that are 
    passed as parameter to it finally return a single value
"""

from functools import reduce

total = reduce(lambda a, b: a + b, number_list)

print(total)

# Lambda for algebra

linear = lambda x, y: 3 * x + 4 * y

print(linear(3, 4))

# Quadratic question (a + b ) ** 2

Quadratic = lambda a, b : (a + b) ** 2

print(Quadratic(3, 4))
