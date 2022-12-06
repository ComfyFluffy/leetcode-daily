#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
from typing import Optional, Generator


class BSTIterator:

    next_val: int = None
    gen: Generator[int, None, None]

    def __init__(self, root: Optional[TreeNode]):

        def gen(root: Optional[TreeNode]) -> Generator[int, None, None]:
            if not root:
                return

            yield from gen(root.left)
            yield root.val
            yield from gen(root.right)

        self.gen = gen(root)
        self.next()

    def next(self) -> int:
        r = self.next_val
        try:
            self.next_val = next(self.gen)
        except StopIteration:
            self.next_val = None
        return r

    def hasNext(self) -> bool:
        return self.next_val is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
