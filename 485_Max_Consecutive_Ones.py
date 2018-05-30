# Given a binary array, find the maximum number of consecutive 1s in this array.
#
# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i, j = 0, -1
        result = []
        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(i - j - 1)
                j = i
        if nums[i] == 1:
            result.append(i - j)
        return max(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1, 1]))
    print(solution.findMaxConsecutiveOnes([1, 1, 0]))
    print(solution.findMaxConsecutiveOnes([0]))
    print(solution.findMaxConsecutiveOnes([]))
    print(solution.findMaxConsecutiveOnes([0, 1, 1, 0, 1, 1, 1, 0]))