class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        characters_last_index = {}
        for index, char in enumerate(s):
            characters_last_index[char] = index

        substrings = []
        substring_start = 0
        substring_end = 0
        for index, char in enumerate(s):
            substring_end = max(substring_end, characters_last_index[char])
            if index == substring_end:
                length = substring_end - substring_start + 1
                substrings.append(length)
                substring_start = index + 1
        
        return substrings
            