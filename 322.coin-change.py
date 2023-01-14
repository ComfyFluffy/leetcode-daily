#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from functools import cache


class Solution:

    # Won't work :(
    def coinChange1(self, coins: list[int], amount: int) -> int:
        coins.sort(reverse=True)

        def dfs(current_sum=0, index=0, depth=0) -> int:
            if current_sum == amount:
                return depth
            if index == len(coins):
                return -1

            if current_sum < amount:
                for i in range(index, len(coins)):
                    res = dfs(current_sum + coins[i], i, depth + 1)
                    if res != -1:
                        return res

            return -1

        return dfs()

    def coinChange(self, coins: list[int], amount: int) -> int:

        @cache
        def dfs(amount: int):
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            min_coins = float('inf')
            for c in coins:
                res = dfs(amount - c)
                if res != -1:
                    min_coins = min(min_coins, res + 1)
            if min_coins == float('inf'):
                return -1
            return min_coins

        return dfs(amount)


# @lc code=end
print(Solution().coinChange([1, 2, 5], 12))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))
print(Solution().coinChange([1, 100], 5))
print(Solution().coinChange([186, 419, 83, 408], 6249))
