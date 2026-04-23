class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        longest = 0
        for num in nums:
            if num - 1 not in count:
                current = num
                streak = 1
                while current + 1 in count:
                    current += 1
                    streak += 1
                longest = max(longest, streak)
        return longest

