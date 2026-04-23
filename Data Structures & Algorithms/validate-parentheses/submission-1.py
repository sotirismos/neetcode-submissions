class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        associations = {")": "(", "}": "{", "]": "["}
        for index, char in enumerate(s):
            if char not in associations:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != associations[char]:
                    return False
                else:
                    stack.pop(-1)
        return stack == []