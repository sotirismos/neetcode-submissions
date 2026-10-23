class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_index = 0

        for sell_index in range(1, len(prices)):
            if prices[sell_index] < prices[buy_index]:
                buy_index = sell_index
            else:
                profit = max(profit, prices[sell_index] - prices[buy_index])
        
        return profit
