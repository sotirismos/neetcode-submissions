class Solution:
    def validPalindrome(self, s: str) -> bool:
        counter = 0
        left, right = 0, len(s) - 1

        def isPalindrome(left_pointer: int, right_pointer: int, s: str) -> bool:
            while left_pointer < right_pointer:
                if s[left_pointer] != s[right_pointer]:
                    return False
                left_pointer += 1
                right_pointer -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                is_first_potential_palindrome = isPalindrome(left + 1, right, s)
                is_second_potential_palindrome = isPalindrome(left, right - 1, s)
                return is_first_potential_palindrome or is_second_potential_palindrome
            else:
                left += 1
                right -= 1
        
        return True