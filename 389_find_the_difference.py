# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one
#  more letter at a random position.
#
# Find the letter that was added in t.
#
# Example:
#
# Input:
# s = "abcd"
# t = "abcde"
#
# Output:
# e
#
# Explanation:
# 'e' is the letter that was added.
import collections


class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # first one by myself

        # a = collections.Counter(s)
        # b = collections.Counter(t)
        # d  = b - a
        # for k, _ in d.items():
        #     return k
        return list(collections.Counter(t) - collections.Counter(s))[0]

if __name__ == '__main__':
    print(Solution().findTheDifference('abcd', 'acdeb'))
