#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    left: 'TreeNode'
    right: 'TreeNode'

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
def bfs(node: Optional[TreeNode], l: list[list[int]], depth=0):
    if not node:
        return
    try:
        l[depth].append(node.val)
    except IndexError:
        l.append([node.val])
    for n in filter(None, [node.left, node.right]):
        bfs(n, l, depth + 1)


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        l = []
        bfs(
            root,
            l,
        )
        return l


# @lc code=end
