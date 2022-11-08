#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    left: Optional['TreeNode']
    right: Optional['TreeNode']

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start

from math import inf


def verify(n: Optional[TreeNode], low: int = -inf, high: int = inf) -> bool:
    if not n:
        return True

    if n.val <= low or n.val >= high:
        return False

    return verify(n.right, n.val, high) and verify(n.left, low, n.val)


class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return verify(root)


class Solution2:

    def isValidBST(self, root: TreeNode) -> bool:

        prev = -inf

        def inorder(root):
            nonlocal prev
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= prev:
                return False
            prev = root.val
            return inorder(root.right)

        return inorder(root)


# @lc code=end
# print(Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3))))
print(Solution2().isValidBST(
    TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))))
