# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        else:
            s = self.getRow(rowIndex - 1)
            my_list = [1]
            i = 0
            while i <= len(s) - 2:
                my_list.append(s[i] + s[i+1])
                i += 1
            my_list.append(1)
            return my_list

if __name__ == "__main__":
    solution = Solution()
    for i in range(10):
        print(solution.getRow(i))