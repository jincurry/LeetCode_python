# In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different
#     size but keep its original data.
#
# You're given a matrix represented by a two-dimensional array, and two positive integers r ' \
#    'and c representing the row number and column number of the wanted reshaped matrix, ' \
#    'respectively.
#
# The reshaped matrix need to be filled with all the elements of the original matrix in
# the same row-traversing order as they were.
#
# If the 'reshape' operation with given parameters is possible and legal, output the new
# reshaped matrix; Otherwise, output the original matrix.

# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# Output:
# [[1,2,3,4]]
#
# Input:
# nums =
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# Output:
# [[1,2],
#  [3,4]]


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        i = len(nums)
        j = len(nums[0])
        if i * j != r * c:
            return nums
        else:
            result = []
            elements = []
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    elements.append(nums[i][j])
            for i in range(r):
                result.append(elements[i * c:(i+1) * c])
            return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.matrixReshape([[1, 2], [3, 4]], 1, 4))
    print(solution.matrixReshape([[1, 2], [3, 4]], 2, 2))
    print(solution.matrixReshape([[1, 2], [3, 4]], 2, 4))
