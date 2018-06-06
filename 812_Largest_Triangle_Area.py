# You have a list of points in the plane. Return the area of the largest triangle that can be
# formed by any 3 of the points.
#
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation:
# The five points are show in the figure below. The red triangle is the largest.
import itertools


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
            for i, j, k in itertools.combinations(points, 3))


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))