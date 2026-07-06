class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        for right in range(len(s2)):
            if (right - left + 1) > len(s1):
                left += 1
            if ''.join(sorted(s2[left:right + 1])) == ''.join(sorted(s1)):
                return True
        
        return False
