import operator

# Given an array of integers, return indices of the two numbers such that they
#   add up to a specific target.

# You may assume that each input would have exactly one solution, and you may
#   not use the same element twice.
# example:Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = [(i, nums[i]) for i in range(len(nums))]
        a.sort(key=operator.itemgetter(1))

        i = 0
        j = len(nums) - 1
        while True:
            if i == j:
                break
            sum = a[i][1] + a[j][1]
            if sum == target:
                break
            elif sum < target:
                i += 1
            else:
                j -= 1
        return sorted([a[i][0], a[j][0]])