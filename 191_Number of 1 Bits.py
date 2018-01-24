# Write a function that takes an unsigned integer and returns the number of ’1' bits it has
# (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation
# 00000000000000000000000000001011, so the function should return 3.


class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result += n & 1
            n >>= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(8))