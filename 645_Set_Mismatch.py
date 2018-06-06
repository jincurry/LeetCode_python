# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error,
#
#  one of the numbers in the set got duplicated to another number in the set, which results in
#
# repetition of one number and loss of another number.
#
# Given an array nums representing the data status of this set after the error. Your task is to
#  firstly find the number occurs twice and then find the number that is missing. Return them
# in the form of an array.
#
# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # this method exceed time
        # miss = sum(range(1, len(nums)+1)) - sum(nums)
        # for x in set(nums):
        #     nums.remove(x)
        # twice = nums[0]
        # miss += twice
        # return [twice, miss]
        total = sum(range(1, len(nums) + 1))
        miss = total - sum(set(nums))
        twice = miss - total + sum(nums)
        return [twice, miss]




if __name__ == '__main__':
    solution = Solution()
    print(solution.findErrorNums([1, 2, 2, 4]))