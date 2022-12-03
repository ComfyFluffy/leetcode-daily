#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        flattened = [x for row in matrix for x in row]

        start, end = 0, len(flattened)
        while end - start > 1:
            mid = (start + end) // 2
            if flattened[mid] > target:
                end = mid
            elif flattened[mid] == target:
                return True
            else:
                start = mid + 1
        return start in range(0, len(flattened)) and flattened[start] == target


# @lc code=end
print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(Solution().searchMatrix([[1, 1]], 13))
