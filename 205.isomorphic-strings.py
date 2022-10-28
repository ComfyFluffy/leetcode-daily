#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start


def standarize(s: str):
    d = {}
    l = []
    last_id = 0
    for x in s:
        id = d.get(x)
        if id is not None:
            l.append(id)
        else:
            l.append(last_id)
            d[x] = last_id
            last_id += 1
    return l


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        return standarize(s) == standarize(t)


# @lc code=end
Solution().isIsomorphic('foo', 'bar')
