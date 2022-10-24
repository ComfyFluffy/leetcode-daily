#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
brackets = {'(': ')', '[': ']', '{': '}'}


class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in brackets:
                stack.append(x)
            else:
                if not len(stack):
                    return False
                start = stack.pop()
                if brackets.get(start) != x:
                    return False
        if len(stack):
            return False
        return True


# @lc code=end
