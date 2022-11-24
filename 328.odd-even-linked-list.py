#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_list():

        return


# @lc code=start
from typing import Optional


class Solution:

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = 1
        odd_head = odd_tail = ListNode()
        even_head = even_tail = ListNode()

        while head:
            if i % 2 == 0:
                even_tail.next = head
                even_tail = even_tail.next
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
            i += 1
            head = head.next
        even_tail.next = None
        odd_tail.next = even_head.next

        return odd_head.next


# @lc code=end
Solution().oddEvenList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
