class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ceil(x):
            num = int(x)
            return num + 1 if x > num else num
            
        def helper(piles: list[int], rate: int, hours: int):
            hours_to_eat = 0
            for pile in piles:
                hours_to_eat += ceil(pile/rate)
            if hours_to_eat > hours:
                return False
            else:
                return True
        
        lower_bound = 1
        upper_bound = max(piles)
        res = upper_bound
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if helper(piles, mid, h):
                res = mid
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1
        
        return res

                

