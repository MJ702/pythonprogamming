from typing import List


def getLeftPosition(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            if mid == 0 or nums[mid - 1] != target:
                return mid
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def getRightPosition(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if nums[mid] == target:
            if mid == len(nums) - 1 or nums[mid + 1] != target:
                return mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def searchRange(nums: List[int], target: int) -> List[int]:
    left = getLeftPosition(nums, target)
    right = getRightPosition(nums, target)

    return [left, right]


answer = searchRange([10, 11, 11, 11, 14, 15], 11)
print(answer)
