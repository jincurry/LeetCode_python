# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.


class Solution:
    # this solution will not pass,even it is correct.due to it wastes a lot of time.
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        if n == 2:
            return 2
        else:
            s1 = self.climbStairs(n - 1)
            s2 = self.climbStairs(n - 2)
            return s1 + s2


class Solution1:
    # this one will pass the test, I think the reason is due to this method keep the history
    def __init__(self):
        self.dict = {1: 1, 2: 2}

    def climbStairs(self, n):
        if n not in self.dict:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dict[n]


if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution1()
    print(solution.climbStairs(5))
    print(solution2.climbStairs(5))
