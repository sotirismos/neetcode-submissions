
import math

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        output = []
        for key in count:
            if count[key] > math.floor(len(nums) / 3):
                output.append(key)
        
        return output
        