# Given an integer n, return the number of trailing zeroes in n!.


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            result += n//5
            n //= 5
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(100))