class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Now I want to sort the keys based on the values
        # sorted_keys = sorted(count.keys(), key=lambda k: count[k], reverse=True)

        # return sorted_keys[:k]
        
        # TODO: Review the following bug
        # bucket_sort = [[]] * len(nums)
        bucket_sort = [[] for _ in range(len(nums) + 1)]
        for key, freq in count.items():
            bucket_sort[freq].append(key)

        top_k = []
        for index, bucket in enumerate(bucket_sort[::-1]):
            if len(bucket) != 0:
                for j in range(len(bucket)):
                    top_k.append(bucket_sort[len(bucket_sort) - 1 - index][j])

        return top_k[:k]
        