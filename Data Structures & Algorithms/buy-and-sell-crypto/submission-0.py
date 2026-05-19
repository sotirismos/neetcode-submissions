class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        for right in range(1, len(prices)):
            current_profit = prices[right] - prices[left]
            if current_profit > 0:
                profit = max(profit, current_profit)

            if prices[right] < prices[left]:
                left = right

        return profit