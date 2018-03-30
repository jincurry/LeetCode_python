# Given an integer, write a function to determine if it is a power of two.

# this problem worth attention. let's think 2**3 =8, which binary is 1000, 8-1 = 7, so can see 0111,
# when we use 8 & 7 ,we will get 0. so we know 8 is power of 2.

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n & (n-1) == 0


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(8))
    print(Solution().isPowerOfTwo(7))
    print(Solution().isPowerOfTwo(27))
    print(Solution().isPowerOfTwo(1024))