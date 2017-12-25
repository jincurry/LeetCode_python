# Determine whether an integer is a palindrome. Do this without extra space.


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        a, result = x, 0

        while a:
            result = result * 10
            result += a % 10
            a = a // 10
        if x == result:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(1234567))
    print(solution.isPalindrome(12321))