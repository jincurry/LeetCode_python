# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between
# a letter in pattern and a non-empty word in str.
#
# Examples:
# pattern = "abba", str = "dog cat cat dog" should return true.
# pattern = "abba", str = "dog cat cat fish" should return false.
# pattern = "aaaa", str = "dog cat cat dog" should return false.
# pattern = "abba", str = "dog dog dog dog" should return false.
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters separated by a single space.


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        slist = str.split()

        # here we need to consider the len difference
        # eg: pattern:"aaa" str:"aa aa aa aa"
        if len(pattern) != len(slist):
            return False

        for k, w in zip(pattern, slist):
            print(k, w)

        # just like we do in isomorphic problem.
        return (len(set(pattern)) == len(set(slist)) == len(set(zip(pattern, slist))))


if __name__ == '__main__':
    print(Solution().wordPattern('abba', 'dog cat cat fish'))
    print(Solution().wordPattern('abba', 'dog cat cat dog'))
