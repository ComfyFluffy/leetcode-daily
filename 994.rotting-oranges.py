#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
from collections import deque


class Solution:

    def orangesRotting(self, grid: list[list[int]]) -> int:

        def step(i: int, j: int) -> list[tuple[int, int]]:
            r = []
            for ix, jx in [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]]:
                try:
                    if ix < 0 or jx < 0:
                        continue
                    if grid[ix][jx] == 1:
                        grid[ix][jx] = 2
                        r.append((ix, jx))
                except IndexError:
                    pass
            return r

        result = -1

        recently_rotted: list[tuple[int, int]] = []
        has_fresh = False
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 2:
                    recently_rotted.append((i, j))
                elif x == 1:
                    has_fresh = True

        if not recently_rotted:
            return -1 if has_fresh else 0

        while True:
            result += 1
            next_rotted = []
            for i, j in recently_rotted:
                next_rotted.extend(step(i, j))
            if not next_rotted:
                break
            recently_rotted = next_rotted

        for row in grid:
            for x in row:
                if x == 1:
                    return -1

        return result


# @lc code=end

print(Solution().orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(Solution().orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(Solution().orangesRotting([[1]]))
