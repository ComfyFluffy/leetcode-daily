#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
from typing import Optional


class Solution:

    def removeNthFromEnd1(self, head: Optional[ListNode],
                          n: int) -> Optional[ListNode]:
        l: list[ListNode] = []
        p = head
        while p:
            l.append(p)
            p = p.next

        if len(l) == 1:
            return None

        if n + 1 <= len(l):
            l[-n - 1].next = l[-n + 1] if -n + 1 != 0 else None
        else:
            head = l[1]
        return head

    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        slow = fast = head

        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next

        while fast.next:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next
        return head


# @lc code=end
