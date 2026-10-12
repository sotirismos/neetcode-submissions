class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       nums_dict = {}
       for index, num in enumerate(nums):
            nums_dict[num] = index
    
       for index, num in enumerate(nums):
            candidate = target - nums[index]
            if candidate in nums_dict and index != nums_dict[candidate]:
                return [index, nums_dict[candidate]]
