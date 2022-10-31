#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# Definition for singly-linked list.


class ListNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# @lc code=start
from typing import Optional


def detect(s: set[ListNode], node: ListNode):
    if not node or node in s:
        return node
    s.add(node)
    return detect(s, node.next)


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return detect(set(), head)


# @lc code=end
cycle_start = ListNode(2)
cycle_end = ListNode(-4, cycle_start)
cycle_start.next = ListNode(0, cycle_end)
head = ListNode(3, cycle_start)
Solution().detectCycle(head)
