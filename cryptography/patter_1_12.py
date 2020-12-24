raw = int(input("Enter your raw: "))

for i in range(1, raw+1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')
