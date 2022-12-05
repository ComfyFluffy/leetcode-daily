#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def traverse(root: TreeNode):
            nonlocal count
            if root is None:
                return
            r = traverse(root.left)
            if r is not None:
                return r
            count += 1
            if count == k:
                return root.val
            r = traverse(root.right)
            if r is not None:
                return r

        return traverse(root)


# @lc code=end
print(Solution().kthSmallest(
    TreeNode(3, TreeNode(1, right=TreeNode(2)), TreeNode(4)), 4))
print(Solution().kthSmallest(
    TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
             TreeNode(6)), 7))
