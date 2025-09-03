class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 0
        max_price = float("-inf")
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[min_price]:
                min_price = i
            if prices[i] > prices[min_price] and i > min_price:
                max_price = prices[i]
            temp = max_price - prices[min_price]
            profit = max(profit,temp)
        return profit