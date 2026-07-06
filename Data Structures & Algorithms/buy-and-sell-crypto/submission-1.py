class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 0
        while right < len(prices):
            profit = max(prices[right] - prices[left], profit)
            if prices[right] < prices[left]:
                left = right
            right += 1
        return profit