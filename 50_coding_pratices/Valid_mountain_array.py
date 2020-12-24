from typing import List


class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        if len(a) < 3:
            return False

        i = 1
        while i < len(a) and a[i] > a[i - 1]:
            i += 1

        if i == 1 or i == len(a):
            return False

        while i < len(a) and a[i] < a[i - 1]:
            i += 1

        return i == len(a)


s = Solution()
answer = s.validMountainArray([1, 2, 3, 4, 3, 2, 1])
print(answer)
