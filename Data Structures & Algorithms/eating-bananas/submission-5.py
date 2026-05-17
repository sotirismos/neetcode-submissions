class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ceil(x):
            num = int(x)
            return num + 1 if x > num else num
        
        lower_bound = 1
        upper_bound = max(piles)
        res = upper_bound
        while lower_bound <= upper_bound:
            mid = (lower_bound + upper_bound) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)

            if hours <= h:
                res = min(res, mid)
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1
        
        return res

                

