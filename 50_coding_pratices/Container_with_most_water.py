def ContainerWithMostWater(array):
    left = 0
    right = len(array) - 1
    maxArea = 0
    while left < right:
        maxArea = max(maxArea,  min(array[left], array[right])*(right - left))
        if array[left] < array[right]:
            left += 1
        else:
            right -= 1
    return maxArea


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
answer = ContainerWithMostWater(height)
print(answer)
