import numpy as np
import math


def calculate_matrix_size(length):
    global size
    temp = [i * i for i in range(1, 100)]
    for i in temp:
        if length <= i:
            size = i
            break

    return size


def create_matrix_key(key):
    size = calculate_matrix_size(len(key))
    temp = []
    for i in key:
        temp.append(i)
    for i in range(size - len(key)):
        temp.append('x')

    # Matrix_key = np.array(temp).reshape(int(math.sqrt(size)), int(math.sqrt(size)))

    return temp


def matrix_to_int(Matrix):
    temp = []
    for i in Matrix:
        for j in range(len(i)):

            if i[j].isupper():
                x = ord(i[j]) - 65
                temp.append(x)
            else:
                x = ord(i[j]) - 97
                temp.append(x)
    #   print(temp)
    return temp


def shapping_key(temp):
    Matrix_key = np.array(temp).reshape(int(math.sqrt(size)), int(math.sqrt(size)))
    # print(Matrix_key)
    return Matrix_key


def shapping_plaintext(temp):
    matrix_plaintext = np.array(temp).reshape(-1, int(math.sqrt(size))).T
    # print(matrix_plaintext)
    return matrix_plaintext


def create_matrix_plaintext(plaintext):
    plaintext = plaintext.replace(" ", '')
    plain_text_list = list(plaintext)
    while len(plain_text_list) % math.sqrt(size) != 0:
        plain_text_list.append('x')

    #   print(plain_text_list)
    return plain_text_list


def int_to_char(mul_text):
    temp = []
    for i in mul_text:
        for j in range(len(i)):
            x = chr(i[j] % 26 + 65)
            temp.append(x)
    #   print(temp)
    return temp


def control():
    Matrix = create_matrix_key(str(input("Enter your key: ")))
    matrix_unshaped_key = matrix_to_int(Matrix)
    shapped_key = shapping_key(matrix_unshaped_key)

    matrix_plaintext = create_matrix_plaintext(str(input("Enter your plaintext: ")))
    matrix_unshaped_plaintext = matrix_to_int(matrix_plaintext)
    shapped_plaintext = shapping_plaintext(matrix_unshaped_plaintext)

    mul_text = shapped_key.dot(shapped_plaintext)
    result = int_to_char(mul_text)
    print(result)


control()
