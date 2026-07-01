class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = []
        postfix = []
        
        prefix_prod = 1
        for i in range(len(nums)):
            prefix_prod *= nums[i]
            prefix.append(prefix_prod)
        
        postfix_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix_prod *= nums[i]
            postfix.append(postfix_prod)
        postfix.reverse()

        out = []
        for i in range(len(nums)):
            if i - 1 < 0:
                out.append(postfix[i+1])
            elif i == len(nums) - 1:
                out.append(prefix[i-1])
            else:
                out.append(prefix[i-1] * postfix[i+1])
        return out


        
    