# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s
# and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".


import collections


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # //下面的方法能够计算出结果，但是在leetcode上超时了

        # if not s or not p or len(s) < len(p):
        #     return []
        #
        # need = collections.Counter(p)
        # left, offset, missing = 0, len(p), len(p)
        # result = []
        #
        # while left <= len(s) - len(p):
        #     newString = s[left: left+offset]
        #     match = collections.Counter(newString)
        #     if match == need:
        #         result.append(left)
        #     left += 1
        # return result
        a = [0] * 26
        b = [0] * 26
        res = []
        if len(s) < len(p):
            return res
        for i in range(0, len(p)):
            a[ord(p[i]) - ord('a')] += 1
            b[ord(s[i]) - ord('a')] += 1
        if a == b:
            res.append(0)
        for j in range(1, len(s)):
            if j + len(p) > len(s):
                break
            b[ord(s[j - 1]) - ord('a')] -= 1
            b[ord(s[j + len(p) - 1]) - ord('a')] += 1
            if a == b:
                res.append(j)
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.findAnagrams('cbaebabacd', 'abc'))
    print(solution.findAnagrams('abab', 'ab'))




