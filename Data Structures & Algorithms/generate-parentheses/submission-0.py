class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_par = 0
        close_par = 0
        curr_str = ""
        out = []

        self.helper(open_par, close_par, curr_str, out, n)
        return out

    def helper(self, open_par, close_par, curr_str, out, n):
        if len(curr_str) == 2 * n:
            out.append(curr_str)
            return

        if open_par < n:
            self.helper(open_par + 1, close_par, curr_str + '(', out, n)

        if close_par < open_par:
            self.helper(open_par, close_par + 1, curr_str + ')', out, n)
        
