"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # sum of prices[i + 1] - prices[i], if prices[i + 1] > prices[i]
        max_profit = 0
        if len(prices) == 0 or len(prices) == 1: return 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                max_profit += prices[i+1] - prices[i]
        return max_profit

    def maxProfit(self, prices):
        return sum([y - x for x, y in zip(prices[0:-1], prices[1:]) if x < y])