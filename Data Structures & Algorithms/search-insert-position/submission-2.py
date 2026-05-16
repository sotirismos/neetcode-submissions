class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        if target < nums[left]:
            return left
        elif target > nums[right]:
            return right + 1
        else:
            return right
    
