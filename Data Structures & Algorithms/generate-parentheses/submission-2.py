class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []

        def backtracking(num_open: int, num_closed: int, current_path: List[str]):
            # Base case (reached a leaf)
            if len(current_path) == (2 * n):
                parentheses.append("".join(current_path.copy()))
                return

            if num_open < n:
                current_path.append('(')
                num_open += 1
                backtracking(num_open, num_closed, current_path)
                current_path.pop()
                num_open -= 1

            if num_closed < num_open:
                current_path.append(')')
                num_closed += 1
                backtracking(num_open, num_closed, current_path)
                current_path.pop()
                num_closed -= 1
            
        backtracking(0, 0, [])
        return parentheses


        
    