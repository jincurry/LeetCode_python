# Given a non-empty integer array of size n, find the minimum number of moves required
# to make all array elements equal, where a move is incrementing n - 1 elements by 1.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 3
#
# Explanation:
# Only three moves are needed (remember each move increments two elements):
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 这个方法超时了
        # result = 0
        # while len(set(nums)) != 1:
        #     max_index = nums.index(max(nums))
        #     for k, _ in enumerate(nums):
        #         if k == max_index:
        #             continue
        #         nums[k] += 1
        #     result += 1
        # return result
        return sum(nums) - min(nums) * len(nums)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minMoves([1, 2, 3]))