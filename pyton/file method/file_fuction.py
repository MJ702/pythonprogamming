# context manager
with open("test.txt", "r") as f:
    """
    this method is used for perform particular file operation.
    in this file.close statement not required
    """
    f_contents = f.read()
    print(f_contents)

    f_contents = f.read(100)
    # just print a 100 number of world
    print(f_contents)
    for line in f:
        print(line, end='')

# check for context manager file is closed or we open particular file closed or in form of true or false
print("\nThis is check for file is closed or not:")
print(f.closed)

file = open("test.txt", "r")

# print the file name
print("\nThis is file name: ")
print(file.name)

# print the mode of file
print("\nThis is file mode: ")
print(file.mode)
