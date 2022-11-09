#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#


# @lc code=start
class Solution:

    def floodFill(self, image: list[list[int]], sr: int, sc: int,
                  color: int) -> list[list[int]]:
        start = image[sr][sc]
        if start == color:
            return image

        def fill(sr: int, sc: int, color: int) -> list[list[int]]:
            image[sr][sc] = color
            for r, c in [[sr + 1, sc], [sr, sc + 1], [sr - 1, sc],
                         [sr, sc - 1]]:
                try:
                    if min(r, c) < 0:
                        raise IndexError
                    if image[r][c] == start:
                        fill(r, c, color)
                except IndexError:
                    pass

        fill(sr, sc, color)
        return image


# @lc code=end7
print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
