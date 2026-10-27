class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) < 2:
            return nums[left]
        
        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:
            mid = (left + right) // 2
            # 1st case: mid is the first element after the "deflection" point
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # 2nd case: we need to decide if we're going to perform binary search on the left OR right of mid
            else:
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
