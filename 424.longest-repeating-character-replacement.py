#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict, OrderedDict


class Solution:

    def characterReplacement1(self, s: str, k: int) -> int:

        def verify(l: int) -> bool:
            count = defaultdict(int)

            for j in range(len(s)):
                i = j - l
                if i >= 0:
                    count[s[i]] -= 1
                count[s[j]] += 1

                if i >= -1 and max(count.values()) + k >= l:
                    return True

            return False

        def search(start: int, end: int) -> int:
            if end - start == 1:
                return start
            mid = (start + end) // 2
            if verify(mid):
                return search(mid, end)
            return search(start, mid)

        return search(0, len(s) + 1)

    # Optimize max_frequency
    def characterReplacement(self, s: str, k: int) -> int:

        def verify(l: int) -> bool:
            count = defaultdict(int)
            max_frequency = 0

            for j in range(len(s)):
                i = j - l
                if i >= 0:
                    count[s[i]] -= 1
                count[s[j]] += 1

                max_frequency = max(max_frequency, count[s[j]])
                if i >= -1 and max_frequency + k >= l:
                    return True

            return False

        def search(start: int, end: int) -> int:
            if end - start == 1:
                return start
            mid = (start + end) // 2
            if verify(mid):
                return search(mid, end)
            return search(start, mid)

        return search(0, len(s) + 1)


# @lc code=end
print(Solution().characterReplacement('AABABBA', 1))
