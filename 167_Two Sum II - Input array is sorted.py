# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a
# specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
#  less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution and you may not use the same element twice.
#
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start , end = 0, len(numbers)-1

        while start != end:
            sums = numbers[start] + numbers[end]
            if sums < target:
                start += 1
            elif sums > target:
                end -= 1
            else:
                return [start+1, end+1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2,7,9,11,23], 13))
    solution2 = Solution()
    print(solution2.twoSum([2,7,11,15], 9))
