#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start

from typing import Optional


class Solution:

    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:

        def create_tree(left: int, right: int) -> TreeNode:
            if left == right:
                return None
            if right - left == 1:
                return TreeNode(nums[left])
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = create_tree(left, mid)
            root.right = create_tree(mid + 1, right)
            return root

        root = create_tree(0, len(nums))
        return root


# @lc code=end
Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
