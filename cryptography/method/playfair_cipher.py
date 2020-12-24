import numpy as np

# create for matrix
table = list()

# empty answer
answer = list()


# append remaining latter to table
def table_has_letter():
    latter = 'abcdefghiklmnopqrstuvwxyz'
    for i in latter:
        if i not in table:
            table.append(i)
        else:
            pass
    print("Matrix was create successfully: ")
    # temp = np.array(table).reshape(5, 5)
    # print(temp)


# Create table using key
def create_table(key):
    for i in key:
        if i not in table:
            table.append(i)

    table_has_letter()


# find the pair in which raw or column and according call function
def find_latter(pair, table):
    # Create a matrix of table list because matrix as many method
    Matrix = np.array(table).reshape(5, 5)
    first_element = pair[0]
    second_element = pair[1]
    check_pair = True

    while check_pair:
        for i in range(5):
            # fetch raw
            table_raw = list(Matrix[i])

            # Check pair in same raw
            if (pair[0] in table_raw) and (pair[1] in table_raw):
                table_raw_column(table_raw, first_element, second_element)
                check_pair = False

        while check_pair:
            for i in range(5):
                # Fetch column
                table_column = list(Matrix[:, i])

                # Check pair in same column
                if (pair[0] in table_column) and (pair[1] in table_column):
                    table_raw_column(table_column, first_element, second_element)
                    check_pair = False

            # Check for cross raw and column
            while check_pair:
                for i in range(5):
                    table_raw = list(Matrix[i])
                    if pair[0] in table_raw:
                        for j in range(5):
                            table_column = list(Matrix[:, j])
                            if pair[1] in table_column:
                                cross_check(table_raw, table_column)
                                check_pair = True

                                while check_pair:
                                    for k in range(5):
                                        table_raw = list(Matrix[k])
                                        if pair[1] in table_raw:
                                            for x in range(5):
                                                table_column = list(Matrix[:, x])
                                                if pair[0] in table_column:
                                                    cross_check(table_raw, table_column)
                                                    check_pair = False


# append encrypt text for same raw and column to the answer
def table_raw_column(raw, first_element, second_element):
    j0 = raw.index(first_element)
    j1 = raw.index(second_element)

    answer.append(list(raw[(j0 + 1) % 5]))
    answer.append(list(raw[(j1 + 1) % 5]))


# append encrypt text for cross element
def cross_check(raw, column, ):
    a = list(set(raw).intersection(column))
    answer.append(a)


# accept two number and create a pair and call find_latter function
def encode_pair(a, b):
    if a == b:
        print('ERROR: letters to encode_pair must be distinct')

    else:
        pair = [a, b]
        find_latter(pair, table)


# Fix problem
def fix_problem(plaintext):
    # remove two sequence char
    for i in range(len(plaintext) - 1):
        if plaintext[i] == plaintext[i + 1]:
            plaintext.insert(i + 1, 'x')

    # Check for len it must in even
    if len(plaintext) % 2 != 0:
        if plaintext[len(plaintext) - 1] == 'x':
            plaintext.insert(len(plaintext), 'y')
        else:
            plaintext.insert(len(plaintext), 'x')

    return plaintext


# Clean code or remove white space
def cleanup(plaintext):
    plaintext = list(plaintext.replace(" ", ""))
    plaintext_1 = fix_problem(plaintext)
    return plaintext_1


# encode plaintext and print answer
def encode(plaintext_1):
    encrypt_text = ''
    for i in range(0, len(plaintext_1), 2):
        encode_pair(plaintext_1[i], plaintext_1[i + 1])

    for i in answer:
        encrypt_text += str(i)

    print("Encrypt text: " + encrypt_text)


# playfair control
def control():
    print('#########################################################')
    create_table(str(input("Enter your key: ")))
    print('#########################################################')
    plaintext_1 = cleanup(str(input("Enter your plaintext: ")))
    print('#########################################################')
    encode(plaintext_1)


control()
