class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # contains_zero = False
        # zero_count = 0
        # overall_product = 0
        # for i in range(len(nums)):
        #     multiplier = nums[i]
        #     if multiplier == 0:
        #         contains_zero = True
        #         zero_count += 1
        #     if nums[i] != 0:
        #         if i == 0:
        #             overall_product = multiplier
        #         else:
        #             overall_product *= multiplier

        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         if contains_zero:
        #             nums[i] = 0
        #         else:
        #             nums[i] = int(overall_product / nums[i])
        #     else:
        #         if overall_product != 0:
        #             if zero_count > 1:
        #                 nums[i] = 0
        #             else:
        #                 nums[i] = overall_product
        #         else:
        #             nums[i] = 0

        # return nums

        prefix = []
        postfix = []
        for i in range(len(nums)):
            prefix_product = 1
            postfix_product = 1
            for j in range(0, i):
                prefix_product *= nums[j]
            prefix.append(prefix_product)
            for k in range(i + 1, len(nums)):
                postfix_product *= nums[k]
            postfix.append(postfix_product)
        
        output = []
        for i in range(len(nums)):
            output.append(prefix[i] * postfix[i])
        
        return output



        
    