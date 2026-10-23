class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        state_nums = {}
        state_sum = 0
        start = 0

        for end in range(len(nums)):
            if nums[end] in state_nums:
                duplicate_index = state_nums[nums[end]]
                for index in range(start, duplicate_index + 1):
                    state_nums.pop(nums[index])
                    state_sum -= nums[index]
                start = duplicate_index + 1
            state_nums[nums[end]] = end
            state_sum += nums[end]

            if (end - start + 1) == k:
                max_sum = max(max_sum, state_sum)
                state_nums.pop(nums[start])
                state_sum -= nums[start]
                start += 1
        
        return max_sum
