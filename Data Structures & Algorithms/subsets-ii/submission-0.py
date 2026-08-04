class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        current_subset = []
        index = 0
        nums.sort()

        self.helper(index, nums, current_subset, subsets) 
        return subsets

    def helper(self, index: int, nums: List[int], current_subset: List[int], subsets: List[List[int]]):
        # Base case
        if index >= len(nums):
            subsets.append(current_subset.copy())
            return

        # Include ith element
        current_subset.append(nums[index])
        self.helper(index + 1, nums, current_subset, subsets)

        # do NOT include ith element
        current_subset.pop()
        while index < len(nums) - 1 and nums[index] == nums[index + 1]:
            index += 1
        self.helper(index + 1, nums, current_subset, subsets)