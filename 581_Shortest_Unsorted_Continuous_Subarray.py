# Given an integer array, you need to find one continuous subarray that if
# you only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array
# sorted in ascending order.


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        backup = nums[:]
        i, j = 0, len(nums)-1
        backup.sort()
        while backup[i] == nums[i] and i < len(nums) - 1:
            i += 1
        while backup[j] == nums[j] and j >= 0:
            j -= 1
        return j -i + 1 if i < j else 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(solution.findUnsortedSubarray([2, 2, 2, 2, 2, 2, 2]))
    print(solution.findUnsortedSubarray([1, 2, 3, 5, 4, 6, 7]))
    print(solution.findUnsortedSubarray([1]))
    print(solution.findUnsortedSubarray([1, 2]))
    print(solution.findUnsortedSubarray([2, 1]))