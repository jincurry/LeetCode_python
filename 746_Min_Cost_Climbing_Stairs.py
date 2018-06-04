# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
#
# Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
#
# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        costlist = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            if cost[i] + cost[i-2] > cost[i] + cost[i-1]:
                costlist.append(cost[i] + cost[i-1])
                cost[i] = costlist[i]
            else:
                costlist.append(cost[i] + cost[i-2])
                cost[i] = costlist[i]
        return costlist[-1] if costlist[-1] < costlist[-2] else costlist[-2]

        # 下面的方法更好
        # f1 = f2 = 0
        # for x in cost:
        #     f1, f2 = x + min(f1, f2), f1
        # return min(f1, f2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostClimbingStairs([10, 15, 20]))
    print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))