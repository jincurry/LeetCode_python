# Given an array and a value, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the
# input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

class Solution:
    def removeElement(self, nums, val):
        """

        :param nums: list[int]
        :param val: int
        :return: int
        """
        i, j = 0,len(nums)-1
        while i <= j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
            else:
                i = i + 1
        return j+1

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement([3,2,3,3,45,64,3,61,3],val=3))