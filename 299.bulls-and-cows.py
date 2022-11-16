#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
from collections import defaultdict


class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        count = defaultdict(int)
        bulls = 0

        for i, x in enumerate(secret):
            if guess[i] != x:
                count[x] += 1
            else:
                bulls += 1

        cows = 0
        for i, x in enumerate(guess):
            if secret[i] != x and count[x] > 0:
                count[x] -= 1
                cows += 1

        return f'{bulls}A{cows}B'


# @lc code=end
print(Solution().getHint('1807', '7810'))
print(Solution().getHint('1123', '0111'))
