class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first_pointer, second_pointer = 0, 0
        output = ""

        while first_pointer < len(word1) or second_pointer < len(word2): 
            if first_pointer < len(word1):
                output += word1[first_pointer]
                first_pointer += 1
            if second_pointer < len(word2):
                output += word2[second_pointer]
                second_pointer += 1
        
        return output
