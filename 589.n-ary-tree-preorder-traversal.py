#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#


# Definition for a Node.
class Node:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# @lc code=start


def dfs(node: 'Node', l: list[int]):
    if not node:
        return
    l.append(node.val)
    if node.children:
        for c in node.children:
            dfs(c, l)


class Solution:

    def preorder(self, root: 'Node') -> list[int]:
        l = []
        dfs(root, l)
        return l


# @lc code=end
