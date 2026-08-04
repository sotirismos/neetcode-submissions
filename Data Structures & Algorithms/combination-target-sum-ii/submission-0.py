class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        index = 0
        current_combination = []
        combinations = []
        candidates.sort()
        self.helper(index, candidates, current_combination, target, combinations)
        return combinations

    def helper(self, index, candidates, current_combination, target, combinations):
        # Base cases
        if sum(current_combination) == target:
            combinations.append(current_combination.copy())
            return 
        if sum(current_combination) > target:
            return
        if index == len(candidates):
            return
        
        # decision to include nums[i]
        current_combination.append(candidates[index])
        self.helper(index + 1, candidates, current_combination, target, combinations)
        
        while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
            index += 1
        current_combination.pop()
        self.helper(index + 1, candidates, current_combination, target, combinations)

        