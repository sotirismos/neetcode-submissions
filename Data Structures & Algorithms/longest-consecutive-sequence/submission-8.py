class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        longest = 0
        hash_set = set(nums)
        for num in hash_set:
            if (num - 1) not in hash_set:
                current = 1
                next_element = num + 1
                while next_element in hash_set:
                    current += 1
                    next_element += 1
                longest = max(current, longest)
        return longest


