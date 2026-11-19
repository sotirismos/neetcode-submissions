class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtracking(current_subset: List[int], index: int):
            # Base case
            if index == len(nums):
                subsets.append(current_subset.copy())
                return
            
            current_subset.append(nums[index])
            backtracking(current_subset, index + 1)

            current_subset.pop()
            backtracking(current_subset, index + 1)

        if not nums:
            return []
        else:
            backtracking([], 0)
        
        return subsets

