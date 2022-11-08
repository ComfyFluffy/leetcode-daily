#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#


# Definition for a binary tree node.
class TreeNode:
    val: int
    left: 'TreeNode'
    right: 'TreeNode'

    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        small, large = (p.val, q.val) if p.val < q.val else (q.val, p.val)

        while root:
            if root.val < small:
                root = root.right
            elif root.val > large:
                root = root.left
            else:
                return root


# @lc code=end
