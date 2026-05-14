class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for index in range(len(nums)):
            left = 0
            right = len(nums) - 1
            while left < right:
                if left == index:
                    left += 1
                    continue
                if right == index:
                    right -= 1
                    continue
                if nums[left] + nums[right] + nums[index] < 0:
                    left += 1
                    continue
                if nums[left] + nums[right] + nums[index] > 0:
                    right -= 1
                    continue
                if nums[left] + nums[right] + nums[index] == 0:
                    triplet = [nums[left], nums[right], nums[index]]
                    triplet.sort()
                    if triplet not in triplets:
                        triplets.append(triplet)
                    left += 1
        return triplets

