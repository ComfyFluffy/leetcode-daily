#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        for i in range(len(s)):
            substring = set()
            for x in s[i:]:
                if not x in substring:
                    substring.add(x)
                else:
                    break
            length = max(len(substring), length)
        return length


# @lc code=end
