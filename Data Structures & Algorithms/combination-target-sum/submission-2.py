class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        index = 0
        current_combination = []
        combinations = []
        self.helper(index, nums, current_combination, target, combinations)
        return combinations

    def helper(self, index, nums, current_combination, target, combinations):
        # Base cases
        if sum(current_combination) == target:
            combinations.append(current_combination.copy())
            return 
        if sum(current_combination) > target:
            return
        if index == len(nums):
            return
        
        # decision to include nums[i]
        current_combination.append(nums[index])
        self.helper(index, nums, current_combination, target, combinations)
        
        current_combination.pop()
        self.helper(index + 1, nums, current_combination, target, combinations)
        