class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        count = {}
        for index, num in enumerate(nums):
            if (target - num) in count:
                return [count[target - num], index]
            else:
                count[num] = index