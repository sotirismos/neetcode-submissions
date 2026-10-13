class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = [1] * len(nums)
        for index in range(1, len(nums)):
            prefix_prod[index] = prefix_prod[index - 1] * nums[index - 1]
        
        postfix_prod = [1] * len(nums)
        for index in range(len(nums) - 2, -1, -1):
            postfix_prod[index] = postfix_prod[index + 1] * nums[index + 1]
        
        output = []
        for index in range(len(nums)):
            output.append(prefix_prod[index] * postfix_prod[index])
        
        return output