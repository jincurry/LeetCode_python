# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)
# You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
#
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the
# island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)
            return 0

        areas = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(areas) if areas else 0


# 使用栈实现的方法
# row_n = len(grid)
# col_n = len(grid[0])
#
# ans = 0
# for i in range(row_n):
#     for j in range(col_n):
#         if grid[i][j]:
#             area = 0
#             stack = [(i, j)]
#             grid[i][j] = 0
#             while stack:
#                 cur_i, cur_j = stack.pop()
#                 area += 1
#                 if cur_i - 1 >= 0 and grid[cur_i - 1][cur_j]:
#                     stack.append((cur_i - 1, cur_j))
#                     grid[cur_i - 1][cur_j] = 0
#                 if cur_i + 1 < row_n and grid[cur_i + 1][cur_j]:
#                     stack.append((cur_i + 1, cur_j))
#                     grid[cur_i + 1][cur_j] = 0
#                 if cur_j - 1 >= 0 and grid[cur_i][cur_j - 1]:
#                     stack.append((cur_i, cur_j - 1))
#                     grid[cur_i][cur_j - 1] = 0
#                 if cur_j + 1 < col_n and grid[cur_i][cur_j + 1]:
#                     stack.append((cur_i, cur_j + 1))
#                     grid[cur_i][cur_j + 1] = 0
#             ans = max(ans, area)
# return ans

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))