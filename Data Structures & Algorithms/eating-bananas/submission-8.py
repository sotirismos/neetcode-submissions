class Solution:
    def exceeds_h(self, piles: List[int], h: int, k: int):
        total_hours = 0
        for pile in piles:
            total_hours += math.ceil(pile/k)
        
        if total_hours > h:
            return True
        else:
            return False


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_range = 1
        right_range = max(piles)

        while left_range <= right_range:
            mid_range = (left_range + right_range) // 2

            if self.exceeds_h(piles, h, mid_range):
                left_range = mid_range + 1
            else:
                right_range = mid_range - 1
        
        return left_range
