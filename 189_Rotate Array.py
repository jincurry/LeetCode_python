# Rotate an array of n elements to the right by k steps.
#
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
#


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution = Solution()
    solution.rotate(nums, 3)
    print(nums)