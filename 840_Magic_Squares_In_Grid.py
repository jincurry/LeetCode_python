# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row,
#  column, and both diagonals all have the same sum.
#
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?
# (Each subgrid is contiguous).
# Example 1:
#
# Input: [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]
# Output: 1
# Explanation:
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276
#
# while this one is not:
# 384
# 519
# 762
#
# In total, there is only one magic square inside the given grid.


class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        def checkit(i, j):

            if 0 < i < rows - 1 and 0 < j < cols - 1:
                    return (sorted(
                        [grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1], grid[i][j - 1], grid[i][j],
                         grid[i][j + 1],
                         grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]]) == list(range(1, 10)) and
                            (grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] == grid[i][j - 1] + grid[i][j] +
                             grid[i][j + 1] ==
                             grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1] == grid[i - 1][j - 1] + grid[i][
                                 j - 1] + grid[i + 1][j - 1] ==
                             grid[i - 1][j] + grid[i][j] + grid[i + 1][j] == grid[i - 1][j + 1] + grid[i][j + 1] +
                             grid[i + 1][j + 1] ==
                             grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1] == grid[i - 1][j + 1] + grid[i][j] +
                             grid[i + 1][j - 1]
                             ))

        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 5:
                    if checkit(i, j):
                        result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))

