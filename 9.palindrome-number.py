#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start

from math import ceil


class Solution:

    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        return x[:int(len(x) / 2)] == list(reversed(x[ceil(len(x) / 2):]))


# @lc code=end
