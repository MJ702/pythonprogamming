import random

latter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
keyword = []
plaintext = str(input("Enter your plaintext: "))


def generate_key():
    check_key = True
    while check_key:
        random_number = random.randint(0, 25)
        temp = latter[random_number]
        if temp not in keyword:
            keyword.append(temp)

        elif len(keyword) == 26:
            check_key = False


def encrypt(i):
    if i in plaintext:
        temp = latter.index(i)
        return keyword[temp]


def control():
    answer = ''
    generate_key()
    for i in plaintext:
        answer += encrypt(i)

    print(answer)
    print(latter)
    print(keyword)


control()
