#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
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
    height_map = {}

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if root in self.height_map:
            return self.height_map[root]

        h = max(self.height(root.left), self.height(root.right)) + 1
        self.height_map[root] = h

        return h

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(
            root.right
        ) and abs(self.height(root.left) - self.height(root.right)) <= 1


class Solution:

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if -1 in [left, right] or abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0


# @lc code=end
print(Solution().isBalanced(TreeNode(1, right=TreeNode(2, right=TreeNode(3)))))
