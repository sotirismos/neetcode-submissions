class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                first_operand = int(stack.pop())
                second_operand = int(stack.pop())

                if token == '+':
                    stack.append(first_operand + second_operand)
                elif token == '-':
                    stack.append(second_operand - first_operand)
                elif token == '*':
                    stack.append(first_operand * second_operand)
                else:
                    stack.append(int(second_operand / first_operand))
        
        return int(stack[-1])