class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        if len(nums) < 2:
            if nums[left] == target:
                return left
            else:
                return -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] > nums[mid]:
                cutoff = mid
                break
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        if target >= nums[cutoff] and target <= nums[-1]:
            left = cutoff
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    return mid 
        else:
            left = 0
            right = cutoff - 1
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    return mid 
        return -1