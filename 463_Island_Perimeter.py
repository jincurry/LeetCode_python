# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water. Grid cells are connected
# horizontally/vertically (not diagonally). The grid is completely
# surrounded by water, and there is exactly one island (i.e., one or more
# connected land cells). The island doesn't have"lakes"(water inside that
# isn't connected to the water around the island). One cell is a square with
# side length 1. The grid is rectangular, width and height don't exceed 100.
# Determine the perimeter of the island.
#
# Example:
#
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# Answer: 16


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # perimeter = 0
        # for line in grid:
        #     perimeter += line.count(1) * 4
        #
        # for line in grid:
        #     for i in range(len(line) - 1):
        #         if line[i] == 1 and line[i + 1] == 1:
        #             perimeter -= 2
        #
        # for i in range(len(grid) - 1):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1 and grid[i+1][j] == 1:
        #             perimeter -= 2
        # return perimeter

        ret = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    ret += 4
                    if j and grid[i][j - 1]:
                        ret -= 2
                    if i and grid[i - 1][j]:
                        ret -= 2
        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
