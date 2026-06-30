class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        buckets = []
        for _ in range(len(nums) + 1):
            buckets.append([])

        for key, value in counter.items():
            buckets[value].append(key)

        out = []
        for index in range(len(buckets) - 1, -1, -1):
            for num in buckets[index]:
                out.append(num)
            if len(out) == k:
                return out
