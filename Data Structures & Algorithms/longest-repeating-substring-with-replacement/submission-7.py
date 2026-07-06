class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        best = 0
        for right in range(len(s)):
            while not self.is_affordable(s[left:right+1], k):
                left += 1
            best = max(best, right - left + 1)
        return best

    def is_affordable(self, substring: str, k: int) -> bool:
        count = {}
        for char in substring:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        if count:
            max_freq = max(count.values())
        else:
            max_freq = 0
        replacements_needed = len(substring) - max_freq
        if replacements_needed <= k:
            return True
        else:
            return False

        