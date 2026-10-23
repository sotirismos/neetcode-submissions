class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        state_nums = {}
        state_sum = 0
        start = 0

        for end in range(len(nums)):
            state_nums[nums[end]] = state_nums.get(nums[end], 0) + 1
            state_sum += nums[end]

            if (end - start + 1) == k:
                if len(state_nums) == k:
                    max_sum = max(max_sum, state_sum)
                state_nums[nums[start]] -= 1
                state_sum -= nums[start]
                if state_nums[nums[start]] == 0:
                    del state_nums[nums[start]]
                start += 1
        
        return max_sum
