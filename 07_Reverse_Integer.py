# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# Assume we are dealing with an environment which could only hold integers within the
# 32-bit signed integer range. For the purpose of this problem, assume that your function
# returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        string = str(x)
        string = string[-1::-1]
        for i in range(len(string)):
            if string[i] != "0":
                break
        string = string[i:]
        a = int(string)
        return a if a <= 0x7fffffff else 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(-123))
    print(solution.reverse(23423))
    print(solution.reverse(123456789))