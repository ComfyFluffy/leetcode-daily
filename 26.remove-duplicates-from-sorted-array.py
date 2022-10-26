#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        replace = 0
        current = None
        for x in nums:
            if current != x:
                current = x
                nums[replace] = x
                replace += 1
        return replace


# @lc code=end
# Solution().removeDuplicates([1, 2, 3, 4])
Solution().removeDuplicates([1, 1, 3, 3, 3, 4])
