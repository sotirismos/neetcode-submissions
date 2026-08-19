class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_pali = ""
        for i in range(len(s)):
            # Odd length
            left, right = i, i
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if (right - left + 1) > len(longest_pali):
                    longest_pali = s[left:right + 1] 
                left -= 1
                right += 1
            
            # Even length
            left, right = i, i + 1
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if (right - left + 1) > len(longest_pali):
                    longest_pali = s[left:right + 1] 
                left -= 1
                right += 1

        return longest_pali           