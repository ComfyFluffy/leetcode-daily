#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start


def verify(prefix: str, strs: list[str]) -> bool:
    for s in strs:
        if not s.startswith(prefix):
            return False
    return True


class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = sorted(strs, key=lambda x: len(x))[0]
        prefix = ''
        for i in range(1, len(shortest) + 1):
            current_prefix = shortest[:i]
            if not verify(current_prefix, strs):
                return prefix
            prefix = current_prefix
        return prefix


Solution().longestCommonPrefix(['x'])

# @lc code=end
