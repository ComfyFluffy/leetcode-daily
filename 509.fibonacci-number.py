#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# @lc code=start
class Solution:

    def fib_recursion(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)

    dp = [0] * 31

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if self.dp[n] != 0:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


# @lc code=end
print(Solution().fib(3))
