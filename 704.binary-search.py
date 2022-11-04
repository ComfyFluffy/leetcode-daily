#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start


def binary_search(start: int, end: int, nums: list[int], target: int) -> int:
    if end - start == 1:
        return start if nums[start] == target else -1
    mid = (start + end) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search(mid, end, nums, target)
    return binary_search(start, mid, nums, target)


class Solution:

    def search(self, nums: list[int], target: int) -> int:
        return binary_search(0, len(nums), nums, target)


# @lc code=end
print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
