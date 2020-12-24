# Decorator in python are use very powerful which modify the behavior
# of a function without modifying permanently

"""
def function1(function):
    def wrapper():
        print("Hello")
        function()
        print("Welcome to my website.")
    return wrapper()


@function1
def function2():
    print("Bad_boy")
"""

# Decorator with argument

"""
print("\n")


def function1(function):
    def wrapper(*args, **kwargs):
        print("Hello")
        function(*args, **kwargs)
        print("Welcome my website.")
    return wrapper


@function1
def function2(fristname, secondname):
    print(f"{fristname}" + " " + f"{secondname}")


function2("Kasodiya", "meet")
"""

