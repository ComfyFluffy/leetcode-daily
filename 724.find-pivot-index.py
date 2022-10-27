#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#


# @lc code=start
class Solution:

    def pivotIndex(self, nums: list[int]) -> int:
        # nums.sort(reverse=True)
        sumLeft = 0
        sumRight = sum(nums)
        for i, x in enumerate(nums):
            if i - 1 >= 0:
                sumLeft += nums[i - 1]
            sumRight -= x
            if sumLeft == sumRight:
                return i

        return -1


# @lc code=end
Solution().pivotIndex([1, 7, 3, 6, 5, 6])
