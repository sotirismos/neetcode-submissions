class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            # check if the preceding subarray can help us or not
            if current_sum <= 0:
                current_sum = 0
            
            current_sum += num

            if current_sum >= max_sum:
                max_sum = current_sum
        
        return max_sum