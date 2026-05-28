class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        min_strs_length = float('inf')
        for string in strs:
            min_strs_length = min(min_strs_length, len(string))
        output = ""
        index = 0
        
        first_string = strs[0]
        while index < min_strs_length:
            for string in strs[1:]:
                if string[index] != first_string[index]:
                    return output
            output += string[index]
            index += 1
        return output
            



