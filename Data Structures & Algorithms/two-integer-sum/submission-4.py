class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return[num_dict[target - num], i]
            else:
                num_dict[num] = i
        return num_dict