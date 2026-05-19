class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0 
        right = len(s1) - 1
        while right <= len(s2):
            if "".join(sorted(s1)) == "".join(sorted(s2[left:right + 1])):
                return True
            left += 1
            right += 1
        return False
