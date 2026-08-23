class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane's
        max_prod = nums[0]
        curr_min, curr_max = 1, 1

        for num in nums:
            temporal = curr_max * num
            curr_max = max(num, curr_min * num, curr_max * num)
            curr_min = min(num, curr_min * num, temporal)
            max_prod = max(max_prod, curr_max)
        
        return max_prod