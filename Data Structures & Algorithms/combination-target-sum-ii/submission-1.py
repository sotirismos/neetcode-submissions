class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()

        def backtracking(current_set: List[int], current_total: int, current_index: int):
            # Base case: Add combination to final list
            if (current_total == target):
                combinations.append(current_set.copy())
                return
            # Base case: Pruning
            if current_total > target:
                return
            # Base case: out of bounds
            if current_index >= len(candidates):
                return

            for index in range(current_index, len(candidates)):

                if (index > current_index) and (candidates[index] == candidates[index - 1]):
                    continue
                    
                current_set.append(candidates[index])
                current_total += candidates[index]

                backtracking(current_set, current_total, index + 1)
                
                current_set.pop()
                current_total -= candidates[index]
            
        backtracking([], 0, 0)
        
        return combinations