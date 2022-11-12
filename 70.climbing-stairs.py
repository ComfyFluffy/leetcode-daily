#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    dp = [0] * 46

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        if self.dp[n] != 0:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]


# @lc code=end
