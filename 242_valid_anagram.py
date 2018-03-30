# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.
import collections


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        col = collections.defaultdict(int)
        for c in s:
            col[c] += 1
        for c in t:
            col[c] -= 1
            if col[c] < 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isAnagram('anagram', 'nagaram'))
