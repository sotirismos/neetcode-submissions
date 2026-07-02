class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                if token == "+":
                    res = int(stack[-2]) + int(stack[-1])
                elif token == "-":
                    res = int(stack[-2]) - int(stack[-1])
                elif token == "*":
                    res = int(stack[-2]) * int(stack[-1])
                else:
                    res = int(int(stack[-2]) / int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(str(res))

        return int(stack[-1])