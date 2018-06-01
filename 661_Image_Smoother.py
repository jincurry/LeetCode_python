# Given a 2D integer matrix M representing the gray scale of an image, you need to
# design a smoother to make the gray scale of each cell becomes the average gray
# scale (rounding down) of all the 8 surrounding cells and itself. If a cell has
# less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
from math import floor


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M or not M[0]:
            return []
        res = [[[0] for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                neighbors = [M[i + r][j + c] for r in [-1, 0, 1] for c in [-1, 0, 1] if
                             (0 <= i + r < len(M) and 0 <= j + c < len(M[0]))]
                res[i][j] = floor(sum(neighbors) / len(neighbors))
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(solution.imageSmoother([[1]]))

