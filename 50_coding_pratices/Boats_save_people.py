def numRescueBoats(people_weight, boats_limit):
    people_weight.sort()
    left = 0
    right = len(people_weight) - 1
    boats_counter = 0

    while left <= right:
        if left == right:
            boats_counter += 1
            break
        if people_weight[left] + people_weight[right] <= boats_limit:
            left += 1
            right -= 1
            boats_counter += 1

        right -= 1
        boats_counter += 1

    return boats_counter


people_weight = [1, 2, 3, 4]
boats_limit = 4
answer = numRescueBoats(people_weight, boats_limit)
