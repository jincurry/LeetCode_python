# Given a matrix A, return the transpose of A.

# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column
# indices of the matrix.


# Example 1:

# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
# Example 2:

# Input: [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]


class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        n, m = len(A), len(A[0])
        for i in range(m):
            res = []
            for j in range(n):
                res.append(A[j][i])
            result.append(res)
        return result

    def transpose2(self, A):
        return [list(i) for i in list(zip(*A))]


if __name__ == '__main__':
    solution = Solution()
    result = solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(result)
    print(solution.transpose2([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
