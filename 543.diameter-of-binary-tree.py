#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def depth(root: Optional[TreeNode]):
            nonlocal max_diameter
            if not root:
                return 0
            depths = list(map(depth, [root.left, root.right]))
            max_diameter = max(max_diameter, sum(depths))
            return max(depths) + 1

        depth(root)

        return max_diameter


# @lc code=end
print(Solution().diameterOfBinaryTree(
    TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
