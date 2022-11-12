#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
import numpy as np


class Solution:

    def minCostClimbingStairs1(self, cost: list[int]) -> int:
        dp = np.zeros((len(cost) + 1, 2), np.int32)
        dp[1] = [cost[0], 0]
        for i in range(2, len(cost) + 1):
            dp[i] = [
                min(dp[i - 1]) + cost[i - 1],
                min(dp[i - 2]) + cost[i - 2]
            ]

        return min(dp[-1])

    def minCostClimbingStairs2(self, cost: list[int]) -> int:
        dp = [0] * len(cost)

        for i, x in enumerate(cost):
            if i < 2:
                dp[i] = x
            else:
                dp[i] = min(dp[i - 1], dp[i - 2]) + x

        print(dp)
        return min(dp[-1], dp[-2])

    def minCostClimbingStairs(self, cost: list[int]) -> int:
        l = len(cost)
        if l <= 2:
            return min(cost)

        first, second = cost[0], cost[1]
        for x in cost[2:]:
            temp = min(first, second) + x
            first = second
            second = temp

        return min(first, second)


# @lc code=end
print(Solution().minCostClimbingStairs([10, 15]))
print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
