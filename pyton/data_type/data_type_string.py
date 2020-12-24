"""
    String data type in python
        2.String
"""

print("\n")
print("-------------------- String --------------------")
"""
   Here message is variable to store the string values
   string is denoted between single quote('') or double quote ("")
"""
message = "Insane programer ."
message_1 = "insaneprogramer"
message_4 = " Inasane\nprogramer"
print(message)

"""
    In python index number is start with '0' index value
    In message variable 0 position I, 1 position n, 2 position s, .... , 
    Index number consider in space for example 6 position in message is space 
    you try to print(message[6]) out is space   
"""
print(message[6])

"""
    String is immutable data type which means it can not be change like
    message[6] = H this sentence give error
"""

# message[6] = H
# print(message) gives a error

"""
    In string data data type you want customized out ues square bracket
    syntax message[stating_index:End_index]
    
    Ending index not include in print statement 
    staring index is include in print statement
    
    if you give end index number more then sting existing it automatically consider whole sting 
"""
print("\nFunction name [stating_index:End_index] :")
print(message[7:16])

# Whole sting convert into lower case
print("\nFunction name lower :")
print(message.lower())

# Whole sting convert into upper case
print("\nFunction name upper :")
print(message.upper())

# Whole sting convert upper case after space
print("\nFunction name title :")
print(message.title())

# Give a lenght of sting
print("\nFunction name len :")
print("\tThe lenght of string :")
print(len(message))

# Converts the first character to upper case
print("\nFunction name capitalize :")
print(message.capitalize())

# convert string into lower case same as lower function
print("\nFunction name caseflod :")
print(message.casefold())

# Return a center string in bracket ( put number >len of string)
print("\nFunction name center :")
print("\t " + message.center(17))

# Return the number of times a specified in string
print("\nFunction name count :")
print(message.count("a"))

# Return an encoded version of string
print("\nFunction name encode :")
print(message.encode())

# Return the true if string endswith specified values
print("\nFunction name endswith :")
print(message.endswith("r"))

# Set the tab size of sting if give in string other wish it's not working
message_2 = "I\tn\ts\ta\tn\te"
print("\nFunction name expandtabs :")
print(message_2.expandtabs(1))

"""
    Searches the string for a specified value and returns 
    the position of where it was found it only work with first letter
    once found latter after searching is stop 
"""
print("\nFunction name find :")
print(message.find("r"))

# Formats specified values in a string compulsory in {}
message_3 = "Insane {text}"
print("\nFunction name format :")
print(message_3.format(text="programer"))

# Searches the string for a specified value and returns the position of where it was found same as find
print("\nFunction name index :")
print(message.index("r"))

# Returns True if all characters in the string are numeric not work with space false
print("\nFunction name isalnum :")
print(message.isalnum())

# Returns True if all characters in the string are alphanumeric not work with space give false
print("\nFunction name isalpha :")
print(message_1.isalpha())

# Returns True if all characters in the string are decimal not working with space give false
print("\nFunction name isdecimal :")
print(message_1.isdecimal())

# Returns True if all characters in the string are digits not working with space give false
print("\nFunction name isdigit :")
print(message_1.isdigit())

# Return the true if string endswith specified values not working with space give false
print("\nFunction name isidentifier :")
print(message_1.isidentifier())

# Returns True if all characters in the string are lower case
print('\nFunction name islower :')
print(message_1.islower())

# Returns True if all characters in the string are printable
print('\nFunction name isprintable :')
print(message_1.isprintable())

# Returns True if all characters in the string are whitespaces for example message = "   "
print('\nFunction name isspace :')
print(message_1.isspace())

# Returns True if the string follows the rules of a title
# title rules is string first latter is capital after each space fist latter is capital
print('\nFunction name istitle :')
print(message.istitle())

# Returns True if all characters in the string are upper case
print('\nFunction name isupper :')
print(message_1.isupper())

# joins the elements of an iterable to the end of the string
print('\nFunction name join :')
print(".".join(message))

# Returns a left justified version of the string
print('\nFunction name ljust :')
print(message.ljust(5), ".")

# Returns a tuple where the string is parted into three parts
print('\nFunction name partition :')
print(message.partition('programer'))

# Returns a tuple where the string is parted into three parts
print('\nFunction name replace :')
print(message.replace('programer'"""old value""", 'Programer' """new value"""))

# Searches the string for a specified value and returns the last position of where it was found
print('\nFunction name rfind :')
print(message.rfind('programer'))

# Searches the string for a specified value and returns the last position of where it was found same as find
print('\nFunction name rindex :')
print(message.rindex('programer'))

# Returns a right justified version of the string
print('\nFunction name rindex :')
print(message.rjust(20), 'Hello')

# Returns a right justified version of the string
print('\nFunction name rindex :')
print(message.rjust(20), 'Hello')

# Returns a right justified version of the string
print('\nFunction name rindex :')
print(message.rpartition("programer"))

# Splits the string at the specified separator, and returns a list
print("\nFunction name rsplit :")
print(message.rsplit("programer"))

# Returns a right trim version of the string
print("\nFunction name rstrip :")
print("Hellow i am " + message.rstrip())

# Splits the string at the specified separator, and returns a list
print("\nFunction name split :")
print(message_4.split())

# Returns true if the string starts with the specified value
print("\nFunction name startswith :")
print(message.startswith("Insane"))

# Returns a trimmed version of the string
print("\nFunction name strip :")
print("Hellow i am " + message.strip())

# Swaps cases, lower case becomes upper case and vice versa
print("\nFunction name swapcase :")
print(message.swapcase())

# Fills the string with a specified number of 0 values at the beginning
# In barcket values is must be gather then len of variable
print("\nFunction name zfill :")
# print(len(message))
print(message.zfill(19))
