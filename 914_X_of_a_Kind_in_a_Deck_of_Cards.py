# In a deck of cards, each card has an integer written on it.

# Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck
# into 1 or more groups of cards, where:

# Each group has exactly X cards.
# All the cards in each group have the same integer.


# Example 1:

# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
# Example 2:

# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
# Example 3:

# Input: [1]
# Output: false
# Explanation: No possible partition.
# Example 4:

# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
# Example 5:

# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = Counter(deck)
        X = min(count.values())
        for x in range(2, X + 1):
            if all(v % x == 0 for v in count.values()):
                return True
        return False


if __name__ == '__main__':
    result = Solution().hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1])
    print(result)
