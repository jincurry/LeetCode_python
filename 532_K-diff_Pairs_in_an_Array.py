# Given an array of integers and an integer k, you need to find the number of unique
# k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j),
# where i and j are both numbers in the array and their absolute difference is k.
#
# Example 1:
# Input: [3, 1, 4, 1, 5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.
# Example 2:
# Input:[1, 2, 3, 4, 5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
# Example 3:
# Input: [1, 3, 1, 5, 4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

from collections import Counter


class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        counter = Counter(nums)
        result = 0
        if k > 0:
            for x in counter:
                low = x - k
                high = x + k
                if counter[low] >= 1:
                    result += 1
                if counter[high] >= 1:
                    result += 1
            return result // 2
        else:
            for x in counter:
                if counter[x] >= 2:
                    result += 1
            return result


if __name__ == '__main__':
    print(Solution().findPairs([1, 1, 1, 1, 1, 1], k=0))
    print(Solution().findPairs([1, 2, 3, 4, 5], k=1))
    print(Solution().findPairs([1, 1, 3, 4, 5], k=2))
    print(Solution().findPairs([1, 3, 1, 5, 4], k=0))