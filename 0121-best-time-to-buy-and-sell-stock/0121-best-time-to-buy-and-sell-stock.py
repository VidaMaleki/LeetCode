class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest_price = prices[0]
        profit= 0
        for i in range(1,len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            if prices[i] > lowest_price:
                profit = max(profit, prices[i] - lowest_price)
        return profit