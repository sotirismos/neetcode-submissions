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
        if index > len(nums):
            return
        
        for i in range(index, len(nums)):
            current_combination.append(nums[i])
            self.helper(i, nums, current_combination, target, combinations)
            current_combination.pop()
        