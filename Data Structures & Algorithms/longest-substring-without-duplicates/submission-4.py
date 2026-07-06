class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring_set = set()
        left = 0
        length = 0
        for right in range(len(s)):
            while s[right] in substring_set:
                substring_set.remove(s[left])
                left += 1
            length = max(len(substring_set) + 1, length)
            substring_set.add(s[right])
        return length