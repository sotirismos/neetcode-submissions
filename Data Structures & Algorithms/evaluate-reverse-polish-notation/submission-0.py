class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if token == "+":
                    result = stack[-1] + stack[-2]
                elif token == "-":
                    result = stack[-2] - stack[-1]
                elif token == "*":
                    result = stack[-1] * stack[-2]
                elif token == "/":
                    result = int(stack[-2] / stack[-1])
                stack.pop(-1)
                stack.pop(-1)
                stack.append(result)
        return stack[-1]
