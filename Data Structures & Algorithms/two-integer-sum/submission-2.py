class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     for j in range (i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        num_dict = {}
        for index, value in enumerate(nums):
            num_dict[target - value] = index
        
        for index, value in enumerate(nums):
            if value in num_dict and index != num_dict[value]:
                return [index, num_dict[value]]


        
        