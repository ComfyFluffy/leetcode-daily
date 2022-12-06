#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:

    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums, target, left, right):
        if left > right:
            return -1

        mid = left + (right - left + 1) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                return self.binary_search(nums, target, left, mid - 1)
            else:
                return self.binary_search(nums, target, mid + 1, right)
        else:
            if nums[mid] < target <= nums[right]:
                return self.binary_search(nums, target, mid + 1, right)
            else:
                return self.binary_search(nums, target, left, mid - 1)


# @lc code=end
Solution().search([4, 5, 6, 7, 0, 1, 2], 1)
