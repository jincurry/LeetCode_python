# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1],[1,1]]
        j = 0
        while j < numRows - 2:
            my_list = [1]
            i = 0
            while i <= len(result[-1]) - 2:
                my_list.append(result[-1][i] + result[-1][i + 1])
                i += 1
            my_list.append(1)
            result.append(my_list)
            j += 1
        return result[:numRows]


if __name__ == "__main__":
    solution = Solution()
    for i in range(1, 10):
        print(solution.generate(i))