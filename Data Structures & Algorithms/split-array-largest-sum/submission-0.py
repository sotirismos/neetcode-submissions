class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            if self.canSplit(nums, mid, k):
                right = mid - 1
            else:
                left = mid + 1
        
        # minimun valid answer
        return left
    
    def canSplit(self, nums: List[int], mid: int, k: int) -> bool:
        subarrays = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > mid:
                subarrays += 1
                current_sum = num
            else:
                current_sum += num

        return subarrays <= k