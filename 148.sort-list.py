#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
from typing import Optional


class Solution:

    def merge(self, l1: ListNode, l2: ListNode):
        p = l = ListNode()

        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next

        if l1 is not None:
            p.next = l1
        if l2 is not None:
            p.next = l2

        return l.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        slow = fast = head
        slow_prev = None

        while fast is not None and fast.next is not None:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next

        slow_prev.next = None
        return self.merge(self.sortList(head), self.sortList(slow))


# @lc code=end
