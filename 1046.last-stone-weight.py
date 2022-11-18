#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import bisect


class Solution:

    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            bisect.insort(stones, abs(stones.pop() - stones.pop()))
        return stones[0]


# @lc code=end
print(Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]))
