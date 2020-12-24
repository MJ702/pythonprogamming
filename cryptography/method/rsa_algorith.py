def find_d(e, fey):
    check_find = True
    i = 0
    while check_find:
        i = i + 1
        if (i * e) % fey == 1:
            return i


def find_cipher_text(e, n, plain_text):
    return (plain_text ** e) % n


def find_plain_text(d, n, answer):
    return (answer ** d) % n


def find_e(factor, fey, p, q):
    possibility = [x for x in range(1, fey + 1)]
    for i in factor:
        if i in possibility:
            possibility.remove(i)

    nonprimes = [j for i in range(2, 8) for j in range(i * 2, 100, i)]
    primes = [x for x in range(2, 100) if x not in nonprimes]

    for i in possibility:
        if i != p and i != q and i in primes:
            return i


def find_factor(fey):
    temp = list()
    for i in range(1, fey + 1):
        if fey % i == 0:
            temp.append(i)

    return temp


def find_fey(p, q):
    return (p - 1) * (q - 1)


def find_n(p, q):
    return p * q


def control():
    p = int(input("Enter your p: "))
    q = int(input("Enter your q: "))
    plain_text = int(input("Enter your plaintext number: "))
    # find n (first step) P * q
    n = find_n(p, q)
    # print("n=", n)
    # find fye (second step) p-1*q-1

    fey = find_fey(p, q)
    # print("fey=", fey)

    # find fye factor
    factor = find_factor(fey)
    # print('factor=', factor)

    # find e
    e = find_e(factor, fey, p, q)
    # print("e= ", e)

    # find d
    d = find_d(e, fey)
    # print("d=", d)
    # find cipher text
    answer = find_cipher_text(e, n, plain_text)
    print(answer)

    plain_text = find_plain_text(d, n, answer)
    print(plain_text)


control()
