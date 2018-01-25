# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such
# that nums[i] = nums[j] and the absolute difference between i and j is at most k.


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i
            else:
                if i - lookup[num] <= k:
                    return True
                else:
                    lookup[num] = i

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 1], 9))
