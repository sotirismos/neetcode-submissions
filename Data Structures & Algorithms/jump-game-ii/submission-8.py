class Solution:
    def jump(self, nums: List[int]) -> int:
        left = 0
        count = 0

        while (left + nums[left]) < len(nums) - 1:
            index_range = nums[left]
            max_jump = 0
            for right in range(index_range):
                jump = nums[left + right + 1]
                if (right + 1 + jump) >= len(nums) - 1:
                    count += 1
                    return count + 1
                if jump >= max_jump:
                    desired = left + right + 1
                    max_jump = jump
            left = desired 
            count += 1
        return count + 1 if len(nums) > 1 else count
