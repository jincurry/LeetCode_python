# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
#
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
#
# Example 2:
#
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.

# this one waste too much time and can't pass the leetcode test


class Solution1:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        my_profit = []
        for i in range(len(prices)):
            j = i
            max_profit = []
            while j < len(prices):
                s = prices[j] - prices[i]
                if s >= 0:
                    max_profit.append(s)
                else:
                    max_profit.append(0)
                j += 1
            my_profit.append(max(max_profit))

        if not my_profit:
            return 0
        else:
            return max(my_profit)


class Solution:
    def maxProfit(self, prices):

        max_profit, min_price = 0, float("inf")
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([]))
    print(solution.maxProfit([1]))
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
    print(solution.maxProfit([7, 6, 5, 4, 3, 2, 1]))
