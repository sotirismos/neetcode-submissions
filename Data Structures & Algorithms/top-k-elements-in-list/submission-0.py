class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Now I want to sort the keys based on the values
        sorted_keys = sorted(count.keys(), key=lambda k: count[k], reverse=True)

        return sorted_keys[:k]
        