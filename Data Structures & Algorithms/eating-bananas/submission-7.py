class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)

        while min_speed <= max_speed:
            mid_speed = (min_speed + max_speed) // 2
            if self.exceeds_desired_hours(piles, mid_speed, h):
                min_speed = mid_speed + 1
            else:
                max_speed = mid_speed - 1
        
        return min_speed

    def exceeds_desired_hours(self, piles: List[int], speed: int, h: int):
        hours_spent = 0
        for pile in piles:
            hours_spent += math.ceil(pile / speed)
        if hours_spent > h:
            return True
        else:
            return False

