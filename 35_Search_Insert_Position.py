# Given a sorted array and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.
# Example Input: [1,3,5,6], 5
# Output: 2
# Example Input: [1,3,5,6], 2
# Output: 1


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        j = len(nums)-1
        while nums[j] >= target and j >= 0:
            j = j - 1
        return j + 1

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1, 3, 5, 6], 0))
    print(solution.searchInsert([1,3,5,6], 7))
