#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#


# @lc code=start
class Solution:

    def findBall(self, grid: list[list[int]]) -> list[int]:
        rows = len(grid)
        cols = len(grid[0])

        def calc(col: int) -> int:
            x = col
            y = 0

            while y < rows:
                current = grid[y][x]
                if x + current in [-1, cols
                                   ] or grid[y][x + current] == -current:
                    return -1
                x += current
                y += 1
            return x

        return list(map(calc, range(cols)))


# @lc code=end
print(Solution().findBall([[1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1],
                           [1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1]]))

print(Solution().findBall([[1, 1, 1, -1, -1], [1, 1, 1, -1, -1],
                           [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1],
                           [-1, -1, -1, -1, -1]]))
print(Solution().findBall([[-1]]))
