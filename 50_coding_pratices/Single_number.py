def singleNumber(array):
    return 2 * sum(set(array)) - sum(array)


array = [1, 1, 2, 2, 3]
result = singleNumber(array)
print(result)
