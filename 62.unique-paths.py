#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
import numpy as np


class Solution:

    def uniquePaths1(self, m: int, n: int) -> int:
        dp = np.ones((m, n), np.int32)
        for i in range(m):
            for j in range(n):
                if i or j:
                    up = dp[i - 1][j] if i > 0 else 0
                    left = dp[i][j - 1] if j > 0 else 0
                    dp[i][j] = up + left
        return dp[-1][-1]

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                up = dp[j]
                left = dp[j - 1] if j > 0 else 0
                dp[j] = up + left
        return dp[-1]


# @lc code=end
print(Solution().uniquePaths(10, 10))
