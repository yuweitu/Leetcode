"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
"""


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # 1. when prices = [] !
        # 2. Set one pointer and one counter correctly

        if len(prices) == 0: return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            curr = price - min_price
            if curr > max_profit:
                max_profit = curr

            if price < min_price:
                min_price = price

        return max_profit