array = [3, 0, 1]


def missingNumber(array):
    array.sort()
    current_sum = sum(array)
    n = len(array)
    indented = n*(n+1) / 2

    return int(indented - current_sum)


result = missingNumber(array)
print("Missing number is : ", result)
