class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        catalog = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        curr_comb = ""
        combinations = []
        index = 0

        def backtracking(curr_comb: str, index: int):
            # Base case (reached leaf)
            if index == len(digits):
                combinations.append(curr_comb)
                return

            for letter in catalog[digits[index]]:
                backtracking(curr_comb + letter, index + 1)    
        
        if digits:
           backtracking(curr_comb, index)
           
        return combinations
        
