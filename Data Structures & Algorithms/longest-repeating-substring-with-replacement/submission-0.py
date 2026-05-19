class Solution:
    def most_popular_char(self, s: str):
        char_counter = {}
        for char in s:
            if char not in char_counter:
                char_counter[char] = 1
            else:
                char_counter[char] += 1

        return max(char_counter.values())

    def characterReplacement(self, s: str, k: int) -> int:
        length = 1
        left, right = 0, 1

        while right < len(s):
            while (right - left + 1) - (self.most_popular_char(s[left:right + 1])) > k:
                left += 1
            length = max(length, right - left + 1)
            right += 1
        
        return length