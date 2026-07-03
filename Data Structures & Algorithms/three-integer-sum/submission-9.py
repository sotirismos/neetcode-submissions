class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort()

        for i in range(len(nums)):
            left = 0
            right = len(nums) - 1
            while left < right:
                if left == i:
                    left += 1
                    continue
                if right == i:
                    right -= 1
                    continue
                if nums[left] + nums[i] + nums[right] < 0:
                    left += 1
                elif nums[left] + nums[i] + nums[right] > 0:
                    right -= 1
                else:
                    triplet = [nums[left], nums[i], nums[right]]
                    triplet.sort()
                    if triplet not in out:
                        out.append(triplet)
                    left += 1
        return out
