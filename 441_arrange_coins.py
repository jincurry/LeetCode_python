# You have a total of n coins that you want to form in a staircase shape,
#  where every k-th row must have exactly k coins.
#
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.
import math


class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 0:
        #     return 0
        # level = 1
        # while n - level > level:
        #     n -= level
        #     level += 1
        # return level

        # solution2: 解方程组 x层能放置的总数是(x^2+x)/2
        # 则 计算(x^2+x)/2 = n的解
        return int((math.sqrt(1 + 8*n) - 1) / 2)


if __name__ == '__main__':
    print(Solution().arrangeCoins(100))
