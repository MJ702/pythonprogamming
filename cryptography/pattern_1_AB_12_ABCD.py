raw = int(input("Enter your raw: "))

for i in range(1, raw + 1):
    if i % 2 != 0:
        for j in range(1, i + 1):
            print(j, end=' ')
        print('')
    else:
        for j in range(65, 65 + i, 2):
            a = chr(j)
            b = chr(j + 1)
            print(a, b, end=' ')
        print('')
