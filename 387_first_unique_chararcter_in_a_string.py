# Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.
import collections


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        i = 0
        string = list(s)
        while i < len(s):
            if counter[string[i]] == 1:
                return i
            else:
                i += 1
        return -1


if __name__ == '__main__':
    c = Solution().firstUniqChar('')
    print(c)
