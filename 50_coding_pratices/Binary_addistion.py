def addBinary(a, b):
    carry = 0
    result = []
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:

        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1
        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))
        carry = total // 2

    return "".join(reversed(result))


a = '00110'
b = '00111'
answer = addBinary(a, b)
print(answer)
