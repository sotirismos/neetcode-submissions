class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(current_set: List[int], current_total: int, current_index: int):
            # Base case: Add combination to final list
            if (current_total == target):
                combinations.append(current_set.copy())
                return
            # Base case: Pruning
            if current_total > target:
                return
            # Base case: out of bounds
            if current_index > len(nums):
                return

            for index in range(current_index, len(nums)):
                current_set.append(nums[index])
                current_total += nums[index]

                backtracking(current_set, current_total, index)
                
                current_set.pop()
                current_total -= nums[index]
            
        backtracking([], 0, 0)
        
        return combinations