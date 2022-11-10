#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:

    def numIslands(self, grid: list[list[str]]) -> int:

        def fill(sr: int, sc: int):
            grid[sr][sc] = '2'
            for r, c in [[sr + 1, sc], [sr, sc + 1], [sr - 1, sc],
                         [sr, sc - 1]]:
                try:
                    if min(r, c) < 0:
                        raise IndexError
                    if grid[r][c] == '1':
                        fill(r, c)
                except IndexError:
                    pass

        count = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == '1':
                    fill(i, j)
                    count += 1
        return count


# @lc code=end
print(Solution().numIslands([["1", "1", "0", "0", "0"],
                             ["1", "1", "0", "0", "0"],
                             ["0", "0", "1", "0", "0"],
                             ["0", "0", "0", "1", "1"]]))
