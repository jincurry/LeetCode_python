# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
# Example 1:
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
# Example 2:
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.


class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # one, two = nums[:], nums[:]
        #
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         one[i] = nums[i + 1]
        #         two[i + 1] = nums[i]
        #         break
        # return one == sorted(one) or two == sorted(two)

        count = 0
        if len(nums) == 1:
            return True
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if nums[i + 1] < nums[i - 1] and i - 1 >= 0:
                    count += 1
                    if count > 1:
                        break
                    if i + 1 != (len(nums) - 1):
                        nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
                    count += 1
                    if count > 1:
                        break
                    if count == 1:
                        nums[i] -= 1
        return count <= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPossibility([4, 2, 3]))
    print(solution.checkPossibility([4, 2, 1]))
    print(solution.checkPossibility([]))
    print(solution.checkPossibility([1]))
    print(solution.checkPossibility([3, 4, 2, 3]))
    print(solution.checkPossibility([3, 4]))
    print(solution.checkPossibility([4, 3]))
