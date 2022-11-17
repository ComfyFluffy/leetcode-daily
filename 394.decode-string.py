#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#


# @lc code=start
class Solution:

    def decodeString(self, s: str) -> str:
        stack = []
        brackets = {}
        for i, x in enumerate(s):
            if x == '[':
                stack.append(i)
            elif x == ']':
                brackets[stack.pop()] = i

        def decode(start: int, end: int) -> str:
            i = start
            num_buf = ''
            r = ''
            while i < end:
                if s[i] == '[':
                    bracket_end = brackets[i]
                    r += decode(i + 1, bracket_end) * int(num_buf)
                    num_buf = ''
                    i = bracket_end
                elif s[i].isdigit():
                    num_buf += s[i]
                else:
                    r += s[i]
                i += 1
            return r

        return decode(0, len(s))


# @lc code=end
print(Solution().decodeString('3[a]2[bc]'))
print(Solution().decodeString('3[a2[c]]'))
print(Solution().decodeString('2[abc]3[cd]ef'))
