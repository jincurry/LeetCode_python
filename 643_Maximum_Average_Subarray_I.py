# Given an array consisting of n integers, find the contiguous subarray of given
# length k that has the maximum average value. And you need to output the maximum average value.
#
# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 0 or nums is None:
            return 0.0

        if k == len(nums):
            return sum(nums) / k
        max_sub, cur_sub = sum(nums[:k]), sum(nums[:k])
        for i in range(k, len(nums)):
            pre_sub = cur_sub
            cur_sub = pre_sub + nums[i] - nums[i - k]
            if max_sub < cur_sub:
                max_sub = cur_sub
        return max_sub / k

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], k=4))
    print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], k=6))
    print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], k=1))
    print(solution.findMaxAverage([0, 1, 1, 3, 3], k=4))