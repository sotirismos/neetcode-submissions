class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        if len(nums) == 1:
            return nums[0]
        
        total_money = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i <= len(nums) - 1:
            total_money.append(max(total_money[-2] + nums[i], total_money[-1]))
            i += 1

        return total_money[-1]