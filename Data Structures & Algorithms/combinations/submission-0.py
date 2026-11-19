class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtracking(current_set: List[int], i: int):
            # Base case(s)
            # Add combination to final list
            if (len(current_set) == k):
                combinations.append(current_set.copy())
                return
            
            # Pruning
            if i > n:
                return

            current_set.append(i)
            backtracking(current_set, i + 1)

            current_set.pop()
            backtracking(current_set, i + 1)
        
        backtracking([], 1)
        
        return combinations