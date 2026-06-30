class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        out = sorted(counter.keys(), key=lambda x: counter[x], reverse=True)[:k]
        return out