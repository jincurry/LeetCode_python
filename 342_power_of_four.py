# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num and not (num & 0b11):
            num >>= 2
        return (num == 1)


if __name__ == '__main__':
    print(Solution().isPowerOfFour(345234))
    print(Solution().isPowerOfFour(16))
