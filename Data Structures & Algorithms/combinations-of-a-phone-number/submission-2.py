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
        combs = []
        index = 0
        if len(digits) < 1:
            return []
        self.helper(digits, index, catalog, curr_comb, combs)
        return combs

    def helper(self, digits, index, catalog, curr_comb, combs):
        # Base case
        if index >= len(digits):
            combs.append(curr_comb)
            return

        for char in catalog[digits[index]]:
            curr_comb += char
            self.helper(digits, index + 1, catalog, curr_comb, combs)
            curr_comb = curr_comb[:-1]
    

        
