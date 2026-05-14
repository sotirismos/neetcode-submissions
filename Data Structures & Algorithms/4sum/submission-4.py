class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    score = nums[i] + nums[j] + nums[left] + nums[right]
                    if score < target:
                        left += 1
                    elif score > target:
                        right -= 1
                    else:
                        quadruple = [nums[i], nums[j], nums[left], nums[right]]
                        quadruple.sort()
                        if quadruple not in output:
                            output.append(quadruple)
                        left += 1
        return output


