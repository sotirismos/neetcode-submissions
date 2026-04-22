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
        output = []
        prefix = 1
        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output



        
    