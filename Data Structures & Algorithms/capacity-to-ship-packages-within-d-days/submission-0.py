class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def shipped_days(weights: List[int], capacity: int) -> int:
            total_weight = 0
            total_days = 1  
            for package in weights:
                total_weight += package
                if total_weight > capacity:
                    total_days += 1
                    total_weight = package  
            return total_days
        
        min_capacity =  max(weights)
        max_capacity = sum(weights)
        res = max_capacity

        while min_capacity <= max_capacity:
            mid = (min_capacity + max_capacity) // 2
            total_days = shipped_days(weights, mid)
            if total_days > days:
                min_capacity = mid + 1
            else:
                res = min(res, mid)
                max_capacity = mid - 1
        
        return res


        