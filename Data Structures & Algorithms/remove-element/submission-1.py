class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] != val:
                left += 1
            else:
                if nums[right] != val:
                    temp_1 = nums[right]
                    temp_2 = nums[left]
                    nums[left] = temp_1
                    nums[right] = temp_2
                    left += 1
                    right -= 1
                else:
                    right -= 1
        count = 0
        for num in nums:
            if num != val:
                count += 1
        return count