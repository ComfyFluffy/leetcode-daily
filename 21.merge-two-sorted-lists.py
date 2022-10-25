#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result
        while list1 and list2:
            r = ListNode()
            if list1.val > list2.val:
                r.val = list2.val
                list2 = list2.next
            else:
                r.val = list1.val
                list1 = list1.next
            current.next = r
            current = r

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return result.next


# @lc code=end
