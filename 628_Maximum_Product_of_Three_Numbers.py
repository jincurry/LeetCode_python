# Given an integer array, find three numbers whose product is maximum and output
# the maximum product.
#
# Example 1:
# Input: [1,2,3]
# Output: 6
# Example 2:
# Input: [1,2,3,4]
# Output: 24


class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        first = nums[1] * nums[2]
        second = nums[-1] * nums[-2]
        if nums[0] <= 0:
            return nums[0] * first
        big = first if first > second else second
        return nums[0] * big


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumProduct([1, 2, 3, 4]))
    print(solution.maximumProduct([-1, -2, -3, -4]))
