#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
from typing import Generator


class Solution:

    def backspaceCompare1(self, s: str, t: str) -> bool:

        def typed(s: str) -> list[str]:
            stack = []
            for x in s:
                if x == '#':
                    stack.pop()
                else:
                    stack.append(x)
            return stack

        return typed(s) == typed(t)

    def backspaceCompare(self, s: str, t: str) -> bool:

        def valid_str(s: str) -> Generator[str, None, None]:
            rs = reversed(s)
            backspaces = 0

            for x in rs:
                if x == '#':
                    backspaces += 1
                elif backspaces == 0:
                    yield x
                else:
                    backspaces -= 1

        try:
            return all(
                x == y
                for x, y in zip(valid_str(s), valid_str(t), strict=True))
        except ValueError:
            return False


# @lc code=end
print(Solution().backspaceCompare('bxj##tw', 'bxj###tw'))
print(Solution().backspaceCompare('ab#c', 'ad#c'))
print(Solution().backspaceCompare('a#c', 'b'))
