# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum = digits[0]
        alist = []
        for i in range(1,len(digits)):
            sum  = sum*10 + digits[i]
        sum = sum + 1
        while sum:
            alist.append(sum%10)
            sum = sum//10
        return alist[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3, 4]))
    print(solution.plusOne([1, 9, 9, 9]))
    print(solution.plusOne([1, 0, 0, 0]))
    print(solution.plusOne([9, 9, 9, 9]))