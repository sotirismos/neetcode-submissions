class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        result = self.dfs(coins, amount, cache)
        if result == float('inf'):
             return -1
        return result

    def dfs(self, coins: List[int], amount: int, cache: dict) -> int:
        if amount == 0:
            return 0
        if amount in cache:
            return cache[amount]
        
        min_coins = float('inf')
        for index, coin_value in enumerate(coins):
            if (amount - coin_value) >= 0:
                min_coins = min(min_coins, self.dfs(coins, amount - coin_value, cache) + 1)

        cache[amount] = min_coins
        return min_coins