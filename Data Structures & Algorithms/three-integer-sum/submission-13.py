class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the input array
        nums.sort()
        triplets = []

        index = 0
        while index < len(nums):
            left = index + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] + nums[index] < 0:
                    left += 1
                elif nums[left] + nums[right] + nums[index] > 0:
                    right -= 1
                else:
                    triplet = [nums[left], nums[right], nums[index]]
                    triplet.sort()
                    if triplet not in triplets:
                        triplets.append(triplet)
                    left += 1
            index += 1
        
        return triplets