class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0    
        sliding = set()

        for right in range(len(s)):
            while s[right] in sliding:
                sliding.remove(s[left])
                left += 1
            sliding.add(s[right])
            length = max(length, right - left + 1)
        return length

