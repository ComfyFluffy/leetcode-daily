#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0

        for x in nums:
            if x != val:
                nums[index] = x
                index += 1
        return index


# @lc code=end
l = [4, 2, 0, 2, 2, 1, 4, 4, 1, 4, 3, 2]
print(Solution().removeElement(l, 4))
print(l)
