# We define the Perfect Number is a positive integer that is equal to the sum of all its
# positive divisors except itself.
#
# Now, given an integer n, write a function that returns true when it is a perfect number
#  and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
import math


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 4:
            return False
        result = []
        for x in range(2, int(math.sqrt(num) + 1)):
            if num % x == 0:
                result.append(x)
                result.append(num // x)
        result.append(1)
        return num == sum(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPerfectNumber(28))
    print(solution.checkPerfectNumber(2))
    print(solution.checkPerfectNumber(0))
    print(solution.checkPerfectNumber(1))
    print(solution.checkPerfectNumber(6))

