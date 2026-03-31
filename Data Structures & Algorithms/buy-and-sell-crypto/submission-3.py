class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy_price = prices[0]
        profit = 0
        
        for i in range (1, len(prices)):
            if prices[i] > lowest_buy_price and prices[i] - lowest_buy_price > profit:
                profit = prices[i] - lowest_buy_price
            elif prices[i]<lowest_buy_price:
                lowest_buy_price = prices[i]
        return profit
            