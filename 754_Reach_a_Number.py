# You are standing at position 0 on an infinite number line. There is a goal at position target.

# On each move, you can either go left or right. During the n-th move (starting from 1),
# you take n steps.

# Return the minimum number of steps required to reach the destination.

# Example 1:
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
# Example 2:
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.


class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = int((2 * target)**(1 / 2))
        while self.sum_number(k) < target:
            k += 1
        d = self.sum_number(k) - target
        if d % 2 == 0:
            return k
        else:
            return k + 1 + (k % 2)

    def sum_number(self, k):
        return sum([i for i in range(k + 1)])


if __name__ == '__main__':
    solution = Solution()
    result = solution.reachNumber(3)
    print(result)
    result = solution.reachNumber(2)
    print(result)
    result = solution.reachNumber(1)
    print(result)
