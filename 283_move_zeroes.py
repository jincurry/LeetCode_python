# Given an array nums, write a function to move all 0's to the
# end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function,
#  nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        while j <= len(nums) - 1:
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] == 0 and nums[j] == 0:
                j += 1
            else:
                i += 1
                j += 1
        return nums # 提交leetcode时候不用加返回值


if __name__ == '__main__':
    s = Solution()
    r = s.moveZeroes([1, 0, 1])
    print(r)
