class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        balance = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            temp = prices[i] - balance
            profit = max(temp, profit)
            balance = min(prices[i], balance)
        return profit