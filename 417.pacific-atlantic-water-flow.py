#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#


# @lc code=start
class StopSearchException(Exception):
    pass


class Solution:

    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        result = []

        def can_flow_to_both(row: int, col: int) -> bool:
            pacific = False
            atlantic = False
            visited = set()

            def dfs(row: int, col: int):
                nonlocal pacific, atlantic
                if row - 1 < 0 or col - 1 < 0:
                    pacific = True
                if row + 1 == rows or col + 1 == cols:
                    atlantic = True
                if pacific and atlantic:
                    raise StopSearchException
                for x, y in [[row - 1, col], [row, col - 1], [row + 1, col],
                             [row, col + 1]]:
                    if 0 <= x < rows and 0 <= y < cols and heights[x][
                            y] <= heights[row][col] and not (x, y) in visited:
                        visited.add((x, y))
                        dfs(x, y)

            try:
                dfs(row, col)
            except StopSearchException:
                pass

            return pacific and atlantic

        for row in range(rows):
            for col in range(cols):
                if can_flow_to_both(row, col):
                    result.append([row, col])

        return result


# @lc code=end
print(Solution().pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4],
                                  [2, 4, 5, 3, 1], [6, 7, 1, 4, 5],
                                  [5, 1, 1, 2, 4]]))
