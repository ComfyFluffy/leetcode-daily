#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#


# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 4


# @lc code=start


def search(start: int, end: int) -> int:
    if start == end:
        return start
    mid = (start + end) // 2
    if isBadVersion(mid):
        return search(start, mid)
    else:
        return search(mid + 1, end)


class Solution:

    def firstBadVersion(self, n: int) -> int:
        return search(1, n)


# @lc code=end
print(Solution().firstBadVersion(5))
