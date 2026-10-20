class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                temp_string = ""
                while stack and stack[-1] != "[":
                    temp_string = stack.pop() + temp_string
                # get rid of "["
                stack.pop()
                multiplier = ""
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier
                stack.append(int(multiplier) * temp_string)
            else:
                stack.append(char)
        return "".join(stack)