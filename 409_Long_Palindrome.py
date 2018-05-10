# Given a string which consists of lowercase or uppercase letters, find the length of the
# longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
import collections


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = 0
        for k, v in collections.Counter(s).items():
            odds += v & 1
        return len(s) - odds + int(odds > 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('abccccdd'))


