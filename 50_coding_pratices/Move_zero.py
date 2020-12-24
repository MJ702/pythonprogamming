def move_zero(arr):
    j = 0
    for i in arr:
        if i != 0:
            arr[j] = i
            j += 1

    for i in range(j, len(arr)):
        arr[i] = 0

    return arr


arr = [0, 1, 0, 3, 12]
result = move_zero(arr)
print(result)
