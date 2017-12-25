# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        for i in range(len(s)):
            if i > 0 and mapping[s[i]] > mapping[s[i-1]]:
                sum = sum + mapping[s[i]] - 2 * mapping[s[i-1]]
            else:
                sum += mapping[s[i]]
        return sum