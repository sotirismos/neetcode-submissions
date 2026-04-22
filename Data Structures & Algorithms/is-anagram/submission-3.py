class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashMap = {}
        for char_s in s:
            if char_s in hashMap:
                hashMap[char_s] += 1
            else:
                hashMap[char_s] = 1
        
        for char_t in t:
            if char_t not in hashMap:
                return False
            else:
                hashMap[char_t] -= 1
        
        for key in hashMap:
            if hashMap[key] != 0:
                return False
        return True
        