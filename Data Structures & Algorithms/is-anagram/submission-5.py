class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        out = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            out[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            out[index] -= 1
        
        for count in out:
            if count != 0:
                return False
        
        return True