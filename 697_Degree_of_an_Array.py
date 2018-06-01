# Given a non-empty array of non-negative integers nums, the degree of this array is
# defined as the maximum frequency of any one of its elements.
#
# Your task is to find the smallest possible length of a (contiguous) subarray of nums,
# that has the same degree as nums.
#
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
from collections import Counter


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        sorted_c = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        key, value = sorted_c[0][0], sorted_c[0][1]
        if value == 1:
            return 1
        start, end = nums.index(key), len(nums) - 1 - nums[::-1].index(key)
        res = end - start + 1
        for item in sorted_c[1:]:
            if item[1] == value:
                start, end = nums.index(item[0]), len(nums) - 1 - nums[::-1].index(item[0])
                if end - start + 1 < res:
                    res = end - start + 1
            else:
                break
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findShortestSubArray([1, 2, 1, 2, 1]))
    print(solution.findShortestSubArray([1, 2, 2, 3, 1]))
