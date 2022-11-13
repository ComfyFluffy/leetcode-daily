#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import defaultdict


class Solution:

    def findAnagramsTLE(self, s: str, p: str) -> list[int]:
        r = []

        def count(s: str) -> dict[str, int]:
            r = {}
            for x in s:
                try:
                    r[x] += 1
                except KeyError:
                    r[x] = 1
            return r

        l = len(p)
        cp = count(p)
        for i in range(len(s) - l + 1):
            if count(s[i:i + l]) == cp:
                r.append(i)

        return r

    def findAnagrams1(self, s: str, p: str) -> list[int]:
        result = []
        count = defaultdict(lambda: 0)
        if len(p) > len(s):
            return []

        for x in p:
            count[x] += 1

        for i in range(len(p) - 1):
            x = s[i]
            if x in count:
                count[x] -= 1

        for i in range(-1, len(s) - len(p) + 1):
            if i > -1 and s[i] in count:
                count[s[i]] += 1
            if i + len(p) < len(s) and s[i + len(p)] in count:
                count[s[i + len(p)]] -= 1

            if all(v == 0 for v in count.values()):
                result.append(i + 1)

        return result

    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        count = defaultdict(lambda: 0)
        for x in p:
            count[x] += 1

        i = -len(p)
        j = 0

        while j < len(s):
            if i >= 0 and s[i] in count:
                count[s[i]] += 1
            if s[j] in count:
                count[s[j]] -= 1

            i += 1
            j += 1
            if i >= 0 and all(v == 0 for v in count.values()):
                result.append(i)
        return result


# @lc code=end
print(Solution().findAnagrams('beeaaedcbc', 'c'))
print(Solution().findAnagrams('cbaebabacd', 'abc'))
print(Solution().findAnagrams('abab', 'ab'))
