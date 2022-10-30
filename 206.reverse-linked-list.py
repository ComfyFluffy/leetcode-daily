#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
from typing import Optional


class Solution:

    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
    #     slow = head
    #     fast: ListNode = head.next
    #     while fast:
    #         first = slow
    #         second = fast
    #         slow = fast
    #         fast = fast.next
    #         second.next = first
    #     head.next = None
    #     return slow

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


# @lc code=end

Solution().reverseList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
