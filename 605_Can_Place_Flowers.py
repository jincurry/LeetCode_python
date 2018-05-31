# Suppose you have a long flowerbed in which some of the plots are planted and
# some are not. However, flowers cannot be planted in adjacent
# plots - they would compete for water and both would die.
#
# Given a flowerbed (represented as an array containing 0 and 1,
# where 0 means empty and 1 means not empty), and a number n, return if
# n new flowers can be planted in it without violating the no-adjacent-flowers rule.
#
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
from collections import Counter


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        counter = Counter(flowerbed)
        if counter[0] < n:
            return False
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] + flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n


if __name__ == '__main__':
    solution = Solution()
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 2))
    print(solution.canPlaceFlowers([0, 0, 1, 0, 0], 1))
    print(solution.canPlaceFlowers([0, 0, 1, 0, 0], 2))
    print(solution.canPlaceFlowers([1], 0))