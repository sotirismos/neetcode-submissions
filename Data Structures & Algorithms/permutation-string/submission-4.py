class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = {}
        s2_counter = {}

        for char_s1 in s1:
            if char_s1 not in s1_counter:
                s1_counter[char_s1] = 1
            else:
                s1_counter[char_s1] += 1
        
        left = 0
        for right in range(len(s2)):
            if s2[right] not in s2_counter:
                s2_counter[s2[right]] = 1
            else:
                s2_counter[s2[right]] += 1
            
            if (right - left + 1) > len(s1):
                s2_counter[s2[left]] -= 1
                left += 1
            
            matches = 0
            for char in s2_counter:
                if char in s1_counter and s2_counter[char] == s1_counter[char]:
                    matches += 1
            
            if matches == len(s1_counter):
                return True
            
        return False
