class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) <= 2:
            return max(nums)
        
        total_money_with_first = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i <= len(nums) - 2:
            total_money_with_first.append(max(total_money_with_first[-2] + nums[i], total_money_with_first[-1]))
            i += 1
        
        total_money_without_first = [nums[1], max(nums[1], nums[2])]
        i = 3
        while i <= len(nums) - 1:
            total_money_without_first.append(max(total_money_without_first[-2] + nums[i], total_money_without_first[-1]))
            i += 1

        return max(total_money_with_first[-1], total_money_without_first[-1])