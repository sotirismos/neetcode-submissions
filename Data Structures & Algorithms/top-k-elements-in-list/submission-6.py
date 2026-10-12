class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        sorted_list = sorted(frequency_dict, key=lambda x: frequency_dict[x], reverse=True)
        return sorted_list[:k]