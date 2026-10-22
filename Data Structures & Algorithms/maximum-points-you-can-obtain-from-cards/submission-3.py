class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        state = sum(cardPoints[0:k])
        max_sum = state

        left = k - 1    
        right = len(cardPoints) - 1

        while left >= 0:

            state -= cardPoints[left]
            state += cardPoints[right]

            max_sum = max(max_sum, state)
            left -= 1
            right -= 1

            
        return max_sum
