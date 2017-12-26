# Given a sorted array, remove the duplicates in-place such that
# each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do
# this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j +=1
        return i+1

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates([1,1,2,3,4,4,5]))
