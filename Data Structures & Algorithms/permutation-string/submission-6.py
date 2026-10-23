class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_counter = {}
        s2_char_counter = {}

        s1_index = 0
        while s1_index < len(s1):
            s1_char_counter[s1[s1_index]] = s1_char_counter.get(s1[s1_index], 0) + 1
            s1_index += 1


        s2_start = 0
        for s2_end in range(len(s2)):
            s2_char_counter[s2[s2_end]] = s2_char_counter.get(s2[s2_end], 0) + 1

            if s2[s2_end] not in s1_char_counter:
                s2_char_counter = {}
                s2_start = s2_end + 1
            else:
                while s2_char_counter[s2[s2_end]] > s1_char_counter[s2[s2_end]]:
                    s2_char_counter[s2[s2_start]] -= 1
                    if s2_char_counter[s2[s2_start]] == 0:
                        del s2_char_counter[s2[s2_start]]
                    s2_start += 1

            if (s2_end - s2_start + 1) == len(s1):
                return True
            

        return False