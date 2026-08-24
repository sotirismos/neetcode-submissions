class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n + 1)]
        offset = 1
        
        for num in range(n + 1):
            if (2 * offset) == num:
                offset = num
            if (num - offset) >= 0:
                dp[num] = dp[num - offset] + 1
        
        return dp