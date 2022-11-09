#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#


# Definition for a binary tree node.
class TreeNode:
    val: int
    left: 'TreeNode'
    right: 'TreeNode'

    def __init__(self,
                 x: int,
                 left: 'TreeNode' = None,
                 right: 'TreeNode' = None):
        self.val = x
        self.left = left
        self.right = right


# @lc code=start


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)

        if (left_res and right_res) or (root in [p, q]):
            return root
        else:
            return left_res or right_res


# @lc code=end
T = TreeNode
p = T(8)
q = T(1, T(0), p)
print(Solution().lowestCommonAncestor(T(3, T(5, T(6), T(2)), q), p, q).val)
