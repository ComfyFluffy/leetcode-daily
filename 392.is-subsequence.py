#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for x in s:
            try:
                while t[i] != x:
                    i += 1
                else:
                    i += 1
            except IndexError:
                return False
        return True


# @lc code=end
Solution().isSubsequence('aaaaaa', 'bbaaaa')
