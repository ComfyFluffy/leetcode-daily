#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
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

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0

        def calc(root: Optional[TreeNode], sums: list[int] = []):
            nonlocal result

            if not root:
                return

            new_sums = []
            for s in sums + [0]:
                new = s + root.val
                if new == targetSum:
                    result += 1
                new_sums.append(new)

            calc(root.left, new_sums)
            calc(root.right, [*new_sums])

        calc(root)
        return result


# @lc code=end
