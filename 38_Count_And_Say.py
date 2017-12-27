# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        i, ch, tmp = 0, s[0],''
        for j in range(1,len(s)):
            if s[j] != ch:
                tmp += str(j-i) + ch
                i, ch = j, s[j]
        tmp += str(len(s)-i) + ch
        return tmp


if __name__ == "__main__":
    solution = Solution()
    print(solution.countAndSay(1))
    print(solution.countAndSay(2))
    print(solution.countAndSay(3))
    print(solution.countAndSay(4))
    print(solution.countAndSay(5))
    print(solution.countAndSay(6))
    print(solution.countAndSay(7))
    print(solution.countAndSay(8))
    print(solution.countAndSay(9))
    print(solution.countAndSay(10))
