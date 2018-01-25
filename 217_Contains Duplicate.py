# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
# appears at least twice in the array, and it should return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 1]))
    print(solution.containsDuplicate([]))
    print(solution.containsDuplicate([0]))
