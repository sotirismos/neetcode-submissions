class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for index in range(len(nums)):
            # We cannot reach this index
            if index > max_reach:
                return False
            
            # Break early
            if max_reach == len(nums) - 1:
                return True
            
            max_reach = max(max_reach, index + nums[index])

        return True

