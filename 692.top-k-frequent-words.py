#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

# @lc code=start
from collections import Counter
from heapq import nlargest, nsmallest


class Solution:

    # def topKFrequent(self, words: list[str], k: int) -> list[str]:
    # count: dict[str, int] = defaultdict(int)

    # for w in words:
    #     count[w] += 1
    # count_r = defaultdict(list)
    # for word, c in count.items():
    #     count_r[c].append(word)

    # r = []
    # for x in (item for v in (v for _, v in sorted(
    #         count_r.items(), key=lambda m: m[0], reverse=True))
    #           for item in v):
    #     if len(r) < k:
    #         r.append(x)
    # return r
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        return [
            word for _, word in nsmallest(k, (
                (-count, word) for word, count in Counter(words).items()))
        ]


# @lc code=end
print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],
                              2))
print(Solution().topKFrequent(
    ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
    4))
