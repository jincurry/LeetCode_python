# Given a non-negative integer c, your task is to decide whether there're two integers a
# and b such that a2 + b2 = c.
#
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False
import math


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # this method exceed time
        # result = []
        # for i in range(1, int(math.sqrt(c) + 1)):
        #     result.append(i ** 2)
        # for i in range(int(math.sqrt(c) + 1)):
        #     remain = c - i * i
        #     if remain in result:
        #         return True
        # return False
        d = int(math.sqrt(c))
        for i in range(d + 1):
            if math.sqrt(c - math.pow(i, 2)).is_integer():
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    for i in range(15):
        print(solution.judgeSquareSum(i))