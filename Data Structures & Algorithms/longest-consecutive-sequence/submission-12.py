class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest = 0
        index = 0
        while index < len(nums):
            if nums[index] - 1 not in unique_nums:
                current = 1
                current_value = nums[index]
                while index < len(nums) and current_value + 1 in unique_nums:
                    current += 1
                    current_value += 1
                longest = max(longest, current)
            index += 1  
        return longest