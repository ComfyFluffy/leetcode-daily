#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
from typing import Generator


class Solution:

    def isHappy(self, n: int) -> bool:

        def digits(n: int) -> Generator[int, None, None]:
            while n > 0:
                yield n % 10
                n //= 10

        s = set()
        while n != 1 and not n in s:
            s.add(n)
            n = sum(d**2 for d in digits(n))
        return n == 1


# @lc code=end
print(Solution().isHappy(2))
print(Solution().isHappy(19))
