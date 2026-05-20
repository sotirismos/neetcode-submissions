class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = float('inf')
        left = 0

        for right in range(len(nums)):
            while sum(nums[left:right + 1]) >= target:
                length = min(length, right - left + 1)
                left += 1
            
            right += 1
        
        if length == float('inf'):
            return 0
        else:
            return length