class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        less_price = prices[0]
        diff = 0
        for i in range(1,len(prices)):
            
            if prices[i] < less_price:
                less_price = prices[i]
            else:
                diff = max(diff,prices[i] - less_price )
        return diff
            

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         if not prices:
#             return 0

#         min_price = prices[0]
#         max_profit = 0
        
#         for price in prices[1:]:
#             if price < min_price:
#                 min_price = price
#             else:
#                 max_profit = max(max_profit, price - min_price)

#         return max_profit