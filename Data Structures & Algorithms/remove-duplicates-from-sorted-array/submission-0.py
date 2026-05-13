class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = 1
        right_pointer = 1
        while right_pointer < len(nums):
            if nums[right_pointer] != nums[right_pointer - 1]:
                nums[left_pointer] = nums[right_pointer]
                left_pointer += 1
            right_pointer += 1
        return left_pointer

