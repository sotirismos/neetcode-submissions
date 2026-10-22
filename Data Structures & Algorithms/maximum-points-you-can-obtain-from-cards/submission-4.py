class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        if k == len(cardPoints):
            return total

        state = 0
        max_sum = 0
        start = 0
        end = 0

        while end < (len(cardPoints)):
            state += cardPoints[end]

            if (end - start + 1) == len(cardPoints) - k:
                max_sum = max(max_sum, total - state)
                state -= cardPoints[start]
                start += 1
            
            end += 1

        return max_sum
