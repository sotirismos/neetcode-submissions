class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ord_list = [0] * 26

        for char in s:
            ord_list[ord(char) - ord('a')] += 1
        
        for char in t:
            ord_list[ord(char) - ord('a')] -= 1
        
        for char in ord_list:
            if char != 0:
                return False
        
        return True