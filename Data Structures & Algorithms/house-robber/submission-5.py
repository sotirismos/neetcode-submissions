class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        total_money = [nums[0], nums[1]]
        i = 2
        while i <= len(nums) - 1:
            total_money.append(max(total_money[0: i - 1]) + nums[i])
            i += 1

        return max(total_money[-1], total_money[-2])