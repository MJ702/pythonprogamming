# passing a function in other function
"""
def fun_1(name):
    return f"Hello{name}"


def fun_2(name):
    return f"{name} , How you doing?"


def fun_3(fun_4):
    return fun_4(" I am insane progammar")


print(fun_3(fun_1))
print(fun_3(fun_2))
"""

# Inner function

"""
def fun():
    print("You in function:")

    def fun_1():
        print("\tThis a first inner function")

    def fun_2():
        print("\tThis a second inner function")

    fun_1()
    fun_2()


fun()
"""

# Return a function from a function

"""
def fun(n):

    def func_1():
        return "function 1 "

    def func_2():
        return "function 2"

    if n == 1:
        return func_1()
    else:
        return func_2()


a = fun(1)
b = fun(2)

print(a)
print(b)

"""
