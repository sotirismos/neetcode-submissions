class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        buckets_list = [[] for _ in range(len(nums) + 1)]
        for key, value in frequency_dict.items():
            buckets_list[value].append(key)
        
        output = []
        for index in range(len(buckets_list) - 1, -1, -1):
            for num in buckets_list[index]:
                output.append(num)
                if len(output) == k:
                    return output



