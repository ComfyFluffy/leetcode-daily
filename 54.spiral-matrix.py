#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import Generator


class Solution:
    # 🥲
    def spiralOrder0(self, matrix: list[list[int]]) -> list[int]:

        def indexes(rows: int,
                    cols: int) -> Generator[tuple[int, int], None, None]:
            limit = 0
            start_row = rows
            start_col = cols

            while True:
                yielded = False
                for x in range(0 + limit, start_col):
                    yielded = True
                    yield limit, x
                if not yielded: break

                yielded = False
                for x in range(1 + limit, start_row):
                    yielded = True
                    yield x, -1 - limit
                if not yielded: break

                yielded = False
                for x in range(start_col - 2, -1 + limit, -1):
                    yielded = True
                    yield -1 - limit, x
                if not yielded: break

                yielded = False
                for x in range(start_row - 2, 0 + limit, -1):
                    yielded = True
                    yield x, limit
                if not yielded: break

                limit += 1
                start_col -= limit
                start_row -= limit

        return [matrix[i][j] for i, j in indexes(len(matrix), len(matrix[0]))]

    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)
                                                               ][::-1])


# @lc code=end
print(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(Solution().spiralOrder([[2, 5, 8], [4, 0, -1]]))
