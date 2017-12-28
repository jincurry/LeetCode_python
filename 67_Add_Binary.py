# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        alist = []
        c, i, j = 0, len(a)-1, len(b)-1
        while max(i,j) >= 0:
            m = a[i] if i >=0 else 0
            n = b[j] if j >=0 else 0
            if int(m) + int(n) + c == 2:
                alist.append('0')
                c = 1
            elif int(m) + int(n) +c == 3:
                alist.append('1')
                c = 1
            elif int(m) + int(n) +c == 1:
                alist.append('1')
                c = 0
            else:
                alist.append('0')
            i = i - 1
            j = j - 1
        if c == 1:
            alist.append('1')
        y = ''
        for x in reversed(alist):
            y += x
        return y

if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary('11', '1'))



