#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#


# @lc code=start
class Solution:

    def runningSum(self, nums: list[int]) -> list[int]:
        r = []
        s = 0
        for x in nums:
            s += x
            r.append(s)
        return r


# @lc code=end
