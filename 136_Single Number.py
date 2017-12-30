# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
import operator
from functools import reduce


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([1, 1, 2, 2, 3, 4, 4]))
