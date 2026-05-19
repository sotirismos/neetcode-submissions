class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sliding = set()
        left = 0

        for right in range(len(nums)):
            if (right - left) > k:
                sliding.remove(nums[left])
                left += 1
            
            if nums[right] in sliding:
                return True
            else:
                sliding.add(nums[right])
        
        return False