def convert_to_int(key):
    key = key.replace(' ', '')
    temp = list()
    key = key.upper()
    for i in key:
        number = ord(i) - 65
        temp.append(number)
    return temp


def encrypt(key_int, plaintext_int):
    answer = list()

    for i in range(len(plaintext_int) - len(key_int)):
        key_int.append(key_int[i])

    for i in range(len(plaintext_int)):
        answer.append(key_int[i] + plaintext_int[i] % 26)
        answer.append(key_int[i] + plaintext_int[i] % 26)

    return answer


def convert_to_char(answer):
    temp = list()
    for i in answer:
        charter = chr((i % 26) + 65)
        temp.append(charter)

    print(temp)


def control():
    key_int = convert_to_int(str(input("Enter your key: ")))
    plaintext_int = convert_to_int(str(input("Enter your plaintext: ")))
    answer = encrypt(key_int, plaintext_int)
    convert_to_char(answer)


control()