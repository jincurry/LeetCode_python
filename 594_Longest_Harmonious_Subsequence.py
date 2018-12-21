# We define a harmonious array is an array where the difference between its maximum value
#  and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious
# subsequence among all its possible subsequences.
#
# Example 1:
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
import collections


class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        ret = 0
        for i in count:
            if i + 1 in count:
                ret = max(ret, count[i] + count[i + 1])

        return ret


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
    print(solution.findLHS([]))
    print(solution.findLHS([1, 1, 1, 1, 1]))
